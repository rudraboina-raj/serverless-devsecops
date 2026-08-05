from google.cloud import pubsub_v1


class PubSubSubscriber:

    def __init__(self, project_id, subscription_name):

        self.subscriber = pubsub_v1.SubscriberClient()

        self.subscription_path = self.subscriber.subscription_path(
            project_id,
            subscription_name,
        )

    def start(self, callback):

        print(f"Listening on {self.subscription_path}")

        streaming_pull_future = self.subscriber.subscribe(
            self.subscription_path,
            callback=callback,
        )

        try:

            streaming_pull_future.result()

        except KeyboardInterrupt:

            streaming_pull_future.cancel()

            print("Subscriber stopped.")

        except Exception as ex:

            streaming_pull_future.cancel()

            print(f"Subscriber error: {ex}")
