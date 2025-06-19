# main.tf

# 1. Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    Environment = var.environment
    Project     = "DataPipeline"
  }
}

# 2. Storage Account (ADLS Gen2)
# Nomes de Storage Accounts devem ser globalmente únicos e em minúsculas
resource "azurerm_storage_account" "adls_gen2" {
  name                     = "${var.storage_account_name_prefix}${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "GRS" # Geo-Redundant Storage (para maior durabilidade)
  is_hns_enabled           = true  # Essencial para habilitar o ADLS Gen2 (Hierarchical Namespace)

  tags = {
    Environment = var.environment
    Project     = "DataPipeline"
  }
}

# Gerar um sufixo aleatório para o nome da Storage Account para garantir unicidade
resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
  number  = true
}

resource "azurerm_storage_container" "landing" {
  name                  = "landing"
  storage_account_name  = azurerm_storage_account.adls_gen2.name
  container_access_type = "private"
}

# 3. Containers (Bronze, Silver, Gold)
resource "azurerm_storage_container" "bronze" {
  name                  = "bronze"
  storage_account_name  = azurerm_storage_account.adls_gen2.name
  container_access_type = "private" # "private" é o padrão e mais seguro
}

resource "azurerm_storage_container" "silver" {
  name                  = "silver"
  storage_account_name  = azurerm_storage_account.adls_gen2.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "gold" {
  name                  = "gold"
  storage_account_name  = azurerm_storage_account.adls_gen2.name
  container_access_type = "private"
}

# Opcional: Container para logs ou outros fins
resource "azurerm_storage_container" "logs" {
  name                  = "logs"
  storage_account_name  = azurerm_storage_account.adls_gen2.name
  container_access_type = "private"
}