# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 2294033))
    API_HASH = os.environ.get("API_HASH", "6a8fba10d5e2747b3c101c03d2d22752")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1948020257:AAGYFIg1kdt6BTsTyvsZdWQ861VTq-AsdCo")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1340254734").split())
    DOWNLOAD_LOCATION = "./NexaBots"
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "True")
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "tg.nexabots@gmail.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "hirusha2006")


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

Log: {}

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
