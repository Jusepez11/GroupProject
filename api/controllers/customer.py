from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import customer as model
from ..schemas import customer as schema

def create_customer(db: Session, request: schema.CustomerCreate):
    new_customer = model.Customer(
        name=request.name,
        phone_number=request.phone_number,
        email=request.email,
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_customer

def read_all_customers(db: Session):
    return db.query(model.Customer).all()

def read_customer(db: Session, customer_id: int):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

def update_customer(db: Session, customer_id: int, request: schema.CustomerUpdate):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted successfully"}