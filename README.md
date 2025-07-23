For disabling IPv6-specific fields DISABLE THESE, such as:

| Resource                    | Attribute            | Purpose                                   |
| --------------------------- | -------------------- | ----------------------------------------- |
| `google_compute_subnetwork` | `stack_type`         | `IPV4_ONLY` or `IPV4_IPV6` (enables IPv6) |
| `google_compute_subnetwork` | `ipv6_access_type`   | `INTERNAL` or `EXTERNAL` IPv6 access      |
| `google_compute_subnetwork` | `ipv6_cidr_range`    | Optional manually set IPv6 range          |
| `google_compute_instance`   | `ipv6_access_config` | Enables IPv6 on NIC                       |


SO I HAVE TO ENSURE THESE ATTRIBUTES ARE NOT PRESENT UNDER THESE Two RESOURCES 

