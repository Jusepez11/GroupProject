from .order_details import OrderDetail
from .customer import CustomerRead
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from ..models.payment import Payment


# Shared schema
class OrderBase(BaseModel):
    total_amount: float
    order_status: Optional[str] = 'Pending'
    order_type: Optional[str] = 'Takeout'

# For creating a new order
class OrderCreate(OrderBase):
    customer_id: Optional[int] = None

# For updating an order
class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None


# For reading/returning an order (e.g. in a GET request)
class OrderRead(OrderBase):
    id: int
    order_details: list[OrderDetail] = None
    customer: Optional[CustomerRead] = None

class RevenueReportResponse(BaseModel):
    date: datetime
    total_revenue: float

class OrdersInDateRangeResponse(BaseModel):
    id: int
    total_amount: float
    order_status: str
    order_type: str
    order_date: datetime

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