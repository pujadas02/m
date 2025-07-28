resource "google_storage_bucket" "no-public-access" {
  name          = "no-public-access-bucket"
  location      = "US"
  force_destroy = true
  uniform_bucket_level_access = true
}



resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
