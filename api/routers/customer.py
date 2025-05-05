from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.customer import CustomerCreate,CustomerUpdate,CustomerRead
from api.controllers import customer as controller
from api.dependencies.database import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerRead)
def create_customer(request: CustomerCreate, db: Session = Depends(get_db)):
    return controller.create_customer(db, request)

@router.get("/", response_model=list[CustomerRead])
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all_customers(db)

@router.get("/{customer_id}", response_model=CustomerRead)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_customer(db, customer_id)

@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: int, request: CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update_customer(db, customer_id, request)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete_customer(db, customer_id)