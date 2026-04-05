from typing import Optional, List
from pydantic import BaseModel, Field

# ==========================================
# КОМИССИИ
# ==========================================
class CommissionItem(BaseModel):
    parent_id: int = Field(alias="parentID")
    parent_name: str = Field(alias="parentName")
    subject_id: int = Field(alias="subjectID")
    subject_name: str = Field(alias="subjectName")

    # Поля зависят от локали (страны продавца)
    kgvp_booking: Optional[float] = Field(None, alias="kgvpBooking")
    kgvp_marketplace: Optional[float] = Field(None, alias="kgvpMarketplace")
    kgvp_pickup: Optional[float] = Field(None, alias="kgvpPickup")
    kgvp_supplier: Optional[float] = Field(None, alias="kgvpSupplier")
    kgvp_supplier_express: Optional[float] = Field(None, alias="kgvpSupplierExpress")
    paid_storage_kgvp: Optional[float] = Field(None, alias="paidStorageKgvp")
    kgvp_china: Optional[float] = Field(None, alias="kgvpChina")
    kgvp_turkey: Optional[float] = Field(None, alias="kgvpTurkey")
    kgvp_marketplace_uz: Optional[float] = Field(None, alias="kgvpMarketplaceUz")
    kgvp_paid_storage_uz: Optional[float] = Field(None, alias="kgvpPaidStorageUz")
    kgvp_supplier_uz: Optional[float] = Field(None, alias="kgvpSupplierUz")
    kgvp_uae: Optional[float] = Field(None, alias="kgvpUAE")


class CommissionResponse(BaseModel):
    report: List[CommissionItem]


# ==========================================
# ТАРИФЫ: КОРОБА (Box)
# ==========================================
class WarehouseBoxRates(BaseModel):
    warehouse_name: str = Field(alias="warehouseName")
    geo_name: str = Field(alias="geoName")
    box_delivery_base: str = Field(alias="boxDeliveryBase")
    box_delivery_liter: str = Field(alias="boxDeliveryLiter")
    box_delivery_coef_expr: str = Field(alias="boxDeliveryCoefExpr")
    box_delivery_marketplace_base: str = Field(alias="boxDeliveryMarketplaceBase")
    box_delivery_marketplace_liter: str = Field(alias="boxDeliveryMarketplaceLiter")
    box_delivery_marketplace_coef_expr: str = Field(
        alias="boxDeliveryMarketplaceCoefExpr"
    )
    box_storage_base: str = Field(alias="boxStorageBase")
    box_storage_liter: str = Field(alias="boxStorageLiter")
    box_storage_coef_expr: str = Field(alias="boxStorageCoefExpr")


class WarehousesBoxRates(BaseModel):
    dt_next_box: str = Field(alias="dtNextBox")
    dt_till_max: str = Field(alias="dtTillMax")
    warehouse_list: Optional[List[WarehouseBoxRates]] = Field(
        None, alias="warehouseList"
    )


class TariffsBoxData(BaseModel):
    data: WarehousesBoxRates


class TariffsBoxResponse(BaseModel):
    response: TariffsBoxData


# ==========================================
# ТАРИФЫ: ПАЛЛЕТЫ (Pallet)
# ==========================================
class WarehousePalletRates(BaseModel):
    warehouse_name: str = Field(alias="warehouseName")
    pallet_delivery_value_base: str = Field(alias="palletDeliveryValueBase")
    pallet_delivery_value_liter: str = Field(alias="palletDeliveryValueLiter")
    pallet_delivery_expr: str = Field(alias="palletDeliveryExpr")
    pallet_storage_value_expr: str = Field(alias="palletStorageValueExpr")
    pallet_storage_expr: str = Field(alias="palletStorageExpr")


class WarehousesPalletRates(BaseModel):
    dt_next_pallet: str = Field(alias="dtNextPallet")
    dt_till_max: str = Field(alias="dtTillMax")
    warehouse_list: Optional[List[WarehousePalletRates]] = Field(
        None, alias="warehouseList"
    )


class TariffsPalletData(BaseModel):
    data: WarehousesPalletRates


class TariffsPalletResponse(BaseModel):
    response: TariffsPalletData


# ==========================================
# ТАРИФЫ: ВОЗВРАТЫ (Return)
# ==========================================
class WarehouseReturnRates(BaseModel):
    warehouse_name: str = Field(alias="warehouseName")
    delivery_dump_kgt_office_base: str = Field(alias="deliveryDumpKgtOfficeBase")
    delivery_dump_kgt_office_liter: str = Field(alias="deliveryDumpKgtOfficeLiter")
    delivery_dump_kgt_return_expr: str = Field(alias="deliveryDumpKgtReturnExpr")
    delivery_dump_srg_office_expr: str = Field(alias="deliveryDumpSrgOfficeExpr")
    delivery_dump_srg_return_expr: str = Field(alias="deliveryDumpSrgReturnExpr")
    delivery_dump_sup_courier_base: str = Field(alias="deliveryDumpSupCourierBase")
    delivery_dump_sup_courier_liter: str = Field(alias="deliveryDumpSupCourierLiter")
    delivery_dump_sup_office_base: str = Field(alias="deliveryDumpSupOfficeBase")
    delivery_dump_sup_office_liter: str = Field(alias="deliveryDumpSupOfficeLiter")
    delivery_dump_sup_return_expr: str = Field(alias="deliveryDumpSupReturnExpr")


class WarehousesReturnRates(BaseModel):
    dt_next_delivery_dump_kgt: str = Field(alias="dtNextDeliveryDumpKgt")
    dt_next_delivery_dump_srg: str = Field(alias="dtNextDeliveryDumpSrg")
    dt_next_delivery_dump_sup: str = Field(alias="dtNextDeliveryDumpSup")
    warehouse_list: Optional[List[WarehouseReturnRates]] = Field(
        None, alias="warehouseList"
    )


class ReturnTariffsData(BaseModel):
    data: WarehousesReturnRates


class ReturnTariffsResponse(BaseModel):
    response: ReturnTariffsData


# ==========================================
# КОЭФФИЦИЕНТЫ ПРИЕМКИ
# ==========================================
class AcceptanceCoefficient(BaseModel):
    date: str
    coefficient: float
    warehouse_id: int = Field(alias="warehouseID")
    warehouse_name: str = Field(alias="warehouseName")
    allow_unload: bool = Field(alias="allowUnload")
    box_type_id: Optional[int] = Field(None, alias="boxTypeID")
    storage_coef: Optional[str] = Field(None, alias="storageCoef")
    delivery_coef: Optional[str] = Field(None, alias="deliveryCoef")
    delivery_base_liter: Optional[str] = Field(None, alias="deliveryBaseLiter")
    delivery_additional_liter: Optional[str] = Field(
        None, alias="deliveryAdditionalLiter"
    )
    storage_base_liter: Optional[str] = Field(None, alias="storageBaseLiter")
    storage_additional_liter: Optional[str] = Field(
        None, alias="storageAdditionalLiter"
    )
    is_sorting_center: bool = Field(alias="isSortingCenter")
