from pydantic import BaseModel, conint
from typing import Optional

class ReviewBase(BaseModel):
    content: str
    rating: conint(ge=1, le=5)  # Only allow ratings between 1 and 5

class ReviewCreate(ReviewBase):
    customer_id: int
    sandwich_id: int

class ReviewRead(ReviewBase):
    id: int
    customer_id: int
    sandwich_id: int

    class Config:
        from_attributes = True