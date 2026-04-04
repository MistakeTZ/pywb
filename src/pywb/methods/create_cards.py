from typing import ClassVar, List, Any

from .base import WBMethod
from ..enums import WBDomain
from ..types import WBContentResponse, CreateCardItem


class CreateCards(WBMethod[WBContentResponse[Any]]):
    """Создание новых карточек товаров."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/content/v2/cards/upload"
    __domain__: ClassVar[WBDomain] = WBDomain.CONTENT
    __returning__: ClassVar[type] = WBContentResponse[Any]

    # Данные передаются не как словарь, а как корневой список.
    # В базовом классе WBMethod потребуется небольшая адаптация,
    # либо можно передать данные в специальном поле и переопределить model_dump.
    items: List[CreateCardItem]
