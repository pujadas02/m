### **Audit Logging Exemption Policy**

This policy controls the auditing of activities in Google Cloud. It enables or disables audit logging for specified IAM roles and actions. The `exempted_members` field allows exclusion of certain users or service accounts from being logged for specific `log_type` operations (e.g., `ADMIN_READ`, `DATA_READ`).

When you **disable audit logging exemption**, any previously excluded members will now have their actions logged under the specified log types.

#### **Key Concepts:**

* **Enabled Logging**: Logs are generated for operations like `ADMIN_READ`, `DATA_READ`, etc.
* **Exemption**: Certain users, service accounts, or groups can be excluded from logs.
* **Disabling Exemption**: Removes users from the `exempted_members` list, ensuring their actions are logged.

### **Example Terraform Configuration (Success)**

This example shows how to **enable audit logging** and ensure that no users are exempted:

```hcl
resource "google_organization_iam_audit_config" "organization" {
  org_id  = "1234567890"
  service = "allServices"

  # Enabling logging for all services
  audit_log_config {
    log_type = "DATA_READ"
    # No exempted members, so all actions will be logged
  }
}
```

In this case, **all users' actions** for `DATA_READ` will be logged, and no one is exempted.

### **Example Terraform Configuration (Failure)**

This example demonstrates what happens when **exemption is applied** to a specific user, meaning their actions will **not be logged** for `DATA_READ`:

```hcl
resource "google_organization_iam_audit_config" "organization" {
  org_id  = "1234567890"
  service = "allServices"

  # Enabling logging for all services
  audit_log_config {
    log_type = "DATA_READ"
    exempted_members = [
      "user:joebloggs@hashicorp.com",  # Exempting joebloggs from data read logs
    ]
  }
}
```

In this case, the user **`joebloggs@hashicorp.com`** will be **exempted from data read logs**, and their actions will not be logged for `DATA_READ`.

### **Disabling the Exemption (Failure Case)**

To **disable the exemption** and ensure that the user is **no longer exempt** from logging, you remove the `exempted_members` or empty the list:

```hcl
resource "google_organization_iam_audit_config" "organization" {
  org_id  = "1234567890"
  service = "allServices"

  # Enabling logging for all services
  audit_log_config {
    log_type = "DATA_READ"
    # Removed exempted_members block, now all actions are logged
  }
}
```

In this **failure case**, the user `joebloggs@hashicorp.com` will now have their actions logged for `DATA_READ`, as they are no longer excluded.


