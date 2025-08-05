When the "Require IAM invoker check for Cloud Run services" policy is enforced in Google Cloud, it ensures that:

All Cloud Run services must require IAM-based access to invoke them. Specifically, it prevents unauthenticated access and requires that Cloud Run services are invoked using IAM credentials (i.e., service accounts or users with specific permissions).

This constraint is enforced via Google Cloud's Organization Policy, which is different from managing IAM roles directly through Terraform or other methods. It applies organization-wide to ensure compliance for all Cloud Run services within a GCP organization or folder.

Unauthenticated access to Cloud Run services is disabled by default when this constraint is enforced
