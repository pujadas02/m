resource "google_compute_subnetwork" "subnetwork-ipv6" {
  name          = "ipv6-test-subnetwork"
  ip_cidr_range = "10.0.0.0/22"
  region        = "us-west2"
  network       = google_compute_network.custom-test.id
  stack_type    = "IPV4_ONLY"
  ipv6_access_type = "EXTERNAL"
}







resource "azurerm_cognitive_account" "example" {
  name                = "example-cognitive-account"
  location            = "eastus"
  resource_group_name = "example-rg"
  kind                = "CognitiveServices"
  sku_name            = "S1"

  public_network_access_enabled = true

  network_acls {
    default_action = "Deny"
  }
}


resource "azurerm_search_service" "example" {
  name                = "example-search-service"
  location            = "eastus"
  resource_group_name = "example-rg"
  sku                 = "basic"

  public_network_access_enabled = false
}












resource "google_service_account" "default" {
  account_id   = "my-custom-sa"
  display_name = "Custom SA for VM Instance"
}

resource "google_compute_instance" "default" {
  name         = "my-instance"
  machine_type = "n2-standard-2"
  zone         = "us-central1-a"

  tags = ["foo", "bar"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
      }
    }
  }

  // Local SSD disk
  scratch_disk {
    interface = "NVME"
  }

  network_interface {
    network = "default"
    stack_type = "IPV4_ONLY"
    access_config {
    }
  }
  metadata = {
    foo = "bar"
  }
  metadata_startup_script = "echo hi > /test.txt"
  service_account {
    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    email  = google_service_account.default.email
    scopes = ["cloud-platform"]
  }
}

