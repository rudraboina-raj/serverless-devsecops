variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "GCP region where the repository will be created"
  type        = string
}

variable "repository_id" {
  description = "Artifact Registry repository name"
  type        = string
}