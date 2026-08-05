from flask import Blueprint
from flask import jsonify
from flask import request

from applications.payment_service.app.dependencies.database import get_db
from applications.payment_service.app.schemas.payment_schema import PaymentRequest
from applications.payment_service.app.services.payment_service import PaymentService

payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/payments", methods=["POST"])
def create_payment():

    data = request.get_json()

    PaymentRequest.validate(data)

    db = next(get_db())

    payment = PaymentService.create_payment(db, data)

    return (
        jsonify(
            {
                "message": "Payment completed successfully",
                "payment_id": payment.payment_id,
            }
        ),
        201,
    )


@payment_bp.route("/payments", methods=["GET"])
def get_all_payments():

    db = next(get_db())

    payments = PaymentService.get_all_payments(db)

    return jsonify(
        [
            {
                "payment_id": p.payment_id,
                "order_id": p.order_id,
                "amount": p.amount,
                "payment_method": p.payment_method,
                "status": p.status,
            }
            for p in payments
        ]
    )


@payment_bp.route("/payments/<payment_id>", methods=["GET"])
def get_payment(payment_id):

    db = next(get_db())

    payment = PaymentService.get_payment(db, payment_id)

    return jsonify(
        {
            "payment_id": payment.payment_id,
            "order_id": payment.order_id,
            "amount": payment.amount,
            "payment_method": payment.payment_method,
            "status": payment.status,
        }
    )


@payment_bp.route("/payments/<payment_id>", methods=["PUT"])
def update_payment(payment_id):

    data = request.get_json()

    db = next(get_db())

    payment = PaymentService.update_payment(db, payment_id, data)

    return jsonify(
        {"message": "Payment updated successfully", "status": payment.status}
    )
