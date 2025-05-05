from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotion"

    promoCode = Column(String(100), primary_key=True, index=True)
    description = Column(String(355), nullable=False)
    discount_percent = Column(DECIMAL, nullable=False)
