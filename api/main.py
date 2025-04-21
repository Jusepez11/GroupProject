import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf
from .models.menu_items import menu_items
from .schemas.menu_items import MenuItemRead
from sqlalchemy.orm import Session
from .dependencies.database import get_db

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


# Daniel

# Get Menu
@app.get("/menu", response_model=list[MenuItemRead])
def get_menu(db: Session = Depends(get_db)):
    menu = db.query(menu_items).all()
    if not menu:
        raise HTTPException(status_code=404, detail="No menu items found.")
    return menu

# View General Information
@app.get("/info")
def view_general_information():
    return {
        "restaurant_name": "Nova",
        "hours": {            
            "monday-friday": "11:00 AM - 9:00 PM",
            "saturday": "12:00 PM - 10:00 PM",
            "sunday": "Closed",
        },
        "location": "123 Nova St, Charlotte, NC 28202",
        "Contact Information": "Phone: (704)-123-4567 | Email: info@nova.com"
    }
    
    
    
if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)