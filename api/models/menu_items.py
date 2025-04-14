from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class menu_items(Base):
    __tablename__ = "menu_items"
    item_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), unique=True, nullable=False)
    item_description = Column(String(300), nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)
    item_category = Column(String(100), nullable=False)
    item_ingredients = Column(String(300), nullable=False)
    
    getDetails = relationship("OrderDetail", back_populates="menu_items")