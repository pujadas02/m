
## 🔒 Disable Guest Attributes of Compute Engine Metadata

**Constraint Purpose:**
Prevent the exposure of runtime metadata from virtual machines by disabling guest attributes on Compute Engine instances.

**Constraint Type:**
This is a configuration-based best practice (not a GCP org policy constraint) that ensures `enable_guest_attributes` is not enabled in VM instances.

### ✅ Why Disable Guest Attributes?

* **Data Minimization** – Prevents exposure of guest-level system information to the metadata server.
* **Security Hardening** – Reduces the surface area for introspection and potential abuse.
* **Best Practice Compliance** – Aligns with secure-by-default principles in cloud environments.

| Setting             | Description                                                                     | Behavior               |
| ------------------- | ------------------------------------------------------------------------------- | ---------------------- |
| `false` *(default)* | Disables guest attribute access; protects sensitive runtime metadata.           | ✅ Secure – Compliant   |
| `true`              | Enables guest attributes, exposing system-level details to the metadata server. | ❌ Risk – Non-compliant |


### ✅ Compliant Configuration (PASS)

```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  enable_guest_attributes = false

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
```



### ❌ Non-Compliant Configuration (FAIL)

```hcl
resource "google_compute_instance" "insecure_vm" {
  name         = "insecure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  enable_guest_attributes = true

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
```



**Reference:** [Manage guest attributes on VMs – GCP Docs](https://cloud.google.com/compute/docs/metadata/manage-guest-attributes)


