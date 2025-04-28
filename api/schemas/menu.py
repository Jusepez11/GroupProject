from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class MenuBase(BaseModel):
    name: str
    price: int
    menu_id: int;

class MenuCreate(MenuBase):
    manager_ID : int

class Menu(MenuBase):
    id: int
    sandwiches: list[Sandwich]

    class ConfigDict:
        from_attributes = True