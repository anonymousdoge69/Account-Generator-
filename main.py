from telethon import TelegramClient
from telethon import events, functions
from telethon import Button
from os import getenv
import asyncio
import random

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
TOKEN = getenv("TOKEN")
ADMIN_ID = int(getenv("ADMIN"))
combos = open("combos.txt", "r").read().split("\n")
used_list = []
used_users = []

bot = TelegramClient("Bot", API_ID, API_HASH)
bot.start(bot_token=TOKEN)
loop = asyncio.get_event_loop()

async def remove_user(uid):
    global used_users
    await asyncio.sleep(3600*24)
    if uid in used_users:
        used_users.remove(uid)

@bot.on(events.NewMessage(pattern="^[?!/]start$"))
async def start_msg(e):
    try:
        p = await bot(functions.channels.GetParticipantRequest(e.chat_id, e.sender_id))
        p = True
    except:
        p = False
    start_cmd = "**🔥Hey Pro, Welcome To Accounts Generator Bot🔥**\nClick /gen to generate account."
    if not p:
        start_cmd += "\n\nTo use the Bot You Have to join **[Piro Giveaways]**(https://t.me/Piro_giveaways)"
    await e.respond(start_cmd, buttons=Button.url("Join Channel", "https://t.me/Piro_giveaways") if not p else None)

@bot.on(events.NewMessage(pattern="^[?!/]gen$"))
async def gen_account(e):
    try:
        await bot(functions.channels.GetParticipantRequest(e.chat_id, e.sender_id))
    except:
        return await e.respond("**You Have to join [Piro Giveaways](https://t.me/Piro_giveaways)**")
    if e.sender_id in used_users and e.sender_id == ADMIN_ID:
        return await e.respond("**You have already used your account today.**")
    msg = await e.respond("**Generating Account...**")
    ok = False
    retry_count = 0
    while not ok:
        retry_count += 1
        if retry_count > 100:
            return await msg.edit("**Failed To Generate Account.**")
        combo = combos[random.randint(0, len(combos) - 1)]
        if not combo in used_list:
            used_list.append(combo)
            loop.create_task(remove_user(e.sender_id))
            ok = True
    text = "**Account Generated Successfully**\n\nLogin: {}".format(combo)
    await msg.edit(text, buttons=Button.url("Channel", "https://t.me/Piro_giveaways"))


bot.run_until_disconnected()