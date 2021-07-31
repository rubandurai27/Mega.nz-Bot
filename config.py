# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 123456))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "")
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "")

# Text Prints
B_START_TEXT = """
Starting Mega.nz-Bot! Please Wait...
"""

MEGA_LOGIN_TEXT = """
Trying Login Into Mega.nz
"""

LOGGED_AS_USER = """
Successfully Logged Into Mega.nz User Account
"""

LOGIN_ERROR_TEXT = """
Can't Get Mega Email and Password Login as an Anonymouse User
"""

ERROR_TEXT = """
 _____                     
| ____|_ __ _ __ ___  _ __ 
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |   
|_____|_|  |_|  \___/|_|  


Save the Log file and Send it to @Nexa_bots for Help :)
"""

START_TEXT="""
    _   __                   ____        __      
   / | / /__  _  ______ _   / __ )____  / /______
  /  |/ / _ \| |/_/ __ `/  / __  / __ \/ __/ ___/
 / /|  /  __/>  </ /_/ /  / /_/ / /_/ / /_(__  ) 
/_/ |_/\___/_/|_|\__,_/  /_____/\____/\__/____/ 


Bot is Running Now! Join @NexaBotsUpdates
"""
