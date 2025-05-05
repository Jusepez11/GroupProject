from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .orders import OrderRead 


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    email: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None


class CustomerRead(CustomerBase):
    id: int

    model_config = {
        "from_attributes": True
    }
