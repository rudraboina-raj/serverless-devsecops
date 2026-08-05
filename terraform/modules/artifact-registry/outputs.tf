output "repository_name" {
  description = "Full name of the Artifact Registry repository"
  value       = google_artifact_registry_repository.repository.name
}

output "repository_id" {
  description = "Artifact Registry repository ID"
  value       = google_artifact_registry_repository.repository.repository_id
}

output "location" {
  description = "Region where the repository is created"
  value       = google_artifact_registry_repository.repository.location
}