resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "false"
  }
}

resource "google_compute_project_metadata_item" "default" {
  key   = "attributes"
  value = "false"
}


resource "google_compute_project_metadata" "default" {
  metadata = {
    
  }

}
