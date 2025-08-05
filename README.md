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

Terraform cannot prevent GCP from initially creating the default network (Terraform describes desired state but cannot stop backend default resource creation).

What auto_create_network = false does is delete the default network after it’s been created, during Terraform apply.

Because the default network is created first by GCP, Terraform cannot create a new network named default until the original default network is deleted.

To manage or remove the default network with Terraform, you need to:

Import the default network resource into Terraform state (because it exists outside Terraform control initially),

Or rely on auto_create_network = false when creating the project, which deletes it later.

If you delete the original default network and create your own network named "default", that network will become the default network for the project.


[**REF**](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project)
