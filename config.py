import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nI am Kylie Simple Youtube to Mp3 Downloader Bot\nI can Download Any Music with best quality👀 Just send me name or Link with using command of `/song`</b>\nExample:/song Can we kiss Forever\n\n C R E A T O R: @Psycho_Bots")
    START_IMG = os.environ.get("START_IMG", "")
    OWNER = os.environ.get("OWNER", "Alone_loverboy") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
# Builder Pack of FFMPEG: https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest
