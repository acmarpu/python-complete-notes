import json
from logging import config
import os


def load_config(config_file="config.json"):
    """
    Load configuration from JSON file.
    """

    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"Configuration file '{config_file}' not found."
        )

    try:
        with open(config_file, "r") as file:
            config = json.load(file)

        return config

    except json.JSONDecodeError as e:
        raise Exception(
            f"Invalid JSON format in '{config_file}': {e}"
        )
    

def create_resource_group_from_config(resource_client, config):
    try:
        rg_name = config["resource_group"]["name"]
        location = config["resource_group"]["location"]

        result = resource_client.resource_groups.create_or_update(
            rg_name,
            {
                "location": location
            }
        )

        print(
            f"Resource group '{result.name}' created successfully."
        )

    except KeyError as e:
        print(f"Missing JSON key: {e}")

    except Exception as e:
        print(f"Failed to create resource group: {e}")


def create_storage_account_from_config(
    resource_client,
    storage_client,
    config
):
    try:
        rg_name = config["resource_group"]["name"]

        storage_config = config["storage_account"]

        storage_account_name = storage_config["name"]
        sku = storage_config.get("sku", "Standard_LRS")
        kind = storage_config.get("kind", "StorageV2")

        rg = resource_client.resource_groups.get(rg_name)

        params = {
            "sku": {
                "name": sku
            },
            "kind": kind,
            "location": rg.location
        }

        poller = storage_client.storage_accounts.begin_create(
            rg_name,
            storage_account_name,
            params
        )

        account = poller.result()

        print(
            f"Storage account '{account.name}' created successfully."
        )

    except KeyError as e:
        print(f"Missing JSON key: {e}")

    except Exception as e:
        print(f"Failed to create storage account: {e}")

