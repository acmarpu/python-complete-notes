from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
tenant_id = os.getenv("AZURE_TENANT_ID")
account_url = os.getenv("AZURE_STORAGE_ACCOUNT_URL")


# Create a credential object using ClientSecretCredential
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# Configure sftp to Azure Storage Blob
def configure_sftp_to_container(container_name):
    """
    Configure SFTP access to an Azure Storage Blob container.
    
    Args:
        container_name (str): The name of the Azure Storage Blob container.
    
    Returns:
        BlobServiceClient: A client to interact with the specified container.
    """
    try:
        # Create a BlobServiceClient using the account URL and credential
        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)
        
        # Get a client for the specified container
        container_client = blob_service_client.get_container_client(container_name)
        
        print(f"Successfully configured SFTP access to container: {container_name}")
        return container_client
    except Exception as e:
        print(f"Failed to configure SFTP access to container: {e}")
        raise

    # main function to test the configuration
if __name__ == "__main__":
    container_name = "your-container-name"  # Replace with your actual container name
    configure_sftp_to_container(container_name)