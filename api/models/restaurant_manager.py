from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class RestaurantManager(Base):
    __tablename__ = "restaurant_manager"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    menu_items = relationship("MenuItem", back_populates="restaurant_manager")

