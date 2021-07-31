# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae
import os

from pyrogram import Client, idle
from config import Config, B_START_TEXT, MEGA_LOGIN_TEXT, START_TEXT
from megadl.account import login_to_mega

if __name__ == "__main__" :
    print(B_START_TEXT)
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="megadl")
    app = Client(
        "MegaBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    print(MEGA_LOGIN_TEXT)
    login_to_mega()
    app.start()
    print(START_TEXT)
    idle()
