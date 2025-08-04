## tf resource - https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_preview_feature

## Use google_compute_preview_feature in Terraform to block known project-level features.
  
   These are explicit GCE preview features you can toggle on/off at the project level.
  
```hcl
resource "google_compute_preview_feature" "block_ipv6" {
  project = "your-project-id"
  name    = "ENABLE_IPV6"
  enabled = false
}
```
Use this to block features like:
       ENABLE_HYPERDISK

  ENABLE_IPV6

   ENABLE_NETLB_IPV6

- Effect: This prevents GCP from allowing preview access to those features at the Compute API level.



## Use Checkov or custom scanners to detect:


## Detect:
Use of the google-beta provider — indicates opt-in to preview.

Use of preview-only fields, e.g.:

enable_nested_virtualization

advanced_machine_features

reservation_affinity

**-Effect: Prevents usage of Terraform constructs that tap into preview functionality, even if the project allows it.**

## Enforce org-wide guidance via documentation or CI/CD pipelines.

search beta feature in mars
