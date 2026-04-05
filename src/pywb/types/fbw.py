from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

# ==========================================
# ВАРИАНТЫ ПРИЕМКИ (Acceptance Options)
# ==========================================


class Good(BaseModel):
    quantity: int
    barcode: str


class OptionsError(BaseModel):
    title: Optional[str] = None
    detail: Optional[str] = None


class WarehouseOption(BaseModel):
    warehouse_id: int = Field(alias="warehouseID")
    can_box: bool = Field(alias="canBox")
    can_monopallet: bool = Field(alias="canMonopallet")
    can_supersafe: bool = Field(alias="canSupersafe")
    is_box_on_pallet: bool = Field(alias="isBoxOnPallet")


class OptionsResultItem(BaseModel):
    barcode: str
    error: Optional[OptionsError] = None
    is_error: Optional[bool] = Field(None, alias="isError")
    warehouses: Optional[List[WarehouseOption]] = None


class OptionsResultModel(BaseModel):
    result: List[OptionsResultItem]
    request_id: Optional[str] = Field(None, alias="requestId")


# ==========================================
# ИНФОРМАЦИЯ О СКЛАДАХ И ТАРИФАХ
# ==========================================


class WarehouseItemFBW(BaseModel):
    id: int = Field(alias="ID")
    name: str
    address: str
    work_time: str = Field(alias="workTime")
    is_active: bool = Field(alias="isActive")
    is_transit_active: bool = Field(alias="isTransitActive")


class VolumeTariff(BaseModel):
    from_liters: int = Field(alias="from")
    to_liters: int = Field(alias="to")
    value: float


class TransitTariff(BaseModel):
    transit_warehouse_name: str = Field(alias="transitWarehouseName")
    destination_warehouse_name: str = Field(alias="destinationWarehouseName")
    active_from: datetime = Field(alias="activeFrom")
    box_tariff: Optional[List[VolumeTariff]] = Field(None, alias="boxTariff")
    pallet_tariff: int = Field(alias="palletTariff")


# ==========================================
# ПОСТАВКИ (Supplies)
# ==========================================


class DateFilterRequest(BaseModel):
    from_date: str = Field(alias="from")  # ISO 8601 string
    till: str
    type: str  # factDate, createDate, supplyDate, updatedDate


class SuppliesFiltersRequest(BaseModel):
    dates: Optional[List[DateFilterRequest]] = None
    status_ids: Optional[List[int]] = Field(None, alias="statusIDs")


class SupplyFBW(BaseModel):
    phone: str
    supply_id: Optional[int] = Field(None, alias="supplyID")
    preorder_id: int = Field(alias="preorderID")
    create_date: datetime = Field(alias="createDate")
    supply_date: Optional[datetime] = Field(None, alias="supplyDate")
    fact_date: Optional[datetime] = Field(None, alias="factDate")
    updated_date: Optional[datetime] = Field(None, alias="updatedDate")
    status_id: int = Field(alias="statusID")
    box_type_id: int = Field(alias="boxTypeID")
    is_box_on_pallet: Optional[bool] = Field(None, alias="isBoxOnPallet")


class SupplyDetailsFBW(BaseModel):
    phone: str
    status_id: int = Field(alias="statusID")
    virtual_type_id: Optional[int] = Field(None, alias="virtualTypeID")
    box_type_id: int = Field(alias="boxTypeID")
    create_date: datetime = Field(alias="createDate")
    supply_date: Optional[datetime] = Field(None, alias="supplyDate")
    fact_date: Optional[datetime] = Field(None, alias="factDate")
    updated_date: Optional[datetime] = Field(None, alias="updatedDate")
    warehouse_id: int = Field(alias="warehouseID")
    warehouse_name: str = Field(alias="warehouseName")
    actual_warehouse_id: Optional[int] = Field(None, alias="actualWarehouseID")
    actual_warehouse_name: str = Field(alias="actualWarehouseName")
    transit_warehouse_id: Optional[int] = Field(None, alias="transitWarehouseID")
    transit_warehouse_name: str = Field(alias="transitWarehouseName")
    acceptance_cost: Optional[float] = Field(None, alias="acceptanceCost")
    paid_acceptance_coefficient: Optional[float] = Field(
        None, alias="paidAcceptanceCoefficient"
    )
    reject_reason: Optional[str] = Field(None, alias="rejectReason")
    supplier_assign_name: str = Field(alias="supplierAssignName")
    storage_coef: Optional[str] = Field(None, alias="storageCoef")
    delivery_coef: Optional[str] = Field(None, alias="deliveryCoef")
    quantity: int
    ready_for_sale_quantity: int = Field(alias="readyForSaleQuantity")
    accepted_quantity: int = Field(alias="acceptedQuantity")
    unloading_quantity: int = Field(alias="unloadingQuantity")
    depersonalized_quantity: Optional[int] = Field(None, alias="depersonalizedQuantity")
    is_box_on_pallet: Optional[bool] = Field(None, alias="isBoxOnPallet")


# ==========================================
# ТОВАРЫ И КОРОБА В ПОСТАВКЕ
# ==========================================


class GoodInSupplyFBW(BaseModel):
    barcode: str
    vendor_code: str = Field(alias="vendorCode")
    nm_id: int = Field(alias="nmID")
    need_kiz: bool = Field(alias="needKiz")
    tnved: Optional[str] = None
    tech_size: str = Field(alias="techSize")
    color: Optional[str] = None
    supplier_box_amount: Optional[int] = Field(None, alias="supplierBoxAmount")
    quantity: int
    ready_for_sale_quantity: Optional[int] = Field(None, alias="readyForSaleQuantity")
    accepted_quantity: Optional[int] = Field(None, alias="acceptedQuantity")
    unloading_quantity: Optional[int] = Field(None, alias="unloadingQuantity")


class GoodInBoxFBW(BaseModel):
    barcode: str
    quantity: int


class BoxFBW(BaseModel):
    package_code: str = Field(alias="packageCode")
    quantity: int
    barcodes: List[GoodInBoxFBW]
