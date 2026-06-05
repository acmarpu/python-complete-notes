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


# Azure cli for resource group
# Configuration need to check 

# Storage account 
# read from config file from yaml 

# file handling concepts 

# conditional statement pre check 




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
    print("3. List Storage Accounts")
    print("4. Update Storage Account")
    print("5. Delete Storage Account")
    print("6. Create Container")
    print("7. List Containers")
    print("8. Update Container")
    print("9. Delete Container")
    print("10. List Activity Logs")
    print("11. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        resource_group_name = input("Enter resource group name: ")
        location = input("Enter location (e.g., eastus): ")
        create_resource_group(resource_client, resource_group_name, location)

    elif choice == "2":
        resource_group_name = input("Enter resource group name: ")
        storage_account_name_input = input("Enter storage account name: ")
        location = input("Enter location (e.g., eastus): ")
        create_storage_account(storage_client, resource_group_name, storage_account_name_input, location)

    elif choice == "3":
        print("Listing storage accounts...")
        subscription_id_input = input("Enter subscription ID: ")
        list_storage_accounts(subscription_id_input)

    elif choice == "4":
        print("Updating storage account...")
        storage_account_name_input = input("Enter storage account name: ")
        new_location = input("Enter new location (e.g., westus): ")
        update_storage_account(storage_account_name_input, new_location)

    elif choice == "5":
        print("Deleting storage account...")
        storage_account_name_input = input("Enter storage account name: ")
        delete_storage_account(storage_account_name_input)

    elif choice == "6":
        print("Creating container...")
        storage_account_name = input("Enter storage account name: ")
        container_name = input("Enter container name: ")
        create_container(storage_account_name, container_name)

    elif choice == "7":
        print("Listing containers...")
        storage_account_name = input("Enter storage account name: ")
        list_containers(storage_account_name)

        
    elif choice == "8":
        print("Updating container...")
        storage_account_name = input("Enter storage account name: ")
        container_name = input("Enter container name: ")
        new_container_name = input("Enter new container name: ")
        update_container(storage_account_name, container_name, new_container_name)

    elif choice == "9":
        print("Deleting container...")
        storage_account_name = input("Enter storage account name: ")
        container_name = input("Enter container name: ")
        delete_container(storage_account_name, container_name)

    elif choice == "10":
        print("Listing activity logs...")
        storage_account_name = input("Enter storage account name: ")
        list_activity_logs(storage_account_name)

    elif choice == "11":
        print("Exiting...")
        sys.exit(0)
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
    
    

def create_storage_account(storage_client, resource_group_name, storage_account_name, location):
    try:
        resource_group_name = resource_group_name.strip()
        storage_account_name = storage_account_name.strip()
        location = location.strip()

        params = {
            "sku": {"name": "Standard_LRS"},
            "kind": "StorageV2",
            "location": location,
            "access_tier": "Hot"
        }

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

def list_storage_accounts(subscription_id):
    print(f"list_storage_accounts() called for subscription '{subscription_id}'")
    # TODO: implement storage account listing logic here


def update_storage_account(storage_account_name, new_location):
    print(f"update_storage_account() called for '{storage_account_name}' to '{new_location}'")
    # TODO: implement storage account update logic here


def delete_storage_account(storage_account_name):
    print(f"delete_storage_account() called for '{storage_account_name}'")
    # TODO: implement storage account deletion logic here


def create_container(storage_account_name, container_name):
    print(f"create_container() called for container '{container_name}' in storage account '{storage_account_name}'")
    # TODO: implement container creation logic here


def list_containers(storage_account_name):
    print(f"list_containers() called for storage account '{storage_account_name}'")
    # TODO: implement container listing logic here


def update_container(storage_account_name, container_name, new_container_name):
    print(f"update_container() called for container '{container_name}' in storage account '{storage_account_name}'")
    # TODO: implement container update logic here


def delete_container(storage_account_name, container_name):
    print(f"delete_container() called for container '{container_name}' in storage account '{storage_account_name}'")
    # TODO: implement container deletion logic here


def list_activity_logs(storage_account_name):
    print(f"list_activity_logs() called for storage account '{storage_account_name}'")
    # TODO: implement activity log retrieval logic here


# display the cloud storage activity logs for the storage account


# if __name__ == "__main__":

if __name__ == "__main__":
    main()