"""Get anysong u like
\nJust type .song (song name)
"""
from telethon import events
import subprocess, instantmusic
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from uniborg.util import admin_cmd
import glob
import os
 
os.system("rm -rf *.mp3")

def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

@borg.on(admin_cmd(pattern="song ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("`Ok finding the Song`")    
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Sending Song`")
    await event.delete()
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
