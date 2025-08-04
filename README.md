# Why Terraform and Checkov cannot fully track default service accounts’ broad roles (Editor/Owner) even if imported:

## Terraform state includes the resource info, but not the full IAM bindings unless explicitly managed

Importing a service account brings the SA resource into state.

But Terraform does NOT automatically import or know about IAM bindings/roles granted outside Terraform (like Editor or Owner granted via console or other means).

IAM bindings must be managed explicitly in Terraform (google_project_iam_binding, google_service_account_iam_member, etc.).

## Most default service account Editor/Owner roles are assigned automatically by GCP, not via Terraform

So these broad roles often exist only in GCP’s live IAM policies, not in Terraform code or state.

## Checkov only scans Terraform code/resources, not live GCP IAM state

Checkov cannot detect permissions granted outside Terraform code.

So it cannot warn about Editor/Owner roles assigned to default service accounts unless those are explicitly managed in the Terraform files.

