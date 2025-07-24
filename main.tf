resource "google_compute_ssl_certificate" "self_managed" {
  name        = "global-self-managed-cert"
  private_key = file("private-key.pem")
  certificate = file("certificate.pem")
}














resource "google_bigquery_connection" "aws_connection" {
  provider      = google-beta
  connection_id = "my-aws-connection"
  friendly_name = "AWS Connection for BigQuery Omni"
  aws {
    cross_account_role_arn = "arn:aws:iam::123456789012:role/BigQueryOmniAccess"
    s3_staging_dir         = "s3://my-bq-omni-staging-bucket"
    region                 = "us-east-1"
  }
}
resource "google_bigquery_connection" "connection" {
  connection_id = local.bigquery_prefix
  location      = var.bigquery_omni_region
  friendly_name = local.bigquery_prefix
  description   = "External connection to Azure"

  azure {
    customer_tenant_id               = var.azure_tenant_id
    federated_application_client_id = azuread_application.bigquery_connection.application_id
  }
}

