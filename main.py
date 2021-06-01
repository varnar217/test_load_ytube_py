#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from pytube import YouTube
from pathlib import Path
from mhyt import yt_download

import os
#Получаем ссылку на видео
link = input("Вставьте ссылку на видео:  ")
try:

    yt_download(link,"test\download.mp4")

except:
    print("ссылку не правильно  Error")
