import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7194020492").split()))

API_ID = int(os.getenv("API_ID", "25163976"))

API_HASH = os.getenv("API_HASH", "ee0375e95176805f45faf32bc054c247")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7817086838:AAHWvkRxy5YnJs7V7V7H8uex3x9Uzkep3Vk")

OWNER_ID = int(os.getenv("OWNER_ID", "7194020492"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002163862717").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://neoxr:neoxr123@cluster0.4cyrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002430921595"))
