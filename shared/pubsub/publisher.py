import json

from google.cloud import pubsub_v1


class PubSubPublisher:
    """
    Reusable Google Cloud Pub/Sub Publisher
    """

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.publisher = pubsub_v1.PublisherClient()

    def publish(self, topic_name: str, message: dict):
        """
        Publish JSON message to Pub/Sub
        """

        topic_path = self.publisher.topic_path(self.project_id, topic_name)

        data = json.dumps(message).encode("utf-8")

        future = self.publisher.publish(topic_path, data=data)

        message_id = future.result()

        print(f"Published Message ID: {message_id}")

        return message_id
