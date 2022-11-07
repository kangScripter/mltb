from random import SystemRandom
from string import ascii_letters, digits
from telegram.ext import CommandHandler
from threading import Thread
from time import sleep

from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, delete_all_messages, update_all_messages, sendStatusMessage, sendFile, sendMarkup
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.mirror_utils.status_utils.clone_status import CloneStatus
from bot import dispatcher, LOGGER, STOP_DUPLICATE, download_dict, download_dict_lock, Interval
from bot.helper.ext_utils.bot_utils import is_gdrive_link, new_thread, is_gdtot_link, is_appdrive_link, is_gp_link, is_mdisk_link, is_dl_link, is_ouo_link, is_htp_link, is_rock_link, is_kolop_link, is_gt_link, is_psm_link, is_loan_link, is_ola_link, is_try2link_link, is_htpm_link
from bot.helper.mirror_utils.download_utils.direct_link_generator import gdtot, appdrive_dl, gplinks, mdisk, dlbypass, ouo, htp, rock, kolop_dl, gt, psm, loan, ola, try2link, htpm
from bot.helper.ext_utils.exceptions import DirectDownloadLinkException


def _clone(message, bot):
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
    is_psm = is_psm_link(link)
    if is_psm:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = psm(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"PSMlink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_ola = is_ola_link(link)
    if is_ola:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = ola(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"olalink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_htp = is_htp_link(link)
    if is_htp:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = htp(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"htplink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_htpm = is_htpm_link(link)
    if is_htpm:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = htpm(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"htplink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_gt = is_gt_link(link)
    if is_gt:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = gt(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"gtlink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_rock = is_rock_link(link)
    if is_rock:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = rock(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"rocklink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_gp = is_gp_link(link)
    if is_gp:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = gplinks(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"gplink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_ouo = is_ouo_link(link)
    if is_ouo:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = ouo(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"ouo_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_dl = is_dl_link(link)
    if is_dl:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = dlbypass(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"droplink_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_mdisk = is_mdisk_link(link)
    if is_mdisk:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = mdisk(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"mdisk_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_loan = is_loan_link(link)
    if is_loan:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = loan(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"link_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_try2link = is_try2link_link(link)
    if is_try2link:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = try2link(link)
            deleteMessage(bot, msg)
            msg = sendMessage(f"try2link_bypassed-Jack:<code>{link}</code>", bot, message) 
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_gdtot = is_gdtot_link(link)
    if is_gdtot:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = gdtot(link)
            deleteMessage(bot, msg)
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_appdrive = is_appdrive_link(link)
    if is_appdrive:
        try:
            msg = sendMessage(f"Processing:<code>{link}</code>", bot, message)
            link = appdrive_dl(link)
            deleteMessage(bot, msg)
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    is_kolop = is_kolop_link(link)
    if is_kolop:
        try:
            msg = sendMessage(f"Processing: <code>{link}</code>", bot, message)
            link = kolop_dl(link)
            deleteMessage(bot, msg)
        except DirectDownloadLinkException as e:
            deleteMessage(bot, msg)
            return sendMessage(str(e), bot, message)
    if is_gdrive_link(link):
        gd = GoogleDriveHelper()
        res, size, name, files = gd.helper(link)
        if res != "":
            return sendMessage(res, bot, message)
        if STOP_DUPLICATE:
            LOGGER.info('Checking File/Folder if already in Drive...')
            cap, f_name = gd.drive_list(name, True, True)
            if cap:
                cap = f"File/Folder is already available in Drive. Here are the search results:\n\n{cap}"
                sendFile(bot, message, f_name, cap)
                return
        if multi > 1:
            sleep(4)
            nextmsg = type('nextmsg', (object, ), {'chat_id': message.chat_id, 'message_id': message.reply_to_message.message_id + 1})
            cmsg = message.text.split()
            cmsg[1] = f"{multi - 1}"
            nextmsg = sendMessage(" ".join(cmsg), bot, nextmsg)
            nextmsg.from_user.id = message.from_user.id
            sleep(4)
            Thread(target=_clone, args=(nextmsg, bot)).start()
        if files <= 20:
            msg = sendMessage(f"Cloning: <code>{link}</code>", bot, message)
            result, button = gd.clone(link)
            deleteMessage(bot, msg)
        else:
            drive = GoogleDriveHelper(name)
            gid = ''.join(SystemRandom().choices(ascii_letters + digits, k=12))
            clone_status = CloneStatus(drive, size, message, gid)
            with download_dict_lock:
                download_dict[message.message_id] = clone_status
            sendStatusMessage(message, bot)
            result, button = drive.clone(link)
            with download_dict_lock:
                del download_dict[message.message_id]
                count = len(download_dict)
            try:
                if count == 0:
                    Interval[0].cancel()
                    del Interval[0]
                    delete_all_messages()
                else:
                    update_all_messages()
            except IndexError:
                pass
        cc = f'\n\n<b>cc: </b>{tag}'
        if button in ["cancelled", ""]:
            sendMessage(f"{tag} {result}", bot, message)
        else:
            sendMarkup(result + cc, bot, message, button)
            LOGGER.info(f'Cloning Done: {name}')
    else:
        sendMessage("Again clone the above link or invalid link", bot, message)

@new_thread
def cloneNode(update, context):
    _clone(update.message, context.bot)

clone_handler = CommandHandler(BotCommands.CloneCommand, cloneNode, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(clone_handler)
