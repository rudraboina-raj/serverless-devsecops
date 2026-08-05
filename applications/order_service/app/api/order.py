from flask import Blueprint
from flask import jsonify
from flask import request

from ..dependencies.database import get_db
from ..services.order_service import OrderService

order_bp = Blueprint("orders", __name__)


@order_bp.post("/orders")
def create_order():

    db = next(get_db())

    try:

        data = request.get_json()

        result = OrderService.create_order(db, data)

        return jsonify(result), 201

    finally:

        db.close()


@order_bp.get("/orders")
def get_orders():

    db = next(get_db())

    try:

        orders = OrderService.get_orders(db)

        result = []

        for order in orders:

            result.append(
                {
                    "order_id": order.order_id,
                    "employee_id": order.employee_id,
                    "product_id": order.product_id,
                    "quantity": order.quantity,
                    "total_price": order.total_price,
                    "status": order.status,
                }
            )

        return jsonify(result), 200

    finally:

        db.close()


@order_bp.get("/orders/<order_id>")
def get_order(order_id):

    db = next(get_db())

    try:

        order = OrderService.get_order(db, order_id)

        if not order:

            return jsonify({"message": "Order not found"}), 404

        return (
            jsonify(
                {
                    "order_id": order.order_id,
                    "employee_id": order.employee_id,
                    "product_id": order.product_id,
                    "quantity": order.quantity,
                    "total_price": order.total_price,
                    "status": order.status,
                }
            ),
            200,
        )

    finally:

        db.close()
