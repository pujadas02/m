For disabling IPv6-specific fields DISABLE THESE, such as:

  ipv6_access_config on network_interface in "google_compute_instance" (enables IPv6 access)

  ipv6_cidr_range on "google_compute_subnetwork" (assigns IPv6 ranges)

  stack_type set to IPV4_IPV6 on "google_compute_network"

SO I HAVE TO ENSURE THESE ATTRIBUTES ARE NOT PRESENT UNDER THESE THREE RESOURCES 

