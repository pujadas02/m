## Disable BigQuery Omni for Cloud Azure

BigQuery Omni allows querying data stored in Microsoft Azure directly from Google BigQuery. Disabling this feature helps prevent data exfiltration to Azure, ensures compliance with data residency policies, and reduces security risks by restricting cross-cloud data processing.

### How to Disable:

To disable BigQuery Omni for Azure, do not create any `google_bigquery_connection` resource with an `azure` configuration block in your Terraform code. This effectively blocks connections from BigQuery to Azure.

### Example of enabling BigQuery Omni for Azure (DO NOT include this to disable):

```hcl
resource "google_bigquery_connection" "azure_connection" {
  provider      = google-beta
  connection_id = "my-azure-connection"
  friendly_name = "Azure Connection for BigQuery Omni"

  azure {
    tenant_id         = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    service_principal_id = "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
    service_principal_key = "azure-service-principal-key"
    azure_ad_resource = "https://storage.azure.com/"
    storage_account   = "myazurestorageaccount"
    container        = "bq-omni-staging-container"
  }
}
```

### To disable:

Simply ensure no such resource exists or remove any BigQuery connection that references Azure.
