from .order_details import OrderDetail

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Shared schema
class OrderBase(BaseModel):
    total_amount: float
    order_status: Optional[str] = 'Pending'


# For creating a new order
class OrderCreate(OrderBase):
    pass


# For reading/returning an order (e.g. in a GET request)
class OrderRead(OrderBase):
    id: int

    class Config:
        orm_mode = True


# For updating an order
class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    order_status: Optional[str] = None

    class Config:
        orm_mode = True


# ---- NEW CLASSES ADDED FROM averyBranch ----
class GuestOrderItem(BaseModel):
    sandwich_id: int
    amount: int

class GuestOrder(BaseModel):    # <-- FIX here, was wrong before
    name: str
    email: str
    address: str
    items: list[GuestOrderItem]
