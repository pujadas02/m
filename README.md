## 🔒 Disable Guest Attributes of Compute Engine Metadata

**Constraint Purpose:**
Prevent the exposure of runtime metadata from virtual machines by disabling guest attributes on Compute Engine instances.It applies to:

- Google Compute Engine instances (`google_compute_instance`)
- Project-wide metadata (`google_compute_project_metadata`)
- Individual project metadata items (`google_compute_project_metadata_item`)

## Policy Logic
- For `google_compute_instance` and `google_compute_project_metadata`:  
  The key `enable-guest-attributes` must **either be absent** or explicitly set to `"false"`.

- For `google_compute_project_metadata_item`:  
  If the `key` is `enable-guest-attributes`, the `value` must be `"false"`.

### ✅ Why Disable Guest Attributes?

* **Data Minimization** – Prevents exposure of guest-level system information to the metadata server.
* **Security Hardening** – Reduces the surface area for introspection and potential abuse.
* **Best Practice Compliance** – Aligns with secure-by-default principles in cloud environments.

| Setting             | Description                                                                     | Behavior               |
| ------------------- | ------------------------------------------------------------------------------- | ---------------------- |
| `false` *(default)*| Disables guest attribute access; protects sensitive runtime metadata.           | ✅ Secure – Compliant   |
| `true`  | Enables guest attributes, exposing system-level details to the metadata server. | ❌ Risk – Non-compliant |

### ✅ Compliant Configuration (PASS) 

```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "false"
  }
}
```

### ✅ It will also pass:(if attribute doesnot exists)
```hcl 
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    
  }
}
```
### ❌ Non-Compliant Configuration (FAIL) this or missing attribute will fail

```hcl
resource "google_compute_instance" "insecure_vm" {
  name         = "insecure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "true"
  }
}
```
**Reference:** [Manage guest attributes on VMs – GCP Docs](https://cloud.google.com/compute/docs/metadata/manage-guest-attributes)
              
**Reference:** [main doc](https://cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata)

### We can Set enable-guest-attributes in project-wide metadata so that it applies to all of the VMs in your project.
### WE can also Set enable-guest-attributes in instance metadata .
### here its written - https://cloud.google.com/compute/docs/metadata/manage-guest-attributes#enable_attributes

