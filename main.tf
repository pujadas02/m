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

resource "google_compute_subnetwork" "subnetwork-ipv6" {
  name          = "ipv6-test-subnetwork"
  region        = "us-west2"
  stack_type    = "IPV4_ONLY"
  ipv6_access_type = "EXTERNAL"
}

resource "google_compute_network" "vpc_fail" {
  name                    = "vpc-ipv6"
  auto_create_subnetworks = false
  enable_ula_internal_ipv6 = false
}

resource "google_compute_instance" "default" {
  name         = "my-instance"
  machine_type = "n2-standard-2"
  zone         = "us-central1-a"
  network_interface {
    network = "default"
    stack_type = "IPV4_ONLY"
    ipv6_access_config {
    }
  }
}
