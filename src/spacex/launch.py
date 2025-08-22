from datetime import datetime

import constants
import requests
from helpers import write_blob


def invoke_api(api, prefix, current_date):
    response = requests.get(api)
    write_blob(response.json(), constants.BUCKET, f"{prefix}/{current_date}.json")


def get_spacex_data(latest=None):
    current_date = datetime.today().strftime("%Y-%m-%d")
    invoke_api(constants.API["launches"], constants.RAW_LAUNCHES, current_date)
    invoke_api(constants.API["rockets"], constants.RAW_ROCKETS, current_date)
