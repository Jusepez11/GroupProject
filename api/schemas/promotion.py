from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promoCode: str
    description: str
    discount_percent: float
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promoCode: Optional[str] = None
    description: Optional[str] = None
    discount_percent: Optional[float] = None
    expiration_date: Optional[datetime] = None


class PromotionRead(PromotionBase):
    promoCode: str

    model_config = {
        "from_attributes": True
    }
