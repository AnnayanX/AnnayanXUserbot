from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("**🥀 𝐀𝐧𝐧𝐚𝐲𝐚𝐧𝐗 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐢𝐬 𝐀𝐥𝐢𝐯𝐞 ✨ ...**")



__NAME__ = "Alive"
__MENU__ = f"""
**🥀 Check Userbot Working
Or Not ..**

**Example:** `.alive`
"""
