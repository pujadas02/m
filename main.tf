resource "google_compute_subnetwork" "subnetwork-ipv6" {
  name          = "ipv6-test-subnetwork"
  ip_cidr_range = "10.0.0.0/22"
  region        = "us-west2"
  network       = google_compute_network.custom-test.id
}

resource "google_compute_network" "custom-test" {
  name                    = "ipv6-test-network"
  auto_create_subnetworks = false
}

resource "azurerm_redis_cache" "example" {
  name                = "example-redis"
  location            = "East US"
  resource_group_name = "example-resources"
  capacity            = 1
  family              = "C"
  sku_name            = "Basic"

  # Attributes checked by the policy
  non_ssl_port_enabled = false
  enable_non_ssl_port  = false
}
