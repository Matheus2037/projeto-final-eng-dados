terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0" # Use a versão mais recente compatível
    }
  }
  required_version = ">= 1.0.0"
}

provider "azurerm" {
  features {} # Este bloco é necessário para habilitar as features do provider
}