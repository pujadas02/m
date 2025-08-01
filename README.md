# Disable VM Nested Virtualization

This policy ensures that all virtual machines (VMs) created in Google Cloud Platform (GCP) have nested virtualization explicitly disabled unless required. This prevents potential misuse of virtualized environments within VMs, which can increase your attack surface or lead to resource management challenges.

### Nested Virtualization Inheritance Summary

Nested virtualization in GCP is a per-VM setting that allows a virtual machine to run nested hypervisors. This setting can be explicitly enabled or disabled when creating a VM.

However, **nested virtualization can also be inherited indirectly from the custom image used to create the VM**. If a custom image is created from a VM that had nested virtualization enabled, any new VM launched from that image may inherit the nested virtualization capability unless it is explicitly disabled in the VM configuration.

**Key points:**

* Nested virtualization is **not controlled at the project level** in GCP.
* It is configured **per VM instance** via the `advanced_machine_features` setting.
* Custom images **carry the nested virtualization flag** from their source VM.
* To prevent unintended inheritance, always explicitly disable nested virtualization on new VMs regardless of the image.

```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-standard-2"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  advanced_machine_features {
    enable_nested_virtualization = false
  }
}
```
### enable_nested_virtualization - (Optional) Defines whether the instance should have nested virtualization enabled. Defaults to false.
**REF** [doc](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance#enable_nested_virtualization-1)
