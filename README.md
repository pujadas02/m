# Checkov Custom Policy: Disallow Authorized Networks in Cloud SQL
### ✅ Policy Name
**Ensure Cloud SQL instances do not configure authorized networks**

This custom Checkov policy checks that **no `authorized_networks` are configured** in Cloud SQL instance resources (`google_sql_database_instance`) in your Terraform code.



## 🎯 Why This Matters

By default, Google Cloud SQL supports allowing public IP addresses to connect via **authorized networks**. While convenient, this increases your attack surface and can lead to **exposure of your databases to the public internet** — especially if `0.0.0.0/0` or overly broad CIDRs are allowed.

This policy enforces a **zero-trust posture** by ensuring Cloud SQL instances **do not rely on IP-based access** and encourages the use of **private IPs**, **Cloud SQL Auth Proxy**, or **VPC connectivity** instead.

## ✅ Benefits

- Prevents unintended exposure of Cloud SQL instances
- Aligns with **GCP security best practices**
- Helps enforce **private or proxied database access**
- Easy to integrate into your existing CI/CD pipelines using Checkov

## ensure that:
**Resource type checked:**  
- `google_sql_database_instance`

**Check passes if:**  
- The `authorized_networks` attribute **is not present**

