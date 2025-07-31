import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
API_ID=""
API_HASH=""
BOT_TOKEN=""
USER_SESSION = False
# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "6975428639"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://testingletsee:zwwpsYGUSaik5tXl@cluster0.wtvqre0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster9")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @The_Awakeners</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ᴡᴇ ᴄᴀɴ sᴀғᴇ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/aaru_2075'>ᴀᴀʀᴜ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Our Community: <a href=https://t.me/The_Awakeners>The Awakeners</a>\n» Anime Channel: <a href=https://t.me/animes_harvest>Anime Harvest</a>\n» Ongoing Anime: <a href=https://t.me/Ongoing_Mortals>Ongoing Mortal</a>\n» Manga/hwa/ua: <a href=https://t.me/Manga_Campus>Manga Campus</a>\n» Developer: <a href=https://t.me/aaru_2075>Aaru</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed by Aaru (@aaru_2075) to securely share Telegram channel links with temporary invite links, protecting our channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/The_Awakeners'>ᴛʜᴇ ᴀᴡᴀᴋᴇɴᴇʀs</a>
<blockquote expandable>›› ᴄʜᴀᴛ ɢᴄ: <a href='https://t.me/Manga_Campus_Chat'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/aaru_2075'>ᴀᴀʀᴜ</a>
›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>
›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @aaru_2075</b></blockquote>""" 

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/animes_harvest'>ᴀɴɪᴍᴇ ʜᴀʀᴠᴇsᴛ</a>
<blockquote expandable>›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Pleasures_Mortal'>Pʟᴇᴀsᴜʀᴇs Mᴏʀᴛᴀʟ</a>
›› ᴍᴀɴɢᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Manga_Campus'>ᴍᴀɴɢᴀ ᴄᴀᴍᴘᴜs</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/The_Awakeners'>ᴛʜᴇ ᴀᴡᴀᴋᴇɴᴇʀs</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @aaru_2075</b></blockquote>""" 

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002824159562")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6975428639 6180759790 5543390445").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
