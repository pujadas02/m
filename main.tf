
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-standard-2"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
 advanced_machine_features {
    enable_nested_virtualization = false
  }
  
}

resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
