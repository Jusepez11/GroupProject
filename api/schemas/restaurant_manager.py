from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class RestaurantManagerBase(BaseModel):
    name: str

class RestaurantManagerCreate(RestaurantManagerBase):
    pass

class RestaurantManagerRead(RestaurantManagerBase):
    id: int

class RestaurantManagerUpdate(BaseModel):
    name: Optional[str] = None

    class ConfigDict:
        from_attributes = True
