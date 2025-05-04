from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import SandwichRead

class MenuBase(BaseModel):
    name: str
    price: int

class MenuCreate(MenuBase):
    manager_ID : int

class Menu(MenuBase):
    id: int
    sandwiches: list[SandwichRead]

    class ConfigDict:
        from_attributes = True