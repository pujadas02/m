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

## Terraform / advanced_machine_features default (enable_nested_virtualization = false)

When you create a VM via Terraform without specifying enable_nested_virtualization, it defaults to false — nested virtualization is disabled.

So Terraform is explicit in how it configures the VM at creation.

## GCP organization-level boolean constraint (“Disable VM nested virtualization”)

This is a policy at the GCP Org/Project/Folder level, independent of Terraform defaults.

By default, if a user creates a VM via the GCP console, gcloud, or API, nested virtualization is allowed on Intel Haswell or newer CPUs. That’s what the “allowed by default” line refers to — GCP’s platform default, not Terraform.

The boolean constraint ensures that even if someone tries to enable it manually, it will be blocked — it’s an enforcement mechanism across the whole organization.

### Key difference:

Terraform default: disables nested virtualization unless you set it true.

GCP platform default: allows nested virtualization unless an org-level policy disables it.

**In gcp-app-terraform-modules repo variable.tf file we have value is false but the resource is something else so i will check enable_nested_virtualization must be false**
