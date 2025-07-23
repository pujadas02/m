resource "google_compute_subnetwork" "subnet_pass1" {
  name       = "subnet-pass1"
  region     = "us-central1"
  network    = "default"
  ip_cidr_range = "10.0.0.0/24"
}

