


resource "google_compute_project_metadata_item" "default" {
  key   = "enable-guest-attributes"
  value = "false"
}

resource "google_compute_project_metadata" "default" {
  metadata = {
    enable-guest-attributes = "false"
  }
}

