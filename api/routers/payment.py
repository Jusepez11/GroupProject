from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas.payment import PaymentCreate, PaymentUpdate, PaymentRead
from ..controllers import payment

router = APIRouter()

@router.post("/payments", response_model=PaymentRead)
def create_payment(request: PaymentCreate, db: Session = Depends(get_db)):
    return payment.create(db, request)

@router.get("/payments", response_model=list[PaymentRead])
def get_all_payments(db: Session = Depends(get_db)):
    return payment.read_all(db)

@router.get("/payments/{payment_id}", response_model=PaymentRead)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.read_one(db, payment_id)

@router.put("/payments/{payment_id}", response_model=PaymentRead)
def update_payment(payment_id: int, request: PaymentUpdate, db: Session = Depends(get_db)):
    return payment.update(db, payment_id, request)

@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.delete(db, payment_id)