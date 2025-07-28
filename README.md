# 🚫 Disable VM Serial Port Logging to Stackdriver (Cloud Logging)

This policy enforces that VM instances to **not** send their serial port output logs to Stackdriver (now called Cloud Logging), reducing exposure of potentially sensitive boot and runtime data.

## Serial Port Logging & Stackdriver (Cloud Logging)
Serial port logging refers to the ability of a VM instance to send its serial port output (low-level boot and runtime logs) somewhere for inspection.
Stackdriver Logging (now called Cloud Logging) is the destination service where logs are collected and stored.

## 📋 Enforcement Behavior

| Feature                              | Setting                                        | Behavior                                         |
| ------------------------------------ | ---------------------------------------------- | ------------------------------------------------ |
| Serial Port Logging to Cloud Logging | `serial-port-enable-logging: "false"` or unset | ❌ Serial port logs **not sent** to Cloud Logging |
| Serial Port Logging to Cloud Logging | `serial-port-enable-logging: "true"`           | ✅ Serial port logs **sent** to Cloud Logging     |

## ✅ How to enforce disabling serial port logging to Cloud Logging

Ensure that VM instances have the metadata key `serial-port-enable-logging` set to `"false"` or removed entirely.

## Example: Terraform snippet for disabling serial port logging

```hcl
resource "google_compute_instance" "example" {
  name         = "example-instance"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  metadata = {
    "serial-port-enable-logging" = "false"
  }

  # other instance configs...
}
```
## References

[* Serial Port Logging Metadata — Google Cloud Docs](https://cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#setting_project_and_instance_metadata)
  
