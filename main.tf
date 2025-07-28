resource "google_compute_subnetwork" "subnetwork-ipv6" {
  name          = "ipv6-test-subnetwork"
  region        = "us-west2"
  stack_type    = "IPV4_ONLY"
  ipv6_access_type = "external"
}

resource "google_compute_network" "vpc_fail" {
  name                    = "vpc-ipv6"
  auto_create_subnetworks = false
  enable_ula_internal_ipv6 = false
}


resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
