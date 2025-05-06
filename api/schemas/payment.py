from pydantic import BaseModel
from typing import Optional, List
from .promotion import PromotionRead


class PaymentBase(BaseModel):
    amount: Optional[float] = 0.0
    card_info:str
    approved: Optional[bool] = False
    order_id: int
    customer_id: int
    promo_code: Optional[str] = None

class PaymentCreate(BaseModel):
    approved: Optional[bool] = False
    order_id: int
    card_info:str
    customer_id: int
    promo_code: Optional[str] = None


class PaymentUpdate(BaseModel):
    approved: Optional[bool] = False
    order_id: Optional[int] = None
    card_info:Optional[str] = None
    customer_id: Optional[int] = None
    promo_code: Optional[str] = None

class PaymentRead(PaymentBase):
    id: int

    model_config = {
        "from_attributes": True
    }
