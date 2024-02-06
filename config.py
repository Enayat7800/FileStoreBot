import os

API_ID = int(os.environ.get("28150346", 0))
API_HASH = os.environ.get("426f0d0a1da02dea8fb71cb0bd3ab7e1", None)
BOT_TOKEN = os.environ.get("6611439999:AAEDykIF7TG7aaRXLSwDXIqhvBm1Z6XEN74", None)
DB_CHANNEL_ID = os.environ.get("-1001819528169")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("1251962299"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
