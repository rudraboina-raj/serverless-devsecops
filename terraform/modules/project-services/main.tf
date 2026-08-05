resource "google_project_service" "services" {

  for_each = toset([
    "compute.googleapis.com",
    "artifactregistry.googleapis.com",
    "run.googleapis.com",
    "servicenetworking.googleapis.com",
    "sqladmin.googleapis.com",
    "secretmanager.googleapis.com",
    "pubsub.googleapis.com",
    "cloudresourcemanager.googleapis.com"
  ])

  project = var.project_id

  service = each.value

  disable_on_destroy = false
}