from . import orders, order_details, promotions, menu_items, payment


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(payment.router)
