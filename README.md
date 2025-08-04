# Why We Cannot Manage or Fully Check Cross-Project Service Account (XPSA) Liens Like Custom User Liens:

## 1 Cross-Project Service Account Liens are System-Managed

These liens are automatically created and removed by GCP when you grant or remove IAM roles to a service account from another project.

You cannot create or delete these liens manually via Terraform or API.

## 2 Custom User Liens Are User-Managed

Custom liens can be created and deleted explicitly by users (via Terraform or API).

This means you can track, control, and check them directly.

## 3 Because XPSA Liens Are Automatic & Hidden:

You cannot manage XPSA liens directly in Terraform or any tool.

You only manage the IAM bindings that cause those liens to exist or be removed.

The actual lien removal happens after you remove the IAM binding.

## 4 Why This Makes Detection of Removal Hard

Terraform and Checkov see only the desired Terraform config, not the live current state.

If a binding disappears from your Terraform code, you don’t know if it’s a removal or just not added yet.

Without comparing previous state vs current state or live IAM policies, you cannot know if the binding is being removed (which triggers lien removal).



## but we can do this- (it might not work also)
## Use Terraform Plan Output with External Scripts
Use terraform plan to get a diff of what will be added/removed.

Parse the plan to detect removal of cross-project IAM bindings.

Integrate that as a guard or pre-commit hook or CI step.
