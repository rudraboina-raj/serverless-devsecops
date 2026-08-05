resource "google_service_account" "service_account" {

  project = var.project_id

  account_id = var.account_id

  display_name = var.display_name

}

resource "google_project_iam_member" "secret_accessor" {

  project = var.project_id

  role = "roles/secretmanager.secretAccessor"

  member = "serviceAccount:${google_service_account.service_account.email}"

}

resource "google_project_iam_member" "cloudsql_client" {

  project = var.project_id

  role = "roles/cloudsql.client"

  member = "serviceAccount:${google_service_account.service_account.email}"

}

resource "google_project_iam_member" "pubsub_publisher" {

  project = var.project_id

  role = "roles/pubsub.publisher"

  member = "serviceAccount:${google_service_account.service_account.email}"

}