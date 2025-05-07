from pydantic import BaseModel
from typing import Optional
from .recipes import RecipeRead


class MenuItemBase(BaseModel):
    item_name: str
    item_description: str
    item_price: float
    item_category: str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str]
    item_description: Optional[str]
    item_price: Optional[float]
    item_category: Optional[str]


class MenuItemRead(MenuItemBase):
    item_ID: int
    recipes: list[RecipeRead] = None

    class Config:
        orm_mode = True
