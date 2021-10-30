from accgen import bot, DB_URL
from telethon import events
from pymongo import MongoClient

db = MongoClient (DB_URL)
db = db["accgen"]


@bot.on(events.NewMessage(pattern="^[/?!]cmds$"))
async def cmds_help(e):
 print("#")

# ...
