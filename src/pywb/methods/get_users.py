from typing import ClassVar
from pydantic import Field

from ..types.users import GetUsersResponse
from .base import WBMethod
from ..enums import WBDomain


class GetUsers(WBMethod[GetUsersResponse]):
    """Получение списка активных или приглашенных пользователей."""

    __http_method__: ClassVar[str] = "GET"
    __api_path__: ClassVar[str] = "/api/v1/users"
    __domain__: ClassVar[WBDomain] = WBDomain.USER_MANAGEMENT
    __returning__: ClassVar[type] = GetUsersResponse

    limit: int = 100
    offset: int = 0
    is_invite_only: bool = Field(False, alias="isInviteOnly")
