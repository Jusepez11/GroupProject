from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import service_rep
from ..schemas.service_rep import (
    ServiceRepresentativeCreate,
    ServiceRepresentativeUpdate,
    ServiceRepresentativeRead,
)

router = APIRouter(prefix="/service_reps", tags=["Service Representatives"])

@router.post("/", response_model=ServiceRepresentativeRead)
def create_rep(request: ServiceRepresentativeCreate, db: Session = Depends(get_db)):
    return service_rep.create(db, request)

@router.get("/", response_model=list[ServiceRepresentativeRead])
def get_all_reps(db: Session = Depends(get_db)):
    return service_rep.read_all(db)

@router.get("/{employeeID}", response_model=ServiceRepresentativeRead)
def get_rep(employeeID: int, db: Session = Depends(get_db)):
    return service_rep.read_one(db, employeeID)

@router.put("/{employeeID}", response_model=ServiceRepresentativeRead)
def update_rep(employeeID: int, request: ServiceRepresentativeUpdate, db: Session = Depends(get_db)):
    return service_rep.update(db, employeeID, request)

@router.delete("/{employeeID}")
def delete_rep(employeeID: int, db: Session = Depends(get_db)):
    return service_rep.delete(db, employeeID)