resource "google_compute_instance" "secure_vm" {
  name         = "allowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  can_ip_forward = true
}
resource "google_compute_instance" "secure" {
  name         = "allowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  can_ip_forward = false
}


resource "google_compute_instance" "allowed_vm" {
  name         = "allowed-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  can_ip_forward = true
}

resource "google_compute_instance" "allowed_vmm" {
  name         = "allowed-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  can_ip_forward = false
}

resource "google_compute_instance" "vm_static" {
  name         = "disallowed-vm-1"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
 
}


resource"google_project" "hy" {

}
