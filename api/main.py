from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich
from .routers import menu  # <-- New line added here



app = FastAPI()

app.include_router(menu.router)  # <-- This is the new line (include the menu router)


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


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)