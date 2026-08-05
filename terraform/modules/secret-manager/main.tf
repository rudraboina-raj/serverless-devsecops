resource "google_secret_manager_secret" "db_password" {

  project = var.project_id

  secret_id = var.secret_id

  replication {

    auto {}

  }

}

resource "google_secret_manager_secret_version" "db_password_version" {

  secret = google_secret_manager_secret.db_password.id

  secret_data = var.secret_value

}