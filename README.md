Disable BigQuery Omni for Cloud AWS
BigQuery Omni allows querying data stored in AWS S3 directly from Google BigQuery. Disabling this feature helps prevent data exfiltration to AWS, ensures compliance with data residency policies, and reduces security risks by restricting cross-cloud data processing.

How to Disable:

To disable BigQuery Omni for AWS, do not create any google_bigquery_connection resource with an aws configuration block in your Terraform code. This effectively blocks connections from BigQuery to AWS.

Example of enabling BigQuery Omni for AWS (DO NOT include this to disable):

hcl
Copy
Edit
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
To disable:
Simply ensure no such resource exists or remove any BigQuery connection that references AWS.
