from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(10), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    payment = relationship('Payment', back_populates='customer')
