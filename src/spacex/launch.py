from collections import defaultdict
from datetime import datetime

import requests
from constants import BUCKET
from helpers import write_blob


def get_launches(launches_api, latest=None):
    if latest:
        launches_api = f"{launches_api}/latest"

    launches_response = requests.get(launches_api)
    current_date = datetime.today().strftime("%Y-%m-%d")
    write_blob(launches_response.json(), BUCKET, f"raw/launches_{current_date}.json")

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
    write_blob(launches, BUCKET, f"clean/launches_{current_date}.json")
