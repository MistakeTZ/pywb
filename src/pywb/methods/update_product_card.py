from typing import Optional
from .base import WBMethod


class UpdateProductCard(WBMethod[bool]):
    """
    Класс-команда для обновления карточки товара.
    """

    __http_method__ = "POST"
    __api_path__ = "/content/v1/cards/update"
    __returning__ = bool

    card_id: str
    price: int
    discount: Optional[int] = None
