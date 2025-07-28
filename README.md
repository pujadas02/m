## What is Domain Restricted Contacts in GCP?
Domain Restricted Contacts is a security feature that restricts the ability to add users as contacts (like project owners, editors, or viewers) to only those users who belong to specified trusted domains. This helps prevent adding external or unauthorized users to your Google Cloud projects or organizations, reducing risk from unintended or malicious access.

## Summary

The domain restriction happens via an organization policy (google_organization_policy resource).

No direct Terraform resource to restrict "contacts" domain on actual resource level.

Custom Checkov policy can only enforce that the org policy resource exists with correct settings.
