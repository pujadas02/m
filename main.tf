resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "false"
  }
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
}
