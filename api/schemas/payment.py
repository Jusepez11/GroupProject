from pydantic import BaseModel
from typing import Optional


class PaymentBase(BaseModel):
    amount: float
    approved: Optional[bool] = False
    order_id: int
    customer_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    approved: Optional[bool] = None
    order_id: Optional[int] = None
    customer_id: Optional[int] = None


class PaymentRead(PaymentBase):
    id: int

    model_config = {
        "from_attributes": True
    }
