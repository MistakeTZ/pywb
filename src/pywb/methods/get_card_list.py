from typing import ClassVar, Dict, Any

from .base import WBMethod
from ..enums import WBDomain
from ..types import WBContentResponse, CardsListData


class GetCardsList(WBMethod[WBContentResponse[CardsListData]]):
    """Получение списка созданных карточек товаров."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/content/v2/get/cards/list"
    __domain__: ClassVar[WBDomain] = WBDomain.CONTENT
    __returning__: ClassVar[type] = WBContentResponse[CardsListData]

    settings: Dict[
        str, Any
    ]  # В реальном проекте лучше типизировать settings через отдельную Pydantic модель
