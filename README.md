# Restrict public IP access on new Vertex AI Workbench notebooks and instances	

This boolean constraint, when enforced, restricts public IP access to newly created Vertex AI Workbench notebooks and instances. By default, public IPs can access Vertex AI Workbench notebooks and instances.
constraints/ainotebooks.restrictPublicIp  


so to mimic this logic in checkov -

| Scenario                                                         | Public IP assigned?               | How to control it                  |
| ---------------------------------------------------------------- | --------------------------------- | ---------------------------------- |
| `access_configs` omitted + `disable_public_ip = false` (default) | YES, ephemeral public IP assigned | default behavior                   |
| `access_configs` present + `external_ip` defined                 | YES, static public IP assigned    | explicit static IP                 |
| `access_configs` present + no `external_ip`                      | YES, ephemeral public IP assigned | explicit ephemeral IP              |
| `disable_public_ip = true` + `access_configs` omitted            | NO public IP assigned             | restrict public IP (what you want) |
| `disable_public_ip = true` + `access_configs` present            | ERROR (conflict)                  | invalid configuration              |



so we have to make sure in google_workbench_instance resource disable-public-ip = true and no access config is mentioned.




**search google_workbench_instance in mars to see how they use**
















[docs for google_notebooks_instance](https://docs.prowler.com/checks/gcp/google-cloud-public-policies/ensure-gcp-vertex-ai-workbench-does-not-have-public-ips/#:~:text=It%27s%20not%20currently%20possible%20to%20edit%20a%20Vertex,Locate%20the%20External%20IP%20dropdown%20and%20select%20None.)



https://github.com/teamdatatonic/terraform-google-secure-vertex-workbench/blob/b6b887bdaf746bc78c2e23d2fd42c03f223fff0b/notebooks.tf#L20



