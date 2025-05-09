from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .order_details import OrderDetail



class MenuItems(Base):
    __tablename__ = "menu_items"
    item_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=False)
    item_description = Column(String(300), nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)
    item_category = Column(String(100), nullable=False)
    
    order_details = relationship(OrderDetail, back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item")
    recipes = relationship("Recipe", back_populates="menu_item")