from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    ts: str = Field(alias="TS")
    status: str = Field(alias="Status")
