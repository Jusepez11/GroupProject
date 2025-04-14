from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotion"

    promoCode = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    discount_percent = Column(DECIMAL, nullable=False)
    menu_id = Column(Integer, ForeignKey("menu.id"))

    menu_item = relationship("Menu", back_populates="promotions")