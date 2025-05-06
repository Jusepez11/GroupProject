from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import date

from ..schemas.orders import OrdersInDateRangeResponse

router = APIRouter(
    tags=['Order'],
    prefix="/orders"
)


@router.post("/", response_model=schema.OrderRead)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderRead])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.OrderRead)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.OrderRead)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.get("/orders/date-range", response_model=list[OrdersInDateRangeResponse])
def orders_within_range(
        start_date: date,
        end_date: date,
        db: Session = Depends(get_db),
):
    return controller.get_orders_within_date_range(
        db, start_date=start_date, end_date=end_date,
    )
