from typing import ClassVar, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    GetNewOrdersDBWResponse,
    GetOrdersDBWResponse,
    GetDeliveryDatesDBWResponse,
    GetClientInfoDBWResponse,
    GetOrdersStatusesDBWResponse,
    GetStickersDBWResponse,
    GetCourierInfoDBWResponse,
    GetOrderMetaDBWResponse,
)


# ==========================================
# DBW: ПОЛУЧЕНИЕ ЗАКАЗОВ И ИНФОРМАЦИИ
# ==========================================
class GetNewOrdersDBW(WBMethod[GetNewOrdersDBWResponse]):
    """Получение списка новых заказов DBW."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders/new"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetNewOrdersDBWResponse
class GetOrdersDBW(WBMethod[GetOrdersDBWResponse]):
    """Получение информации по завершенным (отмененным или проданным) заказам."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersDBWResponse

    date_from: int = Field(alias="dateFrom")
    date_to: int = Field(alias="dateTo")
    limit: int = 1000
    next: int = 0
class GetDeliveryDateDBW(WBMethod[GetDeliveryDatesDBWResponse]):
    """Получение даты и времени доставки, выбранных покупателем."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders/delivery-date"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetDeliveryDatesDBWResponse

    orders: List[int]
class GetBuyerInfoDBW(WBMethod[GetClientInfoDBWResponse]):
    """Получение информации о покупателе (для курьерской доставки)."""

    __http_method__: ClassVar[str] = "POST"
    # Внимание: здесь используется префикс /api/marketplace/v3/
    __api_path__: ClassVar[str] = "/api/marketplace/v3/dbw/orders/client"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetClientInfoDBWResponse

    orders: List[int]
class GetOrdersStatusesDBW(WBMethod[GetOrdersStatusesDBWResponse]):
    """Получение актуальных статусов заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders/status"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersStatusesDBWResponse

    orders: List[int]
class GetOrderStickersDBW(WBMethod[GetStickersDBWResponse]):
    """Получение этикеток (стикеров) для заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders/stickers"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetStickersDBWResponse

    sticker_type: str = Field(alias="type")
    width: int
    height: int
    orders: List[int]
class GetCourierInfoDBW(WBMethod[GetCourierInfoDBWResponse]):
    """Получение контактов курьера по ID заказа."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/dbw/orders/courier"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetCourierInfoDBWResponse

    orders: List[int]


# ==========================================
# ИЗМЕНЕНИЕ СТАТУСОВ (Управление)
# ==========================================
class ConfirmOrderDBW(WBMethod[bool]):
    """Перевод заказа в сборку (confirm)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/confirm"
class AssembleOrderDBW(WBMethod[bool]):
    """Перевод заказа в доставку (complete)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/assemble"
class CancelOrderDBW(WBMethod[bool]):
    """Отмена заказа продавцом."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/cancel"


# ==========================================
# УПРАВЛЕНИЕ МЕТАДАННЫМИ (Metadata)
# ==========================================
class GetOrderMetaDBW(WBMethod[GetOrderMetaDBWResponse]):
    """Получение метаданных (IMEI, УИН, КИЗ) заказа."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrderMetaDBWResponse

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta"
class DeleteOrderMetaDBW(WBMethod[bool]):
    """Удаление метаданных заказа по ключу."""

    __http_method__: ClassVar[str] = "DELETE"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    key: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta"
class UpdateOrderMetaSgtinDBW(WBMethod[bool]):
    """Добавление КиЗов (Честный ЗНАК)."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    sgtins: List[str]

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta/sgtin"
class UpdateOrderMetaUinDBW(WBMethod[bool]):
    """Добавление УИНа."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    uin: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta/uin"
class UpdateOrderMetaImeiDBW(WBMethod[bool]):
    """Добавление IMEI."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    imei: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta/imei"
class UpdateOrderMetaGtinDBW(WBMethod[bool]):
    """Добавление GTIN (РБ)."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    gtin: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/dbw/orders/{self.order_id}/meta/gtin"
