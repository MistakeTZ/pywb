from typing import ClassVar, Optional
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    GetNewsResponse,
)


# --- News API ---
class GetNews(WBMethod[GetNewsResponse]):
    """Получение новостей портала продавцов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/communications/v2/news"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = GetNewsResponse

    from_date: Optional[str] = Field(None, alias="from")
    from_id: Optional[int] = Field(None, alias="fromID")
