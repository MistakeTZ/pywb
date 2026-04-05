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
    UnseenFQ,
    GetQuestionsData,
    GetFeedbacksData,
    AnswerFeedback,
    ChatItem,
    ChatEventsResult,
    GetClaimsResponse,
    GetChatEvents,
    GetChats,
    GetClaims,
    GetFeedbacks,
    GetQuestions,
    GetUnseenFQ,
    PatchQuestion,
    SendChatMessage,
    AnswerClaim,
    CountResponse,
    GetAdvertsResponse,
    BalanceResponse,
    BudgetResponse,
    DepositResponse,
    UpdItem,
    FullStatsItem,
    GetAdverts,
    GetBalance,
    GetBudget,
    GetCalendarPromotions,
    GetCampaignsCount,
    GetFullStats,
    GetUpd,
    StopCampaign,
    PauseCampaign,
    StartCampaign,
    RenameCampaign,
    DepositBudget,
    GetNewOrdersCCResponse,
    GetOrdersCCResponse,
    ClientInfoCCResp,
    OrderStatusesCCResp,
    GetStickersCCResponse,
    GetOrderMetaCCResponse,
    GetNewOrdersCC,
    GetBuyerInfoCC,
    GetOrderMetaCC,
    GetOrdersCC,
    GetOrdersStatusesCC,
    GetOrderStickersCC,
    UpdateOrderMetaGtinCC,
    UpdateOrderMetaImeiCC,
    UpdateOrderMetaSgtinCC,
    UpdateOrderMetaUinCC,
    CancelOrderCC,
    DeliverOrderCC,
    DeleteOrderMetaCC,
    GetAcceptanceOptions,
    GetSuppliesFBW,
    GetSupplyDetailsFBW,
    GetSupplyGoodsFBW,
    GetSupplyPackageFBW,
    GetTransitTariffs,
    GetWarehousesFBW,
    GetBlockedProducts,
    GetDeductions,
    GetMeasurementPenalties,
    GetPaidStorageFile,
    GetPaidStorageStatus,
    GetSales,
    GetShadowedProducts,
    CreatePaidStorageReport,
    GetCsvReportsList,
    GetFunnelGroupedHistory,
    GetFunnelHistory,
    GetFunnelProducts,
    GetReportFile,
    GetSearchMainReport,
    GetStocksGroups,
    GetStocksWbWarehouses,
    CreateCsvReport,
    RetryCsvReport,
    GetAcceptanceCoefficients,
    GetBoxTariffs,
    GetCommission,
    GetPalletTariffs,
    GetReturnTariffs,
    GetDocumentCategories,
    GetBalance,
    GetDocumentsList,
    GetRealizationReport,
    DownloadDocument,
    DownloadDocumentsAll,
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
    GetNewOrdersCCResponse,
    GetOrdersCCResponse,
    ClientInfoCCResp,
    OrderStatusesCCResp,
    GetStickersCCResponse,
    GetOrderMetaCCResponse,
    CountResponse,
    GetAdvertsResponse,
    BalanceResponse,
    BudgetResponse,
    DepositResponse,
    UpdItem,
    FullStatsItem,
    UnseenFQ,
    GetQuestionsData,
    GetFeedbacksData,
    ChatItem,
    ChatEventsResult,
    GetClaimsResponse,
    Good,
    OptionsResultModel,
    WarehouseItemFBW,
    TransitTariff,
    SuppliesFiltersRequest,
    SupplyFBW,
    SupplyDetailsFBW,
    GoodInSupplyFBW,
    BoxFBW,
    CommissionResponse,
    AcceptanceCoefficient,
    SalesItem,
    MeasurementPenaltiesResponse,
    DeductionsResponse,
    BannedProductItem,
    BalanceData,
    DetailReportItem,
    WarehousesBoxRates,
    WarehousesPalletRates,
    WarehousesReturnRates,
    DocumentDownloadItem,
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

    # ==========================================
    # ИНТЕГРАЦИЯ C&C: Самовывоз из магазина
    # ==========================================

    async def get_new_orders_cc(
        self, request_timeout: Optional[int] = None
    ) -> GetNewOrdersCCResponse:
        """
        Получение списка новых заказов Самовывоз из магазина (Click & Collect).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        return await self(GetNewOrdersCC(), request_timeout=request_timeout)

    async def get_orders_cc(
        self,
        date_from: int,
        date_to: int,
        limit: int = 1000,
        next_cursor: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetOrdersCCResponse:
        """
        Получение завершенных или отмененных заказов (Click & Collect).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrdersCC(
            dateFrom=date_from, dateTo=date_to, limit=limit, next=next_cursor
        )
        return await self(call, request_timeout=request_timeout)

    async def get_orders_statuses_cc(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> OrderStatusesCCResp:
        """
        Получение актуальных статусов заказов Click & Collect.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrdersStatusesCC(orders=orders)
        return await self(call, request_timeout=request_timeout)

    async def deliver_order_cc(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Перевод заказа Самовывоз из магазина в статус "Выдан" (deliver).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = DeliverOrderCC(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def cancel_order_cc(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Отмена заказа Самовывоз из магазина продавцом (cancel).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = CancelOrderCC(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def get_order_stickers_cc(
        self,
        orders: List[int],
        sticker_type: str = "png",
        width: int = 58,
        height: int = 40,
        request_timeout: Optional[int] = None,
    ) -> GetStickersCCResponse:
        """
        Получение этикеток для заказов Самовывоз из магазина.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrderStickersCC(
            orders=orders, type=sticker_type, width=width, height=height
        )
        return await self(call, request_timeout=request_timeout)

    async def get_buyer_info_cc(
        self, orders: List[int], request_timeout: Optional[int] = None
    ) -> ClientInfoCCResp:
        """
        Получение информации о покупателе для заказов Самовывоз из магазина.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetBuyerInfoCC(orders=orders)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # C&C: УПРАВЛЕНИЕ МЕТАДАННЫМИ
    # ==========================================

    async def get_order_meta_cc(
        self, order_id: int, request_timeout: Optional[int] = None
    ) -> GetOrderMetaCCResponse:
        """
        Получение привязанных метаданных (УИН, КиЗ, IMEI, GTIN) заказа C&C.

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = GetOrderMetaCC(order_id=order_id)
        return await self(call, request_timeout=request_timeout)

    async def delete_order_meta_cc(
        self, order_id: int, key: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Удаление метаданных заказа C&C по ключу (imei, uin, gtin, sgtin).

        ⚠️ ЛИМИТЫ: 300 запросов в 1 минуту с шагом 200 мс (Burst: 20 запросов).
        """
        call = DeleteOrderMetaCC(order_id=order_id, key=key)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_sgtin_cc(
        self, order_id: int, sgtins: List[str], request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление кодов Data Matrix (Честный ЗНАК) к заказу C&C.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaSgtinCC(order_id=order_id, sgtins=sgtins)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_uin_cc(
        self, order_id: int, uin: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление УИНа к заказу C&C.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaUinCC(order_id=order_id, uin=uin)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_imei_cc(
        self, order_id: int, imei: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление IMEI к заказу C&C.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaImeiCC(order_id=order_id, imei=imei)
        return await self(call, request_timeout=request_timeout)

    async def update_order_meta_gtin_cc(
        self, order_id: int, gtin: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Добавление GTIN (РБ) к заказу C&C.

        ⚠️ ЛИМИТЫ: 1000 запросов в 1 минуту с шагом 60 мс (Burst: 20 запросов).
        """
        call = UpdateOrderMetaGtinCC(order_id=order_id, gtin=gtin)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # FBW: ФОРМИРОВАНИЕ ПОСТАВОК
    # ==========================================

    async def get_acceptance_options(
        self,
        items: List[Good],
        warehouse_id: Optional[int] = None,
        request_timeout: Optional[int] = None,
    ) -> OptionsResultModel:
        """
        Получение информации о доступных складах и типах упаковки для поставки.
        Список складов определяется по штрихкоду и количеству товара.

        ⚠️ ЛИМИТЫ: 6 запросов в 10 секунд (Burst: 6 запросов).

        :param items: Список товаров с их количеством (модель Good).
        :param warehouse_id: ID конкретного склада (опционально, если нужно проверить один склад).
        """
        call = GetAcceptanceOptions(items=items, warehouseID=warehouse_id)
        return await self(call, request_timeout=request_timeout)

    async def get_warehouses_fbw(
        self, request_timeout: Optional[int] = None
    ) -> List[WarehouseItemFBW]:
        """
        Получение списка складов Wildberries.

        ⚠️ ЛИМИТЫ: 6 запросов в 10 секунд (Burst: 6 запросов).
        """
        return await self(GetWarehousesFBW(), request_timeout=request_timeout)

    async def get_transit_tariffs(
        self, request_timeout: Optional[int] = None
    ) -> List[TransitTariff]:
        """
        Получение информации о доступных транзитных направлениях и их тарифах.

        ⚠️ ЛИМИТЫ: 6 запросов в 10 секунд (Burst: 10 запросов).
        """
        return await self(GetTransitTariffs(), request_timeout=request_timeout)

    # ==========================================
    # FBW: ИНФОРМАЦИЯ О ПОСТАВКАХ
    # ==========================================

    async def get_supplies_fbw(
        self,
        filter_data: SuppliesFiltersRequest,
        limit: int = 1000,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> List[SupplyFBW]:
        """
        Получение списка поставок FBW (со склада WB). По умолчанию возвращаются последние 1000 поставок.

        ⚠️ ЛИМИТЫ: 30 запросов в 2 секунды (Burst: 10 запросов).

        :param filter_data: Данные для фильтрации по датам и статусам (SuppliesFiltersRequest).
        :param limit: Количество возвращаемых элементов (максимум 1000).
        :param offset: Смещение для пагинации.
        """
        call = GetSuppliesFBW(filter_data=filter_data, limit=limit, offset=offset)
        return await self(call, request_timeout=request_timeout)

    async def get_supply_details_fbw(
        self,
        supply_id: int,
        is_preorder_id: bool = False,
        request_timeout: Optional[int] = None,
    ) -> SupplyDetailsFBW:
        """
        Получение детализации конкретной поставки.

        ⚠️ ЛИМИТЫ: 30 запросов в 2 секунды (Burst: 10 запросов).

        :param supply_id: ID поставки (или ID заказа, если is_preorder_id=True).
        :param is_preorder_id: Установите True, если ищете по ID заказа (незапланированной поставки).
        """
        call = GetSupplyDetailsFBW(supply_id=supply_id, is_preorder_id=is_preorder_id)
        return await self(call, request_timeout=request_timeout)

    async def get_supply_goods_fbw(
        self,
        supply_id: int,
        limit: int = 100,
        offset: int = 0,
        is_preorder_id: bool = False,
        request_timeout: Optional[int] = None,
    ) -> List[GoodInSupplyFBW]:
        """
        Получение списка товаров (и их статусов приемки), которые находятся в поставке.

        ⚠️ ЛИМИТЫ: 30 запросов в 2 секунды (Burst: 10 запросов).
        """
        call = GetSupplyGoodsFBW(
            supply_id=supply_id,
            limit=limit,
            offset=offset,
            is_preorder_id=is_preorder_id,
        )
        return await self(call, request_timeout=request_timeout)

    async def get_supply_package_fbw(
        self,
        supply_id: int,
        request_timeout: Optional[int] = None,
    ) -> List[BoxFBW]:
        """
        Получение информации об упаковке поставки (коробах и штрихкодах внутри них).

        ⚠️ ЛИМИТЫ: 30 запросов в 2 секунды (Burst: 10 запросов).
        """
        call = GetSupplyPackageFBW(supply_id=supply_id)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # PROMOTION: УПРАВЛЕНИЕ КАМПАНИЯМИ
    # ==========================================

    async def get_campaigns_count(
        self, request_timeout: Optional[int] = None
    ) -> CountResponse:
        """
        Получение списков кампаний, сгруппированных по типу и статусу.

        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).
        """
        return await self(GetCampaignsCount(), request_timeout=request_timeout)

    async def get_adverts_info(
        self,
        ids: Optional[List[int]] = None,
        statuses: Optional[List[int]] = None,
        payment_type: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> GetAdvertsResponse:
        """
        Получение детальной информации о кампаниях.

        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).

        :param ids: Список ID кампаний (до 50 шт).
        :param statuses: Список статусов (-1, 4, 7, 8, 9, 11).
        :param payment_type: Тип оплаты (cpm, cpc).
        """
        ids_str = ",".join(map(str, ids)) if ids else None
        statuses_str = ",".join(map(str, statuses)) if statuses else None

        call = GetAdverts(ids=ids_str, statuses=statuses_str, payment_type=payment_type)
        return await self(call, request_timeout=request_timeout)

    async def rename_campaign(
        self, advert_id: int, new_name: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Переименование кампании (до 100 символов).
        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).
        """
        call = RenameCampaign(advertId=advert_id, name=new_name)
        return await self(call, request_timeout=request_timeout)

    async def start_campaign(
        self, advert_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Запуск кампании (из статусов 4 и 11).
        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).
        """
        return await self(StartCampaign(id=advert_id), request_timeout=request_timeout)

    async def pause_campaign(
        self, advert_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Приостановка кампании (из статуса 9).
        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).
        """
        return await self(PauseCampaign(id=advert_id), request_timeout=request_timeout)

    async def stop_campaign(
        self, advert_id: int, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Полная остановка (завершение) кампании.
        ⚠️ ЛИМИТЫ: 5 запросов в 1 секунду (Burst: 5).
        """
        return await self(StopCampaign(id=advert_id), request_timeout=request_timeout)

    # ==========================================
    # PROMOTION: ФИНАНСЫ И БЮДЖЕТ
    # ==========================================

    async def get_balance(
        self, request_timeout: Optional[int] = None
    ) -> BalanceResponse:
        """
        Получение баланса, счета и бонусов продавца.
        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5).
        """
        return await self(GetBalance(), request_timeout=request_timeout)

    async def get_campaign_budget(
        self, advert_id: int, request_timeout: Optional[int] = None
    ) -> BudgetResponse:
        """
        Получение бюджета конкретной кампании.
        ⚠️ ЛИМИТЫ: 4 запроса в 1 секунду (Burst: 4).
        """
        return await self(GetBudget(id=advert_id), request_timeout=request_timeout)

    async def deposit_campaign_budget(
        self,
        advert_id: int,
        amount: int,
        source_type: int = 1,
        request_timeout: Optional[int] = None,
    ) -> DepositResponse:
        """
        Пополнение бюджета кампании. Сумма должна быть кратна 50 руб.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5).

        :param amount: Сумма пополнения (минимум 1000 руб).
        :param source_type: Источник (0 - Счет, 1 - Баланс, 3 - Бонусы).
        """
        call = DepositBudget(id=advert_id, sum=amount, type=source_type)
        return await self(call, request_timeout=request_timeout)

    async def get_costs_history(
        self, date_from: str, date_to: str, request_timeout: Optional[int] = None
    ) -> List[UpdItem]:
        """
        Получение истории затрат (списаний) за период (максимум 31 день).
        Формат дат: YYYY-MM-DD.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 секунду (Burst: 5).
        """
        call = GetUpd(from_date=date_from, to_date=date_to)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # PROMOTION: СТАТИСТИКА И КАЛЕНДАРЬ
    # ==========================================

    async def get_campaigns_full_stats(
        self,
        advert_ids: List[int],
        date_from: str,
        date_to: str,
        request_timeout: Optional[int] = None,
    ) -> List[FullStatsItem]:
        """
        Получение полной ежедневной статистики по кампаниям.
        Период: максимум 31 день. Формат: YYYY-MM-DD.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту с шагом 20 сек (Burst: 1).
        """
        ids_str = ",".join(map(str, advert_ids))
        call = GetFullStats(ids=ids_str, beginDate=date_from, endDate=date_to)
        return await self(call, request_timeout=request_timeout)

    async def get_calendar_promotions(
        self,
        start_date: str,
        end_date: str,
        all_promo: bool = False,
        limit: int = 10,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Получение списка доступных акций в Календаре WB.
        Формат дат: YYYY-MM-DDTHH:MM:SSZ

        ⚠️ ЛИМИТЫ: 10 запросов в 6 секунд (Burst: 5).
        """
        call = GetCalendarPromotions(
            startDateTime=start_date,
            endDateTime=end_date,
            allPromo=all_promo,
            limit=limit,
            offset=offset,
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # ОТЗЫВЫ И ВОПРОСЫ
    # ==========================================

    async def get_unseen_feedbacks_questions(
        self, request_timeout: Optional[int] = None
    ) -> UnseenFQ:
        """
        Проверка наличия новых (непросмотренных) вопросов и отзывов.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 секунду с шагом 333 мс (Burst: 6 запросов).
        """
        result = await self(GetUnseenFQ(), request_timeout=request_timeout)
        return result.data

    async def get_questions(
        self,
        is_answered: bool,
        take: int = 100,
        skip: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetQuestionsData:
        """
        Получение списка вопросов. Максимум 10 000 вопросов за запрос.
        Сумма take + skip не должна превышать 10 000.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 секунду с шагом 333 мс (Burst: 6 запросов).
        """
        call = GetQuestions(isAnswered=is_answered, take=take, skip=skip)
        result = await self(call, request_timeout=request_timeout)
        return result.data

    async def answer_question(
        self, question_id: str, text: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Ответ на вопрос покупателя.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 секунду с шагом 333 мс (Burst: 6 запросов).
        """
        call = PatchQuestion(id=question_id, answer={"text": text}, state="wbRu")
        await self(call, request_timeout=request_timeout)
        return True

    async def get_feedbacks(
        self,
        is_answered: bool,
        take: int = 100,
        skip: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetFeedbacksData:
        """
        Получение списка отзывов с пагинацией (максимум 5 000 отзывов).

        ⚠️ ЛИМИТЫ: 3 запроса в 1 секунду с шагом 333 мс (Burst: 6 запросов).
        """
        call = GetFeedbacks(isAnswered=is_answered, take=take, skip=skip)
        result = await self(call, request_timeout=request_timeout)
        return result.data

    async def answer_feedback(
        self, feedback_id: str, text: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Отправка ответа на отзыв покупателя.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 секунду с шагом 333 мс (Burst: 6 запросов).
        """
        call = AnswerFeedback(id=feedback_id, text=text)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # ЧАТЫ С ПОКУПАТЕЛЯМИ
    # ==========================================

    async def get_seller_chats(
        self, request_timeout: Optional[int] = None
    ) -> List[ChatItem]:
        """
        Получение списка всех чатов продавца с покупателями.

        ⚠️ ЛИМИТЫ: 10 запросов в 10 секунд (Burst: 10 запросов).
        """
        result = await self(GetChats(), request_timeout=request_timeout)
        return result.result

    async def get_chat_events(
        self, next_cursor: Optional[int] = None, request_timeout: Optional[int] = None
    ) -> ChatEventsResult:
        """
        Получение списка новых событий (сообщений) из всех чатов.
        Для получения всех сообщений передавайте next_cursor из предыдущего ответа, пока totalEvents не станет 0.

        ⚠️ ЛИМИТЫ: 10 запросов в 10 секунд (Burst: 10 запросов).
        """
        call = GetChatEvents(next=next_cursor)
        result = await self(call, request_timeout=request_timeout)
        return result.result

    async def send_chat_message(
        self, reply_sign: str, message: str, request_timeout: Optional[int] = None
    ) -> bool:
        """
        Отправка текстового сообщения в чат покупателю.
        Для прикрепления файлов требуется модификация aiohttp сессии (поддержка FormData).

        ⚠️ ЛИМИТЫ: 10 запросов в 10 секунд (Burst: 10 запросов).
        """
        call = SendChatMessage(replySign=reply_sign, message=message)
        await self(call, request_timeout=request_timeout)
        return True

    # ==========================================
    # ЗАЯВКИ НА ВОЗВРАТ (Брак)
    # ==========================================

    async def get_claims(
        self,
        is_archive: bool,
        limit: int = 50,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> GetClaimsResponse:
        """
        Получение заявок покупателей на возврат товара. Заявки хранятся 14 дней.

        ⚠️ ЛИМИТЫ: 20 запросов в 1 минуту с шагом 3 сек (Burst: 10 запросов).

        :param is_archive: False - на рассмотрении, True - в архиве.
        """
        call = GetClaims(is_archive=is_archive, limit=limit, offset=offset)
        return await self(call, request_timeout=request_timeout)

    async def answer_claim(
        self,
        claim_id: str,
        action: str,
        comment: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> bool:
        """
        Ответ (решение) на заявку о возврате брака.

        ⚠️ ЛИМИТЫ: 20 запросов в 1 минуту с шагом 3 сек (Burst: 10 запросов).

        :param action: Действие (например, 'approve1' - вернуть деньги после возврата товара, 'reject1' - отказ и т.д.).
        :param comment: Комментарий продавца (обязателен при action='rejectcustom').
        """
        call = AnswerClaim(id=claim_id, action=action, comment=comment)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # ТАРИФЫ И КОЭФФИЦИЕНТЫ (Tariffs)
    # ==========================================

    async def get_commission(
        self, locale: str = "ru", request_timeout: Optional[int] = None
    ) -> CommissionResponse:
        """
        Получение комиссий WB по категориям товаров (по всем моделям продаж).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 2 запроса).

        :param locale: Язык ответа (ru, en, zh).
        """
        call = GetCommission(locale=locale)
        return await self(call, request_timeout=request_timeout)

    async def get_box_tariffs(
        self, date: str, request_timeout: Optional[int] = None
    ) -> WarehousesBoxRates:
        """
        Получение тарифов на логистику и хранение для коробов (соответствуют тарифам Суперсейф).

        ⚠️ ЛИМИТЫ: 60 запросов в 1 минуту с шагом 1 сек (Burst: 5 запросов).

        :param date: Дата тарифов в формате 'YYYY-MM-DD'.
        :return: Возвращает развернутый объект WarehousesBoxRates напрямую.
        """
        call = GetBoxTariffs(date=date)
        result = await self(call, request_timeout=request_timeout)
        return result.response.data

    async def get_pallet_tariffs(
        self, date: str, request_timeout: Optional[int] = None
    ) -> WarehousesPalletRates:
        """
        Получение тарифов на логистику и хранение для паллет.

        ⚠️ ЛИМИТЫ: 60 запросов в 1 минуту с шагом 1 сек (Burst: 5 запросов).

        :param date: Дата тарифов в формате 'YYYY-MM-DD'.
        :return: Возвращает развернутый объект WarehousesPalletRates напрямую.
        """
        call = GetPalletTariffs(date=date)
        result = await self(call, request_timeout=request_timeout)
        return result.response.data

    async def get_return_tariffs(
        self, date: str, request_timeout: Optional[int] = None
    ) -> WarehousesReturnRates:
        """
        Получение тарифов на возврат товаров продавцу и обратную логистику невостребованных товаров.

        ⚠️ ЛИМИТЫ: 60 запросов в 1 минуту с шагом 1 сек (Burst: 5 запросов).

        :param date: Дата тарифов в формате 'YYYY-MM-DD'.
        :return: Возвращает развернутый объект WarehousesReturnRates напрямую.
        """
        call = GetReturnTariffs(date=date)
        result = await self(call, request_timeout=request_timeout)
        return result.response.data

    async def get_acceptance_coefficients(
        self,
        warehouse_ids: Optional[List[int]] = None,
        request_timeout: Optional[int] = None,
    ) -> List[AcceptanceCoefficient]:
        """
        Получение коэффициентов приемки (стоимости приемки) на складах на ближайшие 14 дней.
        Если коэффициент = -1, приемка закрыта. Приемка доступна только если (coefficient = 0 или 1) И (allowUnload = true).

        ⚠️ ЛИМИТЫ: 6 запросов в 1 минуту с шагом 10 сек (Burst: 6 запросов).

        :param warehouse_ids: Список ID складов. Если не передавать, вернет по всем складам.
        """
        ids_str = ",".join(map(str, warehouse_ids)) if warehouse_ids else None
        call = GetAcceptanceCoefficients(warehouseIDs=ids_str)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # ANALYTICS: ВОРОНКА ПРОДАЖ И ПОИСК
    # ==========================================

    async def get_sales_funnel_products(
        self, payload: dict, request_timeout: Optional[int] = None
    ) -> dict:
        """
        Статистика карточек товаров за период (Воронка продаж).

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).
        Обновление данных: 1 раз в час.

        :param payload: Словарь с параметрами запроса (модель FunnelProductsRequest).
        """
        # Динамически создаем класс с переданными параметрами и распаковываем их
        call = type(
            "DynamicFunnelProducts",
            (GetFunnelProducts,),
            {"__annotations__": {k: Any for k in payload}},
        )(**payload)
        res = await self(call, request_timeout=request_timeout)
        return res.data

    async def get_search_main_report(
        self, payload: dict, request_timeout: Optional[int] = None
    ) -> dict:
        """
        Данные для главной страницы отчета по поисковым запросам.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).

        :param payload: Словарь с параметрами запроса (модель SearchMainRequest).
        """
        call = type(
            "DynamicSearchReport",
            (GetSearchMainReport,),
            {"__annotations__": {k: Any for k in payload}},
        )(**payload)
        res = await self(call, request_timeout=request_timeout)
        return res.data

    # ==========================================
    # ANALYTICS: ОСТАТКИ (Stocks)
    # ==========================================

    async def get_analytics_stocks_wb(
        self,
        nm_ids: Optional[List[int]] = None,
        limit: int = 250000,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> List[dict]:
        """
        Остатки товаров на складах WB с детализацией по складам и размерам.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 1).
        Обновление данных: 1 раз в 30 минут.
        """
        call = GetStocksWbWarehouses(nmIds=nm_ids, limit=limit, offset=offset)
        res = await self(call, request_timeout=request_timeout)
        return res.data.get("items", [])

    async def get_analytics_stocks_groups(
        self, payload: dict, request_timeout: Optional[int] = None
    ) -> dict:
        """
        Сводные данные по остаткам (Stocks Report -> Group Data).

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).
        """
        call = type(
            "DynamicStocksGroup",
            (GetStocksGroups,),
            {"__annotations__": {k: Any for k in payload}},
        )(**payload)
        res = await self(call, request_timeout=request_timeout)
        return res.data

    # ==========================================
    # ANALYTICS: ГЕНЕРАЦИЯ ОТЧЕТОВ (CSV Downloads)
    # ==========================================

    async def create_csv_report_task(
        self,
        task_id: str,
        report_type: str,
        params: dict,
        user_report_name: Optional[str] = None,
        request_timeout: Optional[int] = None,
    ) -> str:
        """
        Создание задачи на генерацию отчета (CSV в ZIP-архиве).

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).

        :param task_id: Уникальный UUID задачи, генерируется вами.
        :param report_type: Тип отчета (например, DETAIL_HISTORY_REPORT, STOCK_HISTORY_REPORT_CSV).
        :param params: Параметры отчета.
        :return: Строка с подтверждением старта генерации.
        """
        call = CreateCsvReport(
            id=task_id,
            reportType=report_type,
            userReportName=user_report_name,
            params=params,
        )
        res = await self(call, request_timeout=request_timeout)
        return res.data

    async def get_csv_reports_list(self, request_timeout: Optional[int] = None) -> list:
        """
        Список созданных отчетов и их статусы (WAITING, PROCESSING, SUCCESS, FAILED).

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).
        """
        res = await self(GetCsvReportsList(), request_timeout=request_timeout)
        return res.data

    async def retry_csv_report_task(
        self, download_id: str, request_timeout: Optional[int] = None
    ) -> str:
        """
        Перезапуск упавшей задачи на генерацию отчета.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).
        """
        res = await self(
            RetryCsvReport(downloadId=download_id), request_timeout=request_timeout
        )
        return res.data

    async def download_csv_report_file(
        self, download_id: str, request_timeout: Optional[int] = None
    ) -> bytes:
        """
        Скачивание готового отчета.
        Возвращает бинарные данные (ZIP-архив, внутри которого лежит CSV). Отчет хранится 48 часов.

        ⚠️ ЛИМИТЫ: 3 запроса в 1 минуту (Burst: 3).

        :param download_id: ID отчета (UUID).
        :return: bytes (сырые данные zip файла). Вы можете сохранить их через `with open('report.zip', 'wb') as f: f.write(result)`
        """
        call = GetReportFile(download_id=download_id)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # REPORTS: ПРОДАЖИ (Синхронные)
    # ==========================================

    async def get_sales_report(
        self, date_from: str, flag: int = 0, request_timeout: Optional[int] = None
    ) -> List[SalesItem]:
        """
        Получение информации о продажах и возвратах.

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 1).

        :param date_from: Дата в формате RFC3339 (например, "2019-06-20T23:59:59").
        :param flag: 0 - получить измененные с даты (макс 80 000 строк). 1 - за конкретный день.
        """
        call = GetSales(dateFrom=date_from, flag=flag)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # REPORTS: АСИНХРОННЫЕ ОТЧЕТЫ (Платное хранение)
    # ==========================================

    async def create_paid_storage_report(
        self, date_from: str, date_to: str, request_timeout: Optional[int] = None
    ) -> str:
        """
        Создание задачи на генерацию отчета "Платное хранение" (период максимум 8 дней).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 5).

        :return: task_id (UUID задачи)
        """
        call = CreatePaidStorageReport(dateFrom=date_from, dateTo=date_to)
        res = await self(call, request_timeout=request_timeout)
        return res.data.task_id

    async def get_paid_storage_status(
        self, task_id: str, request_timeout: Optional[int] = None
    ) -> str:
        """
        Получение статуса задачи на отчет "Платное хранение".
        Возможные статусы: new, processing, done, purged, canceled.

        ⚠️ ЛИМИТЫ: 1 запрос в 5 секунд.
        """
        call = GetPaidStorageStatus(task_id=task_id)
        res = await self(call, request_timeout=request_timeout)
        return res.data.status

    async def download_paid_storage_report(
        self, task_id: str, request_timeout: Optional[int] = None
    ) -> List[dict]:
        """
        Скачивание готового отчета "Платное хранение".

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту.
        """
        call = GetPaidStorageFile(task_id=task_id)
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # REPORTS: УДЕРЖАНИЯ И ШТРАФЫ
    # ==========================================

    async def get_measurement_penalties(
        self,
        date_to: str,
        date_from: Optional[str] = None,
        limit: int = 330,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> MeasurementPenaltiesResponse:
        """
        Отчет "Коэффициент логистики и хранения" (удержания за габариты).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту.
        """
        call = GetMeasurementPenalties(
            dateFrom=date_from, dateTo=date_to, limit=limit, offset=offset
        )
        return await self(call, request_timeout=request_timeout)

    async def get_deductions_report(
        self,
        date_to: str,
        date_from: Optional[str] = None,
        limit: int = 330,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> DeductionsResponse:
        """
        Отчет "Подмены и неверные вложения" (штрафы).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту.
        """
        call = GetDeductions(
            dateFrom=date_from, dateTo=date_to, limit=limit, offset=offset
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # REPORTS: СКРЫТЫЕ / ЗАБЛОКИРОВАННЫЕ КАРТОЧКИ
    # ==========================================

    async def get_blocked_products(
        self,
        sort: str = "nmId",
        order: str = "asc",
        request_timeout: Optional[int] = None,
    ) -> List[BannedProductItem]:
        """
        Список заблокированных карточек товаров.

        ⚠️ ЛИМИТЫ: 1 запрос в 10 секунд (Burst: 6).
        """
        call = GetBlockedProducts(sort=sort, order=order)
        res = await self(call, request_timeout=request_timeout)
        return res.report

    async def get_shadowed_products(
        self,
        sort: str = "nmId",
        order: str = "asc",
        request_timeout: Optional[int] = None,
    ) -> List[BannedProductItem]:
        """
        Список скрытых из каталога карточек товаров (Теневой бан).

        ⚠️ ЛИМИТЫ: 1 запрос в 10 секунд (Burst: 6).
        """
        call = GetShadowedProducts(sort=sort, order=order)
        res = await self(call, request_timeout=request_timeout)
        return res.report

    # ==========================================
    # FINANCES: БАЛАНС И ОТЧЕТЫ
    # ==========================================

    async def get_seller_balance(
        self, request_timeout: Optional[int] = None
    ) -> BalanceData:
        """
        Получение баланса продавца (данные виджета на главной странице).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 1).
        """
        return await self(GetBalance(), request_timeout=request_timeout)

    async def get_realization_report(
        self,
        date_from: str,
        date_to: str,
        rrdid: int = 0,
        limit: int = 100000,
        period: str = "weekly",
        request_timeout: Optional[int] = None,
    ) -> List[DetailReportItem]:
        """
        Получение детализации отчета о реализации.
        Отчет может быть большим, поэтому для получения всех данных нужно использовать пагинацию
        через параметр `rrdid` (брать rrd_id из последней строки предыдущего ответа).

        ⚠️ ЛИМИТЫ: 1 запрос в 1 минуту (Burst: 1).

        :param date_from: Дата начала (RFC3339).
        :param date_to: Дата конца (RFC3339).
        :param rrdid: ID последней строки (для пагинации). Для первого запроса = 0.
        :param period: weekly (еженедельный) или daily (ежедневный).
        """
        call = GetRealizationReport(
            dateFrom=date_from, dateTo=date_to, limit=limit, rrdid=rrdid, period=period
        )
        return await self(call, request_timeout=request_timeout)

    # ==========================================
    # DOCUMENTS: ЗАКРЫВАЮЩИЕ ДОКУМЕНТЫ
    # ==========================================

    async def get_document_categories(
        self, locale: str = "ru", request_timeout: Optional[int] = None
    ) -> list:
        """
        Получение списка категорий документов.

        ⚠️ ЛИМИТЫ: 1 запрос в 10 секунд (Burst: 5).
        """
        res = await self(
            GetDocumentCategories(locale=locale), request_timeout=request_timeout
        )
        return res.data.get("categories", [])

    async def get_documents_list(
        self,
        begin_time: Optional[str] = None,
        end_time: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
        request_timeout: Optional[int] = None,
    ) -> list:
        """
        Получение списка документов продавца.

        ⚠️ ЛИМИТЫ: 1 запрос в 10 секунд (Burst: 5).
        """
        call = GetDocumentsList(
            beginTime=begin_time,
            endTime=end_time,
            category=category,
            limit=limit,
            offset=offset,
        )
        res = await self(call, request_timeout=request_timeout)
        return res.data.get("documents", [])

    async def download_document(
        self, service_name: str, extension: str, request_timeout: Optional[int] = None
    ) -> DocumentDownloadItem:
        """
        Получение одного документа. Возвращает объект, содержащий base64 строку с файлом.

        ⚠️ ЛИМИТЫ: 1 запрос в 10 секунд (Burst: 5).
        """
        call = DownloadDocument(serviceName=service_name, extension=extension)
        res = await self(call, request_timeout=request_timeout)
        return res.data

    async def download_documents_bulk(
        self, documents: List[dict], request_timeout: Optional[int] = None
    ) -> DocumentDownloadItem:
        """
        Скачивание нескольких документов одним архивом (до 50 шт).
        Возвращает объект, содержащий base64 строку с ZIP архивом.

        ⚠️ ЛИМИТЫ: 1 запрос в 5 минут (Burst: 5).

        :param documents: Список словарей вида [{"serviceName": "...", "extension": "zip"}, ...]
        """
        params = [
            {"serviceName": doc["serviceName"], "extension": doc["extension"]}
            for doc in documents
        ]
        call = DownloadDocumentsAll(params=params)
        res = await self(call, request_timeout=request_timeout)
        return res.data
