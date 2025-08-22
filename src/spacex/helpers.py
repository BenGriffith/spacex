import json

from constants import PROJECT_ID
from google.cloud import storage


def write_blob(data, bucket_name, destination_blob_name):
    client = storage.Client(project=PROJECT_ID)

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(
        data=json.dumps(data, indent=2), content_type="application/json"
    )
