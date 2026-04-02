# client.py
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pywb.methods.ping import PingContent
from pywb.methods.statistics import GetOrders
from pywb.types.order import StatisticOrder

from .session.base import BaseSession
from .session.aiohttp import AiohttpWBSession

from ..methods import Ping, WT
from ..types import PingResponse

if TYPE_CHECKING:
    from ..methods.base import WBMethod


class WBClient:
    """
    Асинхронный клиент для работы с API Wildberries.
    """

    def __init__(
        self,
        token: str,
        is_sandbox: bool = False,
        session: BaseSession | None = None,
    ) -> None:
        self.token = token

        if session is None:
            session = AiohttpWBSession(is_sandbox=is_sandbox)

        self.session = session

    async def __call__(
        self, method: WBMethod[WT], request_timeout: int | None = None
    ) -> WT:
        """
        Единая точка входа.
        Вызывает метод API и возвращает результат нужного типа.
        """
        return await self.session(
            token=self.token, method=method, timeout=request_timeout
        )

    async def aclose(self) -> None:
        """Делегируем закрытие соединений сессии"""
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    async def ping(self, request_timeout: int | None = None) -> PingResponse:
        """
        Проверяет доступность серверов Wildberries и валидность токена.
        """
        call = Ping()

        return await self(call, request_timeout=request_timeout)
    
    async def ping_content(self, request_timeout: int | None = None) -> PingResponse:
        """
        Специальный метод для проверки доступности Content API (для карточек, цен и т.д.).
        Полезно, если у вас есть методы, которые работают только с этим доменом.
        """
        call = PingContent()

        return await self(call, request_timeout=request_timeout)

    async def get_orders(
        self,
        date_from: datetime | str,
        flag: int = 0,
        request_timeout: Optional[int] = None
    ) -> list[StatisticOrder]:
        """
        Возвращает информацию о заказах.
        Данные в этом отчете предварительные и используются для оперативного контроля.

        ⚠️ ЛИМИТЫ И ПРАВИЛА ИСПОЛЬЗОВАНИЯ API:
        ---------------------------------------
        - Обновление данных: Каждые 30 минут.
        - Хранение данных: Гарантируется не более 90 дней со дня продажи.
        - Rate Limit: 1 запрос в 1 минуту на один аккаунт продавца (Burst: 1 запрос).
        
        ОСОБЕННОСТИ ПАГИНАЦИИ (Лимит строк):
        ---------------------------------------
        При запросе с flag=0 или без него установлен условный лимит в 80 000 строк.
        Для получения всех заказов:
        1. В первом запросе передайте начальную дату в `date_from`.
        2. Если вернулось 80 000 строк, возьмите значение `last_change_date`
           из ПОСЛЕДНЕЙ строки ответа и передайте его как `date_from` в следующий запрос.
        3. Если ответ вернул пустой массив `[]` — все заказы получены.

        ПРИМЕЧАНИЯ:
        ---------------------------------------
        - 1 строка = 1 заказ = 1 единица товара.
        - `srid` — уникальный идентификатор заказа.
        - В отчет НЕ попадают заказы без подтвержденной оплаты (например, рассрочка).
          Такие продажи можно найти в детализации отчета о реализации.

        :param date_from: Дата в формате ISO 8601 (например, "2022-03-04T18:08:31") 
                          или объект datetime.
        :param flag: 0 (по умолчанию) - получить данные, у которых lastChangeDate >= dateFrom.
                     1 - получить данные, у которых date >= dateFrom.
        :param request_timeout: Таймаут запроса в секундах.
        :return: Список объектов StatisticOrder.
        """

        if isinstance(date_from, datetime):
            date_from_str = date_from.replace(microsecond=0).isoformat()
        else:
            date_from_str = date_from

        call = GetOrders(dateFrom=date_from_str, flag=flag)
        return await self(call, request_timeout=request_timeout)
