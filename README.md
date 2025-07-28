## Summary

The domain restriction happens via an organization policy (google_organization_policy resource).

No direct Terraform resource to restrict "contacts" domain on actual resource level.

Custom Checkov policy can only enforce that the org policy resource exists with correct settings.
