resource "google_compute_project_metadata" "default" {
  metadata = {
    
  }
}

resource "google_compute_instance" "oslogin_instance" {
  name         = "oslogin-instance-name"
  machine_type = "f1-micro"
  zone         = "us-central1-c"
  metadata = {
    enable-oslogin = "TRUE"
  }
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
  network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
  }
}










resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
