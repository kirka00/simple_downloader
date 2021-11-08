from __future__ import unicode_literals
import youtube_dl
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from play import Player
import sqlite3
import datetime
from history_down import DB_down

'''
==Example==
Link:
https://youtu.be/w34ynodBgZI
Path:
D:/op
Чистка кэша:
youtube-dl --rm-cache-dir
'''
''' Окно загрузки '''
class DowloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('downloader.ui', self)
        self.setWindowTitle('Загрузчик')
        self.codec.addItems(  # кодеки
            ['aac', 'm4a', 'mp3', 'mp4', 'wav'])
        self.quality.addItems(['best', 'worst'])  # качество
        ''' Кнпоки '''
        self.down_btn.clicked.connect(self.downloader)  # загрузка
        self.play_btn.clicked.connect(self.player_view)  # медиаплеер
        self.history_downloads.triggered.connect(self.history_view)  # открыть нужный файл

    def history_view(self):
            self.DB = DB_down()
            self.DB.show()

    def player_view(self):
        self.player = Player()
        self.hide()
        self.player.show()

    def downloader(self):  # загрузчик
        self.answer.setText('')  # чистка
        quality = self.quality.currentText()  # качество
        codec = self.codec.currentText()  # кодек
        link = str(self.link.text())  # ссылка на видео
        path = '/'.join(self.path.text().strip().split('/')[:3]) + '/Downloads'

        if codec == 'm4a' or codec == 'aac' or codec == 'wav' or codec == 'mp3':  # аудиоЧформаты
            if quality == 'best':  # выборка нужного качества для аудио
                quality = 'bestaudio/best'
            else:
                quality = 'worstaudio/worst'
            ydl_opts = {  # опции загрузки для аудиофрмата
                'format': self.quality.currentText(),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': codec,
                }],
                'progress_hooks': [self.my_hook],  # процесс загрузки
                'outtmpl': path + '/%(title)s.%(ext)s',
            }
        else:
            if quality == 'best':  # выборка нужного качества для видео
                quality = 'bestvideo/best'
            else:
                quality = 'worstvideo/worst'
            ydl_opts = {  # опции загрузки для видеоформата
                'format': self.quality.currentText(),
                'preferredcodec': codec,
                'progress_hooks': [self.my_hook],
                'outtmpl': path + '/%(title)s.%(ext)s',
            }

        if path or link:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        else:
            self.answer.setText('Введите путь!')
        self.save(path)

    def my_hook(self, downloader):  # прогрессбар
        if downloader['status'] == 'finished':
            self.answer.setText('Успешно скачано!')
            self.link.clear()
            self.progressBar.reset()
        if downloader['status'] == 'downloading':
            percent = downloader['_percent_str']
            percent = percent.replace('%', '')
            self.progressBar.setValue(float(percent))

    def save(self, path):  # сохрание истории скачивания в БД
        files = [file_path  for _, _, file_path in os.walk(path)]
        print(files)

        for file_name in files[0]: # перебор и запись
            name = os.path.splitext(file_name)[0]  # названия фацла
            codec = os.path.splitext(file_name)[1]  # кодек
            date = os.path.getmtime(path)  # дата
            date = datetime.datetime.fromtimestamp(date)  # нужный формат даты
            
            con = sqlite3.connect('DB_simple.db')
            cur = con.cursor()
            cur.execute(
                f'''INSERT INTO downloads (name, codec, date) 
                VALUES ('{name}', '{codec}', '{date}')
                ''')
            con.commit()
            con.close()

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_Escape:  # клавиша Escape для закрытия приложения
            exit()