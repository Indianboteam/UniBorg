"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban REASON"""
import logging

from sample_config import Config
from uniborg.util import admin_cmd, errors_handler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)




@borg.on(admin_cmd(pattern="gban ?(.*)")) # pylint:disable=E0602
@errors_handler
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            "!gban [user](tg://user?id={}) {}".format(r.from_id, reason)
        )
    await event.delete()


@borg.on(admin_cmd(pattern="ungban ?(.*)")) # pylint:disable=E0602
@errors_handler
async def _(event):
    if Config.G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.G_BAN_LOGGER_GROUP,
            "!ungban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
