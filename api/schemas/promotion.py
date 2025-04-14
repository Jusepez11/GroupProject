from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class PromotionBase(BaseModel):
    name: str
    percentage: float

class PromotionCreate(PromotionBase):
    menu_id: int

class Promotion(PromotionBase):
    id: int
    menu_id: int

    class ConfigDict:
        from_attributes = True