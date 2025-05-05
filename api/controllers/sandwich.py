from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models import sandwiches as model
from ..schemas import sandwiches as schema

def create(db: Session, request: schema.SandwichCreate):
    new_sandwich = model.Sandwich(
        id=request.id,
        sandwich_name=request.sandwich_name,
        price=request.price
    )

    try:
        db.add(new_sandwich)
        db.commit()
        db.refresh(new_sandwich)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.orig))
    return new_sandwich

def read_all(db: Session):
    return db.query(model.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == sandwich_id).first()
    if not sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

def update(db: Session, sandwich_id: int, request: schema.SandwichUpdate):
    sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == sandwich_id)
    if not sandwich.first():
        raise HTTPException(status_code=404, detail="Sandwich not found")
    sandwich.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return sandwich.first()

def delete(db: Session, sandwich_id: int):
    sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == sandwich_id).first()
    if not sandwich:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db.delete(sandwich)
    db.commit()
    return {"detail": "Sandwich deleted"}