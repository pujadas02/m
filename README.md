# For disabling internal IPv6-specific fields DISABLE THESE:

| Resource                    | Attribute                  | Purpose                                                                 |
| --------------------------- | -------------------------- | ----------------------------------------------------------------------- |
| `google_compute_subnetwork` | `ipv6_access_type`         | Specifies `INTERNAL` or `EXTERNAL` IPv6 access mode                    |
| `google_compute_network`    | `enable_ula_internal_ipv6` | Enables internal IPv6 (ULA) within the VPC                             |
                                                                                     
### `enable_ula_internal_ipv6` (Boolean)

* This flag **enables or disables internal IPv6 (ULA - Unique Local Address) within the entire VPC network**.
* If set to **`true`**, the VPC supports internal IPv6 addressing (ULA).
* If set to **`false` or unset\`**, internal IPv6 addressing is **disabled** on the VPC.

### `ipv6_access_type` ?

Specifies the type of IPv6 access on the subnet only if IPv6 is enabled(i.e., if stack_type is IPV4_IPV6 or IPV6_ONLY).
Possible values:
INTERNAL — Enables internal IPv6 connectivity (ULA).
EXTERNAL — Enables external IPv6 access.
Unset — No IPv6 access configured.

[doc](https://cloud.google.com/vpc/docs/vpc#org-policies)
