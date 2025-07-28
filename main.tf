resource "google_project_iam_audit_config" "iap-audit-logging" {
  service = "iap.googleapis.com"
  audit_log_config {
    log_type = "DATA_READ"
  }
  audit_log_config {
    log_type = "DATA_WRITE"
  }

}


resource "google_compute_network" "vpc_network" {
  project                                   = "my-project-name"
  name                                      = "vpc-network"
  routing_mode                              = "GLOBAL"
  bgp_best_path_selection_mode              = "STANDARD"
}
