from .base import WBMethod
from ..enums import WBDomain
from ..types import PingResponse


class Ping(WBMethod[PingResponse]):
    __http_method__ = "GET"
    __api_path__ = "/ping"
    __domain__ = WBDomain.COMMON
    __returning__ = PingResponse

class PingContent(WBMethod[PingResponse]):
    __http_method__ = "GET"
    __api_path__ = "/ping"
    __domain__ = WBDomain.CONTENT
    __returning__ = PingResponse


class PingAnalytics(WBMethod[PingResponse]):
    __http_method__ = "GET"
    __api_path__ = "/ping"
    __domain__ = WBDomain.ANALYTICS
    __returning__ = PingResponse
