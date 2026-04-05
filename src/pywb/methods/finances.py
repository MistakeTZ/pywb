from typing import ClassVar, List, Optional

from pydantic import Field

from ..enums import WBDomain
from ..types.finances import (
    BalanceData,
    DetailReportItem,
    DocumentCategoriesData,
    DocumentDownloadData,
    DocumentListData,
    DownloadParam,
)
from .base import WBMethod


# ==========================================
# БАЛАНС И ФИНАНСОВЫЕ ОТЧЕТЫ
# ==========================================
class GetBalance(WBMethod[BalanceData]):
    """Получение баланса продавца."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/account/balance"
    __domain__: ClassVar[WBDomain] = WBDomain.FINANCE
    __returning__: ClassVar[type] = BalanceData


class GetRealizationReport(WBMethod[List[DetailReportItem]]):
    """Детализация отчета о реализации."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v5/supplier/reportDetailByPeriod"
    __domain__: ClassVar[WBDomain] = WBDomain.STATISTICS
    __returning__: ClassVar[type] = List[DetailReportItem]

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int = 100000
    rrdid: int = 0
    period: str = "weekly"


# ==========================================
# ДОКУМЕНТЫ
# ==========================================
class GetDocumentCategories(WBMethod[DocumentCategoriesData]):
    """Категории документов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/documents/categories"
    __domain__: ClassVar[WBDomain] = WBDomain.DOCUMENTS
    __returning__: ClassVar[type] = DocumentCategoriesData

    locale: str = "ru"


class GetDocumentsList(WBMethod[DocumentListData]):
    """Список документов продавца."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/documents/list"
    __domain__: ClassVar[WBDomain] = WBDomain.DOCUMENTS
    __returning__: ClassVar[type] = DocumentListData

    locale: str = "ru"
    begin_time: Optional[str] = Field(None, alias="beginTime")
    end_time: Optional[str] = Field(None, alias="endTime")
    sort: Optional[str] = None
    order: Optional[str] = None
    category: Optional[str] = None
    service_name: Optional[str] = Field(None, alias="serviceName")
    limit: int = 50
    offset: int = 0


class DownloadDocument(WBMethod[DocumentDownloadData]):
    """Скачивание одного документа."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/documents/download"
    __domain__: ClassVar[WBDomain] = WBDomain.DOCUMENTS
    __returning__: ClassVar[type] = DocumentDownloadData

    service_name: str = Field(alias="serviceName")
    extension: str


class DownloadDocumentsAll(WBMethod[DocumentDownloadData]):
    """Скачивание нескольких документов архивом."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v1/documents/download/all"
    __domain__: ClassVar[WBDomain] = WBDomain.DOCUMENTS
    __returning__: ClassVar[type] = DocumentDownloadData

    params: List[DownloadParam]
