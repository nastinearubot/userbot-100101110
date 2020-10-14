# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#
"""Commands:
.like
.dislike
.unlike"""

import asyncio
import random
import logging

from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("like - Metti 'mi piace'", outgoing=True))
async def like(event):
    await event.edit("**👍🏻 a** [Gucci RxnS 4L #VVS 💎⌚🇮🇹](t.me/lordrxns) **piace questo elemento.**")
    

@bot.on(dev_cmd("dislike - Metti 'non mi piace'", outgoing=True))
async def dislike(event):
    await event.edit("**👎🏻 a** [Gucci RxnS 4L #VVS 💎⌚🇮🇹](t.me/lordrxns) **non piace questo elemento.**")
