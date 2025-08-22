from decouple import config

PROJECT_ID = config("PROJECT_ID")
BUCKET = config("BUCKET")
RAW_LAUNCHES = "raw/launches"
RAW_ROCKETS = "raw/rockets"
API = {
    "launches": "https://api.spacexdata.com/v5/launches",
    "rockets": "https://api.spacexdata.com/v4/rockets",
}
