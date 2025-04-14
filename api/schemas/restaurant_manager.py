from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class RestaurantManagerBase(BaseModel):
    name: str
    id : int

class RestaurantManagerCreate(RestaurantManagerBase):
    pass

class RestaurantManager(RestaurantManagerBase):
    id: int

    class ConfigDict:
        from_attributes = True
