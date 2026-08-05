resource "google_compute_network" "vpc" {

  project                 = var.project_id
  name                    = var.network_name
  auto_create_subnetworks = false

}

resource "google_compute_subnetwork" "subnet" {

  name = var.subnet_name

  project = var.project_id

  region = var.region

  network = google_compute_network.vpc.id

  ip_cidr_range = var.subnet_cidr

  private_ip_google_access = true

}

resource "google_compute_firewall" "allow_internal" {

  name = "allow-internal"

  project = var.project_id

  network = google_compute_network.vpc.name

  direction = "INGRESS"

  source_ranges = [
    "10.10.0.0/24"
  ]

  allow {
    protocol = "tcp"
  }

  allow {
    protocol = "udp"
  }

  allow {
    protocol = "icmp"
  }

  description = "Allow internal communication within the VPC"

}