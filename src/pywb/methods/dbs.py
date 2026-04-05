from typing import ClassVar, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    GetNewOrdersDBSResponse,
    GetOrdersDBSResponse,
    OrderGroupDBS,
    ClientInfoDBSResp,
    B2BClientInfoResp,
    OrderStatusesV2Resp,
    StatusSetResponsesResp,
    OrderCodeRequestItem,
    GetStickersDBSResponse,
    OrdersMetaResponse,
    UpdateMetaSgtinItem,
    UpdateMetaUinItem,
    UpdateMetaImeiItem,
    UpdateMetaGtinItem,
    UpdateMetaCustomsItem,
    DeliveryDateInfo,
)


# ==========================================
# СБОРОЧНЫЕ ЗАДАНИЯ DBS (Orders)
# ==========================================
class GetNewOrdersDBS(WBMethod[GetNewOrdersDBSResponse]):
    """Получение списка новых заказов DBS."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/dbs/orders/new"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetNewOrdersDBSResponse


class GetOrdersDBS(WBMethod[GetOrdersDBSResponse]):
    """Получение информации по завершенным заказам."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/dbs/orders"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersDBSResponse

    date_from: int = Field(alias="dateFrom")
    date_to: int = Field(alias="dateTo")
    limit: int = 1000
    next: int = 0


class GetOrderGroupsInfoDBS(WBMethod[List[OrderGroupDBS]]):
    """Получение информации о платной доставке для сгруппированных заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbs/groups/info"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = List[OrderGroupDBS]

    groups: List[str]


class GetBuyerInfoDBS(WBMethod[ClientInfoDBSResp]):
    """Получение информации о покупателе (DBS)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbs/orders/client"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = ClientInfoDBSResp

    orders: List[int]


class GetB2BBuyerInfoDBS(WBMethod[B2BClientInfoResp]):
    """Получение данных B2B покупателей (ИНН, КПП, Название)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/b2b/info"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = B2BClientInfoResp

    orders_ids: List[int] = Field(alias="ordersIds")


class GetDeliveryDateDBS(WBMethod[DeliveryDateInfo]):
    """Получение даты и времени доставки."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbs/orders/delivery-date"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = DeliveryDateInfo

    orders: List[int]


class GetOrderStickersDBS(WBMethod[GetStickersDBSResponse]):
    """Получение этикеток (PDF 58x40) для заказов в ПВЗ."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/stickers"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetStickersDBSResponse

    sticker_type: str = Field(alias="type")
    width: int
    height: int
    orders: List[int]


# ==========================================
# ИЗМЕНЕНИЕ СТАТУСОВ (Бачти)
# ==========================================
class GetOrdersStatusesDBS(WBMethod[OrderStatusesV2Resp]):
    """Получение статусов сборочных заданий."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/info"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = OrderStatusesV2Resp

    orders_ids: List[int] = Field(alias="ordersIds")


class CancelOrdersDBS(WBMethod[StatusSetResponsesResp]):
    """Отмена заказов (перевод в cancel)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/cancel"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders_ids: List[int] = Field(alias="ordersIds")


class ConfirmOrdersDBS(WBMethod[StatusSetResponsesResp]):
    """Перевод заказов в сборку (confirm)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/confirm"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders_ids: List[int] = Field(alias="ordersIds")


class DeliverOrdersDBS(WBMethod[StatusSetResponsesResp]):
    """Перевод заказов в доставку (deliver)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/deliver"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders_ids: List[int] = Field(alias="ordersIds")


class ReceiveOrdersDBS(WBMethod[StatusSetResponsesResp]):
    """Подтверждение получения заказа покупателем (receive)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/receive"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[OrderCodeRequestItem]


class RejectOrdersDBS(WBMethod[StatusSetResponsesResp]):
    """Отказ покупателя от заказа при получении (reject)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/status/reject"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[OrderCodeRequestItem]


# ==========================================
# МЕТАДАННЫЕ (Бачти)
# ==========================================
class GetOrdersMetaDBS(WBMethod[OrdersMetaResponse]):
    """Получение метаданных заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/info"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = OrdersMetaResponse

    orders_ids: List[int] = Field(alias="ordersIds")


class DeleteOrdersMetaDBS(WBMethod[StatusSetResponsesResp]):
    """Удаление метаданных заказов по ключу."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/delete"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    key: str
    order_ids: List[int] = Field(alias="orderIds")


class UpdateOrdersMetaSgtinDBS(WBMethod[StatusSetResponsesResp]):
    """Установка КИЗов (Честный ЗНАК) для списка заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/sgtin"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[UpdateMetaSgtinItem]


class UpdateOrdersMetaUinDBS(WBMethod[StatusSetResponsesResp]):
    """Установка УИНов для списка заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/uin"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[UpdateMetaUinItem]


class UpdateOrdersMetaImeiDBS(WBMethod[StatusSetResponsesResp]):
    """Установка IMEI для списка заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/imei"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[UpdateMetaImeiItem]


class UpdateOrdersMetaGtinDBS(WBMethod[StatusSetResponsesResp]):
    """Установка GTIN для списка заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbs/orders/meta/gtin"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = StatusSetResponsesResp

    orders: List[UpdateMetaGtinItem]


class UpdateOrdersMetaCustomsDBS(WBMethod[bool]):
    """Установка Таможенных деклараций."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = (
        "/api/marketplace/v3/dbs/orders/meta/customs-declaration"
    )
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    orders: List[UpdateMetaCustomsItem]
