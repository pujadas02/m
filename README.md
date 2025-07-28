#  Enable GCP Detailed Audit Logging Mode

This policy ensures that Google Cloud Platform (GCP) projects have **detailed audit logging** enabled, covering all key log types:
* `ADMIN_READ`
* `DATA_READ`
* `DATA_WRITE`
  
Enabling these log types helps organizations meet compliance, security, and operational monitoring requirements by capturing **who did what, where, and when** across the platform.

##  Required Audit Log Types
| Log Type     | Purpose                                                             |
| ------------ | ------------------------------------------------------------------- |
| `ADMIN_READ` | Admin activity logs (e.g., role changes, configuration edits)       |
| `DATA_READ`  | Logs read access to data (e.g., `gcloud compute instances list`)    |
| `DATA_WRITE` | Logs write access to data (e.g., `gcloud compute instances create`) |

```
resource "google_project_iam_audit_config" "iap-audit-logging" {
  service = "iap.googleapis.com"
  audit_log_config {
    log_type = "ADMIN_READ"
  }
  audit_log_config {
    log_type = "DATA_WRITE"
  }
  audit_log_config {
    log_type = "DATA_READ"
  }
}
```
