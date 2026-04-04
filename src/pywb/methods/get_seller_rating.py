from typing import ClassVar

from .base import WBMethod
from ..enums import WBDomain
from ..types import SupplierRatingModel



class GetSellerRating(WBMethod[SupplierRatingModel]):
    """Получение рейтинга продавца (работает через домен Feedbacks)."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/common/v1/rating"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = SupplierRatingModel
