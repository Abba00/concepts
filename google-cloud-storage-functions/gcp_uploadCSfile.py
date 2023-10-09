#import packages
from google.cloud import storage
import os

# set credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google-cloud-storage-functions\pipeline-draft-b08361d7f8a6.json'

# define function that uploads file to the bucket
def upload_cs_file(bucket_name, source_file_name, destination_file_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return True

upload_cs_file('yellow_demo_storage_bucket', 'google-cloud-storage-functions\sample_upload_file.txt', 'json/upload_file.json')
