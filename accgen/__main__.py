from accgen import bot, TOKEN
import sys
from telethon import events

try:
  bot.start(bot_token=TOKEN)
except:
  sys.exit(1)

@bot.on(events.NewMessage(pattern="^[?!/]start$", func=lambda e: e.is_private))
async def start_msg(e):
 await e.reply("**🔥Hey Pro, Welcome To Accounts Generator Bot🔥**\nClick /cmds to Know more")

@bot.run_until_disconnected()
