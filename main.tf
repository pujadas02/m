resource "google_service_account" "myaccount" {
  account_id   = "myaccount"
  display_name = "My Service Account"
}

resource "google_service_account_key" "mykey" {
  service_account_id = google_service_account.myaccount.name
  public_key_type    = "TYPE_X509_PEM_FILE"
}



resource "google_compute_network" "vpc_network" {
  project                                   = "my-project-name"
  name                                      = "vpc-network"
  routing_mode                              = "GLOBAL"
  bgp_best_path_selection_mode              = "STANDARD"
}
