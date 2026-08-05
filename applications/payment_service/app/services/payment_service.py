import uuid

from shared.core.settings import Settings
from shared.pubsub.publisher import PubSubPublisher

from applications.payment_service.app.events.payment_event import PaymentEvent
from applications.payment_service.app.models.payment import Payment
from applications.payment_service.app.repository.payment_repository import PaymentRepository


class PaymentService:

    # Reusable Pub/Sub Publisher
    publisher = PubSubPublisher(Settings.PROJECT_ID)

    @staticmethod
    def create_payment(db, data):

        payment = Payment(

            payment_id=str(uuid.uuid4()),

            order_id=data["order_id"],

            amount=data["amount"],

            payment_method=data["payment_method"],

            status="SUCCESS",

        )

        # Save payment
        payment = PaymentRepository.create(db, payment)

        # Build event
        event = PaymentEvent.build(payment)

        # Publish event
        PaymentService.publisher.publish(
            Settings.PAYMENT_EVENTS_TOPIC,
            event
        )

        return payment

    @staticmethod
    def get_all_payments(db):

        return PaymentRepository.get_all(db)

    @staticmethod
    def get_payment(db, payment_id):

        payment = PaymentRepository.get_by_id(db, payment_id)

        if not payment:

            raise Exception("Payment not found")

        return payment

    @staticmethod
    def update_payment(db, payment_id, data):

        payment = PaymentRepository.get_by_id(db, payment_id)

        if not payment:

            raise Exception("Payment not found")

        payment.status = data["status"]

        return PaymentRepository.update(db, payment)