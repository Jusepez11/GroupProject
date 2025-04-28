from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class ServiceRepresentative(Base):
    __tablename__ = "service_representative"

    employeeID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    # If you have relations, add them here. Based on the UML, Service Rep interacts with orders and payments
    # For example, assuming you have an "Order" and "Payment" model, you can link them:
    # orders = relationship("Order", back_populates="service_rep")
    # payments = relationship("Payment", back_populates="service_rep")
