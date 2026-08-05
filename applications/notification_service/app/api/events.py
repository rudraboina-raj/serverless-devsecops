import base64
import json

from flask import Blueprint
from flask import request

events_bp = Blueprint("events", __name__)


@events_bp.post("/events")
def receive_event():

    envelope = request.get_json()

    if not envelope:
        return {"error": "No Pub/Sub message received."}, 400

    if "message" not in envelope:
        return {"error": "Invalid Pub/Sub message."}, 400

    pubsub_message = envelope["message"]

    data = pubsub_message.get("data")

    if data:

        decoded = base64.b64decode(data).decode("utf-8")

        event = json.loads(decoded)

        print("=" * 60)
        print("Employee Event Received")
        print(json.dumps(event, indent=4))
        print("=" * 60)

    return {"message": "Event processed successfully."}, 200
