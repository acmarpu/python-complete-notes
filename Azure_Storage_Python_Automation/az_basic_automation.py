# Description: Automate Azure storage accounts and container using Python
"""

The goal is to create a command-line tool that allows users to manage Azure cloud storage account and containers easily. 
The tool should authenticate using a .env file environment variable and provide options for creating, updating,
deleting and listing storage accounts and containers.
The user should be able to perform these operations interactively through a menu-driven interface.

"""
 

# import py module to interact with Azure services

import json
import datetime
import os
import sys

from dotenv import load_dotenv

from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient


# Constants and env variables and load
load_dotenv()
TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")

# Define all the methods for azure resource management for storage account
def authenticate_azure():
    """
    Authenticate to Azure using the ClientSecretCredential from azure.identity.
    Returns a credential object that can be used to create clients for Azure services.
    """
    credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )

    if not credential:
        raise Exception("Failed to authenticate with Azure. Please check your credentials.")

    print(f"Successfully authenticated to Azure")
    return credential


# define resource client method
def get_resource_client(credential):
    """
    Create and return a ResourceManagementClient using the provided credential.
    This client can be used to manage Azure resource groups.
    """
    try:
        resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
        print(f"Successfully created ResourceManagementClient")
        return resource_client
    except Exception as e:
        print(f"Failed to create ResourceManagementClient: {e}")
        sys.exit(1)


# define storage client method
def get_storage_client(credential):
    """
    Create and return a StorageManagementClient using the provided credential.
    This client can be used to manage Azure storage accounts.
    """
    try:
        storage_client = StorageManagementClient(credential, SUBSCRIPTION_ID)
        print(f"Successfully created StorageManagementClient")
        return storage_client
    except Exception as e:
        print(f"Failed to create StorageManagementClient: {e}")
        sys.exit(1)


# main method to call the above method and execute the code
def main():
    try:
        credential = authenticate_azure()
        resource_client = get_resource_client(credential)
        storage_client = get_storage_client(credential)
        if storage_client and resource_client:
            print(f"Azure clients are ready to use.")
            while True:
                display_menu(resource_client, storage_client)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Display the cloud storage activity as menu
def display_menu(resource_client, storage_client):
    print("\nAzure Storage Account Management")
    print("1. Create resource group")
    print("2. Create Storage Account")

    print("11. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        resource_group_name = input("Enter resource group name: ")
        location = input("Enter location (e.g., eastus): ")
        create_resource_group(resource_client, resource_group_name, location)

    elif choice == "2":
        resource_group_name = input("Enter existing resource group name: ")
        storage_account_name_input = input("Enter storage account name: ")
        # No location prompt: default to the existing resource group's location
        create_storage_account(resource_client, storage_client, resource_group_name, storage_account_name_input, None)

    else:
        print("Invalid choice. Please try again.")

# CRDU Operations for storage account and container

def create_resource_group(resource_client, resource_group_name, location):
    """Create a resource group in Azure."""
    try:
        resource_group_name = resource_group_name.strip()
        location = location.strip()
        result = resource_client.resource_groups.create_or_update(
            resource_group_name,
            {"location": location}
        )
        print(f"Resource group '{result.name}' created in '{result.location}'")
    except Exception as e:
        print(f"Failed to create resource group: {e}")
        sys.exit(1)
       

def create_storage_account(resource_client, storage_client, resource_group_name, storage_account_name, location):
    try:
        resource_group_name = resource_group_name.strip()
        storage_account_name = storage_account_name.strip()
        # allow None or empty input; we'll default to the resource group's location below
        location = location.strip() if location else ""
        try:
            rg = resource_client.resource_groups.get(resource_group_name)
        except Exception:
            print(f"Resource group '{resource_group_name}' does not exist. Please create it first or enter an existing resource group.")
            return

        # Default to the resource group's location when none provided
        if not location:
            location = getattr(rg, 'location', None)
            if not location:
                print("Unable to determine resource group location; please provide a location.")
                return
            print(f"Using resource group location '{location}' for the storage account.")

        params = {
            "sku": {"name": "Standard_LRS"},
            "kind": "StorageV2",
            "location": location
        }
        # Exit if a storage account with the same name already exists in the resource group
        try:
            for sa in storage_client.storage_accounts.list_by_resource_group(resource_group_name):
                if sa.name.lower() == storage_account_name.lower():
                    print(f"Storage account '{storage_account_name}' already exists in resource group '{resource_group_name}'.")
                    return
        except Exception:
            # If listing fails, continue and let the create call handle errors
            pass

        poller = storage_client.storage_accounts.begin_create(
            resource_group_name,
            storage_account_name,
            params
        )
        account = poller.result()
        print(f"Storage account '{account.name}' created in resource group '{resource_group_name}'")
    except Exception as e:
        print(f"Failed to create storage account: {e}")
        sys.exit(1)


# display the cloud storage activity logs for the storage account


# if __name__ == "__main__":

if __name__ == "__main__":
    main()