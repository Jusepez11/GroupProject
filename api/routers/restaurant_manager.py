from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..schemas.restaurant_manager import (
    RestaurantManagerCreate,
    RestaurantManagerUpdate,
    RestaurantManagerRead
)
from ..controllers import restaurant_manager

router = APIRouter()

@router.post("/restaurant_managers", response_model=RestaurantManagerRead)
def create_manager(request: RestaurantManagerCreate, db: Session = Depends(get_db)):
    return restaurant_manager.create(db, request)

@router.get("/restaurant_managers", response_model=list[RestaurantManagerRead])
def get_all_managers(db: Session = Depends(get_db)):
    return restaurant_manager.read_all(db)

@router.get("/restaurant_managers/{manager_id}", response_model=RestaurantManagerRead)
def get_manager(manager_id: int, db: Session = Depends(get_db)):
    return restaurant_manager.read_one(db, manager_id)

@router.put("/restaurant_managers/{manager_id}", response_model=RestaurantManagerRead)
def update_manager(manager_id: int, request: RestaurantManagerUpdate, db: Session = Depends(get_db)):
    return restaurant_manager.update(db, manager_id, request)

@router.delete("/restaurant_managers/{manager_id}")
def delete_manager(manager_id: int, db: Session = Depends(get_db)):
    return restaurant_manager.delete(db, manager_id)