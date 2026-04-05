from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

# ==========================================
# ОБЩИЕ ТИПЫ
# ==========================================
class DatePeriod(BaseModel):
    start: str  # YYYY-MM-DD
    end: str  # YYYY-MM-DD


class OrderBy(BaseModel):
    field: str
    mode: str  # asc / desc


# ==========================================
# ВОРОНКА ПРОДАЖ (Sales Funnel)
# ==========================================
class FunnelProductsRequest(BaseModel):
    selected_period: DatePeriod = Field(alias="selectedPeriod")
    past_period: Optional[DatePeriod] = Field(None, alias="pastPeriod")
    nm_ids: Optional[List[int]] = Field(None, alias="nmIds")
    brand_names: Optional[List[str]] = Field(None, alias="brandNames")
    subject_ids: Optional[List[int]] = Field(None, alias="subjectIds")
    tag_ids: Optional[List[int]] = Field(None, alias="tagIds")
    skip_deleted_nm: Optional[bool] = Field(None, alias="skipDeletedNm")
    order_by: Optional[OrderBy] = Field(None, alias="orderBy")
    limit: int = 50
    offset: int = 0


class FunnelHistoryRequest(BaseModel):
    selected_period: DatePeriod = Field(alias="selectedPeriod")
    nm_ids: Optional[List[int]] = Field(None, alias="nmIds")
    brand_names: Optional[List[str]] = Field(None, alias="brandNames")
    subject_ids: Optional[List[int]] = Field(None, alias="subjectIds")
    tag_ids: Optional[List[int]] = Field(None, alias="tagIds")
    skip_deleted_nm: Optional[bool] = Field(None, alias="skipDeletedNm")
    aggregation_level: str = Field("day", alias="aggregationLevel")  # day / week


class FunnelResponseData(BaseModel):
    data: Any  # Для глубоко вложенной аналитики используем Any (внутри dict)


# ==========================================
# ПОИСКОВЫЕ ЗАПРОСЫ (Search Report)
# ==========================================


class SearchMainRequest(BaseModel):
    current_period: DatePeriod = Field(alias="currentPeriod")
    past_period: Optional[DatePeriod] = Field(None, alias="pastPeriod")
    nm_ids: Optional[List[int]] = Field(None, alias="nmIds")
    subject_ids: Optional[List[int]] = Field(None, alias="subjectIds")
    brand_names: Optional[List[str]] = Field(None, alias="brandNames")
    tag_ids: Optional[List[int]] = Field(None, alias="tagIds")
    position_cluster: str = Field("all", alias="positionCluster")
    order_by: OrderBy = Field(alias="orderBy")
    include_substituted_skus: bool = Field(True, alias="includeSubstitutedSKUs")
    include_search_texts: bool = Field(True, alias="includeSearchTexts")
    limit: int = 130
    offset: int = 0


class SearchReportResponse(BaseModel):
    data: Any


# ==========================================
# ОСТАТКИ (Stocks Report)
# ==========================================
class StocksWbRequest(BaseModel):
    nm_ids: Optional[List[int]] = Field(None, alias="nmIds")
    chrt_ids: Optional[List[int]] = Field(None, alias="chrtIds")
    limit: int = 250000
    offset: int = 0


class StocksWbItem(BaseModel):
    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    warehouse_id: int = Field(alias="warehouseId")
    warehouse_name: str = Field(alias="warehouseName")
    region_name: str = Field(alias="regionName")
    quantity: int
    in_way_to_client: int = Field(alias="inWayToClient")
    in_way_from_client: int = Field(alias="inWayFromClient")


class StocksWbResponse(BaseModel):
    data: Dict[str, List[StocksWbItem]]  # {"items": [...]}


class StocksGroupRequest(BaseModel):
    nm_ids: Optional[List[int]] = Field(None, alias="nmIDs")
    subject_ids: Optional[List[int]] = Field(None, alias="subjectIDs")
    brand_names: Optional[List[str]] = Field(None, alias="brandNames")
    tag_ids: Optional[List[int]] = Field(None, alias="tagIDs")
    current_period: DatePeriod = Field(alias="currentPeriod")
    stock_type: str = Field(..., alias="stockType")  # "", "wb", "mp"
    skip_deleted_nm: bool = Field(..., alias="skipDeletedNm")
    availability_filters: List[str] = Field(..., alias="availabilityFilters")
    order_by: OrderBy = Field(alias="orderBy")
    limit: int = 100
    offset: int = 0


class StocksGroupResponse(BaseModel):
    data: Any


# ==========================================
# ГЕНЕРАЦИЯ ОТЧЕТОВ (CSV Downloads)
# ==========================================
class CreateReportRequest(BaseModel):
    id: str  # UUID
    report_type: str = Field(alias="reportType")
    user_report_name: Optional[str] = Field(None, alias="userReportName")
    params: Dict[str, Any]


class CreateReportResponse(BaseModel):
    data: str


class ReportStatusItem(BaseModel):
    id: str
    status: str  # WAITING, PROCESSING, SUCCESS, RETRY, FAILED
    name: str
    size: int
    start_date: str = Field(alias="startDate")
    end_date: str = Field(alias="endDate")
    created_at: str = Field(alias="createdAt")


class GetReportsListResponse(BaseModel):
    data: List[ReportStatusItem]
