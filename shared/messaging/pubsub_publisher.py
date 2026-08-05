import json

from google.cloud import pubsub_v1

from shared.core.settings import Settings


class PubSubPublisher:

    def __init__(self):

        self.publisher = pubsub_v1.PublisherClient()

        self.topic_path = self.publisher.topic_path(
            Settings.PROJECT_ID,
            Settings.EMPLOYEE_EVENTS_TOPIC,
        )

    def publish(self, event: dict):

        data = json.dumps(event).encode("utf-8")

        future = self.publisher.publish(
            self.topic_path,
            data=data,
        )

        return future.result()