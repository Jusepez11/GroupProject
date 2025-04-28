import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf

from sqlalchemy.orm import Session
from .dependencies.database import get_db

# Import models
from .models.orders import Orders
from .models.sandwiches import Sandwich
from .models.order_details import OrderDetail
from .models.menu_items import menu_items

# Import schemas
from .schemas.orders import GuestOrder
from .schemas.menu_items import MenuItemRead

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

# ------------------- Your original routes -------------------

# View an Order by ID
@app.get("/orders/{order_id}", response_model=OrderRead)
def view_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# View Status of an Order
@app.get("/orders/{order_id}/status")
def view_order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"order_id": order.id, "order_status": order.order_status}

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

# ------------------- New Guest Order routes -------------------

# Ordering as a guest
@app.post("/guest/orders")
def create_guest_order(order_data: GuestOrder, db: Session = Depends(get_db)):
    # Step 1: Create a new order directly (NO separate customer table)
    new_order = Order(
        customer_name=order_data.name,
        description=f"Guest order for {order_data.email}"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Step 2: Create order details
    for item in order_data.items:
        sandwich = db.query(Sandwich).filter(Sandwich.id == item.sandwich_id).first()
        if not sandwich:
            raise HTTPException(status_code=404, detail=f"Sandwich {item.sandwich_id} not found")

        order_detail = OrderDetail(
            order_id=new_order.id,
            sandwich_id=item.sandwich_id,
            amount=item.amount
        )
        db.add(order_detail)

    db.commit()

    return {
        "message": "Guest order placed successfully!",
        "order_id": new_order.id
    }

# Get customer information for service
@app.get("/service/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Build a list of sandwich details
    order_items = []
    for detail in order.order_details:
        order_items.append({
            "sandwich_id": detail.sandwich_id,
            "sandwich_name": detail.sandwich.name if detail.sandwich else "Unknown",
            "amount": detail.amount
        })

    return {
        "order_id": order.id,
        "customer_name": order.customer_name,
        "order_date": order.order_date,
        "description": order.description,
        "items": order_items
    }

# ------------------- End -------------------

if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
