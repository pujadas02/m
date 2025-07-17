resource "google_compute_network" "example_network" {
  name                    = "example-network"
  auto_create_subnetworks  = true
}


resource "google_compute_subnetwork" "example_subnet" {
  name          = "example-subnet"
  network       = google_compute_network.example_network.name
  region        = "us-central1"
  ip_cidr_range = "10.0.0.0/24"
}


resource "google_compute_network" "peer_network" {
  name                    = "peer-network"
  auto_create_subnetworks  = true
}


resource "google_compute_subnetwork" "peer_subnet" {
  name          = "peer-subnet"
  network       = google_compute_network.peer_network.name
  region        = "us-central1"
  ip_cidr_range = "10.1.0.0/24"
}




