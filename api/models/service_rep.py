from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class ServiceRepresentative(Base):
    __tablename__ = "service_representative"

    employeeID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    orders = relationship('Orders', back_populates='service_representative')
    
