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
