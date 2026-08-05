class PaymentRequest:

    @staticmethod
    def validate(data):

        required_fields = [
            "order_id",
            "amount",
            "payment_method"
        ]

        for field in required_fields:

            if field not in data:

                raise ValueError(f"{field} is required")