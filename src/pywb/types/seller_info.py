from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


# --- Seller Information ---
class SellerInfoResponse(BaseModel):
    name: Optional[str] = None
    sid: Optional[str] = None
    tin: Optional[str] = None
    trade_mark: Optional[str] = Field(None, alias="tradeMark")


class SupplierRatingModel(BaseModel):
    feedback_count: int = Field(alias="feedbackCount")
    valuation: float


class SubscriptionsJamInfo(BaseModel):
    state: str
    activation_source: str = Field(alias="activationSource")
    level: str
    since: datetime
    till: datetime
