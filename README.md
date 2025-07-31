# Enforce Default Cloud Build Service Account Policy

This policy ensures that all Cloud Build triggers and builds use only the default Cloud Build service account, and do not specify any custom service account. This enforces consistent identity and privilege management, helping reduce risk from misconfigured or over-privileged custom service accounts.

### We must ensure that the `service_account` attribute **does not exist** in any `google_cloudbuild_trigger` resource; if it does, it means the trigger uses a custom service account, which is not allowed.

