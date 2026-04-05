from __future__ import annotations

import abc
import datetime
import json
from enum import Enum
from typing import TYPE_CHECKING, Any, Callable, TypeVar, cast

from pydantic import BaseModel, TypeAdapter, ValidationError
from typing_extensions import Self

from ...exceptions import (
    AccessDeniedError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PaymentRequiredError,
    PayloadTooLargeError,
    TooManyRequestsError,
    UnauthorizedError,
    UnprocessableEntityError,
    WBApiError,
    ClientDecodeError,
)

if TYPE_CHECKING:
    from types import TracebackType
    from ...methods import WBMethod

WBType = TypeVar("WBType")

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., str]

DEFAULT_TIMEOUT: float = 60.0
WB_PRODUCTION_API: str = "https://common-api.wildberries.ru"


class BaseSession(abc.ABC):
    """
    Базовый класс для всех HTTP сессий клиента Wildberries.
    Наследуйтесь от него, чтобы реализовать конкретную сессию (например, HttpxSession).
    """

    def __init__(
        self,
        base_url: str = WB_PRODUCTION_API,
        json_loads: _JsonLoads = json.loads,
        json_dumps: _JsonDumps = json.dumps,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        self.base_url = base_url
        self.json_loads = json_loads
        self.json_dumps = json_dumps
        self.timeout = timeout

    def check_response(
        self,
        method: WBMethod[WBType],
        status_code: int,
        content: str,
    ) -> WBType:
        """
        Проверяет статус ответа и десериализует его в нужный тип Pydantic.
        """
        return_type = method.__returning__

        if status_code == 204:
            if return_type is bool:
                return cast(WBType, True)
            return cast(WBType, None)

        if return_type is bytes:
            if status_code >= 400:
                content_str = (
                    content.decode("utf-8") if isinstance(content, bytes) else content
                )
                json_data = self.json_loads(content_str) if content_str else {}
                self._raise_for_status(status_code, json_data)

            return cast(WBType, content)

        try:
            json_data = self.json_loads(content) if content else {}
        except Exception as e:
            raise ClientDecodeError("Failed to decode JSON response", e, content) from e

        if status_code >= 400:
            self._raise_for_status(status_code, json_data)

        if return_type is bool:
            return cast(WBType, True)

        if return_type in (dict, list, Any):
            return cast(WBType, json_data)

        try:
            from pydantic import TypeAdapter, ValidationError

            adapter = TypeAdapter(return_type)
            validated_data = adapter.validate_python(json_data)
            return cast(WBType, validated_data)
        except ValidationError as e:
            raise ClientDecodeError(
                "Failed to deserialize response into Pydantic model", e, json_data
            ) from e

    def _raise_for_status(self, status_code: int, payload: dict[str, Any]) -> None:
        """Внутренний маппинг ошибок HTTP на исключения Python"""
        if status_code == 400:
            raise BadRequestError(status_code, payload)
        if status_code == 401:
            raise UnauthorizedError(status_code, payload)
        if status_code == 402:
            raise PaymentRequiredError(status_code, payload)
        if status_code == 403:
            raise AccessDeniedError(status_code, payload)
        if status_code == 404:
            raise NotFoundError(status_code, payload)
        if status_code == 409:
            raise ConflictError(status_code, payload)
        if status_code == 413:
            raise PayloadTooLargeError(status_code, payload)
        if status_code == 422:
            raise UnprocessableEntityError(status_code, payload)
        if status_code == 429:
            raise TooManyRequestsError(status_code, payload)
        if status_code >= 500:
            raise InternalServerError(status_code, payload)

        raise WBApiError(status_code, payload)

    def prepare_value(self, value: Any) -> Any:
        """
        Подготавливает значения перед отправкой в WB API.
        В отличие от Telegram, WB требует строгий JSON, поэтому
        в основном мы форматируем даты и Enums.
        """
        if value is None:
            return None
        if isinstance(value, str):
            return value
        if isinstance(value, datetime.datetime):
            # WB обычно ожидает ISO 8601 (например "2024-09-30T06:52:38Z")
            return value.isoformat() + "Z"
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, BaseModel):
            return self.prepare_value(value.model_dump(exclude_none=True))
        if isinstance(value, dict):
            return {k: self.prepare_value(v) for k, v in value.items() if v is not None}
        if isinstance(value, list):
            return [self.prepare_value(v) for v in value if v is not None]

        return value

    @abc.abstractmethod
    async def close(self) -> None:
        """Закрытие HTTP сессии (aiohttp/httpx)"""

    @abc.abstractmethod
    async def make_request(
        self,
        token: str,
        method: WBMethod[WBType],
        timeout: int | None = None,
    ) -> WBType:
        """
        Фактическое выполнение HTTP запроса.
        Должно быть реализовано в наследнике (HttpxSession или AiohttpSession).
        """

    async def __call__(
        self,
        token: str,
        method: WBMethod[WBType],
        timeout: int | None = None,
    ) -> WBType:
        """
        Точка входа для выполнения запроса.
        """
        # TODO: Здесь можно добавить мидлвари (логирование, ретраи, метрики) перед вызовом make_request

        return await self.make_request(token, method, timeout=timeout)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()
