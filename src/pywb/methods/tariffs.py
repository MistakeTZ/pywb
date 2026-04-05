from typing import ClassVar, List, Optional
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types.tariffs import (
    CommissionResponse,
    TariffsBoxResponse,
    TariffsPalletResponse,
    ReturnTariffsResponse,
    AcceptanceCoefficient,
)


class GetCommission(WBMethod[CommissionResponse]):
    """Комиссии WB по категориям товаров."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/tariffs/commission"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = CommissionResponse

    locale: Optional[str] = None  # ru, en, zh


class GetBoxTariffs(WBMethod[TariffsBoxResponse]):
    """Тарифы для коробов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/tariffs/box"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = TariffsBoxResponse

    date: str  # YYYY-MM-DD


class GetPalletTariffs(WBMethod[TariffsPalletResponse]):
    """Тарифы для паллет."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/tariffs/pallet"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = TariffsPalletResponse

    date: str  # YYYY-MM-DD


class GetReturnTariffs(WBMethod[ReturnTariffsResponse]):
    """Тарифы на возврат товаров продавцу."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/tariffs/return"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = ReturnTariffsResponse

    date: str  # YYYY-MM-DD


class GetAcceptanceCoefficients(WBMethod[List[AcceptanceCoefficient]]):
    """Коэффициенты приемки на складах WB."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/tariffs/v1/acceptance/coefficients"
    __domain__: ClassVar[WBDomain] = WBDomain.COMMON
    __returning__: ClassVar[type] = List[AcceptanceCoefficient]

    warehouse_ids: Optional[str] = Field(None, alias="warehouseIDs")
