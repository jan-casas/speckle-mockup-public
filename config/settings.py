import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Local Database credentials
PG_USER = os.environ.get('PG_USER')
PG_PASS = os.environ.get('PG_PASS')
PG_HOST = os.environ.get('PG_HOST')
PG_PORT = os.environ.get('PG_PORT')
PG_DATABASE = os.environ.get('PG_DATABASE')

# Azure Database credentials
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_DATABASE")
port = os.environ.get("DB_PORT")

# Mapbox credentials
MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')
MAPBOX_MAP_STYLE = os.environ.get('MAPBOX_MAP_STYLE')
access_token_mapbox = os.environ.get("ACCESS_TOKEN_MAPBOX")
style_token_mapbox = os.environ.get("STYLE_TOKEN_MAPBOX")

# API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("IQAIR_WEATHER_API")

MAPBOX_API = os.getenv("MAPBOX_API")

# Hughingface API
HUGGINGFACE_MAIL = os.getenv("HUGGINGFACE_API")
HUGGINGFACE_PASSWORD = os.getenv("HUGGINGFACE_PASSWORD")
