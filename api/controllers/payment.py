from fastapi import HTTPException, status
from httpx import request
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate, PaymentUpdate
from fastapi.responses import Response
from . import orders as orders_controller
from ..models.orders import Orders
from ..models.order_details import OrderDetail
from ..models.menu_items import MenuItems
from ..models.promotion import Promotion
from datetime import datetime

def create(db: Session, request: PaymentCreate):
    # Get the order
    order = db.query(Orders).filter(Orders.id == request.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Calculate subtotal from order_details
    total = 0.0
    for detail in order.order_details:
        if detail.menu_item:
            total += detail.amount * float(detail.menu_item.item_price)

    # Apply discount if promo code is valid
    if request.promo_code:
        promo = db.query(Promotion).filter(Promotion.promoCode == request.promo_code).first()
        if not promo or promo.expiration_date < datetime.utcnow():
            raise HTTPException(status_code=400, detail="Invalid or expired promo code")
        total = total * (float(100 - promo.discount_percent)/100)

    # Create payment
    new_payment = Payment(
        amount=total,
        approved=request.approved,
        order_id=request.order_id,
        card_info=request.card_info,
        customer_id=request.customer_id,
        promo_code=request.promo_code
    )

    order.total_amount = total

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
        orders_controller.update_order_total(db, request.order_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return payment.first()


def delete(db: Session, payment_id: int):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id)
        payment_detail = payment.first()
        if not payment.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

        payment_id = payment_detail.order_id
        payment.delete(synchronize_session=False)
        db.commit()
        orders_controller.update_order_total(db, payment_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return Response(status_code=status.HTTP_204_NO_CONTENT)