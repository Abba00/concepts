#import packages
from google.cloud import storage
import os

# set credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google-cloud-storage-functions\pipeline-draft-b08361d7f8a6.json'

# define function that uploads file to the bucket
def download_cs_file(bucket_name, file_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.blob(file_name)
    blob.download_to_filename(destination_file_name)

    return True

download_cs_file('yellow_demo_storage_bucket', 'json/download_file.json', 'google-cloud-storage-functions/download_file.txt')
