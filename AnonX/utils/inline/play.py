import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from AnonX import app

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 3 <= anon < 4:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 4 <= anon < 5:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 6 <= anon < 7:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 7 <= anon < 8:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 9 <= anon < 10:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 11 <= anon < 12:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 12 <= anon < 13:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 13 < anon < 14:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 14 <= anon < 15:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 15 <= anon < 16:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 16 <= anon < 17:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 17 <= anon < 18:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 18 <= anon < 19:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 19 <= anon < 20:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 20 <= anon < 21:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 21 <= anon < 22:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 22 <= anon < 23:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 23 <= anon < 24:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 24 <= anon < 25:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 25 <= anon < 26:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 26 <= anon < 27:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 27 <= anon < 28:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 28 <= anon < 29:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 29 <= anon < 30:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 30 <= anon < 31:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 31 <= anon < 32:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 32 <= anon < 33:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 33 <= anon < 34:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 34 <= anon < 35:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 35 <= anon < 36:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 36 <= anon < 37:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 37 <= anon < 38:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 38 <= anon < 39:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 39 <= anon < 40:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 40 <= anon < 41:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 41 <= anon < 42:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 42 <= anon < 43:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 43 <= anon < 44:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 44 < anon < 45:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 45 <= anon < 46:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 46 <= anon < 47:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 47 <= anon < 48:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 48 <= anon < 49:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 49 <= anon < 50:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 50 <= anon < 51:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 51 <= anon < 52:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 52 <= anon < 53:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 53 <= anon < 54:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 54 <= anon < 55:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 55 <= anon < 56:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 56 <= anon < 57:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 57 <= anon < 58:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 58 <= anon < 59:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 59 <= anon < 60:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀ғɪᴅᴀᴀ🥀 "
    elif 61 <= anon < 62:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 62 <= anon < 63:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 63 <= anon < 64:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 64 <= anon < 65:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 65 <= anon < 66:
        bar = " 🥀ғɪᴅᴀᴀ🥀 "
    elif 66 <= anon < 67:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 67 <= anon < 68:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 68 <= anon < 69:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 69 <= anon < 70:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 70 <= anon < 71:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 71 <= anon < 72:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 72 <= anon < 73:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 73 <= anon < 74:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 74 <= anon < 75:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 75 <= anon < 76:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 76 < anon < 77:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 77 <= anon < 78:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 78 <= anon < 79:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 79 <= anon < 80:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 80 <= anon < 81:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 81 <= anon < 82:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 82 <= anon < 83:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 83 <= anon < 84:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 84 <= anon < 85:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 85 <= anon < 86:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 86 <= anon < 87:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 87 <= anon < 88:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 88 <= anon < 89:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 89 <= anon < 90:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 90 <= anon < 91:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 91 <= anon < 92:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 92 <= anon < 93:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 93 <= anon < 94:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 94 <= anon < 95:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 95 <= anon < 96:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 96 <= anon < 97:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 97 <= anon < 98:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 98 <= anon < 99:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    else:
        bar = " 🍷ѕσ ¢ιтє ѕσηg🍷 "
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 3 <= anon < 4:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 4 <= anon < 5:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 6 <= anon < 7:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 7 <= anon < 8:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 9 <= anon < 10:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 11 <= anon < 12:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 12 <= anon < 13:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 13 < anon < 14:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 14 <= anon < 15:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 15 <= anon < 16:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 16 <= anon < 17:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 17 <= anon < 18:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 18 <= anon < 19:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 19 <= anon < 20:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 20 <= anon < 21:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 21 <= anon < 22:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 22 <= anon < 23:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 23 <= anon < 24:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 24 <= anon < 25:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 25 <= anon < 26:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 26 <= anon < 27:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 27 <= anon < 28:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 28 <= anon < 29:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 29 <= anon < 30:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 30 <= anon < 31:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 31 <= anon < 32:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 32 <= anon < 33:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 33 <= anon < 34:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 34 <= anon < 35:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 35 <= anon < 36:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 36 <= anon < 37:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 37 <= anon < 38:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 38 <= anon < 39:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 39 <= anon < 40:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 40 <= anon < 41:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 41 <= anon < 42:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 42 <= anon < 43:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 43 <= anon < 44:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 44 < anon < 45:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 45 <= anon < 46:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 46 <= anon < 47:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 47 <= anon < 48:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 48 <= anon < 49:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 49 <= anon < 50:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 50 <= anon < 51:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 51 <= anon < 52:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 52 <= anon < 53:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 53 <= anon < 54:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 54 <= anon < 55:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 55 <= anon < 56:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 56 <= anon < 57:
        bar = " 🔥ᴘᴏɪsᴏɴ🔥 "
    elif 57 <= anon < 58:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    elif 58 <= anon < 59:
        bar = " 💥ᴘᴏɪsᴏɴ💥 "
    elif 59 <= anon < 60:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀ғɪᴅᴀᴀ🥀 "
    elif 61 <= anon < 62:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 62 <= anon < 63:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 63 <= anon < 64:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 64 <= anon < 65:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 65 <= anon < 66:
        bar = " 🥀ғɪᴅᴀᴀ🥀 "
    elif 66 <= anon < 67:
        bar = " 💥ғɪᴅᴀᴀ💥 "
    elif 67 <= anon < 68:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 68 <= anon < 69:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 69 <= anon < 70:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 70 <= anon < 71:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 71 <= anon < 72:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 72 <= anon < 73:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 73 <= anon < 74:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 74 <= anon < 75:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 75 <= anon < 76:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 76 < anon < 77:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 77 <= anon < 78:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 78 <= anon < 79:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 79 <= anon < 80:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 80 <= anon < 81:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 81 <= anon < 82:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 82 <= anon < 83:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 83 <= anon < 84:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 84 <= anon < 85:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 85 <= anon < 86:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 86 <= anon < 87:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 87 <= anon < 88:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 88 <= anon < 89:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 89 <= anon < 90:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 90 <= anon < 91:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 91 <= anon < 92:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 92 <= anon < 93:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 93 <= anon < 94:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 94 <= anon < 95:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 95 <= anon < 96:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 96 <= anon < 97:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 97 <= anon < 98:
        bar = " 🔥ғɪᴅᴀᴀ🔥 "
    elif 98 <= anon < 99:
        bar = " 🥀ᴘᴏɪsᴏɴ🥀 "
    else:
        bar = " 🍷ℓσνєℓу ѕσηg🍷 "

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [  
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons
