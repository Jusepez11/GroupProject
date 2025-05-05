from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from sqlalchemy import Float

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    total_amount = Column(Float, nullable=False)
    order_status = Column(String(26), default='Pending')
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    order_type = Column(String(26), default='Takeout')

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    customer = relationship('Customer', backref='orders', lazy='joined')

    order_details = relationship("OrderDetail", back_populates="order")
