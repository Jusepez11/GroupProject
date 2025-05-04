from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas import sandwiches as schema
from ..controllers import sandwich as controller

router = APIRouter(
    prefix="/sandwiches",
    tags=["Sandwiches"]
)

@router.post("/", response_model=schema.SandwichRead)
def create_sandwich(request: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.SandwichRead])
def get_all_sandwiches(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{sandwich_id}", response_model=schema.SandwichRead)
def get_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, sandwich_id)

@router.put("/{sandwich_id}", response_model=schema.SandwichRead)
def update_sandwich(sandwich_id: int, request: schema.SandwichUpdate, db: Session = Depends(get_db)):
    return controller.update(db, sandwich_id, request)

@router.delete("/{sandwich_id}")
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, sandwich_id)