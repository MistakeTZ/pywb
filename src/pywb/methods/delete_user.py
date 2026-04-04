from typing import ClassVar
from pydantic import Field
from ..methods.base import WBMethod


from ..enums import WBDomain


class DeleteUser(WBMethod[bool]):
    """Удаление пользователя из кабинета продавца."""

    __http_method__: ClassVar[str] = "DELETE"
    __api_path__: ClassVar[str] = "/api/v1/user"
    __domain__: ClassVar[WBDomain] = WBDomain.USER_MANAGEMENT
    __returning__: ClassVar[type] = bool

    deleted_user_id: int = Field(alias="deletedUserID")
