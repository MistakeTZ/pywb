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
    GetNewOrders,
    CreatePass,
    GetPassOffices,
    GetOrdersList,
    GetOrdersStatuses,
    CancelOrder,
    GetOrderStickers,
    CreateSupply,
    GetSupplies,
    AddOrdersToSupply,
    DeliverSupply,
    GetStickersResponse,
    GetOrdersDBW,
    GetNewOrdersDBW,
    GetOrdersStatusesDBW,
    ConfirmOrderDBW,
    AssembleOrderDBW,
    CancelOrderDBW,
    GetOrderMetaDBW,
    GetBuyerInfoDBW,
    GetOrderStickersDBW,
    GetCourierInfoDBW,
    GetDeliveryDateDBW,
    DeleteOrderMetaDBW,
    UpdateOrderMetaSgtinDBW,
    UpdateOrderMetaUinDBW,
    GetOrdersDBS,
    GetNewOrdersDBS,
    GetOrdersDBS,
    GetOrderGroupsInfoDBS,
    GetBuyerInfoDBS,
    GetB2BBuyerInfoDBS,
    GetDeliveryDateDBS,
    GetOrderStickersDBS,
    GetOrdersStatusesDBS,
    ConfirmOrdersDBS,
    DeliverOrdersDBS,
    DeleteOrdersMetaDBS,
    UpdateOrdersMetaSgtinDBS,
    UpdateOrdersMetaUinDBS,
    UpdateOrdersMetaImeiDBS,
    UpdateOrdersMetaGtinDBS,
    UpdateOrdersMetaSgtinDBS,
    UpdateOrdersMetaUinDBS,
    UpdateOrdersMetaImeiDBS,
    UpdateOrdersMetaGtinDBS,
    UpdateOrdersMetaCustomsDBS,
    UpdateOrderMetaGtinDBW,
    UpdateOrderMetaImeiDBW,
    UpdateMetaCustomsItem,
    UpdateMetaGtinItem,
    UpdateMetaImeiItem,
    UpdateMetaUinItem,
    UpdateMetaSgtinItem,
    CancelOrdersDBS,
    RejectOrdersDBS,
    ReceiveOrdersDBS,
    GetOrdersMetaDBS,
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
    PassOffice,
    CreatePassResponse,
    GetNewOrdersResponse,
    GetOrdersResponse,
    GetOrdersStatusesResponse,
    CreateSupplyResponse,
    GetSuppliesResponse,
    CreateSupplyResponse,
    GetSuppliesResponse,
    GetOrderMetaDBWResponse,
    GetNewOrdersDBWResponse,
    GetOrdersDBWResponse,
    GetOrdersStatusesDBWResponse,
    GetStickersDBWResponse,
    GetStickersResponse,
    OrderCourierInfo,
    ClientInfoDBW,
    DeliveryDateInfo,
    GetNewOrdersDBSResponse,
    GetOrdersDBSResponse,
    OrderGroupDBS,
    ClientInfoDBSResp,
    B2BClientInfoResp,
    DeliveryDateInfo,
    GetStickersDBSResponse,
    OrderStatusesV2Resp,
    StatusSetResponsesResp,
    OrderCodeRequestItem,
    UpdateMetaSgtinItem,
    UpdateMetaUinItem,
    UpdateMetaImeiItem,
    StatusSetResponsesResp,
    OrdersMetaResponse,
    B2BClientInfoResp,
    DeliveryDateInfo,
    GetStickersDBSResponse,
    OrderStatusesV2Resp,
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

    # ==========================================
    # FBS: ПРОПУСКА (Passes)
    # ==========================================

    async def get_pass_offices(
        self, request_timeout: Optional[int] = None
    ) -> List[PassOffice]:
        """
        Получение списка складов, для которых требуется пропуск.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        return await self(GetPassOffices(), request_timeout=request_timeout)

    async def create_pass(
        self,
        first_name: str,
        last_name: str,
        car_model: str,
        car_number: str,
        office_id: int,
        request_timeout: Optional[int] = None,
    ) -> CreatePassResponse:
        """
        Создание пропуска водителя. Пропуск действует 48 часов.

        ⚠️ ЛИМИТЫ: Максимум 1 запрос в 10 минут на один аккаунт продавца.

        :param first_name: Имя водителя.
        :param last_name: Фамилия водителя.
        :param car_model: Марка автомобиля (от 1 до 100 символов).
        :param car_number: Номер автомобиля (только буквы и цифры, 6-9 символов).
        :param office_id: ID склада (офиса), куда оформляется пропуск.
        """
        call = CreatePass(
            firstName=first_name,
            lastName=last_name,
            carModel=car_model,
            carNumber=car_number,
            officeId=office_id,
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # FBS: СБОРОЧНЫЕ ЗАДАНИЯ (Orders)
    # ==========================================

    async def get_new_orders(
        self, request_timeout: Optional[int] = None
    ) -> GetNewOrdersResponse:
        """
        Получение списка новых сборочных заданий (статус "new").

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        return await self(GetNewOrders(), request_timeout=request_timeout)

    async def get_orders_list(
        self,
        limit: int = 1000,
        next_cursor: int = 0,
        date_from: Optional[int] = None,
        date_to: Optional[int] = None,
        request_timeout: Optional[int] = None,
    ) -> GetOrdersResponse:
        """
        Получение информации по сборочным заданиям (без текущего статуса).
        Максимальный период за один запрос — 30 календарных дней.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param limit: Количество заказов в ответе (до 1000).
        :param next_cursor: Параметр пагинации.
        :param date_from: Дата начала периода в формате Unix Timestamp.
        :param date_to: Дата конца периода в формате Unix Timestamp.
        """
        call = GetOrdersList(
            limit=limit,
            next=next_cursor,
            dateFrom=date_from,
            dateTo=date_to,
        )
        return await self(call, request_timeout=request_timeout)

    async def get_orders_statuses(
        self,
        orders: List[int],
        request_timeout: Optional[int] = None,
    ) -> GetOrdersStatusesResponse:
        """
        Получение актуальных статусов сборочных заданий.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param orders: Список ID сборочных заданий (от 1 до 1000 шт).
        """
        call = GetOrdersStatuses(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def cancel_order(
        self,
        order_id: int,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Отмена сборочного задания продавцом (перевод в статус cancel).

        ⚠️ ЛИМИТЫ: 100 запросов в 1 минуту с шагом 600 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.

        :param order_id: ID сборочного задания.
        """
        call = CancelOrder(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def get_order_stickers(
        self,
        orders: List[int],
        sticker_type: str = "png",
        width: int = 58,
        height: int = 40,
        request_timeout: Optional[int] = None,
    ) -> GetStickersResponse:
        """
        Получение этикеток (стикеров) для заказов.
        Работает только для заказов в статусе confirm (В сборке) и complete (В доставке).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param orders: Список ID сборочных заданий (максимум 100 шт за раз).
        :param sticker_type: Формат этикетки (svg, zplv, zplh, png).
        :param width: Ширина (58 или 40).
        :param height: Высота (40 или 30).
        """
        call = GetOrderStickers(
            orders=orders,
            type=sticker_type,
            width=width,
            height=height,
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # FBS: ПОСТАВКИ (Supplies)
    # ==========================================

    async def create_supply(
        self,
        name: str,
        request_timeout: Optional[int] = None,
    ) -> CreateSupplyResponse:
        """
        Создание новой поставки (FBS).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param name: Название поставки (от 1 до 128 символов).
        """
        call = CreateSupply(name=name)
        return await self(call, request_timeout=request_timeout)

    async def get_supplies(
        self,
        limit: int = 1000,
        next_cursor: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetSuppliesResponse:
        """
        Получение списка поставок.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param limit: Лимит выдачи (максимум 1000).
        :param next_cursor: Параметр пагинации.
        """
        call = GetSupplies(limit=limit, next=next_cursor)
        return await self(call, request_timeout=request_timeout)

    async def add_orders_to_supply(
        self,
        supply_id: str,
        orders: List[int],
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Добавление сборочных заданий к поставке.
        Автоматически переводит задания в статус confirm (В сборке).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.

        :param supply_id: ID поставки (например, WB-GI-1234567).
        :param orders: Список ID сборочных заданий (максимум 100 за запрос).
        """
        call = AddOrdersToSupply(supply_id=supply_id, orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def deliver_supply(
        self,
        supply_id: str,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Закрытие поставки и перевод в доставку.
        Все заказы внутри поставки перейдут в статус complete (В доставке).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.

        :param supply_id: ID поставки (например, WB-GI-1234567).
        """
        call = DeliverSupply(supply_id=supply_id)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBW: СБОРОЧНЫЕ ЗАДАНИЯ И СТАТУСЫ
    # ==========================================

    async def get_new_orders_dbw(
        self, request_timeout: Optional[int] = None
    ) -> GetNewOrdersDBWResponse:
        """
        Получение списка новых заказов (DBW).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        return await self(GetNewOrdersDBW(), request_timeout=request_timeout)

    async def get_orders_dbw(
        self,
        date_from: int,
        date_to: int,
        limit: int = 1000,
        next_cursor: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetOrdersDBWResponse:
        """
        Получение информации по завершенным (отмененным или проданным) заказам DBW.
        Максимальный период за один запрос — 30 календарных дней.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param date_from: Дата начала периода (Unix Timestamp).
        :param date_to: Дата конца периода (Unix Timestamp).
        :param limit: Количество заказов в ответе (максимум 1000).
        :param next_cursor: Параметр пагинации.
        """
        call = GetOrdersDBW(
            dateFrom=date_from, dateTo=date_to, limit=limit, next=next_cursor
        )
        return await self(call, request_timeout=request_timeout)

    async def get_orders_statuses_dbw(
        self,
        orders: List[int],
        request_timeout: Optional[int] = None,
    ) -> GetOrdersStatusesDBWResponse:
        """
        Получение актуальных статусов заказов DBW.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param orders: Список ID сборочных заданий (до 1000 штук).
        """
        call = GetOrdersStatusesDBW(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def confirm_order_dbw(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Перевод заказа DBW в статус confirm (на сборке).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.
        """
        call = ConfirmOrderDBW(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def assemble_order_dbw(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Перевод заказа DBW в статус complete (в доставке).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.
        """
        call = AssembleOrderDBW(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def cancel_order_dbw(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Отмена заказа DBW продавцом (перевод в статус cancel).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        Один запрос с ошибкой 409 считается системой за 10 запросов.
        """
        call = CancelOrderDBW(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def get_order_stickers_dbw(
        self,
        orders: List[int],
        sticker_type: str = "png",
        width: int = 58,
        height: int = 40,
        request_timeout: Optional[int] = None,
    ) -> GetStickersDBWResponse:
        """
        Получение этикеток (стикеров) для заказов DBW в статусах confirm и complete.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).

        :param orders: Список ID заданий (максимум 100 шт за раз).
        :param sticker_type: Формат этикетки (svg, zplv, zplh, png).
        """
        call = GetOrderStickersDBW(
            orders=orders, type=sticker_type, width=width, height=height
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBW: ИНФОРМАЦИЯ О ДОСТАВКЕ, КЛИЕНТАХ И КУРЬЕРАХ
    # ==========================================

    async def get_delivery_date_dbw(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> DeliveryDateInfo:
        """
        Получение информации о дате и времени доставки, выбранных покупателем.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetDeliveryDateDBW(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def get_buyer_info_dbw(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> ClientInfoDBW:
        """
        Получение контактной информации о покупателе по ID заказа.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetBuyerInfoDBW(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def get_courier_info_dbw(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> OrderCourierInfo:
        """
        Получение контактов курьера и номера его автомобиля по ID заказа.
        Доступно для заказов в статусе confirm и complete.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetCourierInfoDBW(orders=orders)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBW: УПРАВЛЕНИЕ МЕТАДАННЫМИ (Маркировка)
    # ==========================================

    async def get_order_meta_dbw(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> GetOrderMetaDBWResponse:
        """
        Получение привязанных метаданных заказа (УИН, КиЗ, IMEI, GTIN).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrderMetaDBW(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def delete_order_meta_dbw(
        self, order_id: int, key: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Удаление метаданных заказа по ключу.
        Возможные ключи: imei, uin, gtin, sgtin.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = DeleteOrderMetaDBW(order_id=order_id, key=key)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_sgtin_dbw(
        self, order_id: int, sgtins: List[str], request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление кодов Data Matrix (Честный ЗНАК) к заказу в статусе confirm.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaSgtinDBW(order_id=order_id, sgtins=sgtins)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_uin_dbw(
        self, order_id: int, uin: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление УИНа (Уникального идентификационного номера) к заказу в статусе confirm.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaUinDBW(order_id=order_id, uin=uin)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_imei_dbw(
        self, order_id: int, imei: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление IMEI к заказу в статусе confirm.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaImeiDBW(order_id=order_id, imei=imei)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_gtin_dbw(
        self, order_id: int, gtin: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление GTIN (для товаров из Беларуси) к заказу в статусе confirm.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaGtinDBW(order_id=order_id, gtin=gtin)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBS: СБОРОЧНЫЕ ЗАДАНИЯ И ИНФОРМАЦИЯ
    # ==========================================

    async def get_new_orders_dbs(
        self, request_timeout: Optional[int] = None
    ) -> GetNewOrdersDBSResponse:
        """
        Получение списка новых заказов (DBS).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        return await self(GetNewOrdersDBS(), request_timeout=request_timeout)

    async def get_orders_dbs(
        self,
        date_from: int,
        date_to: int,
        limit: int = 1000,
        next_cursor: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetOrdersDBSResponse:
        """
        Получение завершенных или отмененных заказов (DBS).
        Максимальный период за один запрос — 30 календарных дней.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrdersDBS(
            dateFrom=date_from, dateTo=date_to, limit=limit, next=next_cursor
        )
        return await self(call, request_timeout=request_timeout)

    async def get_order_groups_info_dbs(
        self, groups: List[str], request_timeout: Optional[int] = None
    ) -> List[OrderGroupDBS]:
        """
        Получение информации о платной доставке для объединенных заказов.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrderGroupsInfoDBS(groups=groups)
        return await self(call, request_timeout=request_timeout)

    async def get_buyer_info_dbs(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> ClientInfoDBSResp:
        """
        Получение контактной информации о покупателе по ID заказа.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetBuyerInfoDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def get_b2b_buyer_info_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> B2BClientInfoResp:
        """
        Получение данных B2B покупателей (ИНН, КПП, Наименование).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetB2BBuyerInfoDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def get_delivery_date_dbs(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> DeliveryDateInfo:
        """
        Получение информации о дате и времени доставки, выбранных покупателем.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetDeliveryDateDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def get_order_stickers_dbs(
        self,
        orders: List[int],
        sticker_type: str = "pdf",
        width: int = 58,
        height: int = 40,
        request_timeout: Optional[int] = None,
    ) -> GetStickersDBSResponse:
        """
        Получение этикеток для заказов с доставкой в ПВЗ (в статусах confirm, deliver).
        Формат только PDF. Размер только 58x40.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrderStickersDBS(
            orders=orders, type=sticker_type, width=width, height=height
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBS: УПРАВЛЕНИЕ СТАТУСАМИ (Батч-операции)
    # ==========================================

    async def get_orders_statuses_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> OrderStatusesV2Resp:
        """
        Получение актуальных статусов заказов DBS.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrdersStatusesDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def confirm_orders_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Перевод заказов DBS в статус confirm (на сборке).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).
        """
        call = ConfirmOrdersDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def deliver_orders_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Перевод заказов DBS в статус deliver (в доставке).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).
        """
        call = DeliverOrdersDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def cancel_orders_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Отмена заказов DBS продавцом (перевод в статус cancel).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).
        """
        call = CancelOrdersDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def receive_orders_dbs(
        self, orders: List[OrderCodeRequestItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Подтверждение получения заказа покупателем (receive).
        Требуется код подтверждения `code` от покупателя.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).
        """
        call = ReceiveOrdersDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def reject_orders_dbs(
        self, orders: List[OrderCodeRequestItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Отказ покупателя от заказа при получении (reject).
        Требуется код подтверждения `code` от покупателя.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 10 запросов).
        """
        call = RejectOrdersDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DBS: УПРАВЛЕНИЕ МЕТАДАННЫМИ (Маркировка)
    # ==========================================

    async def get_orders_meta_dbs(
        self, orders_ids: List[int], request_timeout: Optional[int] = None
    ) -> OrdersMetaResponse:
        """
        Получение метаданных заказов (УИН, КиЗ, IMEI, GTIN).

        ⚠️ ЛИМИТЫ: 150 запросов в 1 минуту с шагом 400 мс (Burst: 20 запросов).
        """
        call = GetOrdersMetaDBS(ordersIds=orders_ids)
        return await self(call, request_timeout=request_timeout)

    async def delete_orders_meta_dbs(
        self, order_ids: List[int], key: str, request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Удаление метаданных группы заказов по ключу.
        Возможные ключи: imei, uin, gtin, sgtin, customsDeclaration.

        ⚠️ ЛИМИТЫ: 150 запросов в 1 минуту с шагом 400 мс (Burst: 20 запросов).
        """
        call = DeleteOrdersMetaDBS(orderIds=order_ids, key=key)
        return await self(call, request_timeout=request_timeout)

    async def update_orders_meta_sgtin_dbs(
        self, orders: List[UpdateMetaSgtinItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Установка кодов Data Matrix (Честный ЗНАК) для списка заказов.

        ⚠️ ЛИМИТЫ: 500 запросов в 1 минуту с шагом 120 мс (Burst: 20 запросов).
        """
        call = UpdateOrdersMetaSgtinDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def update_orders_meta_uin_dbs(
        self, orders: List[UpdateMetaUinItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Установка УИНов для списка заказов.

        ⚠️ ЛИМИТЫ: 500 запросов в 1 минуту с шагом 120 мс (Burst: 20 запросов).
        """
        call = UpdateOrdersMetaUinDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def update_orders_meta_imei_dbs(
        self, orders: List[UpdateMetaImeiItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Установка IMEI для списка заказов.

        ⚠️ ЛИМИТЫ: 500 запросов в 1 минуту с шагом 120 мс (Burst: 20 запросов).
        """
        call = UpdateOrdersMetaImeiDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def update_orders_meta_gtin_dbs(
        self, orders: List[UpdateMetaGtinItem], request_timeout: Optional[int] = None
    ) -> StatusSetResponsesResp:
        """
        Установка GTIN для списка заказов.

        ⚠️ ЛИМИТЫ: 500 запросов в 1 минуту с шагом 120 мс (Burst: 20 запросов).
        """
        call = UpdateOrdersMetaGtinDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def update_orders_meta_customs_dbs(
        self, orders: List[UpdateMetaCustomsItem], request_timeout: Optional[int] = None
    ) -> bool:
        """
        Установка номеров таможенных деклараций для списка заказов.

        ⚠️ ЛИМИТЫ: 500 запросов в 1 минуту с шагом 120 мс (Burst: 20 запросов).
        """
        call = UpdateOrdersMetaCustomsDBS(orders=orders)
        return await self(call, request_timeout=request_timeout)
