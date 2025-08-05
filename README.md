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

### To Disable Multiple Preview Features
```hcl
resource "google_compute_preview_feature" "disable_alpha_api_access" {
  provider          = google-beta
  name              = "alpha-api-access"
  activation_status = "DISABLED"
}

resource "google_compute_preview_feature" "disable_beta_api_access" {
  provider          = google-beta
  name              = "beta-api-access"
  activation_status = "DISABLED"
}

resource "google_compute_preview_feature" "disable_other_alpha_feature" {
  provider          = google-beta
  name              = "another-alpha-feature"
  activation_status = "DISABLED"
}
```

but we dont know how many features are there so how can we block all preview features, or else we can ask if there is any certain one they want to block.
also i want doc file of this one policy(as its not a gcp ogr policy)
