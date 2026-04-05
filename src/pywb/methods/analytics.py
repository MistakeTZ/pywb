from typing import ClassVar

from pydantic import Field

from ..enums import WBDomain
from ..types.analytics import (
    CreateReportResponse,
    FunnelResponseData,
    GetReportsListResponse,
    SearchReportResponse,
    StocksGroupResponse,
    StocksWbResponse,
)
from .base import WBMethod


# ==========================================
# ВОРОНКА ПРОДАЖ
# ==========================================
class GetFunnelProducts(WBMethod[FunnelResponseData]):
    """Статистика карточек товаров за период."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/analytics/v3/sales-funnel/products"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = FunnelResponseData

    # Унаследуем все поля из FunnelProductsRequest путем распаковки в клиенте
    pass


class GetFunnelHistory(WBMethod[FunnelResponseData]):
    """Статистика карточек товаров по дням/неделям."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/analytics/v3/sales-funnel/products/history"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = FunnelResponseData


class GetFunnelGroupedHistory(WBMethod[FunnelResponseData]):
    """Статистика карточек товаров по дням (сгруппированная)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/analytics/v3/sales-funnel/grouped/history"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = FunnelResponseData


# ==========================================
# ПОИСКОВЫЕ ЗАПРОСЫ
# ==========================================
class GetSearchMainReport(WBMethod[SearchReportResponse]):
    """Формирует данные для главной страницы отчета по поисковым запросам."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/search-report/report"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = SearchReportResponse


class GetSearchTableDetails(WBMethod[SearchReportResponse]):
    """Пагинация по товарам в группе (поисковые запросы)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/search-report/table/details"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = SearchReportResponse


# ==========================================
# ОСТАТКИ (STOCKS REPORT)
# ==========================================
class GetStocksWbWarehouses(WBMethod[StocksWbResponse]):
    """Остатки товаров на складах WB."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/analytics/v1/stocks-report/wb-warehouses"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = StocksWbResponse


class GetStocksGroups(WBMethod[StocksGroupResponse]):
    """Данные по остаткам, сгруппированные по карточкам."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/stocks-report/products/groups"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = StocksGroupResponse


# ==========================================
# ВЫГРУЗКА CSV ОТЧЕТОВ
# ==========================================
class CreateCsvReport(WBMethod[CreateReportResponse]):
    """Запуск генерации отчета."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/nm-report/downloads"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = CreateReportResponse


class GetCsvReportsList(WBMethod[GetReportsListResponse]):
    """Список созданных отчетов и их статусы."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v2/nm-report/downloads"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = GetReportsListResponse


class RetryCsvReport(WBMethod[CreateReportResponse]):
    """Перезапуск генерации отчета со статусом FAILED."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v2/nm-report/downloads/retry"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = CreateReportResponse

    download_id: str = Field(alias="downloadId")


class GetReportFile(WBMethod[bytes]):
    """Скачивание готового отчета (возвращает ZIP-архив)."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = bytes

    download_id: str = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v2/nm-report/downloads/file/{self.download_id}"
