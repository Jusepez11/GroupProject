import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .dependencies.config import conf
from sqlalchemy.orm import Session
from .dependencies.database import get_db
from .models.orders import Order
from .models.sandwiches import Sandwich
from .models.order_details import OrderDetail
from .schemas.orders import GuestOrder
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

# Get customer information
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
if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)