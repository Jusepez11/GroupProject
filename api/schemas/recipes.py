from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import SandwichRead


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    #sandwich_id: Optional[int] = None
    #resource_id: Optional[int] = None
    amount: Optional[int] = None

class RecipeRead(RecipeBase):
    id: int

    class ConfigDict:
        from_attributes = True