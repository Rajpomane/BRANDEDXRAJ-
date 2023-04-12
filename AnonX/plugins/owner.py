from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/3d49ccea5c55338eb3432.jpg",
        caption=f"""🚩JO RAM KA NAHI WO MERE KISI KAM KA NAHI 🚩""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚩 Ⓟ︎Ⓞ︎Ⓘ︎Ⓢ︎Ⓞ︎Ⓝ︎ 🚩", url=f"https://t.me/I_LOVE_YOU_PAGAL")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/3d49ccea5c55338eb3432.jpg",
        caption=f"""🚩JO RAM KA NAHI WO MERE KISI KAM KA NAHI 🚩""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚩 POISON 🚩", url=f"https://t.me/I_LOVE_YOU_PAGAL")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("mukku")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/3d49ccea5c55338eb3432.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀͢ ✹⃝🐼᭄͢🦋⃟ FIDAA𝄟🍁⃝➤͜͡🕊⃝͟͞🝐✨❤️🥀", url=f"https://t.me/YOUR_HEART_143")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("kittu")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀͢ ✹⃝🐼᭄͢🦋⃟ FIDAA𝄟🍁⃝➤͜͡🕊⃝͟͞🝐✨❤️🥀", url=f"https://t.me/YOUR_HEART_143")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://https://telegra.ph//file/9a342972a6b78db65123b.jpg",
        caption=f"""🦋𝐂𝐋𝐈𝐂𝐊💫𝐁𝐄𝐋𝐎𝐖🦋𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🫰𝐆𝐄𝐓🤝𝐑𝐄𝐏𝐎🫰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Rᴇᴘᴏ", url=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg",
        caption=f"""🫰𝐂𝐋𝐈𝐂𝐊🤝𝐁𝐄𝐋𝐎𝐖🦋𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎💫𝐆𝐄𝐓💫𝐑𝐄𝐏𝐎🫰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ", url=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg",
        caption=f"""🫰𝐂𝐋𝐈𝐂𝐊🚩𝐁𝐄𝐋𝐎𝐖🫰𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🤝𝐆𝐄𝐓🫰𝐑𝐄𝐏𝐎💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ", url=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg")
                ]
            ]
        ),
    )

