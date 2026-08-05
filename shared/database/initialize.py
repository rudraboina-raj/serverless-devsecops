from applications.employee_service.app.models.employee import Employee
from applications.product_service.app.models.product import Product
from applications.order_service.app.models.order import Order
from applications.payment_service.app.models.payment import Payment

from .base import Base
from .connection import engine


def initialize_database():

    Base.metadata.create_all(bind=engine)