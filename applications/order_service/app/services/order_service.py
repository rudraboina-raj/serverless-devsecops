import uuid

from sqlalchemy.orm import Session

from ..models.order import Order
from ..repository.order_repository import OrderRepository
from ..schemas.order_schema import OrderRequest
from ..schemas.order_schema import OrderResponse


class OrderService:

    @staticmethod
    def create_order(db: Session, data: dict):

        OrderRequest.validate(data)

        order = Order(

            order_id=str(uuid.uuid4()),

            employee_id=data["employee_id"],

            product_id=data["product_id"],

            quantity=data["quantity"],

            total_price=data["total_price"],

            status="CREATED",

        )

        saved_order = OrderRepository.create(db, order)

        return OrderResponse.success(saved_order)

    @staticmethod
    def get_order(db: Session, order_id: str):

        return OrderRepository.get_by_id(db, order_id)

    @staticmethod
    def get_orders(db: Session):

        return OrderRepository.get_all(db)