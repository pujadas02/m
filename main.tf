resource "google_project" "my_project" {
  name       = "My Project"
  project_id = "your-project-id"
  org_id     = "1234567"
  
}



resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
