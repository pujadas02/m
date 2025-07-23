resource "google_compute_subnetwork" "subnet_pass1" {
  name       = "subnet-pass1"
  region     = "us-central1"
  network    = "default"
  ip_cidr_range = "10.0.0.0/24"
  stack_type = "IPV4_ONLY"
}
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}

# NOTE: the Name used for Redis needs to be globally unique
resource "azurerm_redis_cache" "example" {
  name                 = "example-cache"
  location             = azurerm_resource_group.example.location
  resource_group_name  = azurerm_resource_group.example.name
  capacity             = 2
  family               = "C"
  sku_name             = "Standard"
  non_ssl_port_enabled = false
  minimum_tls_version  = "1.2"

  redis_configuration {
  }
}
