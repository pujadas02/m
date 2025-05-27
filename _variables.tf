variable "tags" {
  type        = map(any)
}

variable "env" {
  type        = string
  description = "The environment where the resources will be deployed."
  validation {
    # allowed environments are "np", "prod"
    condition     = contains(["np", "prod"], var.env)
    error_message = "The environment must be either `np` or `prod`."
  }
}

variable "app_name" {
  type        = string
  description = "The name of the application."
}
