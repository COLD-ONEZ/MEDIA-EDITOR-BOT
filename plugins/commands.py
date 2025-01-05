from pyrogram import filters, Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Hi {}
  
I am a Media Editor bot ...

You can edit/replace the documents, videos, GIFs, audios, photos, etc., of your channels easily by using me.**

`For more info on usage, hit ➟` /help 

"""

HELP_MSG = """
Follow the steps...

🌀 First, send me a media file that you need to edit/replace the other one.

🌀 Send the link of the media that will be replaced/edited.

NB: Both you and the bot must be admins in the target channel.

"""

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="OWNER", url="t.me/jack_of_tg")]]
        ),
        parse_mode=ParseMode.MARKDOWN
    )

@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=HELP_MSG,
        disable_web_page_preview=True
    )
