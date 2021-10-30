from telethon import TelegramClient
from os import getenv

API_KEY = int(getenv("API_KEY"))
API_HASH = getenv("API_HASH")
TOKEN = getenv("TOKEN")
FJOIN_CHAT_ID = int(getenv("FJOIN_CHAT_ID"))
SUDO = list({int(x) for x in getenv("SUDO").split()}) if getenv("SUDO") else []

bot = TelegramClient (None, API_KEY, API_HASH)

