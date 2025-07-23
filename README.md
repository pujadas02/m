For disabling IPv6-specific fields DISABLE THESE, such as:

| Resource                    | Attribute                  | Purpose                                                                 |
| --------------------------- | -------------------------- | ----------------------------------------------------------------------- |
| `google_compute_subnetwork` | `stack_type`               | `IPV4_ONLY` or `IPV4_IPV6` (enables dual-stack IPv6 support)           |
| `google_compute_subnetwork` | `ipv6_access_type`         | Specifies `INTERNAL` or `EXTERNAL` IPv6 access mode                    |
| `google_compute_subnetwork` | `ipv6_cidr_range`          | Optional manually defined IPv6 CIDR range for the subnetwork           |
| `google_compute_instance`   | `ipv6_access_config`       | Enables IPv6 access on a VM's network interface                        |
| `google_compute_network`    | `enable_ula_internal_ipv6` | Enables internal IPv6 (ULA) within the VPC                             |
| `google_compute_network`    | `internal_ipv6_range`      | References the internal IPv6 range; requires `enable_ula_internal_ipv6 = true` |
| Resource                  | Attribute            | Notes                                                                                                                                                                |
| ------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `google_compute_instance` | `stack_type`         | Indicates if IPv6 is enabled on the NIC. Values: `IPV4_ONLY`, `IPV4_IPV6`, `IPV6_ONLY`. If absent, defaults to `IPV4_ONLY`. You can check this to detect IPv6 usage. |
| `google_compute_instance` | `ipv6_access_config` | Defines IPv6 access (usually external). Absence means no external IPv6 access.                                                                                       |
| `alias_ip_range` block    | `ip_cidr_range`      | Defines IP range for alias IPs. Can be single IP, netmask, or CIDR, but must be in the subnetwork range. Can be IPv4 or IPv6 depending on subnetwork.                |


SO I HAVE TO ENSURE THESE ATTRIBUTES ARE NOT PRESENT UNDER THESE THREE RESOURCES 

