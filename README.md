🔹 constraints/compute.disableHybridCloudIpv6
✅ Description:
This organization policy constraint disables the use of IPv6 for hybrid cloud networking—meaning any scenario where your on-premises infrastructure connects to GCP using Cloud VPN or Cloud Interconnect, and IPv6 is involved.

💡 Hybrid Cloud = On-prem ↔ GCP over VPN or Interconnect

| Resource                                 | Affected When Using IPv6 | Example Blocked Fields                               |
| ---------------------------------------- | ------------------------ | ---------------------------------------------------- |
| `google_compute_ha_vpn_gateway`          | ✅                        | If associated tunnels use IPv6                       |
| `google_compute_vpn_gateway`             | ✅                        | Same as above                                        |
| `google_compute_vpn_tunnel`              | ✅                        | `peer_ip` or `local_traffic_selector` with IPv6      |
| `google_compute_interconnect_attachment` | ✅                        | `ipsec_internal_addresses` or BGP peer IPs with IPv6 |
| `google_compute_router_interface`        | ✅                        | If `ip_range` is IPv6                                |
| `google_compute_router_peer`             | ✅                        | IPv6 BGP peer IPs                                    |

