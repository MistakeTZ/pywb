from pydantic import BaseModel
from typing import TypeVar, Generic, ClassVar

WT = TypeVar("WT")


class WBMethod(BaseModel, Generic[WT]):
    """Базовый класс для всех методов API"""

    __http_method__: ClassVar[str]
    __api_path__: ClassVar[str]
    __returning__: ClassVar[type]

    model_config = {"extra": "forbid"}
