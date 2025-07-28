# What is Public Access Prevention (PAP)?
Public Access Prevention is a Google Cloud feature that blocks all public access to buckets (Cloud Storage). When PAP is enabled on a bucket, even users with permissions cannot make the bucket or its objects publicly accessible.

## Why enforce it?
Prevent accidental or intentional public exposure of sensitive data.
Adds an extra layer of security beyond IAM policies.

## So, to enforce Public Access Prevention we want to make sure:
```hcl
public_access_prevention == "enforced"
```

[EXAmple ref](https://registry.terraform.io/providers/hashicorp/google/6.45.0/docs/resources/storage_bucket#example-usage---enabling-public-access-prevention)

```hcl
resource "google_storage_bucket" "no-public-access" {
  name          = "no-public-access-bucket"
  location      = "US"
  force_destroy = true
  public_access_prevention = "enforced"
}
```
