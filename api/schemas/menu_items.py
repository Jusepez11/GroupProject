from pydantic import BaseModel
from typing import Optional


class MenuItemBase(BaseModel):
    item_ID: int
    item_name: str
    item_description: str
    item_price: float
    item_category: str
    item_ingredients: str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str]
    item_description: Optional[str]
    item_price: Optional[float]
    item_category: Optional[str]
    item_ingredients: Optional[str]


class MenuItemRead(MenuItemBase):
    item_ID: int

    class Config:
        orm_mode = True
