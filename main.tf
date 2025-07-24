resource "google_compute_backend_service" "iap_enabled" {
  name     = "global-backend"
  protocol = "HTTP"

  iap {
    enabled              = true
    oauth2_client_id     = "example-client-id"
    oauth2_client_secret = "example-secret"
  }
}
