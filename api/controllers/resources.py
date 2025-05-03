from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.resources import Resource
from ..schemas.resources import ResourceCreate, ResourceUpdate
from fastapi.responses import Response

def create(db: Session, request: ResourceCreate):
    new_resource = Resource(item=request.item, amount=request.amount)
    try:
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return new_resource

def read_all(db: Session):
    try:
        return db.query(Resource).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))

def read_one(db: Session, resource_id: int):
    try:
        resource = db.query(Resource).filter(Resource.id == resource_id).first()
        if not resource:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return resource

def update(db: Session, resource_id: int, request: ResourceUpdate):
    try:
        resource = db.query(Resource).filter(Resource.id == resource_id)
        if not resource.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
        resource.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return resource.first()

def delete(db: Session, resource_id: int):
    try:
        resource = db.query(Resource).filter(Resource.id == resource_id)
        if not resource.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
        resource.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)