import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7576249578:AAE9BZJww9fCNifNMRCwETRwE2TV8wJnOqQ")

    APP_ID = int(os.environ.get("APP_ID", 20400973))

    API_HASH = os.environ.get("API_HASH", "047838cb76d54bc445e155a7cab44664")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5677517133 5329179170").split())
  
    PORT = "8080"
