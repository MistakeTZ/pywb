from datetime import datetime
from typing import Optional, List, TypeVar, Generic, Any
from pydantic import BaseModel, Field

T = TypeVar("T")


class WBContentResponse(BaseModel, Generic[T]):
    """
    Универсальная обертка для ответов из API Контента.
    Автоматически парсит структуру {"data": ..., "error": false, ...}
    """

    data: Optional[T] = None
    error: bool
    error_text: str = Field(alias="errorText")
    additional_errors: Optional[Any] = Field(None, alias="additionalErrors")


# --- Категории и предметы ---
class SubjectItem(BaseModel):
    subject_id: int = Field(alias="subjectID")
    parent_id: int = Field(alias="parentID")
    subject_name: str = Field(alias="subjectName")
    parent_name: str = Field(alias="parentName")


# --- Карточки товаров (Получение) ---
class CardPhoto(BaseModel):
    big: Optional[str] = None
    c246x328: Optional[str] = None
    c516x688: Optional[str] = None
    square: Optional[str] = None
    tm: Optional[str] = None


class CardDimensions(BaseModel):
    length: int
    width: int
    height: int
    weight_brutto: float = Field(alias="weightBrutto")
    is_valid: Optional[bool] = Field(None, alias="isValid")


class CardCharacteristic(BaseModel):
    id: int
    name: str
    value: Any


class CardSize(BaseModel):
    chrt_id: int = Field(alias="chrtID")
    tech_size: str = Field(alias="techSize")
    wb_size: str = Field(alias="wbSize")
    skus: List[str]


class CardItem(BaseModel):
    nm_id: int = Field(alias="nmID")
    imt_id: int = Field(alias="imtID")
    vendor_code: str = Field(alias="vendorCode")
    subject_id: int = Field(alias="subjectID")
    subject_name: str = Field(alias="subjectName")
    brand: str
    title: str
    description: str
    photos: List[CardPhoto]
    dimensions: CardDimensions
    characteristics: List[CardCharacteristic]
    sizes: List[CardSize]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")


class CardsCursor(BaseModel):
    updated_at: Optional[str] = Field(None, alias="updatedAt")
    nm_id: Optional[int] = Field(None, alias="nmID")
    total: int


class CardsListData(BaseModel):
    cards: List[CardItem]
    cursor: CardsCursor


# --- Карточки товаров (Создание/Обновление) ---
class CreateCardSize(BaseModel):
    tech_size: Optional[str] = Field(None, alias="techSize")
    wb_size: Optional[str] = Field(None, alias="wbSize")
    price: Optional[int] = None
    skus: Optional[List[str]] = None


class CreateCardCharacteristic(BaseModel):
    id: int
    value: Any


class CreateCardVariant(BaseModel):
    vendor_code: str = Field(alias="vendorCode")
    brand: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    dimensions: Optional[CardDimensions] = None
    sizes: List[CreateCardSize]
    characteristics: List[CreateCardCharacteristic]


class CreateCardItem(BaseModel):
    subject_id: int = Field(alias="subjectID")
    variants: List[CreateCardVariant]


# --- Цены и Скидки ---
class GoodPriceItem(BaseModel):
    nm_id: int = Field(alias="nmID")
    price: int
    discount: int


class SetPricesTaskResponse(BaseModel):
    id: int
    already_exists: bool = Field(alias="alreadyExists")


# --- Склады и Остатки (Marketplace) ---
class WarehouseItem(BaseModel):
    id: int
    name: str
    office_id: int = Field(alias="officeId")
    cargo_type: int = Field(alias="cargoType")
    delivery_type: int = Field(alias="deliveryType")


class StockItem(BaseModel):
    chrt_id: int = Field(alias="chrtId")
    amount: int
