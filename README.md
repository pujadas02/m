**Terraform does not support uploading existing keys, only key creation.**

**To detect upload, use GCP audit logs or IAM policy constraints, not Terraform scans.**

## Creating vs Uploading a Service Account Key
**In Terraform, you can only create new service account keys using the google_service_account_key resource.**

**You cannot "upload" an existing public/private key pair to a service account like you might via gcloud or the Google Cloud Console. That capability is not supported by Terraform.**

**Terraform does not support uploading existing keys. It only supports generating a new key pair and optionally writing the private key to disk.**
