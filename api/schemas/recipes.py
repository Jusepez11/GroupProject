from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class RecipeBase(BaseModel):
    menu_item_id:int
    resource_id: int
    amount: int


class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    menu_item_id:Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class RecipeRead(RecipeBase):
    id: int
    menu_item_id: Optional[int] = None

    class ConfigDict:
        from_attributes = True