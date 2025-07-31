# Disable VM Serial Port Logging to Stackdriver (Cloud Logging)

This policy enforces that VM instances to **not** send their serial port output logs to Stackdriver (now called Cloud Logging), reducing exposure of potentially sensitive boot and runtime data.

## Serial Port Logging & Stackdriver (Cloud Logging)
Serial port logging refers to the ability of a VM instance to send its serial port output (low-level boot and runtime logs) somewhere for inspection.
Stackdriver Logging (now called Cloud Logging) is the destination service where logs are collected and stored.
You can control whether your instances send serial port output to Cloud Logging by setting project- or instance-level metadata

## Policy Logic
For google_compute_instance and google_compute_project_metadata:
The key serial-port-logging-enable must either be absent or explicitly set to "false".

For google_compute_project_metadata_item:
If the key is serial-port-logging-enable, the value must be "false".
##  Enforcement Behavior

| Feature                              | Setting                                        | Behavior                                         |
| ------------------------------------ | ---------------------------------------------- | ------------------------------------------------ |
| Serial Port Logging to Cloud Logging | `serial-port-logging-enable: "false"` or unset | ❌ Serial port logs **not sent** to Cloud Logging |
| Serial Port Logging to Cloud Logging | `serial-port-logging-enable: "true"`           | ✅ Serial port logs **sent** to Cloud Logging     |

## ✅ Compliant Configuration (PASS)
```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "false"
  }
}
```
## ✅ It will also pass:(if attribute doesnot exists)
```hcl
resource "google_compute_instance" "secure_vm" {
  name         = "secure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    
  }
}
```
## ❌ Non-Compliant Configuration (FAIL) this or missing attribute will fail
```hcl
resource "google_compute_instance" "insecure_vm" {
  name         = "insecure-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
  metadata = {
    enable-guest-attributes = "true"
  }
}
```

## References

[* Serial Port Logging Metadata — Google Cloud Docs](https://cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#setting_project_and_instance_metadata)
  
