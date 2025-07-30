# Restrict Public IP access on Cloud SQL instances
This Checkov custom policy ensures that Google Cloud SQL instances do **not** have public IPv4 addresses assigned. It helps prevent unintended public exposure of database instances.

## Benefits
- **Enhances Security:** Prevents Cloud SQL instances from being publicly accessible, reducing attack surface.
- **Blocks Implicit Defaults:** Catches cases where the `ip_configuration` block is missing and a public IP would be assigned by default.
- **Ensures Consistency:** Standardizes secure Cloud SQL configurations across infrastructure.
- **Supports Compliance:** Aligns with security best practices and regulatory requirements.
- **Integrates with CI/CD:** Enables automated checks in deployment pipelines to catch misconfigurations early.

## 🎯 Why This Matters

If you omit ip_configuration entirely, public IPv4 access defaults to true, matching GCP’s default behavior.
However, if an ip_configuration block is present but ipv4_enabled isn't explicitly set, Terraform will default it to false, which can cause failures for 2nd‑gen instances without a private_network. 

## ensure that:
**Resource type checked:**  
- `google_sql_database_instance`

**Check passes if:**  
- The `ip_configuration` block must be present and `ipv4_enabled` attribute must set to **false**

```hcl
ip_configuration {
  ipv4_enabled = false
}
```
