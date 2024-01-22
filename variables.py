import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")


RemoveBG_API = os.environ.get("RemoveBG_API", "MJMoiiatXPHcHgFG3D1Wf2aG")



