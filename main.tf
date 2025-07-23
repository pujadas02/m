resource "google_compute_subnetwork" "subnetwork-ipv6" {
  name          = "ipv6-test-subnetwork"

  ip_cidr_range = "10.0.0.0/22"
  region        = "us-west2"

  stack_type       = "IPV4_ONLY"
  ipv6_access_type = "EXTERNAL"

  network       = google_compute_network.custom-test.id
}

resource "google_compute_network" "custom-test" {
  name                    = "ipv6-test-network"
  auto_create_subnetworks = false
}
