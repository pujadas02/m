

variable "env" {
  type = string
}

variable "app_name" {
  type = string
}

variable "location" {
  type = string
}

variable "location_abr" {
  type = string
}

variable "tags" {
  type = map(any)
}

###########
# Network #
###########

variable "vnet_id" {
  type = string
}

variable "pe_subnet_id" {
  type = string
}

variable "app_subnet_id" {
  type = string
}

variable "logic_subnet_id" {
  type = string
}

variable "apim_subnet_id" {
  type = string
}

variable "ase_subnet_id" {
  type = string
}

variable "agw_subnet_id" {
  type = string
}

##############
# SQL Server #
##############

variable "sql_admin_pass" {
  type        = string
  description = "Admin password for SQL Server"
  sensitive   = true
}


###############
# Redis Cache #
###############

variable "redis_capacity" {
  type = string
}

variable "redis_family" {
  type = string
}

variable "redis_sku_name" {
  type = string
}
