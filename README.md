## Disable Global Access to VM Serial Ports

This policy ensures that VM serial port access is disabled globally to prevent unauthorized interactive access or data exfiltration via serial consoles.

**Metadata Key:** `serial-port-enable`

| Value     | Behavior                                                  |
|-----------|-----------------------------------------------------------|
| `false`   | ✅ Disables serial port access                             |
| `true` *(default)* | ❌ Enables serial port access, posing a security risk |

---

### ✅ How to Enforce

Add metadata with `serial-port-enable = "false"` in your VM definition:

```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  metadata = {
    serial-port-enable = "false"
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
```

https://docs.prowler.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_11/#:~:text=To%20change%20the%20policy%20using%20the%20GCP%20Console%2C,located%20below%20the%20Remote%20access%20block.%20Click%20Save. 
