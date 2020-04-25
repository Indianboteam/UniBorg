# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import asyncio
import html
import logging

from telethon import events, utils
from telethon.errors.rpcerrorlist import MessageTooLongError
from telethon.events import NewMessage
from telethon.tl import types

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

def split_message(text, length=4096, offset=200):
    return [text[text.find('\n', i - offset, i + 1) if text.find('\n', i - offset, i + 1) != -1 else i:
                 text.find('\n', i + length - offset, i + length) if text.find('\n', i + length - offset,
                                                                               i + length) != -1 else i + length] for
            i
            in
            range(0, len(text), length)]

def get_who_string(who):
    who_string = html.escape(utils.get_display_name(who))
    if isinstance(who, (types.User, types.Channel)) and who.username:
        who_string += f" <i>(@{who.username})</i>"
    who_string += f", <a href='tg://user?id={who.id}'>#{who.id}</a>"
    return who_string


@borg.on(events.NewMessage(pattern=r"\.who", outgoing=True)) # pylint:disable=E0602
async def _(event):
    if not event.message.is_reply:
        who = await event.get_chat()
    else:
        msg = await event.message.get_reply_message()
        if msg.forward:
          	# FIXME forward privacy memes
            who = await borg.get_entity(
                msg.forward.from_id or msg.forward.channel_id)
        else:
            who = await msg.get_sender()

    await event.edit(get_who_string(who), parse_mode='html')


@borg.on(events.NewMessage(pattern=r"\.members", outgoing=True)) # pylint:disable=E0602
async def _(event):
    members = []
    async for member in borg.iter_participants(event.chat_id):
        messages = await borg.get_messages(
            event.chat_id,
            from_user=member,
            limit=0
        )
        if not member.deleted and not member.bot:
            print(member)
            members.append((
                messages.total,
                f"{messages.total} - {get_who_string(member)}\n"
            ))
    members = (
        m[1] for m in sorted(members, key=lambda m: m[0], reverse=True)
    )
    members = "".join(members)
    try:
        await event.reply(members, parse_mode='html')
    except MessageTooLongError:
        # print("too message")
        for m in split_message(members):
            # print(m)
            await asyncio.sleep(2)
            await event.reply(f"{m}", parse_mode="html")
    del members
