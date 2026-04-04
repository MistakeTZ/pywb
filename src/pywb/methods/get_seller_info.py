from typing import ClassVar

from .base import WBMethod
from ..enums import WBDomain
from ..types import SellerInfoResponse


class GetSellerInfo(WBMethod[SellerInfoResponse]):
    """Получение информации о продавце (имя, ИНН, ID)."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/seller-info"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = SellerInfoResponse
