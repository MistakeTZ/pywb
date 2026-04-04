# client.py
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, Optional
from .session.base import BaseSession
from .session.aiohttp import AiohttpWBSession

from ..methods import (
    WT,
    GetOrders,
    Ping,
    PingContent,
    UpdateUserAccess,
    CreateInvite,
    GetSellerInfo,
    GetNews,
    GetJamSubscription,
    GetSellerRating,
    GetUsers,
)


from ..types import (
    PingResponse,
    StatisticOrder,
    GetNewsResponse,
    SellerInfoResponse,
    GetUsersResponse,
    CreateInviteResponse,
    InviteInfo,
    AccessItem,
    UserAccessUpdate,
)

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

    async def get_news(
        self,
        from_date: datetime | str | None = None,
        from_id: int | None = None,
        request_timeout: Optional[int] = None,
    ) -> GetNewsResponse:
        """
        Получение новостей портала продавцов.

        :param from_date: Дата в формате ISO 8601 (например, "2022-03-04T18:08:31") для фильтрации новостей.
                          Вернутся новости, опубликованные после этой даты. Необязательный параметр.
        :param from_id: Идентификатор новости для пагинации. Вернутся новости с ID больше этого значения. Необязательный параметр.
        :param request_timeout: Таймаут запроса в секундах.
        :return: Список объектов NewsItem с данными о новостях.
        """
        call = GetNews(from_date=from_date, from_id=from_id)
        return await self(call, request_timeout=request_timeout)

    async def get_seller_info(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение информации о продавце, включая его статус, дату регистрации и другую общую информацию.

        :param request_timeout: Таймаут запроса в секундах.
        :return: Объект SellerInfoResponse с данными о продавце.
        """

        call = GetSellerInfo()
        return await self(call, request_timeout=request_timeout)

    async def get_seller_rating(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение рейтинга продавца, который может включать в себя общую оценку, количество отзывов и другую информацию, связанную с рейтингом.

        :param request_timeout: Таймаут запроса в секундах.
        :return: Объект SellerInfoResponse с данными о рейтинге продавца.
        """

        call = GetSellerRating()
        return await self(call, request_timeout=request_timeout)

    async def get_jam_subscription(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение информации о подписке продавца на сервис JAM, который может включать в себя статус подписки, дату окончания и другую информацию, связанную с JAM.

        :param request_timeout: Таймаут запроса в секундах.
        :return: Объект SellerInfoResponse с данными о подписке на JAM.
        """

        call = GetJamSubscription()
        return await self(call, request_timeout=request_timeout)

    async def get_users(
        self, request_timeout: Optional[int] = None
    ) -> GetUsersResponse:
        """
        Получение списка пользователей, имеющих доступ к аккаунту продавца, включая их роли и права доступа.

        :param request_timeout: Таймаут запроса в секундах.
        :return: Объект GetUsersResponse с данными о пользователях.
        """

        call = GetUsers()
        return await self(call, request_timeout=request_timeout)

    async def create_invite(
        self,
        email: str,
        access_items: list[AccessItem],
        request_timeout: Optional[int] = None,
    ) -> CreateInviteResponse:
        """
        Создание приглашения для нового пользователя с определенными правами доступа.

        :param email: Электронная почта приглашенного пользователя.
        :param access_items: Список прав доступа, которые будут предоставлены приглашенному пользователю.
        :param request_timeout: Таймаут запроса в секундах.
        :return: Объект CreateInviteResponse с данными о созданном приглашении.
        """

        invite_info = InviteInfo(phone_number=email)
        call = CreateInvite(invite=invite_info, access=access_items)
        return await self(call, request_timeout=request_timeout)

    async def update_user_access(
        self,
        user_id: int,
        access_items: list[AccessItem],
        request_timeout: Optional[int] = None,
    ) -> None:
        """
        Обновление прав доступа существующего пользователя.

        :param user_id: Идентификатор пользователя, для которого нужно обновить права доступа.
        :param access_items: Новый список прав доступа для пользователя.
        :param request_timeout: Таймаут запроса в секундах.
        :return: None
        """

        user_access_update = UserAccessUpdate(user_id=user_id, access=access_items)
        call = UpdateUserAccess(**user_access_update.model_dump(by_alias=True))
        await self(call, request_timeout=request_timeout)

    async def get_orders(
        self,
        date_from: datetime | str,
        flag: int = 0,
        request_timeout: Optional[int] = None,
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
