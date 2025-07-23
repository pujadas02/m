For disabling IPv6-specific fields DISABLE THESE, such as:

| Resource                    | Attribute                  | Purpose                                                                 |
| --------------------------- | -------------------------- | ----------------------------------------------------------------------- |
| `google_compute_subnetwork` | `stack_type`               | `IPV4_ONLY` or `IPV4_IPV6` (enables dual-stack IPv6 support)           |
| `google_compute_subnetwork` | `ipv6_access_type`         | Specifies `INTERNAL` or `EXTERNAL` IPv6 access mode                    |
| `google_compute_subnetwork` | `ipv6_cidr_range`          | Optional manually defined IPv6 CIDR range for the subnetwork           |
| `google_compute_instance`   | `ipv6_access_config`       | Enables IPv6 access on a VM's network interface                        |
| `google_compute_network`    | `enable_ula_internal_ipv6` | Enables internal IPv6 (ULA) within the VPC                             |
| `google_compute_network`    | `internal_ipv6_range`      | References the internal IPv6 range; requires `enable_ula_internal_ipv6 = true` |

SO I HAVE TO ENSURE THESE ATTRIBUTES ARE NOT PRESENT UNDER THESE THREE RESOURCES 

