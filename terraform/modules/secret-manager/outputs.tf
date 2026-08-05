output "secret_id" {
  description = "Full Secret Manager resource ID"
  value       = google_secret_manager_secret.db_password.id
}

output "secret_name" {
  description = "Secret name"
  value       = google_secret_manager_secret.db_password.secret_id
}