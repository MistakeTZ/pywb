from typing import ClassVar, List

from .base import WBMethod
from ..enums import WBDomain
from ..types import GoodPriceItem



class SetPrices(WBMethod[SetPricesTaskResponse]):
    """Установка цен и скидок."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/upload/task"
    __domain__: ClassVar[WBDomain] = WBDomain.PRICES
    __returning__: ClassVar[type] = SetPricesTaskResponse

    data: List[GoodPriceItem]
