# What is Uniform Bucket-Level Access?
Uniform Bucket-Level Access (UBLA) is a Google Cloud Storage feature that simplifies permission management by disabling all object-level ACLs and enforcing access at the bucket level only.

## Why enforce it?
Simplifies access control management by removing per-object ACLs.
Reduces risk of accidental public exposure via misconfigured ACLs.
Ensures consistent permission enforcement across all objects in a bucket.

## So, we have to make sure:
```hcl
uniform_bucket_level_access = true"
```

[EXAmple ref](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#uniform_bucket_level_access-1)

```hcl
resource "google_storage_bucket" "no-public-access" {
  name          = "no-public-access-bucket"
  location      = "US"
  force_destroy = true
  uniform_bucket_level_access = true
}
```
