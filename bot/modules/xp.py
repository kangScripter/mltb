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
from bot.helper.ext_utils.bot_utils import is_gdrive_link, new_thread
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot import dispatcher, LOGGER, STOP_DUPLICATE, download_dict, download_dict_lock, Interval
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, delete_all_messages, update_all_messages, sendStatusMessage, sendFile, sendMarkup
from cfscrape import create_scraper

SHORTENER = "urlshortx.com"
SHORTENER_API = "8fabf1c36bcaf7fb959b360ac8574f39815ae901"

def _xp(message, bot):
    args = message.text.split()
    reply_to = message.reply_to_message
    link = ''
    multi = 0
    if len(args) > 1:
        link = args[1].strip()
        if link.strip().isdigit():
            multi = int(link)
            link = ''
        elif message.from_user.username:
            tag = f"@{message.from_user.username}"
        else:
            tag = message.from_user.mention_html(message.from_user.first_name)
    if reply_to:
        if len(link) == 0:
            link = reply_to.text.split(maxsplit=1)[0].strip()
        if reply_to.from_user.username:
            tag = f"@{reply_to.from_user.username}"
        else:
            tag = reply_to.from_user.mention_html(reply_to.from_user.first_name)
        cget = create_scraper().get
        xpurl = cget(f'https://{SHORTENER}/api?api={SHORTENER_API}&url={link}&format=text').text
        reply = f"<b>xpshort-Jack</b>:<code>{xpurl}</code>\n"
        LOGGER.info(f"Generated link: {xpurl}")
        return sendMessage(reply, bot, message)
    if multi > 1:
        sleep(4)
        nextmsg = type('nextmsg', (object, ), {'chat_id': message.chat_id, 'message_id': message.reply_to_message.message_id + 1})
        cmsg = message.text.split()
        cmsg[1] = f"{multi - 1}"
        nextmsg = sendMessage(" ".join(cmsg), bot, nextmsg)
        nextmsg.from_user.id = message.from_user.id
        sleep(4)
        Thread(target=_xp, args=(nextmsg, bot)).start()
    else:
        sendMessage("give any link ", bot, message)
        
@new_thread
def xplink(update, context):
    _xp(update.message, context.bot)

xp_handler = CommandHandler(BotCommands.XpCommand, xplink, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(xp_handler)
