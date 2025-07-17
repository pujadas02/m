# VPC Network 1 (This is the source network)
resource "google_compute_network" "example_network" {
  name                    = "example-network"
  auto_create_subnetworks  = true
}

# Subnetwork 1 for the example network
resource "google_compute_subnetwork" "example_subnet" {
  name          = "example-subnet"
  network       = google_compute_network.example_network.name
  region        = "us-central1"
  ip_cidr_range = "10.0.0.0/24"
}

# VPC Network 2 (This is the peer network)
resource "google_compute_network" "peer_network" {
  name                    = "peer-network"
  auto_create_subnetworks  = true
}

# Subnetwork 2 for the peer network
resource "google_compute_subnetwork" "peer_subnet" {
  name          = "peer-subnet"
  network       = google_compute_network.peer_network.name
  region        = "us-central1"
  ip_cidr_range = "10.1.0.0/24"
}

# TEST CASE: VPC Peering Resource (This will trigger the Checkov policy)
resource "google_compute_network_peering" "example_peering" {
  name         = "example-vpc-peering"
  network      = google_compute_network.example_network.name
  peer_network = google_compute_network.peer_network.name
  auto_create_routes = true
}

