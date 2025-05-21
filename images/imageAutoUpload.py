from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
blob_service = BlobServiceClient.from_connection_string(connection_string)
container = blob_service.get_container_client("images")

with open("gta_sample.jpg", "rb") as data:
    container.upload_blob("sampleImg.jpg", data, overwrite=True)
