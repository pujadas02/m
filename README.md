 We check that 'private_connectivity' exists in google_datastream_connection_profile
 to ensure Datastream uses secure private VPC peering and disables public connectivity.
 Without private connectivity, the connection defaults to public, which is less secure.
 Key Datastream resources:
 1) google_datastream_private_connection: sets up private VPC peering.
 2) google_datastream_connection_profile: defines connections, must reference private connection for private access.
 3) google_datastream_stream: manages data replication using these profiles.
