### Terraform Google provider currently does not support API key creation or management, including API keys bound to service accounts. This is due to Google Cloud not exposing a public API for API key creation or binding that Terraform can use.

### Consequently, Terraform cannot import existing API keys (bound to service accounts or not) into its state management.

### Terraform can manage service accounts and service account JSON keys (via google_service_account_key resource), but this is different from API keys used for authenticating APIs.

### The google_service_account_key resource does not support import as well, so keys created outside Terraform may not always be manageable via Terraform either.
