from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promoCode: str
    description: str
    discount_percent: float

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    pass

    class ConfigDict:
        from_attributes = True