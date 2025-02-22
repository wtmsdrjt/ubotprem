import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7194020492").split()))

API_ID = int(os.getenv("API_ID", "27547021"))

API_HASH = os.getenv("API_HASH", "3b45cddbde58f78fb4806973a297194b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8064562403:AAHoCTA3VJD9AayxepS2dLyQ4aB6Wo-B5G8")

OWNER_ID = int(os.getenv("OWNER_ID", "7194020492"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002163862717").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://user:user@cluster0.tdghzxc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002430921595"))
