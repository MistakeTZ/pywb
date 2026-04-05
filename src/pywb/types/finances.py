from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, Field

# ==========================================
# БАЛАНС
# ==========================================


class BalanceData(BaseModel):
    currency: str
    current: float
    for_withdraw: float


# ==========================================
# ОТЧЕТ О РЕАЛИЗАЦИИ (Детализация)
# ==========================================


class DetailReportItem(BaseModel):
    realizationreport_id: Optional[int] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    create_dt: Optional[datetime] = None
    currency_name: Optional[str] = None
    suppliercontract_code: Optional[Any] = None
    rrd_id: Optional[int] = None
    gi_id: Optional[int] = None
    dlv_prc: Optional[float] = None
    fix_tariff_date_from: Optional[datetime] = None
    fix_tariff_date_to: Optional[datetime] = None
    subject_name: Optional[str] = None
    nm_id: Optional[int] = None
    brand_name: Optional[str] = None
    sa_name: Optional[str] = None
    ts_name: Optional[str] = None
    barcode: Optional[str] = None
    doc_type_name: Optional[str] = None
    quantity: Optional[int] = None
    retail_price: Optional[float] = None
    retail_amount: Optional[float] = None
    sale_percent: Optional[int] = None
    commission_percent: Optional[float] = None
    office_name: Optional[str] = None
    supplier_oper_name: Optional[str] = None
    order_dt: Optional[datetime] = None
    sale_dt: Optional[datetime] = None
    rr_dt: Optional[datetime] = None
    shk_id: Optional[int] = None
    retail_price_withdisc_rub: Optional[float] = None
    delivery_amount: Optional[int] = None
    return_amount: Optional[int] = None
    delivery_rub: Optional[float] = None
    gi_box_type_name: Optional[str] = None
    product_discount_for_report: Optional[float] = None
    supplier_promo: Optional[float] = None
    ppvz_spp_prc: Optional[float] = None
    ppvz_kvw_prc_base: Optional[float] = None
    ppvz_kvw_prc: Optional[float] = None
    sup_rating_prc_up: Optional[float] = None
    is_kgvp_v2: Optional[float] = None
    ppvz_sales_commission: Optional[float] = None
    ppvz_for_pay: Optional[float] = None
    ppvz_reward: Optional[float] = None
    acquiring_fee: Optional[float] = None
    acquiring_percent: Optional[float] = None
    payment_processing: Optional[str] = None
    acquiring_bank: Optional[str] = None
    ppvz_vw: Optional[float] = None
    ppvz_vw_nds: Optional[float] = None
    ppvz_office_name: Optional[str] = None
    ppvz_office_id: Optional[int] = None
    ppvz_supplier_id: Optional[int] = None
    ppvz_supplier_name: Optional[str] = None
    ppvz_inn: Optional[str] = None
    declaration_number: Optional[str] = None
    bonus_type_name: Optional[str] = None
    sticker_id: Optional[str] = None
    site_country: Optional[str] = None
    srv_dbs: Optional[bool] = None
    penalty: Optional[float] = None
    additional_payment: Optional[float] = None
    rebill_logistic_cost: Optional[float] = None
    rebill_logistic_org: Optional[str] = None
    storage_fee: Optional[float] = None
    deduction: Optional[float] = None
    acceptance: Optional[float] = None
    assembly_id: Optional[int] = None
    kiz: Optional[str] = None
    srid: Optional[str] = None
    report_type: Optional[int] = None
    is_legal_entity: Optional[bool] = None
    trbx_id: Optional[str] = None
    installment_cofinancing_amount: Optional[float] = None
    wibes_wb_discount_percent: Optional[float] = None
    cashback_amount: Optional[float] = None
    cashback_discount: Optional[float] = None
    cashback_commission_change: Optional[float] = None
    order_uid: Optional[str] = None
    payment_schedule: Optional[float] = None
    delivery_method: Optional[str] = None
    seller_promo_id: Optional[int] = None
    seller_promo_discount: Optional[float] = None
    loyalty_id: Optional[int] = None
    loyalty_discount: Optional[float] = None
    uuid_promocode: Optional[str] = None
    sale_price_promocode_discount_prc: Optional[float] = None


# ==========================================
# ДОКУМЕНТЫ
# ==========================================


class DocumentCategory(BaseModel):
    name: str
    title: str


class DocumentCategoriesData(BaseModel):
    data: dict[str, List[DocumentCategory]]  # {"categories": [...]}


class DocumentItem(BaseModel):
    service_name: str = Field(alias="serviceName")
    name: str
    category: str
    extensions: List[str]
    creation_time: datetime = Field(alias="creationTime")
    viewed: bool


class DocumentListData(BaseModel):
    data: dict[str, List[DocumentItem]]  # {"documents": [...]}


class DocumentDownloadItem(BaseModel):
    file_name: str = Field(alias="fileName")
    extension: str
    document: str  # Base64 encoded


class DocumentDownloadData(BaseModel):
    data: DocumentDownloadItem


class DownloadParam(BaseModel):
    extension: str
    service_name: str = Field(alias="serviceName")
