from typing import ClassVar, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import StockItem


class UpdateStocks(WBMethod[bool]):
    """Обновление остатков товаров на конкретном складе продавца."""

    __http_method__: ClassVar[str] = "PUT"
    __domain__: ClassVar[WBDomain] = WBDomain.MARKETPLACE
    __returning__: ClassVar[type] = bool

    # Исключаем из JSON-тела, так как это параметр URL
    warehouse_id: int = Field(exclude=True)

    # Это поле попадет в JSON-тело
    stocks: List[StockItem]

    @property
    def __api_path__(self) -> str:
        # Динамически формируем путь с учетом переданного ID склада
        return f"/api/v3/stocks/{self.warehouse_id}"
