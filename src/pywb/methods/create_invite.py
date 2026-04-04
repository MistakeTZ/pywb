from typing import ClassVar, Optional, List
from ..methods.base import WBMethod


from ..enums import WBDomain
from ..types import (
    CreateInviteResponse,
    InviteInfo,
    AccessItem,
)


class CreateInvite(WBMethod[CreateInviteResponse]):
    """Создание приглашения для нового пользователя."""

    __http_method__: ClassVar[str] = "POST"
    __api_path__: ClassVar[str] = "/api/v1/invite"
    __domain__: ClassVar[WBDomain] = WBDomain.USER_MANAGEMENT
    __returning__: ClassVar[type] = CreateInviteResponse

    invite: InviteInfo
    access: Optional[List[AccessItem]] = None
