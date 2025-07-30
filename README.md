# **Restrict VM IP Forwarding**
Ensure that VM instances do **not** have IP forwarding enabled, which can allow routing or packet spoofing and poses a security risk.

**IP forwarding** is the ability of a VM (or any network device) to receive network traffic and send it out to another destination — effectively routing traffic.
 
***Why would you use it?***
   If the VM is acting as:
    A gateway,
      A NAT instance,
      A firewall proxy,
      A custom router
      
## ✅ Benefits

- Prevents VMs from acting as routers or spoofing(IP spoofing is when a machine sends network packets with a fake (forged) source IP address — pretending to be another system.) traffic
- Reduces attack surface by disabling unnecessary IP forwarding
- Enforces least privilege and secure defaults
- Catches misconfigurations early in CI/CD

- **Resource Type:** `google_compute_instance`
- **Condition:** 
  - Fails if `can_ip_forward = true`
  - Passes if `can_ip_forward` is:
    - Not set (defaults to `false`)
    - Explicitly set to `false`


