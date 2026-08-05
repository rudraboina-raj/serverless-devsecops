class PaymentEvent:

    @staticmethod
    def build(payment):

        return {

            "event_type": "PAYMENT_COMPLETED",

            "payment_id": payment.payment_id,

            "order_id": payment.order_id,

            "amount": payment.amount,

            "payment_method": payment.payment_method,

            "status": payment.status

        }