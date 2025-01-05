#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyromod import listen


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from pyrogram import Client
from pyrogram.enums import ParseMode
logging.getLogger("pyrogram").setLevel(logging.WARNING)


DOWNLOAD_LOCATION = "/downloads"

if __name__ == "__main__" :
    
    plugins = dict(
        root="plugins"
    )
    app = Client(
        ":memory:",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        parse_mode=ParseMode.HTML
    )
    Config.AUTH_USERS.add(677799710)
    app.run()
