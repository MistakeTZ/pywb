from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, Field

# ==========================================
# ПРОПУСКА (Passes)
# ==========================================
class PassOffice(BaseModel):
    id: int
    name: str
    address: str


class PassItem(BaseModel):
    id: int
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    car_model: str = Field(alias="carModel")
    car_number: str = Field(alias="carNumber")
    office_name: str = Field(alias="officeName")
    office_address: str = Field(alias="officeAddress")
    office_id: int = Field(alias="officeId")
    date_end: datetime = Field(alias="dateEnd")


class CreatePassResponse(BaseModel):
    id: int


# ==========================================
# ЗАКАЗЫ И СТАТУСЫ (Orders)
# ==========================================
class Address(BaseModel):
    full_address: Optional[str] = Field(None, alias="fullAddress")
    longitude: float
    latitude: float


class OrderOptions(BaseModel):
    is_b2b: Optional[bool] = Field(None, alias="isB2B")


class OrderItem(BaseModel):
    id: int
    rid: str
    createdAt: datetime
    warehouseId: int
    officeId: int
    nmId: int
    chrtId: int
    price: int
    convertedPrice: int
    currencyCode: int
    convertedCurrencyCode: int
    cargoType: int
    crossBorderType: int
    article: str
    colorCode: str
    deliveryType: str
    skus: List[str]
    comment: str
    isZeroOrder: bool
    options: Optional[OrderOptions] = None
    address: Optional[Address] = None
    orderUid: Optional[str] = None
    offices: Optional[List[str]] = None
    scanPrice: Optional[int] = None

    # Специфичные для NewOrder
    salePrice: Optional[int] = None
    ddate: Optional[str] = None
    sellerDate: Optional[str] = None
    requiredMeta: Optional[List[str]] = None
    optionalMeta: Optional[List[str]] = None


class GetNewOrdersResponse(BaseModel):
    orders: List[OrderItem]


class GetOrdersResponse(BaseModel):
    next: int
    orders: List[OrderItem]


class OrderStatus(BaseModel):
    id: int
    supplier_status: str = Field(alias="supplierStatus")
    wb_status: str = Field(alias="wbStatus")


class GetOrdersStatusesResponse(BaseModel):
    orders: List[OrderStatus]


class OrderSticker(BaseModel):
    order_id: int = Field(alias="orderId")
    part_a: int = Field(alias="partA")
    part_b: int = Field(alias="partB")
    barcode: str
    file: str  # Base64


class GetStickersResponse(BaseModel):
    stickers: List[OrderSticker]


# ==========================================
# ПОСТАВКИ (Supplies)
# ==========================================
class SupplyItem(BaseModel):
    id: str
    name: str
    cargo_type: int = Field(alias="cargoType")
    done: bool
    created_at: datetime = Field(alias="createdAt")
    closed_at: Optional[datetime] = Field(None, alias="closedAt")
    scan_dt: Optional[datetime] = Field(None, alias="scanDt")
    is_b2b: Optional[bool] = Field(None, alias="isB2b")
    cross_border_type: Optional[int] = Field(None, alias="crossBorderType")
    destination_office_id: Optional[int] = Field(None, alias="destinationOfficeId")


class CreateSupplyResponse(BaseModel):
    id: str


class GetSuppliesResponse(BaseModel):
    next: int
    supplies: List[SupplyItem]


class SupplyOrderIDsResponse(BaseModel):
    order_ids: List[int] = Field(alias="orderIds")


class BarcodeResponse(BaseModel):
    barcode: str
    file: str


class TrbxItem(BaseModel):
    id: str


class GetTrbxResponse(BaseModel):
    trbxes: List[TrbxItem]
