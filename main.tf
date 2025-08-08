resource "google_essential_contacts_contact" "contact" {
  parent = "organizations/123456789012"  
  email  = "alerts@example.com"          
  language_tag = "en-US"
  notification_category_subscriptions = ["BILLING", "SECURITY"]
}








resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
