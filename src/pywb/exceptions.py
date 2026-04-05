from typing import Optional, Dict, Any


class WBApiError(Exception):
    """
    Base exception for all Wildberries API errors.
    Automatically parses the WB error JSON schema to provide clear error messages.
    """

    def __init__(self, status_code: int, payload: Optional[Dict[str, Any]] = None):
        self.status_code = status_code
        self.payload = payload or {}

        self.title = self.payload.get("title", "Unknown API Error")
        self.detail = self.payload.get("detail", "")
        self.timestamp = self.payload.get("timestamp", "")
        self.status_text = self.payload.get("statusText", "")

        message = f"[{self.status_code}] {self.title}"
        if self.detail:
            message += f" | Detail: {self.detail}"

        super().__init__(message)


class ClientDecodeError(Exception):
    """Ошибка при парсинге или валидации ответа от серверов WB"""

    def __init__(self, message: str, original: Exception, data: Any):
        super().__init__(message)
        self.original = original
        self.data = data


class BadRequestError(WBApiError):
    """400: Bad request. Check the request syntax."""

    pass


class UnauthorizedError(WBApiError):
    """401: Unauthorized. Token is missing, expired, or incorrect."""

    pass


class PaymentRequiredError(WBApiError):
    """402: Payment required. Insufficient funds on the Catalog balance."""

    pass


class AccessDeniedError(WBApiError):
    """403: Access denied. Deleted user, blocked access, or missing Jam subscription."""

    pass


class NotFoundError(WBApiError):
    """404: Not found. Check the request URL."""

    pass


class ConflictError(WBApiError):
    """409: Status update error / Error adding label. Data contradicts limits."""

    pass


class PayloadTooLargeError(WBApiError):
    """413: The request body size exceeds the given limit."""

    pass


class UnprocessableEntityError(WBApiError):
    """422: Error processing request parameters or unexpected result."""

    pass


class TooManyRequestsError(WBApiError):
    """429: Too many requests. Rate limit exceeded."""

    pass


class InternalServerError(WBApiError):
    """5XX: Internal service error. Service is unavailable."""

    pass
