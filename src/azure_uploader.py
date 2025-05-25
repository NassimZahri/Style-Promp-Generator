import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

AZURE_CONN_STR = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "images")

blob_service = BlobServiceClient.from_connection_string(AZURE_CONN_STR)
container = blob_service.get_container_client(CONTAINER_NAME)

def upload_image_to_azure(image_path):
    blob_name = os.path.basename(image_path)
    with open(image_path, "rb") as file:
        container.upload_blob(blob_name, file, overwrite=True)

    account_name = AZURE_CONN_STR.split("AccountName=")[1].split(";")[0]
    public_url = f"https://{account_name}.blob.core.windows.net/{CONTAINER_NAME}/{blob_name}"
    return public_url