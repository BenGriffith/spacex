import json
from collections import defaultdict

import requests
from google.cloud import storage


def write_blob(data, bucket_name, destination_blob_name):
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(
        data=json.dumps(data, indent=2), content_type="application/json"
    )


def get_launches(launches_api, latest=None):
    if latest:
        launches_api = f"{launches_api}/latest"

    launches_response = requests.get(launches_api)
    write_blob(launches_response, "spacex-data", "raw/launches.json")

    launches = defaultdict(dict)
    for launch in launches_response.json():
        id = launch.get("id")

        launches[id] = {
            "name": launch.get("name"),
            "date_utc": launch.get("date_utc"),
            "success": launch.get("success"),
            "rocket": launch.get("rocket"),
            "launchpad": launch.get("launchpad"),
            "payloads": launch.get("payloads"),
            "cores": launch.get("cores"),
            "upcoming": launch.get("upcoming"),
            "flight_number": launch.get("flight_number"),
            "image": launch["links"]["patch"]["small"],
            "webcast": launch["links"]["webcast"],
        }
    write_blob(launches, "spacex-data", "clean/launches.json")
