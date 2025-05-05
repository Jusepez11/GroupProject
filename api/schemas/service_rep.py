from datetime import datetime
from typing import Optional
from pydantic import BaseModel
#from .sandwiches import S

# Base schema with shared attributes
class ServiceRepresentativeBase(BaseModel):
    name: str

# Schema for creating a new service rep
class ServiceRepresentativeCreate(ServiceRepresentativeBase):
    pass


# Schema for creating a new service rep
class ServiceRepresentativeUpdate(BaseModel):
    name: Optional[str] = None

# Schema for reading data, with config for ORM mode
class ServiceRepresentativeRead(ServiceRepresentativeBase):
    employeeID: int

    class ConfigDict:
        from_attributes = True
