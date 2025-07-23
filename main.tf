resource "google_datastream_private_connection" "private_conn" {
  name     = "private-connection"
  location = "us-central1"
}
resource "google_datastream_connection_profile" "postgres_private" {
  name                 = "postgres-private-profile"
  location             = "us-central1"
  connection_profile_id = "pg-private-profile"

  postgresql_profile {
    hostname = "10.0.0.5"
    port     = 5432
    username = "pg_user"
    password = "pg_password"
    database = "postgres_db"
  }

  private_connectivity {
    private_connection = google_datastream_private_connection.private_conn.id
  }
}
