from typing import Any, ClassVar, List, Optional

from pydantic import Field

from ..enums import WBDomain
from ..types.reports import (
    BannedProductsResponse,
    CreateTaskResponse,
    DeductionsResponse,
    MeasurementPenaltiesResponse,
    SalesItem,
    TaskStatusResponse,
)
from .base import WBMethod


# ==========================================
# ПРОДАЖИ (Sales)
# ==========================================
class GetSales(WBMethod[List[SalesItem]]):
    """Получение информации о продажах и возвратах."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/supplier/sales"
    __domain__: ClassVar[WBDomain] = WBDomain.STATISTICS
    __returning__: ClassVar[type] = List[SalesItem]

    date_from: str = Field(alias="dateFrom")
    flag: int = 0


# ==========================================
# АСИНХРОННЫЕ ОТЧЕТЫ (Платное хранение)
# ==========================================
class CreatePaidStorageReport(WBMethod[CreateTaskResponse]):
    """Запуск генерации отчета по платному хранению."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/paid_storage"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = CreateTaskResponse

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")


class GetPaidStorageStatus(WBMethod[TaskStatusResponse]):
    """Статус генерации отчета по платному хранению."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = TaskStatusResponse

    task_id: str = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/paid_storage/tasks/{self.task_id}/status"


class GetPaidStorageFile(
    WBMethod[List[Any]]
):  # Возвращает список словарей (CSV/JSON rows)
    """Скачивание отчета по платному хранению."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = List[Any]

    task_id: str = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/paid_storage/tasks/{self.task_id}/download"


# ==========================================
# ШТРАФЫ И УДЕРЖАНИЯ (Retentions)
# ==========================================
class GetMeasurementPenalties(WBMethod[MeasurementPenaltiesResponse]):
    """Удержания за габариты."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/analytics/v1/measurement-penalties"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = MeasurementPenaltiesResponse

    date_from: Optional[str] = Field(None, alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int
    offset: int = 0


class GetDeductions(WBMethod[DeductionsResponse]):
    """Удержания за подмены и неверные вложения."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/analytics/v1/deductions"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = DeductionsResponse

    date_from: Optional[str] = Field(None, alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int
    offset: int = 0
    sort: str = "dtBonus"
    order: str = "desc"


# ==========================================
# СКРЫТЫЕ И ЗАБЛОКИРОВАННЫЕ ТОВАРЫ
# ==========================================
class GetBlockedProducts(WBMethod[BannedProductsResponse]):
    """Заблокированные карточки."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/analytics/banned-products/blocked"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = BannedProductsResponse

    sort: str = "nmId"
    order: str = "asc"


class GetShadowedProducts(WBMethod[BannedProductsResponse]):
    """Скрытые из каталога карточки (Теневой бан)."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/analytics/banned-products/shadowed"
    __domain__: ClassVar[WBDomain] = WBDomain.ANALYTICS
    __returning__: ClassVar[type] = BannedProductsResponse

    sort: str = "nmId"
    order: str = "asc"
