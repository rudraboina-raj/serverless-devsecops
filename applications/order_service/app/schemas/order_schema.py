class OrderRequest:

    @staticmethod
    def validate(data):

        required_fields = [
            "employee_id",
            "product_id",
            "quantity",
            "total_price"
        ]

        for field in required_fields:

            if field not in data:
                raise ValueError(f"{field} is required")


class OrderResponse:

    @staticmethod
    def success(order):

        return {
            "message": "Order created successfully.",
            "order": {
                "order_id": order.order_id,
                "employee_id": order.employee_id,
                "product_id": order.product_id,
                "quantity": order.quantity,
                "total_price": order.total_price,
                "status": order.status,
            },
        }