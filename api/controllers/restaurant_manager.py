from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.restaurant_manager import RestaurantManager
from ..schemas.restaurant_manager import RestaurantManagerCreate, RestaurantManagerUpdate
from fastapi.responses import Response

def create(db: Session, request: RestaurantManagerCreate):
    manager = RestaurantManager(name=request.name)
    try:
        db.add(manager)
        db.commit()
        db.refresh(manager)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return manager

def read_all(db: Session):
    try:
        return db.query(RestaurantManager).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))

def read_one(db: Session, manager_id: int):
    try:
        manager = db.query(RestaurantManager).filter(RestaurantManager.id == manager_id).first()
        if not manager:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return manager

def update(db: Session, manager_id: int, request: RestaurantManagerUpdate):
    try:
        manager = db.query(RestaurantManager).filter(RestaurantManager.id == manager_id)
        if not manager.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found")
        manager.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return manager.first()

def delete(db: Session, manager_id: int):
    try:
        manager = db.query(RestaurantManager).filter(RestaurantManager.id == manager_id)
        if not manager.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Manager not found")
        manager.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)