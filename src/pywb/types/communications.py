from datetime import datetime
from typing import Optional, List, TypeVar, Generic, Any
from pydantic import BaseModel, Field

T = TypeVar("T")


class WBFBResponse(BaseModel, Generic[T]):
    """Универсальная обертка для API Отзывов и Вопросов."""

    data: Optional[T] = None
    error: bool
    error_text: str = Field(alias="errorText")
    additional_errors: Optional[List[str]] = Field(None, alias="additionalErrors")


class WBChatResponse(BaseModel, Generic[T]):
    """Универсальная обертка для API Чатов."""

    result: Optional[T] = None
    errors: Optional[List[str]] = None


# ==========================================
# ВОПРОСЫ И ОТЗЫВЫ
# ==========================================


class UnseenFQ(BaseModel):
    has_new_questions: bool = Field(alias="hasNewQuestions")
    has_new_feedbacks: bool = Field(alias="hasNewFeedbacks")


class CountUnanswered(BaseModel):
    count_unanswered: int = Field(alias="countUnanswered")
    count_unanswered_today: int = Field(alias="countUnansweredToday")


class FQAnswer(BaseModel):
    text: str
    state: Optional[str] = None
    editable: Optional[bool] = None
    create_date: Optional[datetime] = Field(None, alias="createDate")


class ProductDetailsFQ(BaseModel):
    nm_id: int = Field(alias="nmId")
    imt_id: int = Field(alias="imtId")
    product_name: str = Field(alias="productName")
    supplier_article: Optional[str] = Field(None, alias="supplierArticle")
    supplier_name: Optional[str] = Field(None, alias="supplierName")
    brand_name: Optional[str] = Field(None, alias="brandName")
    size: Optional[str] = None


class QuestionItem(BaseModel):
    id: str
    text: str
    created_date: datetime = Field(alias="createdDate")
    state: str
    answer: Optional[FQAnswer] = None
    product_details: ProductDetailsFQ = Field(alias="productDetails")
    was_viewed: bool = Field(alias="wasViewed")
    is_warned: bool = Field(alias="isWarned")


class PhotoLinkFQ(BaseModel):
    full_size: str = Field(alias="fullSize")
    mini_size: str = Field(alias="miniSize")


class VideoFQ(BaseModel):
    preview_image: str = Field(alias="previewImage")
    link: str
    duration_sec: int = Field(alias="durationSec")


class FeedbackItem(BaseModel):
    id: str
    text: str
    pros: str
    cons: str
    product_valuation: int = Field(alias="productValuation")
    created_date: datetime = Field(alias="createdDate")
    answer: Optional[FQAnswer] = None
    state: str
    product_details: ProductDetailsFQ = Field(alias="productDetails")
    photo_links: Optional[List[PhotoLinkFQ]] = Field(None, alias="photoLinks")
    video: Optional[VideoFQ] = None
    was_viewed: bool = Field(alias="wasViewed")
    user_name: str = Field(alias="userName")
    order_status: str = Field(alias="orderStatus")
    matching_size: str = Field(alias="matchingSize")
    bables: Optional[List[str]] = None
    last_order_shk_id: Optional[int] = Field(None, alias="lastOrderShkId")


class GetQuestionsData(BaseModel):
    count_unanswered: int = Field(alias="countUnanswered")
    count_archive: int = Field(alias="countArchive")
    questions: List[QuestionItem]


class GetFeedbacksData(BaseModel):
    count_unanswered: int = Field(alias="countUnanswered")
    count_archive: int = Field(alias="countArchive")
    feedbacks: List[FeedbackItem]


# ==========================================
# ЧАТЫ С ПОКУПАТЕЛЯМИ
# ==========================================


class ChatGoodCard(BaseModel):
    date: datetime
    nm_id: int = Field(alias="nmID")
    price: int
    price_currency: str = Field(alias="priceCurrency")
    rid: str
    size: str


class ChatLastMessage(BaseModel):
    text: str
    add_timestamp: int = Field(alias="addTimestamp")


class ChatItem(BaseModel):
    chat_id: str = Field(alias="chatID")
    reply_sign: str = Field(alias="replySign")
    client_name: str = Field(alias="clientName")
    good_card: ChatGoodCard = Field(alias="goodCard")
    last_message: ChatLastMessage = Field(alias="lastMessage")


class ChatFile(BaseModel):
    content_type: str = Field(alias="contentType")
    date: str
    download_id: str = Field(alias="downloadID")
    name: str
    url: str
    size: int


class ChatEventMessage(BaseModel):
    text: Optional[str] = None
    attachments: Optional[Any] = None


class ChatEvent(BaseModel):
    chat_id: str = Field(alias="chatID")
    event_id: str = Field(alias="eventID")
    event_type: str = Field(alias="eventType")
    is_new_chat: Optional[bool] = Field(None, alias="isNewChat")
    message: Optional[ChatEventMessage] = None
    source: str
    sender: str
    client_name: Optional[str] = Field(None, alias="clientName")


class ChatEventsResult(BaseModel):
    next: Optional[int] = None
    newest_event_time: datetime = Field(alias="newestEventTime")
    oldest_event_time: datetime = Field(alias="oldestEventTime")
    total_events: int = Field(alias="totalEvents")
    events: List[ChatEvent]


# ==========================================
# ЗАЯВКИ НА ВОЗВРАТ
# ==========================================


class ClaimItem(BaseModel):
    id: str
    claim_type: int
    status: int
    status_ex: int
    nm_id: int
    user_comment: str
    wb_comment: Optional[str] = None
    dt: datetime
    imt_name: Optional[str] = None
    order_dt: datetime
    dt_update: datetime
    photos: Optional[List[str]] = None
    video_paths: Optional[List[str]] = None
    actions: List[str]
    price: float
    currency_code: str
    srid: str


class GetClaimsResponse(BaseModel):
    claims: List[ClaimItem]
    total: int
