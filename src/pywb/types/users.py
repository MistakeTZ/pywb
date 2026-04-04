from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class AccessItem(BaseModel):
    code: str
    disabled: bool


class InviteeInfo(BaseModel):
    phone_number: str = Field(alias="phoneNumber")
    position: str
    invite_uuid: str = Field(alias="inviteUuid")
    expired_at: datetime = Field(alias="expiredAt")
    is_active: bool = Field(alias="isActive")


class UserItem(BaseModel):
    id: int
    role: str
    position: str
    phone: str
    email: str
    is_owner: bool = Field(alias="isOwner")
    first_name: str = Field(alias="firstName")
    second_name: str = Field(alias="secondName")
    patronymic: str
    goods_return: bool = Field(alias="goodsReturn")
    is_invitee: bool = Field(alias="isInvitee")
    invitee_info: Optional[InviteeInfo] = Field(None, alias="inviteeInfo")
    access: List[AccessItem]


class GetUsersResponse(BaseModel):
    total: int
    count_in_response: int = Field(alias="countInResponse")
    users: List[UserItem]


class InviteInfo(BaseModel):
    phone_number: str = Field(alias="phoneNumber")
    position: Optional[str] = None


class CreateInviteResponse(BaseModel):
    invite_id: str = Field(alias="inviteID")
    expired_at: datetime = Field(alias="expiredAt")
    is_success: bool = Field(alias="isSuccess")
    invite_url: str = Field(alias="inviteUrl")


class UserAccessUpdate(BaseModel):
    user_id: int = Field(alias="userId")
    access: List[AccessItem]
