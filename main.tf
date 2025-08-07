resource "google_compute_instance" "secure_vm" {
  name         = "allowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  network_interface {
    network = "default"
    access_config {}
  }
}
provider "google" {
  project = "your-project-id"
  region  = "us-central1"
  zone    = "us-central1-a"
}
resource "google_compute_address" "static_ip" {
  name   = "my-static-ip"
  region = "us-central1"
}
resource "google_compute_instance" "vm_ephemeral" {
  name         = "allowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  network_interface {
    network = "default"
    access_config {}
  }
}
resource "google_compute_instance" "vm_static" {
  name         = "disallowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.static_ip.address 
    }
  }
}
