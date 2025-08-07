resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "false"
  }
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
}
provider "google" {
  project = "your-project-id"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# Reserve a static external IP address to assign to one of the VMs
resource "google_compute_address" "static_ip" {
  name   = "my-static-ip"
  region = "us-central1"
}

# VM with ephemeral external IPv4
resource "google_compute_instance" "vm_ephemeral" {
  name         = "allowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {} # assigns ephemeral external IPv4
  }
}

# VM with reserved static external IPv4
resource "google_compute_instance" "vm_static" {
  name         = "disallowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.static_ip.address # assigns reserved static IP
    }
  }
}
