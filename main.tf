resource "google_project_iam_policy" "example" {
  project     = "my-project-id"
  policy_data = data.google_iam_policy.admin.policy_data
}
data "google_iam_policy" "admin" {
  binding {
    role = "roles/hy"
    members = [
      "user:foo@example.com",
    ]
  }
}
