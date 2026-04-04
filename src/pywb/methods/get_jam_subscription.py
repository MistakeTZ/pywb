from typing import ClassVar, Optional, List
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import  SubscriptionsJamInfo


class GetJamSubscription(WBMethod[Optional[SubscriptionsJamInfo]]):
    """
    Получение информации о подписке Джем.
    Если подписка никогда не активировалась, WB возвращает пустой ответ (поэтому Optional).
    """

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/common/v1/subscriptions"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = SubscriptionsJamInfo
