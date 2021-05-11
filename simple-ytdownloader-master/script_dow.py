

from pytube import YouTube
from pathlib import Path

import os.path
BASE_DIR = Path(__file__).resolve().parent.parent
link = input("Вставьте ссылку на видео:  ")
try:

    myVideoStream = YouTube(link).streams
except:
    print("ссылку не правильно  Error")


videostream = myVideoStream.filter(type = "video")

if os.path.exists("videos") == True :
    pass
else:
    os.mkdir("videos")

try:
    videostream.first().download("videos/")
except:
    print("не смогу загрузить видео")
