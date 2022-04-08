import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from logi.events import register
from logi import telethn as tbot
from logi import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, SUPPORT_CHANNEL


PHOTO = "https://te.legra.ph/file/2fc8882813e32c8f90e08.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm  Robot.** \n\n"
    TEXT += "⚪ **I'm Working Properly** \n\n"
    TEXT += f"⚪ **My Master : [KING](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += f"⚪ **My Repo :** [GitHub](https://github.com/LOGI-TECH/LOGI-BOT) \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("Update", "https://t.me/{SUPPORT_CHANNEL}"),
            Button.url("Support", "https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
