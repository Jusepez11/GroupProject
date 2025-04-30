from sqlalchemy.orm import Session
from ..models import menu as menu_model
from ..schemas import menu as menu_schema

def get_menu_item(db: Session, menu_id: int):
    return db.query(menu_model.Menu).filter(menu_model.Menu.menuID == menu_id).first()


def update_menu_item(db: Session, menu_id: int, menu_data: menu_schema.MenuUpdate):
    menu_item = db.query(menu_model.Menu).filter(menu_model.Menu.menuID == menu_id).first()
    if not menu_item:
        return None

    # Update the menu item's fields
    for key, value in menu_data.model_dump(exclude_unset=True).items():
        setattr(menu_item, key, value)

    db.commit()
    db.refresh(menu_item)
    return menu_item
