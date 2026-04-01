from typing import ClassVar
from .base import WBMethod
from ..types import PingResponse


class Ping(WBMethod[PingResponse]):
    """
    Команда для проверки доступности API.
    """

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/ping"
    __returning__: ClassVar[type] = PingResponse
