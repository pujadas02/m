resource "google_compute_instance" "default" {
  name         = "my-instance"
  machine_type = "n2-standard-2"
  zone         = "us-central1-a"
  metadata = {
    serial-port-logging-enable = "false"
  }
}
