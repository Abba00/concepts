# Refer to https://www.youtube.com/watch?v=RQj2LpqsxIQ for tutorial refresh
# Import packages
from google.cloud import storage
import os

# set credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google-cloud-storage-functions\pipeline-draft-b08361d7f8a6.json'

# define function that creates the bucket
def create_bucket(bucket_name, storage_class='STANDARD', location='us-central1'):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class

    bucket = storage_client.create_bucket(bucket, location=location)
    # for dual-locatiion buckets add data_locations=[region_1, region_2]

    return f'Bucket {bucket.name} successfully created.'

## Invoke Function
print(create_bucket('yellow_demo_storage_bucket', 'STANDARD', 'us-central1'))
