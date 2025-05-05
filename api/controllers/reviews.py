from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import reviews as model
from ..schemas import reviews as schema

def create_review(db: Session, request: schema.ReviewCreate):
    new_review = model.Review(
        customer_id=request.customer_id,
        sandwich_id=request.sandwich_id,
        content=request.content,
        rating=request.rating,
    )

    try:
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return new_review

def read_all_reviews(db: Session):
    return db.query(model.Review).all()