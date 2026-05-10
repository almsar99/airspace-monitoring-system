import os

from dotenv import load_dotenv

load_dotenv()

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

OPENSKY_URL = "https://opensky-network.org/api/states/all"

USER_AGENT = os.getenv(
    "USER_AGENT",
    "airspace-monitoring-system",
)

LOG_FILE = os.getenv(
    "LOG_FILE",
    "logs/app.log",
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO",
)
