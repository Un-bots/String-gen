import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐒𝐭𝐫𝐢𝐧𝐠 𝐁𝐨𝐭...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 𝐒𝐔𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘. 𝐌𝐀𝐃𝐄 𝐁𝐘 @un-bots")
    idle()
    app.stop()
    print("𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗!")
