resource "google_bigquery_connection" "aws_connection" {
  provider      = google-beta
  connection_id = "my-aws-connection"
  friendly_name = "AWS Connection for BigQuery Omni"
}

