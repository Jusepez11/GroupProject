from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import reviews as controller
from ..schemas import reviews as schema

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=schema.ReviewRead)
def create_review(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.ReviewRead])
def get_all_reviews(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{rating}", response_model=list[schema.ReviewReadByRating])
def get_review_by_rating(rating:int, db: Session = Depends(get_db)):
    return controller.read_all_rating(db, rating=rating)

@router.get("/{id}", response_model=schema.ReviewRead)
def read_one(id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, id=id)

@router.put("/{id}", response_model=schema.ReviewUpdate)
def update(id: int, request: schema.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, id=id)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, id=id)
