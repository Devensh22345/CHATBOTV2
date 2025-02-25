from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "22207976"
API_HASH = "5c0ad7c48a86afac87630ba28b42560d"
BOT_TOKEN = getenv("BOT_TOKEN", "7906614768:AAEyisvIdXRsGDIztS1XM16xRhsB-YTXvis")
STRING1 = getenv("STRING_SESSION", "BQFBTREAxBhvgRel56TTetaFC3NWAGS8hBfFbN_JkmO13PwRaQ2bf-ONfgSGtig44tGVJOxM1mzZbZD6A_3PT44j-tVhGklu2OiJFPdiAZ_kYThjJuXiWCgC6RF264N6XOfudHmq__53tBn3mG9eE9V7TYowk2I3ueGYdECD7oMfDq-DGhkH0zq5PLRpVcWqqV_GEPtP5Wy_JS8RCqllv_GLbNf8k4uNd8Ro6v42Kj5nDvNMVarm5L71Hi9Vn7vgTVBjur3t9xyJybupJkWPIKVE3tC2RDj2tUV53wp8vjzwm8paBEa9m9Wiy_pxdJi-mwXIkvvnugNdC_Dbygc1pHIrulhJDgAAAAGSmGh2AA")
MONGO_URL = getenv("MONGO_URL", mongodb+srv://Chatbot:Chatbot@cluster0.xtdto.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
OWNER_ID = int(getenv("OWNER_ID", "6872968794"))
SUPPORT_GRP = "alya_bots"
UPDATE_CHNL = "alya_bots"
OWNER_USERNAME = "mai_hu_kira"
