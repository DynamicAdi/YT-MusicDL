import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌴 Support", url="https://t.me/PsychoBots_chat"), 
                    InlineKeyboardButton("Updates Channel📡", url="https://t.me/Psycho_Bots"),
                ],
                [
                    InlineKeyboardButton('Go Inline🐬', switch_inline_query_current_chat='')
                 ]
          ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command('start') & filters.group)
async def start(client, message):
      await message.reply_text("Hey...👀\nDownloas Songs From Me🌴 use command of `/song <song name/link>\n\nI am Created By @Psycho_Bots\n", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ Support⚡", url="https://t.me/PsychoBots_chat"),
                    InlineKeyboardButton('Go Inline🐬', switch_inline_query_current_chat='')
                 ]
          ]
        ),
     )