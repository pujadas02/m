resource "google_storage_bucket" "no-public-access" {
  name          = "no-public-access-bucket"
  location      = "US"
  force_destroy = true
  public_access_prevention = "unspecified"
}



resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
