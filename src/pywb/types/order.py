from datetime import datetime
from pydantic import BaseModel, Field


class StatisticOrder(BaseModel):
    """Модель информации о заказе из API Статистики."""

    date: datetime
    last_change_date: datetime = Field(alias="lastChangeDate")
    warehouse_name: str = Field(alias="warehouseName")
    warehouse_type: str = Field(alias="warehouseType")
    country_name: str = Field(alias="countryName")
    oblast_okrug_name: str = Field(alias="oblastOkrugName")
    region_name: str = Field(alias="regionName")
    supplier_article: str = Field(alias="supplierArticle")
    nm_id: int = Field(alias="nmId")
    barcode: str
    category: str
    subject: str
    brand: str
    tech_size: str = Field(alias="techSize")
    income_id: int = Field(alias="incomeID")
    is_supply: bool = Field(alias="isSupply")
    is_realization: bool = Field(alias="isRealization")
    total_price: float = Field(alias="totalPrice")
    discount_percent: int = Field(alias="discountPercent")
    spp: float
    finished_price: float = Field(alias="finishedPrice")
    price_with_disc: float = Field(alias="priceWithDisc")
    is_cancel: bool = Field(alias="isCancel")
    cancel_date: datetime = Field(alias="cancelDate")
    sticker: str
    g_number: str = Field(alias="gNumber")
    srid: str
