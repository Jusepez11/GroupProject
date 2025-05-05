from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RestaurantManagerBase(BaseModel):
    name: str

class RestaurantManagerCreate(RestaurantManagerBase):
    pass

class RestaurantManagerUpdate(BaseModel):
    name: Optional[str] = None

class RestaurantManagerRead(RestaurantManagerBase):
    id: int

    class ConfigDict:
        from_attributes = True
