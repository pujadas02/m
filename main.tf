resource "google_service_account" "myaccount" {
  account_id   = "myaccount"
  display_name = "My Service Account"
}




resource "google_compute_network" "vpc_network" {
  project                                   = "my-project-name"
  name                                      = "vpc-network"
  routing_mode                              = "GLOBAL"
  bgp_best_path_selection_mode              = "STANDARD"
}
