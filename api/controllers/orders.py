from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from sqlalchemy import func

from ..models.orders import Orders


def create(db: Session, request):
    if not request.customer_id:
        request.customer_id = None

    new_item = model.Orders(
        total_amount=request.total_amount,
        order_type=request.order_type,
        order_status=request.order_status,
        customer_id=request.customer_id,
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Orders).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Orders).filter(model.Orders.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Orders).filter(model.Orders.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Orders).filter(model.Orders.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_revenue_by_date(db: Session, target_date: date):
    revenue = db.query(func.sum(Orders.total_amount)).filter(func.date(Orders.order_date) == target_date).all() or 0.0
    return {"date:" : target_date, "revenue:" : revenue}

def get_orders_within_date_range(db: Session, start_date: date, end_date: date):
    return db.query(Orders).filter(
        func.date(Orders.order_date) >= start_date,
        func.date(Orders.order_date) <= end_date,
    ).all()