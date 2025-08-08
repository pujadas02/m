resource "google_cloud_run_v2_service" "default" {
  provider = google-beta
  name     = "cloudrun-iap-service"
  location = "us-central1"
  deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"
  launch_stage = "BETA"
  iap_enabled = true

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}
resource "google_cloud_run_v2_service" "second" {
  provider = google-beta
  name     = "cloudrun-iap-service"
  location = "us-central1"
  deletion_protection = false
  ingress = var.ingress
  launch_stage = "BETA"
  iap_enabled = true

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
    }
  }
}
