🔒 Disable Enabling Identity-Aware Proxy (IAP) on Global Resources
Description:
This policy ensures that Identity-Aware Proxy (IAP) is not enabled on global backend services. IAP on global services may be restricted to enforce tighter security boundaries or reduce complexity by limiting centralized access gateways.

Security Implications:

Restricts centralized IAP usage to align with security policies or compliance.

Helps avoid unwanted global access exposure.

Ensures IAP is only enabled in explicitly permitted regions or configurations.

https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service
