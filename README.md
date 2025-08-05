### **Approach 1: Using a Simple Script to Track `terraform plan` Output**

You can write a script that **runs `terraform plan`**, looks for any resource deletions (specifically for the `google_resource_manager_lien`), and then **fails the plan** if it detects that the lien is going to be destroyed.

Here's a sample **bash script** that checks the output of `terraform plan`:

#### Example Script to Check `terraform plan` Output

```bash
#!/bin/bash

# Run terraform plan and capture the output
PLAN_OUTPUT=$(terraform plan -no-color)

# Check if a lien is being destroyed in the plan output
if echo "$PLAN_OUTPUT" | grep -q "google_resource_manager_lien.shared_vpc_lien.*Destroy"; then
  echo "Error: Lien resource is being destroyed in the plan!"
  exit 1  # Fail the script (and thus the CI/CD process)
fi

echo "No lien deletion detected. Proceeding with terraform apply."
```

#### **How It Works**:

* This script runs `terraform plan` and captures its output.
* It then checks the output for any line that indicates a **lien resource** (`google_resource_manager_lien.shared_vpc_lien`) is marked for **destruction**.
* If a lien is being destroyed, the script exits with a non-zero status (`exit 1`), which causes the process to fail.
* If no lien is being destroyed, it allows the process to proceed normally.

#### **Steps to Use the Script**:

1. Save the script as `check_lien_removal.sh`.

2. Ensure that it's executable:

   ```bash
   chmod +x check_lien_removal.sh
   ```

3. Run the script instead of directly running `terraform plan`:

   ```bash
   ./check_lien_removal.sh
   ```

This will **fail the Terraform apply** if the lien resource is being removed, as it forces a `terraform plan` failure when it detects that the lien is marked for destruction.

### **Approach: Using `terraform plan` JSON Output for More Structured Detection**

If you prefer a **more structured approach** (e.g., for parsing plan output programmatically), you can use the `terraform plan -out=plan.tfplan` command, which saves the plan in a binary format. Then, you can use `terraform show` to get a JSON representation of the plan and check for any removals of the lien resource.

Here’s how you can do it:

#### Example Script Using `terraform plan -out`:

```bash
#!/bin/bash

# Run terraform plan and output the plan to a file
terraform plan -out=plan.tfplan

# Convert the binary plan to a JSON format
terraform show -json plan.tfplan > plan.json

# Check if the lien resource is being removed
if jq '.resource_changes[] | select(.type == "google_resource_manager_lien" and .change.actions | index("destroy"))' plan.json > /dev/null; then
  echo "Error: Lien resource is being destroyed in the plan!"
  exit 1
fi

echo "No lien deletion detected. Proceeding with terraform apply."
```

#### How It Works:

1. `terraform plan -out=plan.tfplan` creates a plan in binary format.
2. `terraform show -json plan.tfplan` converts the binary plan into a JSON format for easier processing.
3. The script uses `jq` (a command-line JSON processor) to check if any `google_resource_manager_lien` resource is set for **destruction**.
4. If a lien resource is found to be destroyed, it exits with an error.

**Note**: You need to have `jq` installed on the system running the script. On most systems, you can install it via a package manager:

```bash
# For Ubuntu/Debian:
sudo apt-get install jq
```

### **Conclusion**

* You can definitely use `terraform plan` to detect if a **lien** is being removed and fail the plan if necessary.
* Using a simple **bash script** or a more structured approach with **JSON output** and `jq` allows you to inspect the plan and **abort the apply** if the lien is being destroyed.
* This can be integrated into a **CI/CD pipeline** to automatically enforce this check.

By using these methods, you can ensure that **Shared VPC host projects** with **liens** are **protected from accidental deletion** and prevent changes that might violate your organization's policies.

Let me know if you need further help or more detailed examples!
