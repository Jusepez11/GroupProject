from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promoCode: str
    description: str
    discount_percent: float

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promoCode: Optional[str] = None
    description: Optional[str] = None
    discount_percent: Optional[float] = None


class PromotionRead(PromotionBase):
    promoCode: str

    model_config = {
        "from_attributes": True
    }
