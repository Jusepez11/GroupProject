from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from .menu_items import MenuItems

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.item_ID"), nullable=False)
    content = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)


    menu_item = relationship(MenuItems, back_populates="reviews")