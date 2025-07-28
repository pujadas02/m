Terraform does not support uploading existing keys, only key creation.

To disable upload, prevent any use of google_service_account_key resource.

To detect upload, use GCP audit logs or IAM policy constraints, not Terraform scans.
