resource "google_organization_iam_audit_config" "org_success" {
  org_id  = "your-org-id"
  service = "allServices"
  audit_log_config {
    log_type = "DATA_READ"
    exempted_members   = []
  }
}
resource "google_folder_iam_audit_config" "folder_success" {
  folder_id = "your-folder-id"
  service   = "allServices"
  audit_log_config {
    log_type = "ADMIN_READ"
  }
}
resource "google_project_iam_audit_config" "project_success" {
  project = "your-project-id"
  service = "allServices"
  audit_log_config {
    log_type = "ADMIN_READ"
    exempted_members   = [ffhhg]
  }
}
