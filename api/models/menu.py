from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Menu(Base):
    __tablename__ = "menu"

    menuID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    item = Column(String(100), unique=True, nullable=False)
    manager_id = Column(Integer, ForeignKey("manager.id"))

    menu_items = relationship("MenuItem", back_populates="menu")
    promotions = relationship("Promotion", back_populates="menu_item")