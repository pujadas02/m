# What is Require OS Login?
Require OS Login enforces that users must use OS Login (which ties Linux user accounts to IAM identities) to SSH into VM instances. This improves security by centralizing SSH access control through IAM instead of managing individual SSH keys on each VM.

## Why enforce it?
Centralizes and simplifies SSH access management.
Eliminates manual SSH key distribution.
Enforces IAM-based access control and audit logging for SSH.

#### Enabling OS Login at the Project level (via project metadata enable-oslogin = TRUE) means all VM instances in that project inherit the setting by default.

#### However, VM instances can override this setting individually by setting instance metadata enable-oslogin = FALSE.

#### so we have to make sure that:
 Validate that project metadata enable-oslogin is TRUE.
 
 Validate that VM instances either do not have the enable-oslogin metadata or have it set to TRUE

### [doc gcp](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin#enable_os_login_during_vm_creation)

