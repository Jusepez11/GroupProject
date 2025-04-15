from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

# Base schema with shared attributes
class ServiceRepresentativeBase(BaseModel):
    employeeID: int
    name: str

# Schema for creating a new service rep
class ServiceRepresentativeCreate(ServiceRepresentativeBase):
    pass

# Schema for reading data, with config for ORM mode
class ServiceRepresentative(ServiceRepresentativeBase):
    employeeID: int

    class ConfigDict:
        from_attributes = True
