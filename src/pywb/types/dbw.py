from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


# ==========================================
# ОБЩИЕ СТРУКТУРЫ (DBW)
# ==========================================
class AddressDBW(BaseModel):
    full_address: Optional[str] = Field(None, alias="fullAddress")
    longitude: float
    latitude: float


class OrderOptionsDBW(BaseModel):
    is_b2b: Optional[bool] = Field(None, alias="isB2b")


# ==========================================
# ЗАКАЗЫ (Orders)
# ==========================================
class OrderNewDBW(BaseModel):
    address: Optional[AddressDBW] = None
    sale_price: Optional[int] = Field(None, alias="salePrice")
    required_meta: Optional[List[str]] = Field(None, alias="requiredMeta")
    comment: str
    options: Optional[OrderOptionsDBW] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")
    article: str
    color_code: str = Field(alias="colorCode")
    rid: str
    created_at: datetime = Field(alias="createdAt")
    skus: List[str]
    id: int
    warehouse_id: int = Field(alias="warehouseId")
    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    price: int
    converted_price: int = Field(alias="convertedPrice")
    currency_code: int = Field(alias="currencyCode")
    converted_currency_code: int = Field(alias="convertedCurrencyCode")
    cargo_type: int = Field(alias="cargoType")
    is_zero_order: Optional[bool] = Field(None, alias="isZeroOrder")


class GetNewOrdersDBWResponse(BaseModel):
    orders: List[OrderNewDBW]


class OrderDBW(BaseModel):
    address: Optional[AddressDBW] = None
    options: Optional[OrderOptionsDBW] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")
    article: str
    color_code: str = Field(alias="colorCode")
    rid: str
    created_at: datetime = Field(alias="createdAt")
    skus: List[str]
    id: int
    warehouse_id: int = Field(alias="warehouseId")
    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    price: int
    converted_price: int = Field(alias="convertedPrice")
    currency_code: int = Field(alias="currencyCode")
    converted_currency_code: int = Field(alias="convertedCurrencyCode")
    cargo_type: int = Field(alias="cargoType")
    comment: str
    is_zero_order: Optional[bool] = Field(None, alias="isZeroOrder")


class GetOrdersDBWResponse(BaseModel):
    next: int
    orders: List[OrderDBW]


class OrderStatusDBW(BaseModel):
    id: int
    supplier_status: str = Field(alias="supplierStatus")
    wb_status: str = Field(alias="wbStatus")


class GetOrdersStatusesDBWResponse(BaseModel):
    orders: List[OrderStatusDBW]


class OrderStickerDBW(BaseModel):
    order_id: int = Field(alias="orderId")
    part_a: str = Field(alias="partA")
    part_b: str = Field(alias="partB")
    barcode: str
    file: str  # Base64


class GetStickersDBWResponse(BaseModel):
    stickers: List[OrderStickerDBW]


# ==========================================
# ИНФОРМАЦИЯ О ДОСТАВКЕ, КЛИЕНТАХ И КУРЬЕРАХ
# ==========================================
class DeliveryDateInfo(BaseModel):
    d_time_from: Optional[str] = Field(None, alias="dTimeFrom")
    d_time_to: Optional[str] = Field(None, alias="dTimeTo")
    d_time_from_old: Optional[str] = Field(None, alias="dTimeFromOld")
    d_time_to_old: Optional[str] = Field(None, alias="dTimeToOld")
    d_date_old: Optional[str] = Field(None, alias="dDateOld")
    d_date: str = Field(alias="dDate")
    id: int


class GetDeliveryDatesDBWResponse(BaseModel):
    orders: List[DeliveryDateInfo]


class ClientInfoDBW(BaseModel):
    replacement_phone: str = Field(alias="replacementPhone")
    phone: str
    first_name: str = Field(alias="firstName")
    full_name: str = Field(alias="fullName")
    additional_phones: List[str] = Field(alias="additionalPhones")
    additional_phone_codes: List[int] = Field(alias="additionalPhoneCodes")
    order_id: int = Field(alias="orderId")
    phone_code: int = Field(alias="phoneCode")


class GetClientInfoDBWResponse(BaseModel):
    orders: List[ClientInfoDBW]


class CourierContacts(BaseModel):
    car_number: Optional[str] = Field(None, alias="carNumber")
    full_name: Optional[str] = Field(None, alias="fullName")
    phone: Optional[str] = None
    p_time_from: Optional[datetime] = Field(None, alias="pTimeFrom")
    p_time_to: Optional[datetime] = Field(None, alias="pTimeTo")


class CourierInfo(BaseModel):
    contacts: Optional[CourierContacts] = None
    must_be_assigned: bool = Field(alias="mustBeAssigned")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")


class OrderCourierInfo(BaseModel):
    courier_info: CourierInfo = Field(alias="courierInfo")
    order_id: int = Field(alias="orderID")


class GetCourierInfoDBWResponse(BaseModel):
    orders: List[OrderCourierInfo]


# ==========================================
# МЕТАДАННЫЕ (КИЗы, IMEI и т.д.)
# ==========================================
class MetaValueStr(BaseModel):
    value: Optional[str] = None


class MetaValueListStr(BaseModel):
    value: Optional[List[str]] = None


class OrderMetaDBW(BaseModel):
    imei: Optional[MetaValueStr] = None
    uin: Optional[MetaValueStr] = None
    gtin: Optional[MetaValueStr] = None
    sgtin: Optional[MetaValueListStr] = None


class GetOrderMetaDBWResponse(BaseModel):
    meta: Optional[OrderMetaDBW] = None
