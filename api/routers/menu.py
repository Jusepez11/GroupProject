from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from .. import schemas, controllers

router = APIRouter(prefix="/menu", tags=["menu"])

@router.get("/{menu_id}", response_model=schemas.menu.Menu)
def read_menu(menu_id: int, db: Session = Depends(get_db)):
    menu_item = controllers.menu.get_menu_item(db, menu_id)
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return menu_item

@router.put("/{menu_id}", response_model=schemas.menu.Menu)
def update_menu(menu_id: int, menu: schemas.menu.MenuUpdate, db: Session = Depends(get_db)):
    updated_item = controllers.menu.update_menu_item(db, menu_id, menu)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return updated_item
