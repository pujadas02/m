# 🚫 Disable SSH-in-Browser Access in Google Cloud

This policy enforces the removal of the `roles/iap.tunnelResourceAccessor` IAM role and ensures Compute Engine instances are configured to reduce browser-based SSH exposure.

Browser-based SSH (SSH-in-Browser) leverages [Identity-Aware Proxy (IAP) TCP tunneling](https://cloud.google.com/iap/docs/using-tcp-forwarding) to open terminal sessions in the Cloud Console. This can be useful but also introduces a risk of unauthorized or overly broad administrative access.

## 📋 Table: Enforcement Behavior

| Feature                        | Setting                                       | Behavior                                     |
|-------------------------------|-----------------------------------------------|----------------------------------------------|
| IAP TCP Tunneling             | `roles/iap.tunnelResourceAccessor` **removed** | ❌ Blocks SSH-in-browser and IAP tunnel access |
| OS Login                      | `enable-oslogin = "TRUE"`                    | ✅ Uses IAM for SSH access                    |
| Project-wide SSH Keys         | `block-project-ssh-keys = "TRUE"`            | ✅ Prevents inherited SSH key injection       |

## 📘 References

- **IAP TCP Tunneling and Role**  
  [https://cloud.google.com/iap/docs/using-tcp-forwarding](https://cloud.google.com/iap/docs/using-tcp-forwarding)

- **SSH-in-Browser Docs**  
  [https://cloud.google.com/compute/docs/ssh-in-browser](https://cloud.google.com/compute/docs/ssh-in-browser)

- **IAP Role: `roles/iap.tunnelResourceAccessor`**  
  [https://cloud.google.com/iam/docs/understanding-roles#iap-roles](https://cloud.google.com/iam/docs/understanding-roles#iap-roles)

```hcl
# ✅ Enforce secure metadata
metadata = {
  enable-oslogin         = "TRUE"
  block-project-ssh-keys = "TRUE"
}

# ✅ Ensure IAP SSH access is not granted
resource "google_project_iam_binding" "remove_iap_tunnel" {
  project = "your-project-id"
  role    = "roles/iap.tunnelResourceAccessor"
  members = [] # Prevent any assignment
}



🔧 enable-oslogin
✅ When set to "TRUE":
Enables OS Login, which means SSH access is managed via IAM roles and permissions, not manually added SSH keys.

Each user's SSH key is stored and linked to their Google identity.

Access is tightly controlled and auditable via IAM.

❌ If set to "FALSE" or omitted:
VM falls back to project-level or instance-level SSH keys.

Anyone with SSH keys in metadata or added manually can access the VM — potentially bypassing IAM.

Less secure and harder to audit.

🔧 block-project-ssh-keys
✅ When set to "TRUE":
Blocks project-wide SSH keys from being injected into the instance.

Only instance-level SSH keys (or OS Login keys) will be valid.

Prevents accidental access from people with project-level key permissions.

❌ If set to "FALSE" or omitted:
All project-wide SSH keys (defined under project.metadata) are allowed.

Anyone who added their SSH key at the project level will be able to access the VM — even if they shouldn't.


