from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payment as controller
from ..schemas import payment as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payment'],
    prefix="/payments"
)

@router.post("/", response_model=schema.PaymentRead)
def create_payment(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.PaymentRead])
def get_all_payments(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.PaymentRead)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id)

@router.put("/{payment_id}", response_model=schema.PaymentRead)
def update_payment(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
    return controller.update(db, payment_id, request)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id)