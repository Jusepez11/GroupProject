from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotion as controller
from ..schemas import promotion as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)


@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promoCode}", response_model=schema.Promotion)
def read_one(promoCode: str, db: Session = Depends(get_db)):
    return controller.read_one(db, promoCode=promoCode)

@router.post("/", response_model=schema.Promotion)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.delete("/{promoCode}")
def delete(promoCode: str, db: Session = Depends(get_db)):
    return controller.delete(db=db, promoCode=promoCode)


@router.put("/{promoCode}", response_model=schema.Promotion)
def update(promoCode: int, request: schema.Promotion, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, promoCode=promoCode)