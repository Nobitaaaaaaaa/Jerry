import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/19a3795338160236661b0.jpg",
        caption=f"""**ᴛʜɪꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪꜱ ᴀᴅᴠᴀɴᴄᴇ ᴀɴᴅ ɴᴏ ʟᴀɢ ᴜꜱᴇ ɪᴛ ᴄᴏɴᴛɪɴᴜᴏᴜꜱʟʏ .

ᴄᴏᴅᴇʀ :- [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/always_worng_45)


ɪꜰ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛᴇʟʟ ʜᴇʀᴇ = [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/always_worng_45)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕 ᴄʟᴜꜱᴛᴇʀ 💫", url=f"https://t.me/Nobitamusicxd_bot?startgroup=true")
                ]
                
           ]
        ),
    )
    

