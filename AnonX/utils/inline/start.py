from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ ᴍᴏɪ ᴊᴀᴀɴ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ʜᴀᴠᴇʟɪ ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐞𝐥𝐩 🎭",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🕹️ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 🕹️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ ᴍᴏɪ ᴊᴀᴀɴ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ʜᴀᴠᴇʟɪ  ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🚩𝐎𝐰𝐧𝐞𝐫🚩", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="🎭 𝐇𝐞𝐥𝐩 🎭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🫰𝐆𝐫𝐨𝐮𝐩🫰", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🏠𝐎𝐟𝐟𝐢𝐜𝐞🏠", url=f"https://t.me/VIP_CREATORS",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʀᴇᴘᴏ",
                url=f"https://telegra.ph//file/9a342972a6b78db65123b.jpg",
            )
        ],
     ]
    return buttons
