#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from pytube import YouTube
from pathlib import Path

import os
#Получаем ссылку на видео
link = input("Вставьте ссылку на видео:  ")
try:

    yt = YouTube(link)
    #streams = yt.streams
    #print(dir(yt))
except:
    print("ссылку не правильно  Error")

#mp4files = yt.filter('mp4')
#mp4files = streams.filter(res='480p').desc().first()
#yt.get_videos()
print(yt.streams.filter(progressive=True, file_extension='mp4'))
#video = yt.get('mp4', '720p')
BASE_DIR = Path(__file__).resolve().parent.parent
#yt.set_filename('douwnload Video')

#Выводим информацию о видео
print("Название: ",yt.title)
print("Просмотры: ",yt.views)
print("Продолжительность: ",yt.length, "сек\n")
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    SAVE_PATH=BASE_DIR/'test'
    print('SAVE_PATH=',SAVE_PATH)
    video.download(SAVE_PATH)
    print("Загрузка завершена")
except:
    print("не смогу загрузить видео")

#Выбираем поток с максимальным разрешением
#ys = yt.streams.get_highest_resolution()

#Загрузка
#print("Видео загружается...")
#os.mkdir("test")
#os.path.join('Rest project 1', 'districts.json')
#ys.download('/home/daniilshat/Загрузки/')
#ys.download('/test/')
#print("Загрузка завершена")
