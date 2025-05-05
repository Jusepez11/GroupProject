from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    content = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)