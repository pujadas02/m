# Disable Service Account Key Creation

This policy ensures that **no new service account keys are created** in your Google Cloud Platform (GCP) environment. Service account keys are long-lived credentials that can be easily leaked or misused if not properly managed.

## Why is this important?

* **Reduce credential leakage risk:** Keys can be downloaded and accidentally exposed in insecure locations.
* **Enforce best practices:** Encourages using IAM roles, Workload Identity Federation, or OAuth tokens instead of static keys.
* **Simplify security management:** Avoids the overhead of manual key rotation and revocation.
* **Improve compliance:** Aligns with security standards that discourage use of static credentials.

## What does the policy do?

* Detects creation of service account keys (`google_service_account_key` resource).


