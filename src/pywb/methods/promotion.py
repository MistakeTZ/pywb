from typing import ClassVar, List, Optional
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    CountResponse,
    GetAdvertsResponse,
    BalanceResponse,
    BudgetResponse,
    DepositResponse,
    UpdItem,
    FullStatsItem,
)

# ==========================================
# УПРАВЛЕНИЕ КАМПАНИЯМИ
# ==========================================
class GetCampaignsCount(WBMethod[CountResponse]):
    """Получение списков кампаний, сгруппированных по типу и статусу."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/adv/v1/promotion/count"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = CountResponse
class GetAdverts(WBMethod[GetAdvertsResponse]):
    """Получение информации о кампаниях по ID, статусам или типу оплаты."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/advert/v2/adverts"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = GetAdvertsResponse

    ids: Optional[str] = None
    statuses: Optional[str] = None
    payment_type: Optional[str] = None
class RenameCampaign(WBMethod[bool]):
    """Переименование кампании."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/adv/v0/rename"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = bool

    advert_id: int = Field(alias="advertId")
    name: str
class ChangeCampaignStatus(WBMethod[bool]):
    """Базовый класс для изменения статуса (запуск, пауза, остановка)."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = bool

    id: int
class StartCampaign(ChangeCampaignStatus):
    __api_path__: ClassVar[str] = "/adv/v0/start"
class PauseCampaign(ChangeCampaignStatus):
    __api_path__: ClassVar[str] = "/adv/v0/pause"
class StopCampaign(ChangeCampaignStatus):
    __api_path__: ClassVar[str] = "/adv/v0/stop"


# ==========================================
# ФИНАНСЫ И БЮДЖЕТ
# ==========================================
class GetPromoBalance(WBMethod[BalanceResponse]):
    """Получение баланса, счета и бонусов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/adv/v1/balance"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = BalanceResponse
class GetBudget(WBMethod[BudgetResponse]):
    """Получение бюджета конкретной кампании."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/adv/v1/budget"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = BudgetResponse

    id: int
class DepositBudget(WBMethod[DepositResponse]):
    """Пополнение бюджета кампании."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/adv/v1/budget/deposit"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = DepositResponse

    id: int = Field(exclude=True)  # Идет в query параметр
    sum: int
    type: int
    return_flag: bool = Field(True, alias="return")

    @property
    def __api_path__(self) -> str:
        return f"/adv/v1/budget/deposit?id={self.id}"
class GetUpd(WBMethod[List[UpdItem]]):
    """История затрат (списаний)."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/adv/v1/upd"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = List[UpdItem]

    from_date: str = Field(alias="from")
    to_date: str = Field(alias="to")


# ==========================================
# СТАТИСТИКА И КАЛЕНДАРЬ
# ==========================================
class GetFullStats(WBMethod[List[FullStatsItem]]):
    """Получение полной статистики по кампаниям."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/adv/v3/fullstats"
    __domain__: ClassVar[WBDomain] = WBDomain.PROMOTION
    __returning__: ClassVar[type] = List[FullStatsItem]

    ids: str
    begin_date: str = Field(alias="beginDate")
    end_date: str = Field(alias="endDate")
class GetCalendarPromotions(
    WBMethod[dict]
):  # Возвращает обертку {"data": {"promotions": [...]}}
    """Список акций в календаре WB."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/calendar/promotions"
    __domain__: ClassVar[WBDomain] = WBDomain.CALENDAR
    __returning__: ClassVar[type] = dict

    start_date_time: str = Field(alias="startDateTime")
    end_date_time: str = Field(alias="endDateTime")
    all_promo: bool = Field(False, alias="allPromo")
    limit: int = 10
    offset: int = 0
