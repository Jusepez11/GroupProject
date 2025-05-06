from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from sqlalchemy import Float

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_status = Column(String(26), default='Pending')
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    order_type = Column(String(26), default='Takeout')

    order_details = relationship("OrderDetail", back_populates="order")
    payment = relationship("Payment", back_populates="order")