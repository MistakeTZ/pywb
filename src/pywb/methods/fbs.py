from typing import ClassVar, Optional, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    PassOffice,
    CreatePassResponse,
    GetNewOrdersResponse,
    GetOrdersResponse,
    GetOrdersStatusesResponse,
    GetStickersResponse,
    CreateSupplyResponse,
    GetSuppliesResponse,
)


# ==========================================
# ПРОПУСКА (Passes)
# ==========================================
class GetPassOffices(WBMethod[List[PassOffice]]):
    """Получение списка складов, для которых требуется пропуск."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/passes/offices"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = List[PassOffice]


class CreatePass(WBMethod[CreatePassResponse]):
    """Создание пропуска водителя."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/passes"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = CreatePassResponse

    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    car_model: str = Field(alias="carModel")
    car_number: str = Field(alias="carNumber")
    office_id: int = Field(alias="officeId")


# ==========================================
# СБОРОЧНЫЕ ЗАДАНИЯ (Orders)
# ==========================================
class GetNewOrders(WBMethod[GetNewOrdersResponse]):
    """Получение списка НОВЫХ сборочных заданий."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/orders/new"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetNewOrdersResponse


class GetOrdersList(WBMethod[GetOrdersResponse]):
    """Получение сборочных заданий (без статусов) за период до 30 дней."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/orders"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersResponse

    limit: int = 1000
    next: int = 0
    date_from: Optional[int] = Field(None, alias="dateFrom")
    date_to: Optional[int] = Field(None, alias="dateTo")


class GetOrdersStatuses(WBMethod[GetOrdersStatusesResponse]):
    """Получение актуальных статусов сборочных заданий."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/orders/status"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetOrdersStatusesResponse

    orders: List[int]


class CancelOrder(WBMethod[bool]):
    """Отмена заказа продавцом (перевод в статус cancel)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    order_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/orders/{self.order_id}/cancel"


class GetOrderStickers(WBMethod[GetStickersResponse]):
    """Получение этикеток (стикеров) для заказов."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/orders/stickers"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetStickersResponse

    sticker_type: str = Field(alias="type")  # svg, zplv, zplh, png
    width: int
    height: int
    orders: List[int]


# ==========================================
# ПОСТАВКИ (Supplies)
# ==========================================
class CreateSupply(WBMethod[CreateSupplyResponse]):
    """Создание новой поставки."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v3/supplies"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = CreateSupplyResponse

    name: str


class GetSupplies(WBMethod[GetSuppliesResponse]):
    """Получение списка поставок."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/supplies"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = GetSuppliesResponse

    limit: int = 1000
    next: int = 0


class AddOrdersToSupply(WBMethod[bool]):
    """Добавление заказов к поставке (и перевод их в статус confirm)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    supply_id: str = Field(exclude=True)
    orders: List[int]

    @property
    def __api_path__(self) -> str:
        # Внимание: для этого метода WB использует префикс /api/marketplace/v3/
        return f"/api/marketplace/v3/supplies/{self.supply_id}/orders"


class DeliverSupply(WBMethod[bool]):
    """Закрытие поставки и перевод заказов в статус complete (В доставке)."""

    __http_method__: ClassVar[str] = "PATCH"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    supply_id: str = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v3/supplies/{self.supply_id}/deliver"
