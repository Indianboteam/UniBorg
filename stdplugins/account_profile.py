"""Profile Updation Commands
.pbio <Bio>
.pname <Name>
.ppic"""
import logging
import os

from telethon.tl import functions

from sample_config import Config
from uniborg.util import admin_cmd, errors_handler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

@borg.on(admin_cmd(pattern="pbio (.*)"))  # pylint:disable=E0602
@errors_handler
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
@errors_handler
            about=bio
        ))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="pname ((.|\n)*)"))  # pylint:disable=E0602
@errors_handler,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
@errors_handler
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("My name was changed successfully")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@borg.on(admin_cmd(pattern="ppic"))  # pylint:disable=E0602
@errors_handler
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
@errors_handler
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
@errors_handler
    photo = None
    try:
        photo = await borg.download_media(  # pylint:disable=E0602
@errors_handler
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
@errors_handler
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to @Telegram ...")
            file = await borg.upload_file(photo)  # pylint:disable=E0602
@errors_handler
            try:
                await borg(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
@errors_handler
                    file
                ))
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
@errors_handler

@borg.on(admin_cmd(pattern="profilephoto (.*)"))  # pylint:disable=E0602
@errors_handler
async def _(event):
    """getting user profile photo last changed time"""
    if event.fwd_from:
        return
    
    p_number = event.pattern_match.group(1)
    print(p_number)
    chat = await event.get_chat()
    entity = await borg.get_entity(event.chat_id)
    try:
        a = await event.edit("getting profile pic changed or added date")
        photos = await borg.get_profile_photos(entity)
        print(photos[int(p_number)].date)
        msg = photos[int(p_number)].date
        msg = "Last profile photo changed: \n👉 `{}` UTC+3".format(str(msg))
        await a.edit(msg)
    except :
        pass
