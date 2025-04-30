from .order_details import OrderDetail

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Shared schema
class OrderBase(BaseModel):
    id: int
    total_amount: float
    order_status: Optional[str] = 'Pending'
    order_time: Optional[datetime] = None
    customer_id: int
    service_rep_id: int

# For creating a new order

class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    order_status: Optional[str] = None
    order_time: Optional[datetime] = None
    customer_id: Optional[int] = None
    service_rep_id: Optional[int] = None


    class Config:
        orm_mode = True


# ---- NEW CLASSES ADDED FROM averyBranch ----
class GuestOrderItem(BaseModel):
    sandwich_id: int
    amount: int

class GuestOrder(BaseModel):    # <-- FIX here, was wrong before
    name: str
    email: str
    items: list[GuestOrderItem]
