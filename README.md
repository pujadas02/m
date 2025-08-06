# **Skip default network creation**
# Key points about the default network in GCP and Terraform:
Default network is automatically created by GCP when you create a new project.

The default network is just a network named "default" — no special config beyond the name.

## When you create a GCP project via Terraform, you can set:
```hcl
auto_create_network = false
```
— this attempts to delete the default network immediately after it’s created during project provisioning.

This does NOT prevent the default network from being created initially, because:

The network is created automatically by GCP at project creation time.

What auto_create_network = false does is delete the default network after it’s been created, during Terraform apply.

If you delete the original default network and create your own network named "default", that network will become the default network for the project.

[**REF**](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project)
**by default a default network and supporting resources are automatically created when creating a Project resource.**
**but in mars modules we have auto_create_network= false**
**so need to check in repos that auto_create_network must not exists or if exists must be equal to false**
