resource "google_essential_contacts_contact" "contact1" {
  parent = "organizations/123456789012"  
  email  = "alerts@effem.com"          
  language_tag = "en-US"
  notification_category_subscriptions = ["BILLING", "SECURITY"]
}


resource "google_essential_contacts_contact" "contact2" {
  parent = "organizations/123456789012"  
  email  = "alerts@xample.com"          
  language_tag = "en-US"
  notification_category_subscriptions = ["BILLING", "SECURITY"]
}


resource "google_essential_contacts_contact" "contact3" {
  parent = "organizations/123456789012"  
  email  = "alerts@kindsnacking.com"          
  language_tag = "en-US"
  notification_category_subscriptions = ["BILLING", "SECURITY"]
}




resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
