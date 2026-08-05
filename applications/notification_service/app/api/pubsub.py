import json
import base64
import traceback
import logging

from flask import Blueprint, request, jsonify

from ..services.email_service import EmailService

pubsub_bp = Blueprint("pubsub", __name__)

logger = logging.getLogger(__name__)


@pubsub_bp.route("/pubsub", methods=["POST"])
def receive_message():

    logger.info("========== Pub/Sub Request Received ==========")

    try:

        body = request.get_json()

        logger.info(f"Request Body: {body}")

        if body is None:
            logger.error("No request body")
            return jsonify({"error": "Invalid request"}), 400

        if "message" not in body:
            logger.error("No Pub/Sub message")
            return jsonify({"error": "No Pub/Sub message"}), 400

        encoded_data = body["message"].get("data")

        logger.info(f"Encoded Data: {encoded_data}")

        if encoded_data:

            decoded = base64.b64decode(encoded_data).decode("utf-8")

            logger.info(f"Decoded JSON: {decoded}")

            event = json.loads(decoded)

            logger.info(f"Event Type: {event.get('event')}")

            if event.get("event") == "EmployeeCreated":

                logger.info("Calling EmailService...")

                EmailService.send_employee_created_email(event)

                logger.info("EmailService completed.")

            else:

                logger.warning("Unknown event type")

        else:

            logger.warning("No encoded data received")

        return jsonify({"status": "SUCCESS"}), 200

    except Exception:

        logger.exception("Exception while processing Pub/Sub")

        return jsonify({"status": "ERROR"}), 200
