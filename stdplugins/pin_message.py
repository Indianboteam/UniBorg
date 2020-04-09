"""Pins the replied message
Syntax: .cpin [LOUD]"""
import logging

from telethon.tl import functions

from uniborg.util import admin_cmd, errors_handler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


 
@borg.on(admin_cmd(pattern="cpin ?(.*)")) # pylint:disable=E0602
@errors_handler
async def _(event): 
    if event.fwd_from:
        return
    silent = True
    input_str = event.pattern_match.group(1)
    if input_str:
        silent = False
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await borg(functions.messages.UpdatePinnedMessageRequest(
                event.chat_id,
                message_id,
                silent
            ))
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.delete()
    else:
        await event.edit("Reply to a message to pin the message in this Channel.")
