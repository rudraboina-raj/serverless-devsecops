resource "google_vpc_access_connector" "connector" {

  name = "serverless-connector"

  project = var.project_id

  region = var.region

  network = var.network_name

  ip_cidr_range = "10.20.0.0/28"

  min_instances = 2

  max_instances = 3

  machine_type = "e2-micro"
}