variable "location" {
  type        = string
  description = "The location where the resources will be deployed. Allowed values are `eastus2`, `centralus`, `westeurope`, `northeurope`, `southeastasia`, `eastasia`, `chinanorth3`."
  validation {
    # force that only possible values are those in the description
    condition     = contains(["eastus2", "centralus", "westeurope", "northeurope", "southeastasia", "eastasia", "chinanorth3"], var.location)
    error_message = "You can only deploy to 'eastus2', 'centralus', 'westeurope', 'northeurope', 'southeastasia', 'eastasia', 'chinanorth3'."
  }
