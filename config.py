from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "22207976"
API_HASH = "5c0ad7c48a86afac87630ba28b42560d"
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6872968794"))
SUPPORT_GRP = "alya_bots"
UPDATE_CHNL = "alya_bots"
OWNER_USERNAME = "mai_hu_kira"
