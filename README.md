In Terraform, when creating a Google Cloud VM instance, there are mainly 2 ways to specify or assign an external IPv4 address to the VM:

Assign an Ephemeral External IPv4 (Automatic) IP Address

Use an empty access_config {} block inside the VM's network_interface block.

Google Cloud automatically assigns an ephemeral external IPv4 address from the regional pool.

Example:
```hcl
network_interface {
  network = "default"
  access_config {}   # This requests an ephemeral external IPv4
}

```
If you omit the access_config block entirely, the VM will have no external IP.

Assign a Reserved Static External IPv4 Address

First, reserve a static external IP address using the google_compute_address resource.

Then specify that reserved IP's address in the VM's access_config block with nat_ip.

Example:

```hcl
resource "google_compute_address" "static_ip" {
  name   = "my-static-ip"
  region = "us-central1"
}
resource "google_compute_instance" "vm" {
  name         = "my-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.static_ip.address
    }
  }
}
```
This assigns the reserved static IPv4 address to the VM, ensuring it does not change over time.
