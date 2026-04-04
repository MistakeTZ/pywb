from typing import ClassVar, List

from .base import WBMethod
from ..enums import WBDomain
from ..types import WarehouseItem

class GetWarehouses(WBMethod[List[WarehouseItem]]):
    """Получение списка складов продавца."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v3/warehouses"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = List[WarehouseItem]
