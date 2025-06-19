variable "resource_group_name" {
  description = "Sugar"
  type        = string
  default     = "5929f706-6711-4044-90b8-b2d847b54d9f"
}

variable "location" {
  description = "The Azure region where resources will be deployed."
  type        = string
  default     = "eastus" # Escolha a região mais próxima ou desejada (e.g., "brazilsouth")
}

variable "storage_account_name_prefix" {
  description = "A unique prefix for the storage account name."
  type        = string
  default     = "dlsgen2" # Use algo que ajude a identificar sua conta
}

variable "environment" {
  description = "The environment (e.g., dev, test, prod)."
  type        = string
  default     = "dev"
}
