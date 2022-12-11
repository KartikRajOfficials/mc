## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AQBzTNjy2V8dsN8HzfnipeX6sImschCKeVCY_ZwqjPkq017QxiSmwD911QT689NniKcqXMWraq4SjIdDEHOXEKJCp7UgeTLkt_q4x1T6-Lqhcf8nKwgcXXUIXVkEPYTKOPABX-yjnWfoC79xw-nxjW28FUqdx-3UWPZ2-ibg5nXeNI9BvIbyNdNFdi4kHu8v93uV5tgAd6sopbJSRRAZBVCwwZKUYIE_TCON1637cIkS24Yt1ShGZuqIqVBWhlkGV5YauiWZJxTmVARU-YN2zLMO-zs5BViHw4A8rHCXG-mQePxc01TjodV8LthQL6muGrflr0Z5pKwZfe-QFG0xAZYNAAAAAWTDLIWA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5879121142:AAGjOWt7TepgLm9vRhnDF0APr_UBxYznR8Q")
BOT_NAME = getenv("BOT_NAME", "Music_Bot")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://luci:luci@cluster0.kazau1i.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Kartik")
OWNER_USERNAME = getenv("OWNER_USERNAME", "KartikRajofficial")
ALIVE_NAME = getenv("ALIVE_NAME", "Rosy")
BOT_USERNAME = getenv("BOT_USERNAME", "Missrose_Musicbot")
OWNER_ID = getenv("OWNER_ID", "5589515550")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Rosy")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Global_chat_group_1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "loveandaffectionstatus")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5985506444").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/3fcd8a831dfecf80f20ac.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/884938536fbbdbcb72732.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KartikRajOfficials/mc/multi")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
