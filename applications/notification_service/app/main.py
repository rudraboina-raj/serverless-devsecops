import base64
import json
import logging

from flask import Flask, request, jsonify

from applications.notification_service.app.services.notification_service import (
    NotificationService,
)

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/health", methods=["GET"])
def health():

    return jsonify(
        {
            "service": "notification-service",
            "status": "UP",
        }
    ), 200


@app.route("/pubsub", methods=["POST"])
def pubsub():

    try:

        logger.info("=" * 60)
        logger.info("Pub/Sub Request Received")
        logger.info("=" * 60)

        envelope = request.get_json()

        logger.info(f"Request Body: {envelope}")

        if not envelope or "message" not in envelope:

            return jsonify(
                {
                    "message": "Invalid Pub/Sub message"
                }
            ), 400

        pubsub_message = envelope["message"]

        encoded_data = pubsub_message.get("data", "")

        logger.info(f"Encoded Data: {encoded_data}")

        decoded_data = base64.b64decode(
            encoded_data
        ).decode("utf-8")

        logger.info(f"Decoded JSON: {decoded_data}")

        event = json.loads(decoded_data)

        event_type = event.get("event_type") or event.get("event")

        logger.info(f"Event Type: {event_type}")

        if event_type == "EmployeeCreated":

            logger.info("Calling Employee Email Service...")

            NotificationService.send_employee_email(event)

            logger.info("Employee Email Sent Successfully.")

        elif event_type == "PAYMENT_COMPLETED":

            logger.info("Calling Payment Email Service...")

            NotificationService.send_payment_email(event)

            logger.info("Payment Email Sent Successfully.")

        else:

            logger.warning(f"Unknown event type: {event_type}")

        return jsonify(
            {
                "message": "Processed successfully"
            }
        ), 200

    except Exception as ex:

        logger.exception("Notification Service Error")

        return jsonify(
            {
                "message": str(ex)
            }
        ), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080,
    )