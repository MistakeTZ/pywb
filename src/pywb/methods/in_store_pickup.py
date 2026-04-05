from typing import ClassVar, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    GetNewOrdersCCResponse,
    GetOrdersCCResponse,
    ClientInfoCCResp,
    OrderStatusesCCResp,
    GetStickersCCResponse,
    GetOrderMetaCCResponse,
)

# ==========================================
# СБОРОЧНЫЕ ЗАДАНИЯ (Orders)
# ==========================================
class GetNewOrdersCC(WBMethod[GetNewOrdersCCResponse]):
    """Получение списка новых заказов Click & Collect."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/click-collect/orders/new"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetNewOrdersCCResponse
class GetOrdersCC(WBMethod[GetOrdersCCResponse]):
    """Получение списка завершенных или отмененных заказов Click & Collect."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/click-collect/orders"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersCCResponse

    date_from: int = Field(alias="dateFrom")
    date_to: int = Field(alias="dateTo")
    limit: int = 1000
    next: int = 0
class GetOrdersStatusesCC(WBMethod[OrderStatusesCCResp]):
    """Получение актуальных статусов заказов Click & Collect."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/click-collect/orders/status"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = OrderStatusesCCResp

    orders: List[int]
class GetOrderStickersCC(WBMethod[GetStickersCCResponse]):
    """Получение этикеток для заказов Click & Collect."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/click-collect/orders/stickers"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetStickersCCResponse

    sticker_type: str = Field(alias="type")
    width: int
    height: int
    orders: List[int]
class GetBuyerInfoCC(WBMethod[ClientInfoCCResp]):
    """Получение информации о покупателе."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/click-collect/orders/client"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = ClientInfoCCResp

    orders: List[int]


# ==========================================
# ИЗМЕНЕНИЕ СТАТУСОВ
# ==========================================
class DeliverOrderCC(WBMethod[bool]):
    """Перевод заказа в статус 'Выдан' (deliver)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/deliver"
class CancelOrderCC(WBMethod[bool]):
    """Отмена заказа продавцом (cancel)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/cancel"


# ==========================================
# МЕТАДАННЫЕ (Маркировка)
# ==========================================
class GetOrderMetaCC(WBMethod[GetOrderMetaCCResponse]):
    """Получение метаданных заказа."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrderMetaCCResponse

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta"
class DeleteOrderMetaCC(WBMethod[bool]):
    """Удаление метаданных заказа по ключу."""

    __http_method__: ClassVar[str] = "DELETE"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    key: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta"
class UpdateOrderMetaSgtinCC(WBMethod[bool]):
    """Установка КИЗов (Честный ЗНАК)."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    sgtins: List[str]

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta/sgtin"
class UpdateOrderMetaUinCC(WBMethod[bool]):
    """Установка УИНа."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    uin: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta/uin"
class UpdateOrderMetaImeiCC(WBMethod[bool]):
    """Установка IMEI."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    imei: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta/imei"
class UpdateOrderMetaGtinCC(WBMethod[bool]):
    """Установка GTIN."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)
    gtin: str

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/click-collect/orders/{self.order_id}/meta/gtin"
