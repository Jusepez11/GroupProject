from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate, PaymentUpdate
from fastapi.responses import Response

def create(db: Session, request: PaymentCreate):
    new_payment = Payment(
        amount=request.amount,
        approved=request.approved
    )
    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_payment


def read_all(db: Session):
    try:
        return db.query(Payment).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))


def read_one(db: Session, payment_id: int):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return payment


def update(db: Session, payment_id: int, request: PaymentUpdate):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        payment.update(request.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return payment.first()


def delete(db: Session, payment_id: int):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id)
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        payment.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)