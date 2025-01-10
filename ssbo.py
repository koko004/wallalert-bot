#!/usr/bin/python3.11

import requests
import time
import datetime
import telebot
from dbhelper import DBHelper, ChatSearch, Item
from re import sub
from decimal import Decimal
import logging
from logging.handlers import RotatingFileHandler
import sys
import threading
import os
import locale
from fake_useragent import UserAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to Docker console
        RotatingFileHandler("bot.log", maxBytes=5000000, backupCount=5)
    ]
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN", "Bot Token does not exist")

URL = "https://api.telegram.org/bot{}/".format(TOKEN)
URL_ITEMS = "https://api.wallapop.com/api/v3/general/search"
PROFILE = os.getenv("PROFILE")

if PROFILE is None:
    db = DBHelper()
else:
    db = DBHelper("db.sqlite")

logger.info("Bot is starting...")

ICON_VIDEO_GAMES = u'\U0001F3AE'  # 🎮
ICON_WARNING____ = u'\U000026A0'  # ⚠
ICON_HIGH_VOLTAG = u'\U000026A1'  # ⚡
ICON_COLLISION__ = u'\U0001F4A5'  # 💥
ICON_EXCLAMATION = u'\U00002757'  # ❗
ICON_DIRECT_HIT_ = u'\U0001F3AF'  # 🎯

def notel(chat_id, price, title, url_item, obs=None):
    # https://apps.timwhitlock.info/emoji/tables/unicode
    if obs is not None:
        text = ICON_DIRECT_HIT_ + f' {title} {price}€\n{url_item}\n{ICON_WARNING____} {obs}'
    else:
        text = ICON_DIRECT_HIT_ + f' {title} {price}€\n{url_item}'

    logger.info(f"Sending notification to chat_id {chat_id}: {title} - {price}€")
    send_message(chat_id, text)

def send_message(chat_id, text):
    url = URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    logger.info(f"Message sent to chat_id {chat_id}. Response status: {response.status_code}")

def main_loop():
    while True:
        logger.info("Starting new iteration of main loop...")
        # Your main logic here
        time.sleep(20)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user.")
