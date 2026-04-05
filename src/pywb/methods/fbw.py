from typing import ClassVar, List, Optional
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    Good,
    OptionsResultModel,
    WarehouseItemFBW,
    TransitTariff,
    SuppliesFiltersRequest,
    SupplyFBW,
    SupplyDetailsFBW,
    GoodInSupplyFBW,
    BoxFBW,
)

# ==========================================
# ФОРМИРОВАНИЕ ПОСТАВОК
# ==========================================
class GetAcceptanceOptions(WBMethod[OptionsResultModel]):
    """Получение информации о доступных складах и типах упаковки."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v1/acceptance/options"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = OptionsResultModel

    # Query params
    warehouse_id: Optional[int] = Field(None, alias="warehouseID", exclude=True)

    # Body params
    items: List[Good]

    @property
    def __api_path__(self) -> str:
        # Если warehouse_id указан, добавляем его в URL как query параметр
        if self.warehouse_id:
            return f"/api/v1/acceptance/options?warehouseID={self.warehouse_id}"
        return "/api/v1/acceptance/options"

    def model_dump(self, **kwargs):
        # Метод требует список объектов напрямую в Body, а не ключ "items"
        # Поэтому мы переопределяем дамп, чтобы клиент отправил список
        return [item.model_dump(by_alias=True) for item in self.items]
class GetWarehousesFBW(WBMethod[List[WarehouseItemFBW]]):
    """Получение списка складов WB."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/warehouses"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = List[WarehouseItemFBW]
class GetTransitTariffs(WBMethod[List[TransitTariff]]):
    """Получение информации о транзитных направлениях."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/transit-tariffs"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = List[TransitTariff]


# ==========================================
# ИНФОРМАЦИЯ ПО ПОСТАВКАМ
# ==========================================
class GetSuppliesFBW(WBMethod[List[SupplyFBW]]):
    """Получение списка поставок."""

    __http_method__: ClassVar[str] = "POST"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = List[SupplyFBW]

    limit: int = Field(1000, exclude=True)
    offset: int = Field(0, exclude=True)

    # Body
    filter_data: SuppliesFiltersRequest

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/supplies?limit={self.limit}&offset={self.offset}"

    def model_dump(self, **kwargs):
        # Отдаем только то, что должно уйти в Body (фильтры)
        return self.filter_data.model_dump(by_alias=True, exclude_none=True)
class GetSupplyDetailsFBW(WBMethod[SupplyDetailsFBW]):
    """Получение детализации поставки."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = SupplyDetailsFBW

    supply_id: int = Field(exclude=True)
    is_preorder_id: bool = Field(False, exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/supplies/{self.supply_id}?isPreorderID={str(self.is_preorder_id).lower()}"
class GetSupplyGoodsFBW(WBMethod[List[GoodInSupplyFBW]]):
    """Получение списка товаров в поставке."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = List[GoodInSupplyFBW]

    supply_id: int = Field(exclude=True)
    limit: int = Field(100, exclude=True)
    offset: int = Field(0, exclude=True)
    is_preorder_id: bool = Field(False, exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/supplies/{self.supply_id}/goods?limit={self.limit}&offset={self.offset}&isPreorderID={str(self.is_preorder_id).lower()}"
class GetSupplyPackageFBW(WBMethod[List[BoxFBW]]):
    """Получение информации об упаковке поставки."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.SUPPLIES
    __returning__: ClassVar[type] = List[BoxFBW]

    supply_id: int = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/supplies/{self.supply_id}/package"
