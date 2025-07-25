resource "google_project_iam_member" "example_member" {
  project = "my-project-id"
 
  member  = "user:example-user@example.com"
}

resource "google_project_iam_binding" "example_binding" {
  project = "my-project-id"
  role    = "roles/iap.tunnelResourceAccessor"
  members = [
    "user:example-user@example.com",
    "serviceAccount:example-sa@my-project-id.iam.gserviceaccount.com",
  ]
}

resource "google_project_iam_policy" "example_policy" {
  project     = "my-project-id"
  policy_data = data.google_iam_policy.admin.policy_data
}

data "google_iam_policy" "admin" {
  binding {
    role = "roles/iap.tunnelResourceAccessor"
    members = [
      "user:example-user@example.com",
    ]
  }
}



resource "google_folder_iam_member" "example_folder_member" {
  folder = "folders/123456789"
  role   = "roles/iap.tunnelResourceAccessor"
  member = "user:example-user@example.com"
}

resource "google_folder_iam_binding" "example_folder_binding" {
  folder = "folders/123456789"
  role   = "roles/iap.tunnelResourceAccessor"
  members = [
    "user:example-user@example.com",
  ]
}


resource "google_organization_iam_member" "example_org_member" {
  org_id = "123456789012"
  role   = "roles/iap.tunnelResourceAccessor"
  member = "user:example-user@example.com"
}

resource "google_organization_iam_binding" "example_org_binding" {
  org_id = "123456789012"
  role   = "roles/iap.tunnelResourceAccessor"
  members = [
    "user:example-user@example.com",
  ]
}

