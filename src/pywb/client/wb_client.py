from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING, Optional, Any, Dict, List
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
    GetCardsList,
    GetWarehouses,
    DeleteUser,
    UpdateProductCard,
    UpdateStocks,
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
    CardsListData,
    WarehouseItem,
    StockItem,
    CreateCardVariant,
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

    # ==========================================
    # БАЗОВЫЕ МЕТОДЫ И ИНФОРМАЦИЯ
    # ==========================================

    async def ping(self, request_timeout: int | None = None) -> PingResponse:
        """
        Проверяет доступность серверов Wildberries и валидность токена.
        """
        call = Ping()
        return await self(call, request_timeout=request_timeout)

    async def ping_content(self, request_timeout: int | None = None) -> PingResponse:
        """
        Специальный метод для проверки доступности Content API.
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

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 10 запросов).
        """
        call = GetNews(from_date=from_date, from_id=from_id)
        return await self(call, request_timeout=request_timeout)

    async def get_seller_info(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение информации о продавце (имя, ИНН, ID).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 10 запросов).
        """
        call = GetSellerInfo()
        return await self(call, request_timeout=request_timeout)

    async def get_seller_rating(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение рейтинга продавца и количества отзывов.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 1 запрос).
        """
        call = GetSellerRating()
        return await self(call, request_timeout=request_timeout)

    async def get_jam_subscription(
        self, request_timeout: Optional[int] = None
    ) -> SellerInfoResponse:
        """
        Получение информации о подписке продавца на сервис Джем.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 10 запросов).
        """
        call = GetJamSubscription()
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # УПРАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯМИ
    # ==========================================

    async def get_users(
        self, request_timeout: Optional[int] = None
    ) -> GetUsersResponse:
        """
        Получение списка пользователей, имеющих доступ к аккаунту продавца.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5 запросов).
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
        Создание приглашения для нового пользователя с определенными правами.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5 запросов).
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

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5 запросов).
        """
        user_access_update = UserAccessUpdate(user_id=user_id, access=access_items)
        call = UpdateUserAccess(**user_access_update.model_dump(by_alias=True))
        await self(call, request_timeout=request_timeout)

    async def delete_user(
        self,
        user_id: int,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Удаление пользователя из кабинета продавца.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).

        :param user_id: ID пользователя, чей доступ будет отозван.
        """
        call = DeleteUser(deletedUserID=user_id)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # РАБОТА С ТОВАРАМИ (КОНТЕНТ)
    # ==========================================

    async def get_cards_list(
        self,
        settings: Dict[str, Any],
        request_timeout: Optional[int] = None,
    ) -> CardsListData:
        """
        Получение списка созданных карточек товаров.

        ⚠️ ЛИМИТЫ: 100 запросов в 1 минуту с шагом 600 мс (Burst: 5 запросов).
        Внимание: За один раз возвращается не более 100 карточек, используйте курсор для пагинации.

        :param settings: Словарь с настройками фильтрации, сортировки и курсором.
        """
        call = GetCardsList(settings=settings)
        return await self(call, request_timeout=request_timeout)

    async def update_product_card(
        self,
        items: List[CreateCardVariant],
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Редактирование карточек товаров (включая добавление новых размеров).

        ⚠️ ЛИМИТЫ: 10 запросов в 1 минуту с шагом 6 с (Burst: 5 запросов).
        - За один запрос можно редактировать до 3000 карточек.
        - Максимальный размер запроса: 10 МБ.
        - Синхронизация данных занимает до 30 минут.

        :param items: Список карточек для обновления (модель CreateCardVariant).
        """
        call = UpdateProductCard(items=items)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # МАРКЕТПЛЕЙС И ОСТАТКИ (FBS)
    # ==========================================

    async def get_warehouses(
        self, request_timeout: Optional[int] = None
    ) -> List[WarehouseItem]:
        """
        Получение списка всех складов продавца (Marketplace).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetWarehouses()
        return await self(call, request_timeout=request_timeout)

    async def update_stocks(
        self,
        warehouse_id: int,
        stocks: List[StockItem],
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Обновление остатков товаров на складе продавца.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Внимание: Один запрос с ошибкой 409 считается системой за 10 запросов.

        :param warehouse_id: Идентификатор склада продавца.
        :param stocks: Список объектов StockItem с идентификатором размера (chrtId) и количеством (amount).
        """
        call = UpdateStocks(warehouse_id=warehouse_id, stocks=stocks)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # СТАТИСТИКА
    # ==========================================

    async def get_orders(
        self,
        date_from: datetime | str,
        flag: int = 0,
        request_timeout: Optional[int] = None,
    ) -> list[StatisticOrder]:
        """
        Возвращает информацию о заказах (Статистика).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 1 запрос).
        Условный лимит ответа: 80 000 строк за один запрос.
        """
        if isinstance(date_from, datetime):
            date_from_str = date_from.replace(microsecond=0).isoformat()
        else:
            date_from_str = date_from

        call = GetOrders(dateFrom=date_from_str, flag=flag)
        return await self(call, request_timeout=request_timeout)
