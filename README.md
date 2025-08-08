# Checkov Custom Policy: Restrict VM IP Forwarding

## Overview
This Checkov custom policy validates Terraform `google_compute_instance` resources to ensure IP forwarding (`can_ip_forward`) is **only enabled** on VMs explicitly allowed in a whitelist.

## How it works
- Scans `google_compute_instance` resources.
- Checks if `can_ip_forward` is set to `true`.
- Passes if VM name is in the allowed list; fails otherwise.
- Skips if `can_ip_forward` not set or `false`.
