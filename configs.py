import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28408609"))
  API_HASH = os.environ.get("API_HASH", "d6ddeafb0c189d91b8197ad49103e806")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8452718305:AAGfNMdJOm-1IqDr007ctJMNZZ-sS_cStH0")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sample_tests_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002563651230"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "arolinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "4574770a1b3e06b54b609f961e87efe837ea31cf")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "8134543713"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://teddugovardhan544_db_user:WVjIA96jQ31net0j@cluster0.kwkkleo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003094845380")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002563651230"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/lakki_reddy3)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/lakki_reddy3)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
