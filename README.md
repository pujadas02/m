# Disable VPC External IPv6 Usage

This policy ensures that external IPv6 access is disabled on VPC subnetworks by verifying that the `ipv6_access_type` attribute is not set to `EXTERNAL`. Restricting external IPv6 access helps reduce exposure of resources to the public internet and improves network security posture.

## Resources Checked

* `google_compute_subnetwork`

## Attributes

* `ipv6_access_type` (on subnetworks): Should **not** be set to `EXTERNAL`.

## Why This Matters

Disabling external IPv6 prevents VPC subnetworks from having public IPv6 addresses, reducing attack surface and protecting resources from unauthorized access.


