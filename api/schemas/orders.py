from .order_details import OrderDetail

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# Shared schema
class OrderBase(BaseModel):
    total_amount: float
    order_status: Optional[str] = 'Pending'
    order_type: Optional[str] = 'Takeout'

# For creating a new order
class OrderCreate(OrderBase):
    pass

# For updating an order
class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None


# For reading/returning an order (e.g. in a GET request)
class OrderRead(OrderBase):
    id: int
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True

'''
# ---- NEW CLASSES ADDED FROM averyBranch ----
class GuestOrderItem(BaseModel):
    sandwich_id: int
    amount: int

class GuestOrder(BaseModel):    # <-- FIX here, was wrong before
    name: str
    email: str
    address: str
    items: list[GuestOrderItem]
'''