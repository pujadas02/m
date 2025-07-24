# Disable Creation of Global Self-Managed SSL Certificates

**Policy:** constraints/compute.disableGlobalSelfManagedSslCertificate

**Description:**  
This boolean constraint disables the creation of **global self-managed SSL certificates** (`google_compute_ssl_certificate`) in your Google Cloud environment. It ensures consistent security by enforcing the use of Google-managed or regional certificates only, reducing operational overhead and mitigating risks related to manual certificate management.

**Impact:**  
- Prevents creating global self-managed SSL certificates.  
- Allows Google-managed or regional self-managed certificates.  
- Helps maintain compliance and reduces security risks associated with manual SSL certificate management.

**How to Enforce:**  
Apply the `constraints/compute.disableGlobalSelfManagedSslCertificate` constraint at the organization, folder, or project level.

**Example Terraform resource to avoid (disallowed):**

```hcl
resource "google_compute_ssl_certificate" "self_managed" {
  name        = "global-self-managed-cert"
  private_key = file("private-key.pem")
  certificate = file("certificate.pem")
}
