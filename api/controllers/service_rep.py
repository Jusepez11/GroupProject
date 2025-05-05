from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models import service_rep
from ..schemas.service_rep import (
    ServiceRepresentativeCreate,
    ServiceRepresentativeUpdate,
)

def create(db: Session, request: ServiceRepresentativeCreate):
    new_rep = service_rep.ServiceRepresentative(name=request.name)
    try:
        db.add(new_rep)
        db.commit()
        db.refresh(new_rep)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.__dict__['orig'])
        )
    return new_rep

def read_all(db: Session):
    try:
        return db.query(service_rep.ServiceRepresentative).all()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.__dict__['orig'])
        )

def read_one(db: Session, employeeID: int):
    rep = db.query(service_rep.ServiceRepresentative).filter_by(employeeID=employeeID).first()
    if not rep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service rep not found")
    return rep

def update(db: Session, employeeID: int, request: ServiceRepresentativeUpdate):
    rep = db.query(service_rep.ServiceRepresentative).filter_by(employeeID=employeeID)
    if not rep.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service rep not found")
    rep.update(request.dict(exclude_unset=True))
    db.commit()
    return rep.first()

def delete(db: Session, employeeID: int):
    rep = db.query(service_rep.ServiceRepresentative).filter_by(employeeID=employeeID)
    if not rep.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service rep not found")
    rep.delete()
    db.commit()
    return {"detail": "Deleted successfully"}