from typing import ClassVar, List, Optional, Any
from pydantic import Field

from .base import WBMethod
from ..enums import WBDomain
from ..types import (
    WBFBResponse,
    WBChatResponse,
    UnseenFQ,
    GetQuestionsData,
    GetFeedbacksData,
    ChatItem,
    ChatEventsResult,
    GetClaimsResponse,
)


# ==========================================
# ОТЗЫВЫ И ВОПРОСЫ
# ==========================================
class GetUnseenFQ(WBMethod[WBFBResponse[UnseenFQ]]):
    """Проверка наличия непросмотренных отзывов и вопросов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/new-feedbacks-questions"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = WBFBResponse[UnseenFQ]


class GetQuestions(WBMethod[WBFBResponse[GetQuestionsData]]):
    """Получение списка вопросов с пагинацией."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/questions"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = WBFBResponse[GetQuestionsData]

    is_answered: bool = Field(alias="isAnswered")
    take: int
    skip: int
    nm_id: Optional[int] = Field(None, alias="nmId")
    order: Optional[str] = None  # dateAsc / dateDesc


class PatchQuestion(WBMethod[WBFBResponse[Any]]):
    """Просмотр, отклонение или ответ на вопрос."""

    __http_method__: ClassVar[str] = "PATCH"
    __api_path__: ClassVar[str] = "/api/v1/questions"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = WBFBResponse[Any]

    id: str
    was_viewed: Optional[bool] = Field(None, alias="wasViewed")
    answer: Optional[dict] = None
    state: Optional[str] = None


class GetFeedbacks(WBMethod[WBFBResponse[GetFeedbacksData]]):
    """Получение списка отзывов с пагинацией."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/feedbacks"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = WBFBResponse[GetFeedbacksData]

    is_answered: bool = Field(alias="isAnswered")
    take: int
    skip: int
    nm_id: Optional[int] = Field(None, alias="nmId")
    order: Optional[str] = None


class AnswerFeedback(WBMethod[bool]):
    """Отправка ответа на отзыв."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v1/feedbacks/answer"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = bool

    id: str
    text: str


class EditFeedbackAnswer(WBMethod[bool]):
    """Редактирование ответа на отзыв."""

    __http_method__: ClassVar[str] = "PATCH"
    __api_path__: ClassVar[str] = "/api/v1/feedbacks/answer"
    __domain__: ClassVar[WBDomain] = WBDomain.FEEDBACKS
    __returning__: ClassVar[type] = bool

    id: str
    text: str


# ==========================================
# ЧАТЫ С ПОКУПАТЕЛЯМИ
# ==========================================
class GetChats(WBMethod[WBChatResponse[List[ChatItem]]]):
    """Получение списка всех чатов с продавцом."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/seller/chats"
    __domain__: ClassVar[WBDomain] = WBDomain.BUYER_CHAT
    __returning__: ClassVar[type] = WBChatResponse[List[ChatItem]]


class GetChatEvents(WBMethod[WBChatResponse[ChatEventsResult]]):
    """Получение списка сообщений (событий) из всех чатов."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/seller/events"
    __domain__: ClassVar[WBDomain] = WBDomain.BUYER_CHAT
    __returning__: ClassVar[type] = WBChatResponse[ChatEventsResult]

    next: Optional[int] = None


class SendChatMessage(WBMethod[WBChatResponse[Any]]):
    """Отправка сообщения в чат покупателю (формат multipart/form-data)."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v1/seller/message"
    __domain__: ClassVar[WBDomain] = WBDomain.BUYER_CHAT
    __returning__: ClassVar[type] = WBChatResponse[Any]
    __is_multipart__: ClassVar[bool] = True  # Флаг для aiohttp/httpx сессии

    reply_sign: str = Field(alias="replySign")
    message: str


class DownloadChatFile(WBMethod[bytes]):
    """Скачивание файла (картинки, pdf) из чата по ID."""

    __http_method__: ClassVar[str] = "GET"
    __domain__: ClassVar[WBDomain] = WBDomain.BUYER_CHAT
    __returning__: ClassVar[type] = bytes  # Ожидаем сырые байты файла

    file_id: str = Field(exclude=True)

    @property
    def __api_path__(self) -> str:
        return f"/api/v1/seller/download/{self.file_id}"


# ==========================================
# ЗАЯВКИ НА ВОЗВРАТ
# ==========================================
class GetClaims(WBMethod[GetClaimsResponse]):
    """Получение заявок покупателей на возврат товара (брак)."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/claims"
    __domain__: ClassVar[WBDomain] = WBDomain.RETURNS
    __returning__: ClassVar[type] = GetClaimsResponse

    is_archive: bool
    limit: int = 50
    offset: int = 0
    id: Optional[str] = None
    nm_id: Optional[int] = None


class AnswerClaim(WBMethod[bool]):
    """Ответ (одобрение/отказ) на заявку о возврате."""

    __http_method__: ClassVar[str] = "PATCH"
    __api_path__: ClassVar[str] = "/api/v1/claim"
    __domain__: ClassVar[WBDomain] = WBDomain.RETURNS
    __returning__: ClassVar[type] = bool

    id: str
    action: str
    comment: Optional[str] = None
