from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import reviews as controller
from ..schemas import reviews as schema

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=schema.ReviewRead)
def create_review(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create_review(db, request)

@router.get("/", response_model=list[schema.ReviewRead])
def get_all_reviews(db: Session = Depends(get_db)):
    return controller.read_all_reviews(db)