#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# Logging configuration
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# OS and pyromod imports
import os
from pyromod import listen

# Import configuration
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from pyrogram import Client
from pyrogram.enums import ParseMode

# Suppress pyrogram logging
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Set download location
DOWNLOAD_LOCATION = "/downloads"

if __name__ == "__main__":
    # Define plugins folder
    plugins = dict(
        root="plugins"
    )

    # Initialize the bot
    app = Client(
        ":memory:",  # Use a persistent session name if needed, e.g., "my_bot"
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        parse_mode=ParseMode.HTML
    )

    # Ensure AUTH_USERS is a set
    if not hasattr(Config, "AUTH_USERS"):
        Config.AUTH_USERS = set()
    Config.AUTH_USERS.add(677799710)

    # Run the bot
    app.run()
