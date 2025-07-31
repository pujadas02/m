resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

}


resource "google_compute_project_metadata_item" "default" {
  key   = "enable-guest-attributes"
  value = "true"
}

resource "google_compute_project_metadata" "default" {
  metadata = {
    enable-guest-attributes = "false"
  }
}

