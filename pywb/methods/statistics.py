from typing import ClassVar

from pywb.types.order import StatisticOrder
from .base import WBMethod
from ..enums import WBDomain


class GetOrders(WBMethod[list[StatisticOrder]]):
    """
    Команда для получения отчета по заказам.
    """

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/supplier/orders"
    __domain__: ClassVar[WBDomain] = WBDomain.STATISTICS
    __returning__: ClassVar[type] = list[StatisticOrder]

    dateFrom: str
    flag: int = 0
