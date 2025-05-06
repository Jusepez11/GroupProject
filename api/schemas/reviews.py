from pydantic import BaseModel, conint, ConfigDict
from typing import Optional, Annotated

class ReviewBase(BaseModel):
    customer_id:int
    menu_items_id:int
    content: str
    rating: Annotated[int, conint(ge=1, le=5)]  # Only allow ratings between 1 and 5

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    customer_id:Optional[int] = None
    menu_items_id:Optional[int] = None
    content: Optional[str] = None
    rating: Optional[Annotated[int, conint(ge=1, le=5)]] = None

class ReviewRead(ReviewBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class ReviewReadByRating(ReviewBase):
    id: int

    model_config = ConfigDict(from_attributes=True)