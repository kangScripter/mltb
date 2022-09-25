import time
import requests
from subprocess import run
from telegram import ParseMode
import cloudscraper
from threading import Thread
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler
from urllib.parse import urlparse
from telegram import message
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot import LOGGER, dispatcher, bot
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage
from cfscrape import create_scraper

SHORTENER = "urlshortx.com"
SHORTENER_API = "8fabf1c36bcaf7fb959b360ac8574f39815ae901"

def xp(message, bot):
     args = message.text.split(" ", maxsplit=1)
     reply_to = message.reply_to_message
     if len(args) > 1:
         link = args[1]
     elif reply_to is not None:
          link = reply_to.text
     else:
          link = ''
     cget = create_scraper().get
     xpurl = cget(f'https://{SHORTENER}/api?api={SHORTENER_API}&url={link}&format=text').text
     reply = f"*xpshort-Jack*\n<code>{xpurl}</code>\n"
     LOGGER.info(f"Generated link: {xpurl}")
     return sendMessage(reply, context.bot, update.message)


def xplink(update, context):
    _xp(update.message, context.bot)

xp_handler = CommandHandler(BotCommands.XpCommand, xplink, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(xp_handler)
