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
