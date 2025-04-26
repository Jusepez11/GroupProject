from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    total_amount = Column(float, nullable=False)
    order_status = Column(String, default='Pending')
    order_time = Column(DATETIME, default=datetime)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='orders')

    service_rep_id = Column(Integer, ForeignKey('service_representatives.id'))
    service_representative = relationship('ServiceRepresentative', back_populates='orders')

    payment = relationship('Payment', back_populates='order', uselist=False)
    #items = relationship('MenuItem', secondary=order_menuitem, back_populates='orders')
    #foo