resource "google_pubsub_topic" "topic" {

  project = var.project_id

  name = var.topic_name

}

resource "google_pubsub_subscription" "subscription" {

  project = var.project_id

  name = var.subscription_name

  topic = google_pubsub_topic.topic.id

  ack_deadline_seconds = 20

  message_retention_duration = "604800s"

}

# =====================================================
# Payment Events Topic
# =====================================================

resource "google_pubsub_topic" "payment_topic" {

  project = var.project_id

  name = var.payment_topic_name

}