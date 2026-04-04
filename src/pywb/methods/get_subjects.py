from typing import ClassVar, Optional, List

from .base import WBMethod
from ..enums import WBDomain
from ..types import WBContentResponse, SubjectItem


class GetSubjects(WBMethod[WBContentResponse[List[SubjectItem]]]):
    """Получение списка всех доступных предметов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/content/v2/object/all"
    __domain__: ClassVar[WBDomain] = WBDomain.CONTENT
    __returning__: ClassVar[type] = WBContentResponse[List[SubjectItem]]

    name: Optional[str] = None
    limit: int = 1000
    offset: int = 0
