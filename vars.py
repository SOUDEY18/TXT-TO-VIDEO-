# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "11039752"))
API_HASH = environ.get("API_HASH", "c4141ad06d1f37b105841412c1aeb383")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
