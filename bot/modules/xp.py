import time
import requests
from subprocess import run
from telegram import ParseMode
import cloudscraper
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler
from urllib.parse import urlparse
from telegram import message
from bot.modules.clone import _clone
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot import LOGGER, dispatcher, bot
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException
from bot.helper.mirror_utils.download_utils.direct_link_generator import direct_link_generator
from bot.helper.ext_utils.bot_utils import is_gp_link, is_rock_link, is_gdtot_link
from cfscrape import create_scraper

SHORTENER = "urlshortx.com"
SHORTENER_API = "8fabf1c36bcaf7fb959b360ac8574f39815ae901"

def gplink(update, context):
     args = update.message.text.split(" ", maxsplit=1)
     reply_to = update.message.reply_to_message
     if len(args) > 1:
         link = args[1]
     elif reply_to is not None:
          link = reply_to.text
     else:
          link = ''
     if is_gp_link(link):
          link = direct_link_generator(link)
          reply = f"*gplink_bypassed-Jack*\n<code>{link}</code>\n"
          LOGGER.info(f"Generated link: {link}")
          return sendMessage(reply, context.bot, update.message)


XP_HANDLER = CommandHandler(BotCommands.xpCommand, xplink, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(XP_HANDLER)
