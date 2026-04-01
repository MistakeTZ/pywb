from typing import Any, Dict, Optional

from ..exceptions import (
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PayloadTooLargeError,
    PaymentRequiredError,
    TooManyRequestsError,
    UnauthorizedError,
    UnprocessableEntityError,
    AccessDeniedError,
    WBApiError,
)


_EXCEPTION_MAPPING = {
    400: BadRequestError,
    401: UnauthorizedError,
    402: PaymentRequiredError,
    403: AccessDeniedError,
    404: NotFoundError,
    409: ConflictError,
    413: PayloadTooLargeError,
    422: UnprocessableEntityError,
    429: TooManyRequestsError,
}


def raise_for_status(
    status_code: int,
    response_json: Optional[Dict[str, Any]] = None,
):
    """
    Helper function to raise the appropriate exception based on the status code.
    If the status code is 200 or 204, it does nothing.
    """
    if status_code in (200, 204):
        return

    if 500 <= status_code < 600:
        raise InternalServerError(status_code, response_json)

    exception_class = _EXCEPTION_MAPPING.get(status_code, WBApiError)
    raise exception_class(status_code, response_json)
