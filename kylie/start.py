# Psycho_Bots
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text("""
    Hi\nI am Kylie Simple Youtube to Mp3 Downloader Bot\nI can Download Any Music with best quality👀 Just send me name or Link with using command of `/song`</b>\nExample:/song Can we kiss Forever\n\n C R E A T O R: @Psycho_Bots
    """, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌴 Support", url="https://t.me/PsychoBots_chat"), 
                    InlineKeyboardButton("Updates Channel📡", url="https://t.me/Psycho_Bots"),
                ],
                [
                    InlineKeyboardButton('Go Inline🐬', switch_inline_query_current_chat='')
                 ]
          ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text("Hey...👀\nDownloas Songs From Me🌴 use command of `/song <song name/link>\n\nI am Created By @Psycho_Bots\n", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ Support⚡", url="https://t.me/PsychoBots_chat"),
                    InlineKeyboardButton('Go Inline🐬', switch_inline_query_current_chat='')
                 ]
          ]
        ),
     )


