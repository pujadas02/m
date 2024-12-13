
terraform {
    # required_version = "1.0.0"
    required_providers {
    aws = {
        source  = "hashicorp/aws"
        version = "4.0.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.0.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "azurerm" {
  features {}
}
variable "example_list" {
  description = "A list variable"
  type        = list(string)
  default     = ["item1", "item2", "item3"]
}
