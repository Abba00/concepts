#import packages
from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google-cloud-storage-functions\pipeline-draft-b08361d7f8a6.json'

# define function that uploads file to the bucket
def list_cs_files(bucket_name):
    storage_client = storage.Client()

    file_list = storage_client.list_blobs(bucket_name)
    file_list = [file.name for file in file_list]

    return file_list

print(list_cs_files('yellow_demo_storage_bucket'))