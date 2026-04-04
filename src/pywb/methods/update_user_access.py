from typing import ClassVar, List
from pydantic import Field
from ..methods.base import WBMethod


from ..enums import WBDomain
from ..types import UserAccessUpdate


class UpdateUserAccess(WBMethod[bool]):
    """Обновление прав доступа пользователя."""

    __http_method__: ClassVar[str] = "PUT"
    __api_path__: ClassVar[str] = "/api/v1/users/access"
    __domain__: ClassVar[WBDomain] = WBDomain.USER_MANAGEMENT
    __returning__: ClassVar[type] = bool

    users_accesses: List[UserAccessUpdate] = Field(alias="usersAccesses")
