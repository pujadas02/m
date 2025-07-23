resource "google_compute_subnetwork" "subnet_pass1" {
  name       = "subnet-pass1"
  region     = "us-central1"
  network    = "default"
  ip_cidr_range = "10.0.0.0/24"
  stack_type = "IPV4_ONLY"
}
resource "google_compute_instance" "ipv4_only_instance" {
  name         = "ipv4-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }

  stack_type = "IPV4_ONLY"
}
