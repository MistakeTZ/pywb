from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# ==========================================
# ОБЩИЕ МОДЕЛИ ЗАКАЗОВ (Click & Collect)
# ==========================================


class AddressCC(BaseModel):
    full_address: Optional[str] = Field(None, alias="fullAddress")
    longitude: float
    latitude: float


class OrderOptionsCC(BaseModel):
    is_b2b: Optional[bool] = Field(None, alias="isB2b")


class OrderNewCC(BaseModel):
    id: int
    rid: str
    created_at: datetime = Field(alias="createdAt")
    warehouse_id: int = Field(alias="warehouseId")
    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    price: int
    converted_price: int = Field(alias="convertedPrice")
    currency_code: int = Field(alias="currencyCode")
    converted_currency_code: int = Field(alias="convertedCurrencyCode")
    cargo_type: int = Field(alias="cargoType")
    article: str
    color_code: str = Field(alias="colorCode")
    skus: List[str]
    comment: str
    is_zero_order: bool = Field(alias="isZeroOrder")
    options: Optional[OrderOptionsCC] = None
    address: Optional[AddressCC] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")
    sale_price: Optional[int] = Field(None, alias="salePrice")
    required_meta: Optional[List[str]] = Field(None, alias="requiredMeta")


class OrderCC(BaseModel):
    id: int
    rid: str
    created_at: datetime = Field(alias="createdAt")
    warehouse_id: int = Field(alias="warehouseId")
    nm_id: int = Field(alias="nmId")
    chrt_id: int = Field(alias="chrtId")
    price: int
    converted_price: int = Field(alias="convertedPrice")
    currency_code: int = Field(alias="currencyCode")
    converted_currency_code: int = Field(alias="convertedCurrencyCode")
    cargo_type: int = Field(alias="cargoType")
    article: str
    color_code: str = Field(alias="colorCode")
    skus: List[str]
    comment: str
    is_zero_order: bool = Field(alias="isZeroOrder")
    options: Optional[OrderOptionsCC] = None
    address: Optional[AddressCC] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")


class GetNewOrdersCCResponse(BaseModel):
    orders: List[OrderNewCC]


class GetOrdersCCResponse(BaseModel):
    next: int
    orders: List[OrderCC]


# ==========================================
# ИНФОРМАЦИЯ О КЛИЕНТАХ, СТАТУСАХ И СТИКЕРАХ
# ==========================================


class ClientInfoCC(BaseModel):
    order_id: int = Field(alias="orderId")
    first_name: str = Field(alias="firstName")
    full_name: str = Field(alias="fullName")
    phone: str
    phone_code: int = Field(alias="phoneCode")
    replacement_phone: str = Field(alias="replacementPhone")
    additional_phones: List[str] = Field(alias="additionalPhones")
    additional_phone_codes: List[int] = Field(alias="additionalPhoneCodes")


class ClientInfoCCResp(BaseModel):
    orders: List[ClientInfoCC]


class OrderStatusCC(BaseModel):
    id: int
    supplier_status: str = Field(alias="supplierStatus")
    wb_status: str = Field(alias="wbStatus")


class OrderStatusesCCResp(BaseModel):
    orders: List[OrderStatusCC]


class StickerCC(BaseModel):
    order_id: int = Field(alias="orderId")
    part_a: str = Field(alias="partA")
    part_b: str = Field(alias="partB")
    barcode: str
    file: str  # Base64


class GetStickersCCResponse(BaseModel):
    stickers: List[StickerCC]


# ==========================================
# МЕТАДАННЫЕ
# ==========================================


class MetaItemString(BaseModel):
    value: Optional[str] = None


class MetaItemArray(BaseModel):
    value: Optional[List[str]] = None


class MetaCC(BaseModel):
    imei: Optional[MetaItemString] = None
    uin: Optional[MetaItemString] = None
    gtin: Optional[MetaItemString] = None
    sgtin: Optional[MetaItemArray] = None


class GetOrderMetaCCResponse(BaseModel):
    meta: Optional[MetaCC] = None
