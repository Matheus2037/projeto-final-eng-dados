# outputs.tf

output "resource_group_name" {
  description = "The name of the created Resource Group."
  value       = azurerm_resource_group.main.name
}

output "storage_account_name" {
  description = "The name of the created Storage Account (ADLS Gen2)."
  value       = azurerm_storage_account.adls_gen2.name
}

output "storage_account_primary_dfs_endpoint" {
  description = "The primary DFS endpoint for the Storage Account (ADLS Gen2)."
  value       = azurerm_storage_account.adls_gen2.primary_dfs_endpoint
}