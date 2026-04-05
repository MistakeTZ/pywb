from enum import Enum
from typing import Dict, TypedDict


class WBDomain(str, Enum):
    CONTENT = "content"
    ANALYTICS = "analytics"
    PRICES = "prices"
    MARKETPLACE = "marketplace"
    STATISTICS = "statistics"
    SUPPLIES = "supplies"
    FINANCE = "finance"
    DOCUMENTS = "documents"
    COMMON = "common"
    USER_MANAGEMENT = "user_management"
    PROMOTION = "promotion"
    PROMOTION_MEDIA = "promotion_media"
    CALENDAR = "calendar"
    FEEDBACKS = "feedbacks"
    BUYER_CHAT = "buyer_chat"
    RETURNS = "returns"


class DomainUrls(TypedDict):
    prod: str
    sandbox: str | None


WB_ROUTER: Dict[WBDomain, DomainUrls] = {
    WBDomain.CONTENT: {
        "prod": "https://content-api.wildberries.ru",
        "sandbox": "https://content-api-sandbox.wildberries.ru",
    },
    WBDomain.ANALYTICS: {
        "prod": "https://seller-analytics-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.PRICES: {
        "prod": "https://discounts-prices-api.wildberries.ru",
        "sandbox": "https://discounts-prices-api-sandbox.wildberries.ru",
    },
    WBDomain.MARKETPLACE: {
        "prod": "https://marketplace-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.STATISTICS: {
        "prod": "https://statistics-api.wildberries.ru",
        "sandbox": "https://statistics-api-sandbox.wildberries.ru",
    },
    WBDomain.PROMOTION: {
        "prod": "https://advert-api.wildberries.ru",
        "sandbox": "https://advert-api-sandbox.wildberries.ru",
    },
    WBDomain.PROMOTION_MEDIA: {
        "prod": "https://advert-media-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.CALENDAR: {
        "prod": "https://dp-calendar-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.FEEDBACKS: {
        "prod": "https://feedbacks-api.wildberries.ru",
        "sandbox": "https://feedbacks-api-sandbox.wildberries.ru",
    },
    WBDomain.BUYER_CHAT: {
        "prod": "https://buyer-chat-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.RETURNS: {"prod": "https://returns-api.wildberries.ru", "sandbox": None},
    WBDomain.SUPPLIES: {"prod": "https://supplies-api.wildberries.ru", "sandbox": None},
    WBDomain.FINANCE: {"prod": "https://finance-api.wildberries.ru", "sandbox": None},
    WBDomain.DOCUMENTS: {
        "prod": "https://documents-api.wildberries.ru",
        "sandbox": None,
    },
    WBDomain.COMMON: {"prod": "https://common-api.wildberries.ru", "sandbox": None},
    WBDomain.USER_MANAGEMENT: {
        "prod": "https://user-management-api.wildberries.ru",
        "sandbox": None,
    },
}
