# Checkov Custom Policy: Allowed Ingress Settings for Cloud Run

## Overview
This custom policy enforces that Google Cloud Run services (using the `google_cloud_run_v2_service` resource) restrict their ingress settings to only allow internal traffic or internal plus load balancing. It ensures that the ingress attribute is limited to some allowed values:(can be one or more among these 3)

- `INGRESS_TRAFFIC_ALL`
- `INGRESS_TRAFFIC_INTERNAL_ONLY`  
- `INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER`

Any Cloud Run service configured with a different ingress setting will fail this policy.
