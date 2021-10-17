from pyrogram import Client, filters, errors
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

import youtube_dl
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

OWNER="Alone_loverboy"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


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
 
@Client.on_message(filters.command(['song']))
def a(client, message):
    query=message.text
    print(query)
    m = message.reply('fetching datas from YT')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]
            performer = f"[Psycho_Bots]"
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**NOTHING Found!🥺')
            return
    except Exception as e:
        m.edit(
            "**found nothing try again\nwith /song <Song name/link>**"
        )
        print(str(e))
        return
    m.edit("**uploading...From Web😊**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Title:</b> <a href="{link}">{title}</a>\n⌚ <b>Duration:</b> <code>{duration}</code>\n📻 <b>Uploaded By:</b> <a href="https://t.me/kylieMusic_bot">Kylie Music🎷</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('**AN ERROR OCCURED REPORT THIS AT @PsychoBots_Chat !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Client.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Type a YouTube video name...",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out",
                switch_pm_parameter="",
            )
