resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    serial-port-logging-enable = "false"
  }
}


