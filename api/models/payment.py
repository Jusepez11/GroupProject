from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float)
    approved = Column(Boolean, default=False)
    card_info = Column(String(100))
    order_id = Column(Integer, ForeignKey('orders.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    promo_code = Column(String(100), ForeignKey('promotion.promoCode'), nullable=True)

    order = relationship('Orders', back_populates='payment')
    customer = relationship('Customer', back_populates='payment')
    promotion = relationship('Promotion', back_populates='payment')