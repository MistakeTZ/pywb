from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# ==========================================
# ПРОДАЖИ И ОСТАТКИ (Синхронные)
# ==========================================
class SalesItem(BaseModel):
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
    payment_sale_amount: Optional[int] = Field(None, alias="paymentSaleAmount")
    for_pay: float = Field(alias="forPay")
    finished_price: float = Field(alias="finishedPrice")
    price_with_disc: float = Field(alias="priceWithDisc")
    sale_id: str = Field(alias="saleID")
    sticker: str
    g_number: str = Field(alias="gNumber")
    srid: str


# ==========================================
# АСИНХРОННЫЕ ОТЧЕТЫ (Задачи)
# ==========================================


class TaskIdData(BaseModel):
    task_id: str = Field(alias="taskId")


class CreateTaskResponse(BaseModel):
    data: TaskIdData


class TaskStatusData(BaseModel):
    id: str
    status: str


class TaskStatusResponse(BaseModel):
    data: TaskStatusData


# ==========================================
# ШТРАФЫ И УДЕРЖАНИЯ (Retentions)
# ==========================================
class MeasurementPenaltyItem(BaseModel):
    nm_id: int = Field(alias="nmId")
    subject_name: str = Field(alias="subjectName")
    dim_id: int = Field(alias="dimId")
    prc_over: float = Field(alias="prcOver")
    volume: float
    width: int
    length: int
    height: int
    volume_sup: float = Field(alias="volumeSup")
    width_sup: int = Field(alias="widthSup")
    length_sup: int = Field(alias="lengthSup")
    height_sup: int = Field(alias="heightSup")
    photo_urls: Optional[List[str]] = Field(None, alias="photoUrls")
    dt_bonus: datetime = Field(alias="dtBonus")
    is_valid: bool = Field(alias="isValid")
    is_valid_dt: Optional[datetime] = Field(None, alias="isValidDt")
    reversal_amount: float = Field(alias="reversalAmount")
    penalty_amount: float = Field(alias="penaltyAmount")


class RetentionData(BaseModel):
    reports: List[MeasurementPenaltyItem]
    total: int


class MeasurementPenaltiesResponse(BaseModel):
    data: RetentionData


class DeductionItem(BaseModel):
    dt_bonus: datetime = Field(alias="dtBonus")
    nm_id: int = Field(alias="nmId")
    old_shk_id: Optional[int] = Field(None, alias="oldShkId")
    new_shk_id: Optional[int] = Field(None, alias="newShkId")
    bonus_summ: float = Field(alias="bonusSumm")
    bonus_type: str = Field(alias="bonusType")


class DeductionsData(BaseModel):
    reports: List[DeductionItem]
    total: int


class DeductionsResponse(BaseModel):
    data: DeductionsData


# ==========================================
# ПРОЧИЕ ОТЧЕТЫ (Регионы, Бренды, Скрытое)
# ==========================================
class RegionSaleItem(BaseModel):
    city_name: str = Field(alias="cityName")
    country_name: str = Field(alias="countryName")
    fo_name: str = Field(alias="foName")
    nm_id: int = Field(alias="nmID")
    region_name: str = Field(alias="regionName")
    sa: str
    sale_invoice_cost_price: float = Field(alias="saleInvoiceCostPrice")
    sale_item_invoice_qty: int = Field(alias="saleItemInvoiceQty")


class RegionSaleResponse(BaseModel):
    report: List[RegionSaleItem]


class BrandShareItem(BaseModel):
    apply_date: str = Field(alias="applyDate")
    brand_rating: int = Field(alias="brandRating")
    price_percent: float = Field(alias="pricePercent")
    qty_percent: float = Field(alias="qtyPercent")


class BrandShareResponse(BaseModel):
    report: List[BrandShareItem]


class BannedProductItem(BaseModel):
    brand: str
    nm_id: int = Field(alias="nmId")
    title: str
    vendor_code: str = Field(alias="vendorCode")
    reason: Optional[str] = None
    nm_rating: Optional[float] = Field(None, alias="nmRating")


class BannedProductsResponse(BaseModel):
    report: List[BannedProductItem]


class GoodsReturnItem(BaseModel):
    barcode: str
    brand: str
    completed_dt: Optional[str] = Field(None, alias="completedDt")
    nm_id: int = Field(alias="nmId")
    order_dt: str = Field(alias="orderDt")
    reason: str
    status: str
    subject_name: str = Field(alias="subjectName")


class GoodsReturnResponse(BaseModel):
    report: List[GoodsReturnItem]
