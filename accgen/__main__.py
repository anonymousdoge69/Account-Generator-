from accgen import bot, TOKEN
import sys
from telethon import events, Button, functions

try:
  bot.start(bot_token=TOKEN)
except:
  sys.exit(1)

@bot.on(events.NewMessage(pattern="^[?!/]start$", func=lambda e: e.is_private))
async def start_msg(e):
 try:
  p = await bot(functions.channels.GetParticipantRequest(e.chat_id, e.sender_id))
  p = True
 except:
  p = False
 start_cmd = "**🔥Hey Pro, Welcome To Accounts Generator Bot🔥**\nClick /cmds to Know more"
 if not p:
  start_cmd += "\n\nTo use the Bot You Have to join **[Piro Giveaways]**(https://t.me/Piro_giveaways)"
 await e.respond(start_cmd, buttons=Button.url("Join Channel", "https://t.me/Piro_giveaways") if not p else None)



@bot.run_until_disconnected()
