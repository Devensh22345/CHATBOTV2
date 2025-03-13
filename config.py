from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "22207976"
API_HASH = "5c0ad7c48a86afac87630ba28b42560d"
BOT_TOKEN = getenv("BOT_TOKEN", "6963634345:AAFJM2HxC9kkaFB6YcxXNDAEZba5IGZSq1c")
STRING1 = getenv("STRING_SESSION",None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Test:Test@cluster0.pcpx5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "6872968794"))
SUPPORT_GRP = "alya_bots"
UPDATE_CHNL = "alya_bots"
OWNER_USERNAME = "mai_hu_kira"
