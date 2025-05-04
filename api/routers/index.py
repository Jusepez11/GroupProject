from . import orders, order_details, promotions, menu_items, payment, resources, restaurant_manager


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(payment.router)
    app.include_router(resources.router)
    app.include_router(restaurant_manager.router)
