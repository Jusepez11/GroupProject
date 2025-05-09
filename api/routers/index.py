from . import (
    orders,
    order_details,
    promotions,
    menu_items,
    payment,
    resources,
    recipes,
    restaurant_manager,
    service_rep,
    customer,
    reviews
)


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(payment.router)
    app.include_router(resources.router)
    app.include_router(recipes.router)
    app.include_router(restaurant_manager.router)
    app.include_router(service_rep.router)
    app.include_router(customer.router)
    app.include_router(reviews.router)