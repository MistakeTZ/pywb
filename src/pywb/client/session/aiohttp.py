from __future__ import annotations

import asyncio
import ssl
from typing import TYPE_CHECKING, Any, cast

import certifi
from aiohttp import ClientError, ClientSession, TCPConnector
from typing_extensions import Self

from .base import BaseSession, WBType
from ...enums import WB_ROUTER, WBDomain
from ...exceptions import WBApiError

if TYPE_CHECKING:
    from ...methods.base import WBMethod


class WBNetworkError(WBApiError):
    """Ошибка сети (таймаут, обрыв соединения, DNS и т.д.)"""

    def __init__(self, message: str, original_exception: Exception | None = None):
        super().__init__(
            status_code=0, payload={"title": "Network Error", "detail": message}
        )
        self.original_exception = original_exception


class AiohttpWBSession(BaseSession):
    """
    HTTP-сессия на базе aiohttp для работы с Wildberries API.
    """

    def __init__(self, is_sandbox: bool = False, limit: int = 100, **kwargs):
        """
        :param limit: Максимальное количество одновременных соединений (Connection Pooling).
        :param kwargs: Аргументы для BaseSession (base_url, timeout и т.д.).
        """
        super().__init__(**kwargs)

        self.is_sandbox = is_sandbox
        self._session: ClientSession | None = None
        self._connector_type: type[TCPConnector] = TCPConnector
        self._connector_init: dict[str, Any] = {
            "ssl": ssl.create_default_context(cafile=certifi.where()),
            "limit": limit,
            "ttl_dns_cache": 3600,
        }

    async def create_session(self) -> ClientSession:
        """Ленивая инициализация aiohttp сессии."""
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=self._connector_type(**self._connector_init),
                headers={"Content-Type": "application/json"},
            )
        return self._session

    async def close(self) -> None:
        """Аккуратное закрытие сессии и всех TCP соединений."""
        if self._session is not None and not self._session.closed:
            await self._session.close()

            await asyncio.sleep(0.25)

    def _get_url(self, domain: WBDomain, path: str) -> str:
        """Определяет базовый URL на основе домена и флага Sandbox"""
        domain_urls = WB_ROUTER[domain]

        if self.is_sandbox:
            if domain_urls["sandbox"] is None:
                raise ValueError(
                    f"Sandbox environment is not available for domain: {domain}"
                )
            base_url = domain_urls["sandbox"]
        else:
            base_url = domain_urls["prod"]

        return f"{base_url.rstrip('/')}/{path.lstrip('/')}"

    async def make_request(
        self,
        token: str,
        method: WBMethod[WBType],
        timeout: int | None = None,
    ) -> WBType:
        """
        Подготавливает данные, выполняет запрос и передает результат валидатору.
        """
        session = await self.create_session()

        url = self._get_url(method.__domain__, method.__api_path__)

        http_method = method.__http_method__.upper()

        raw_payload = method.model_dump(exclude_none=True, by_alias=True)

        prepared_payload = self.prepare_value(raw_payload)

        request_kwargs: dict[str, Any] = {}
        if http_method in ("GET", "DELETE"):
            request_kwargs["params"] = prepared_payload
        else:
            request_kwargs["json"] = prepared_payload

        try:
            async with session.request(
                method=http_method,
                url=url,
                headers={"Authorization": token},
                timeout=self.timeout if timeout is None else timeout,
                **request_kwargs,
            ) as resp:
                if method.__returning__ is bytes:
                    raw_result = await resp.read()
                else:
                    raw_result = await resp.text()

        except asyncio.TimeoutError as e:
            raise WBNetworkError("Request timeout error", e) from e
        except ClientError as e:
            raise WBNetworkError(f"Network error: {type(e).__name__} - {e}", e) from e

        response_data = self.check_response(
            method=method,
            status_code=resp.status,
            content=raw_result,
        )

        return cast(WBType, response_data)

    async def __aenter__(self) -> Self:
        await self.create_session()
        return self
