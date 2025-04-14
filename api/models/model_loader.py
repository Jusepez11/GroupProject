from . import orders, order_details, recipes, sandwiches, resources, menu, promotion, restaurant_manager

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    promotion.Base.metadata.create_all(engine)
    restaurant_manager.Base.metadata.create_all(engine)
