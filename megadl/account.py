# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from mega import Mega
from pyrogram import Client
from pyrogram.types import Message

from config import Config, LOGIN_ERROR_TEXT, ERROR_TEXT, LOGGED_AS_USER

# Mega user account credentials
email = Config.MEGA_EMAIL
password = Config.MEGA_PASSWORD

mega = Mega()

m = None
# Mega Account Login
def login_to_mega():
  global m
  try:
    if email and password is not None:
      # Login as Mega user account
      m = mega.login(email, password)
      print(LOGGED_AS_USER)
    else:
      print(LOGIN_ERROR_TEXT)
      # Login as anonymous account
      m = mega.login()
  except:
    print(ERROR_TEXT)
    exit()
