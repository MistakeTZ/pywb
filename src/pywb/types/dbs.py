from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, Field


# ==========================================
# ОБЩИЕ МОДЕЛИ ЗАКАЗОВ (DBS)
# ==========================================
class AddressDBS(BaseModel):
    full_address: Optional[str] = Field(None, alias="fullAddress")
    longitude: float
    latitude: float


class OrderOptionsDBS(BaseModel):
    is_b2b: Optional[bool] = Field(None, alias="isB2b")


class OrderNewDBS(BaseModel):
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
    delivery_type: str = Field(alias="deliveryType")
    options: Optional[OrderOptionsDBS] = None
    address: Optional[AddressDBS] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")
    sale_price: Optional[int] = Field(None, alias="salePrice")
    final_price: Optional[int] = Field(None, alias="finalPrice")
    converted_final_price: Optional[int] = Field(None, alias="convertedFinalPrice")
    wb_sticker_id: Optional[int] = Field(None, alias="wbStickerId")
    required_meta: Optional[List[str]] = Field(None, alias="requiredMeta")


class OrderDBS(BaseModel):
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
    delivery_type: str = Field(alias="deliveryType")
    options: Optional[OrderOptionsDBS] = None
    address: Optional[AddressDBS] = None
    order_uid: Optional[str] = Field(None, alias="orderUid")
    group_id: Optional[str] = Field(None, alias="groupId")
    scan_price: Optional[int] = Field(None, alias="scanPrice")
    final_price: Optional[int] = Field(None, alias="finalPrice")
    converted_final_price: Optional[int] = Field(None, alias="convertedFinalPrice")
    wb_sticker_id: Optional[int] = Field(None, alias="wbStickerId")


class GetNewOrdersDBSResponse(BaseModel):
    orders: List[OrderNewDBS]


class GetOrdersDBSResponse(BaseModel):
    next: int
    orders: List[OrderDBS]


# ==========================================
# ИНФОРМАЦИЯ О ПОКУПАТЕЛЯХ И ГРУППАХ
# ==========================================
class OrderGroupDBS(BaseModel):
    group_id: str = Field(alias="groupID")
    delivery_cost: int = Field(alias="deliveryCost")
    converted_delivery_cost: int = Field(alias="convertedDeliveryCost")
    currency_code: int = Field(alias="currencyCode")
    converted_currency_code: int = Field(alias="convertedCurrencyCode")


class ClientInfoDBS(BaseModel):
    order_id: int = Field(alias="orderID")
    first_name: str = Field(alias="firstName")
    full_name: str = Field(alias="fullName")
    phone: str
    phone_code: int = Field(alias="phoneCode")
    replacement_phone: str = Field(alias="replacementPhone")
    additional_phone_codes: List[str] = Field(alias="additionalPhoneCodes")


class ClientInfoDBSResp(BaseModel):
    orders: List[ClientInfoDBS]


class B2BClientInfo(BaseModel):
    inn: Optional[str] = None
    kpp: Optional[str] = None
    org_name: Optional[str] = Field(None, alias="orgName")


class BatchErrorDetail(BaseModel):
    code: int
    detail: str


class B2BClientInfoItem(BaseModel):
    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    data: Optional[B2BClientInfo] = None
    errors: Optional[List[BatchErrorDetail]] = None


class B2BClientInfoResp(BaseModel):
    request_id: str = Field(alias="requestId")
    results: List[B2BClientInfoItem]


# ==========================================
# СТАТУСЫ ЗАКАЗОВ (БАТЧИ)
# ==========================================
class OrderStatusV2(BaseModel):
    order_id: int = Field(alias="orderId")
    supplier_status: str = Field(alias="supplierStatus")
    wb_status: str = Field(alias="wbStatus")
    errors: Optional[List[BatchErrorDetail]] = None


class OrderStatusesV2Resp(BaseModel):
    orders: List[OrderStatusV2]


class StatusSetResponseItem(BaseModel):
    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: Optional[List[BatchErrorDetail]] = None


class StatusSetResponsesResp(BaseModel):
    request_id: str = Field(alias="requestId")
    results: List[StatusSetResponseItem]


class OrderCodeRequestItem(BaseModel):
    order_id: int = Field(alias="orderId")
    code: str


class StickerDBS(BaseModel):
    order_id: int = Field(alias="orderId")
    part_a: str = Field(alias="partA")
    part_b: str = Field(alias="partB")
    barcode: str
    file: str  # Base64 PDF


class GetStickersDBSResponse(BaseModel):
    stickers: List[StickerDBS]


# ==========================================
# МЕТАДАННЫЕ (БАТЧИ)
# ==========================================
class CustomsDeclarationItem(BaseModel):
    value: Optional[str] = None


class OrderMetaV2(BaseModel):
    order_id: int = Field(alias="orderId")
    imei: Optional[str] = None
    uin: Optional[str] = None
    gtin: Optional[str] = None
    sgtin: Optional[List[str]] = None
    customs_declaration: Optional[CustomsDeclarationItem] = Field(
        None, alias="customsDeclaration"
    )
    error: Optional[str] = None


class OrdersMetaResponse(BaseModel):
    meta: List[OrderMetaV2]


class UpdateMetaSgtinItem(BaseModel):
    order_id: int = Field(alias="orderId")
    sgtins: List[str]


class UpdateMetaUinItem(BaseModel):
    order_id: int = Field(alias="orderId")
    uin: str


class UpdateMetaImeiItem(BaseModel):
    order_id: int = Field(alias="orderId")
    imei: str


class UpdateMetaGtinItem(BaseModel):
    order_id: int = Field(alias="orderId")
    gtin: str


class UpdateMetaCustomsItem(BaseModel):
    order_id: int = Field(alias="orderId")
    customs_declaration: str = Field(alias="customsDeclaration")
