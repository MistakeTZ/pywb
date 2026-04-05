from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

# ==========================================
# СПИСКИ И ИНФОРМАЦИЯ О КАМПАНИЯХ
# ==========================================


class AdvertListItem(BaseModel):
    advert_id: int = Field(alias="advertId")
    change_time: datetime = Field(alias="changeTime")


class CountAdvert(BaseModel):
    type: int
    status: int
    count: int
    advert_list: List[AdvertListItem] = Field(alias="advert_list")


class CountResponse(BaseModel):
    adverts: Optional[List[CountAdvert]] = None
    all: int


class AdvertBidsKopecks(BaseModel):
    search: int
    recommendations: int


class AdvertSubject(BaseModel):
    id: int
    name: str


class AdvertNMSettings(BaseModel):
    nm_id: int
    subject: AdvertSubject
    bids_kopecks: AdvertBidsKopecks


class AdvertPlacements(BaseModel):
    search: bool
    recommendations: bool


class AdvertSettings(BaseModel):
    payment_type: str
    name: str
    placements: AdvertPlacements


class AdvertTimestamps(BaseModel):
    created: datetime
    updated: datetime
    started: Optional[datetime] = None
    deleted: Optional[datetime] = None


class AdvertInfo(BaseModel):
    id: int
    bid_type: str
    status: int
    settings: AdvertSettings
    nm_settings: List[AdvertNMSettings]
    timestamps: AdvertTimestamps


class GetAdvertsResponse(BaseModel):
    adverts: List[AdvertInfo]


# ==========================================
# СОЗДАНИЕ И СТАВКИ (Bids)
# ==========================================


class BidItem(BaseModel):
    type: str
    value: int


class NmBidItem(BaseModel):
    nm_id: int
    bids: List[BidItem]


class MinBidsResponse(BaseModel):
    bids: List[NmBidItem]


# ==========================================
# ФИНАНСЫ (Бюджет, Баланс)
# ==========================================


class CashbackInfo(BaseModel):
    sum: int
    percent: int
    expiration_date: datetime


class BalanceResponse(BaseModel):
    balance: int
    net: int
    bonus: int
    cashbacks: Optional[List[CashbackInfo]] = None


class BudgetResponse(BaseModel):
    cash: int
    netting: int
    total: int


class DepositResponse(BaseModel):
    total: int


class UpdItem(BaseModel):
    upd_num: int = Field(alias="updNum")
    upd_time: Optional[datetime] = Field(None, alias="updTime")
    upd_sum: int = Field(alias="updSum")
    advert_id: int = Field(alias="advertId")
    camp_name: str = Field(alias="campName")
    advert_type: int = Field(alias="advertType")
    payment_type: str = Field(alias="paymentType")
    advert_status: int = Field(alias="advertStatus")


class PaymentItem(BaseModel):
    id: int
    date: datetime
    sum: int
    type: int
    status_id: int = Field(alias="statusId")
    card_status: str = Field(alias="cardStatus")


# ==========================================
# СТАТИСТИКА
# ==========================================


class StatNmItem(BaseModel):
    nm_id: int = Field(alias="nmId")
    name: str
    views: int
    clicks: int
    atbs: int
    orders: int
    shks: int
    sum: float
    sum_price: float
    cr: float
    ctr: float
    cpc: float


class StatAppType(BaseModel):
    app_type: int = Field(alias="appType")
    views: int
    clicks: int
    atbs: int
    orders: int
    shks: int
    sum: float
    sum_price: float
    cr: float
    ctr: float
    cpc: float
    nms: List[StatNmItem]


class StatDay(BaseModel):
    date: datetime
    views: int
    clicks: int
    atbs: int
    orders: int
    shks: int
    sum: float
    sum_price: float
    cr: float
    ctr: float
    cpc: float
    apps: List[StatAppType]


class FullStatsItem(BaseModel):
    advert_id: int = Field(alias="advertId")
    views: int
    clicks: int
    atbs: int
    orders: int
    shks: int
    canceled: int
    sum: float
    sum_price: float
    cr: float
    ctr: float
    cpc: float
    days: List[StatDay]


# ==========================================
# КАЛЕНДАРЬ АКЦИЙ
# ==========================================


class PromoItem(BaseModel):
    id: int
    name: str
    start_date_time: datetime = Field(alias="startDateTime")
    end_date_time: datetime = Field(alias="endDateTime")
    type: str


class PromotionsResponse(BaseModel):
    promotions: List[PromoItem]
