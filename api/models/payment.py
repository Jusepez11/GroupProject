from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    approved = Column(Boolean, default=False)

    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Order', back_populates='payment')
