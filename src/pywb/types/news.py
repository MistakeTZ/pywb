from datetime import datetime
from typing import List
from pydantic import BaseModel


class NewsTag(BaseModel):
    id: int
    name: str


class NewsItem(BaseModel):
    content: str
    date: datetime
    header: str
    id: int
    types: List[NewsTag]


class GetNewsResponse(BaseModel):
    data: List[NewsItem]
