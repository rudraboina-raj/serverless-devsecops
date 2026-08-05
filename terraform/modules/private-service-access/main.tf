resource "google_compute_global_address" "private_ip_range" {

  name = "private-service-range"

  project = var.project_id

  purpose = "VPC_PEERING"

  address_type = "INTERNAL"

  prefix_length = 16

  network = var.network_self_link

}

resource "google_service_networking_connection" "private_vpc_connection" {

  network = var.network_self_link

  service = "servicenetworking.googleapis.com"

  reserved_peering_ranges = [
    google_compute_global_address.private_ip_range.name
  ]

}