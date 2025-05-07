from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as model
from sqlalchemy.exc import SQLAlchemyError
from . import resources as resources_controller
from ..models.resources import Resource
from . import recipes as recipes_controller
from ..models.recipes import Recipe
from . import menu_items as menu_items_controller
from ..models.menu_items import MenuItems

def create(db: Session, request):
    menu_item = db.query(MenuItems).filter(MenuItems.item_ID == request.menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Recipe not found")

    for recipe in menu_item.recipes:
        resource = recipe.resource  

        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")

        required_amount = recipe.amount * request.amount
        if resource.amount < required_amount:
            raise HTTPException(status_code=400, detail=f"Not enough {resource.item} in stock")

        resource.amount -= required_amount


    new_item = model.OrderDetail(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        amount=request.amount
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
