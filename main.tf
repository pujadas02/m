resource "google_sql_database_instance" "main" {
  name             = "psc-enabled-main-instance"
  database_version = "MYSQL_8_0"
  settings {
    tier    = "db-f1-micro"

    backup_configuration {
      enabled = true
      binary_log_enabled = true
    }
    availability_type = "REGIONAL"
  }
}

resource "google_compute_network_attachment" "default" {
    name = "basic-network-attachment"
    region = "us-central1"
    description = "basic network attachment description"
    connection_preference = "ACCEPT_MANUAL"
}
