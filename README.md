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


Here’s a **concise explanation** of each Terraform resource, the **field where IPv6 is used**, **why it’s used**, and the **resource's role** in hybrid networking:

---

### 1. `google_compute_ha_vpn_gateway`

* **Purpose:** High Availability (HA) VPN Gateway for connecting GCP to on-prem via IPsec VPN
* **IPv6 Field:** Not directly—IPv6 is enabled **implicitly** via `stack_type = "IPV4_IPV6"`
* **Why/How Used:** Enables support for IPv6 traffic when associated VPN tunnels are configured for it
* **Blocked If:** `disableHybridCloudIPv6 = true` and IPv6 stack is selected

---

### 2. `google_compute_vpn_gateway`

* **Purpose:** Classic (non-HA) VPN Gateway for site-to-site VPN connections
* **IPv6 Field:** Again, indirectly affected via associated tunnels
* **Why/How Used:** IPv6 can flow through if the connected tunnel supports IPv6
* **Blocked If:** Used in IPv6 VPN setup under `disableHybridCloudIPv6`

---

### 3. `google_compute_vpn_tunnel`

* **Purpose:** Defines the actual VPN tunnel (IPsec config) between GCP and remote peer
* **IPv6 Fields:**

  * `peer_ip`: Remote (on-prem) gateway’s **IPv6 address**
  * `local_traffic_selector`: IPv6 CIDRs to route through the tunnel
* **Why/How Used:** IPv6 routes and peer IPs enable dual-stack VPN traffic
* **Blocked If:** Any field uses IPv6 when hybrid IPv6 is disabled

---

### 4. `google_compute_interconnect_attachment`

* **Purpose:** Sets up the virtual interface (VLAN) for Dedicated/Partner Interconnect
* **IPv6 Fields:**

  * `ipsec_internal_addresses`: Internal IPv6 address used for encryption
  * BGP peer IPs: IPv6 addresses for BGP peering with on-prem router
* **Why/How Used:** Required for IPv6 traffic over Interconnect; supports BGP session over IPv6
* **Blocked If:** Any BGP peer or internal IP uses IPv6

---

### 5. `google_compute_router_interface`

* **Purpose:** Connects Cloud Router to a specific network attachment (e.g., VPN, Interconnect)
* **IPv6 Field:** `ip_range`: Can be an IPv6 CIDR
* **Why/How Used:** Used for IPv6 link-local routing or address space over hybrid links
* **Blocked If:** You assign IPv6 range for hybrid link

---

### 6. `google_compute_router_peer`

* **Purpose:** Defines BGP session between Cloud Router and peer (on-prem router or cloud edge)
* **IPv6 Fields:**

  * `ip_address`: IPv6 address of GCP BGP interface
  * `peer_ip_address`: IPv6 address of the on-prem BGP peer
* **Why/How Used:** Enables dynamic IPv6 route exchange using BGP
* **Blocked If:** IPv6 used in either `ip_address` or `peer_ip_address`

---

### ✅ Summary

| Resource                  | Role                     | Why IPv6 Is Used                     |
| ------------------------- | ------------------------ | ------------------------------------ |
| `ha_vpn_gateway`          | Enables HA VPN           | IPv6 support via `stack_type`        |
| `vpn_gateway`             | Classic VPN gateway      | Supports IPv6 via associated tunnel  |
| `vpn_tunnel`              | Defines IPsec tunnel     | IPv6 peer IP or traffic selectors    |
| `interconnect_attachment` | Layer 2/3 hybrid link    | IPv6 BGP or encryption IPs           |
| `router_interface`        | Connects router to link  | IPv6 subnet for interface            |
| `router_peer`             | BGP session with on-prem | IPv6 BGP exchange (peer IPs, routes) |


