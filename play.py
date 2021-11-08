from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import QSize, QUrl, QAbstractListModel, Qt
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent


class PlaylistModel(QAbstractListModel):  # структура данных модели плейлиста
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist  # сам плейлист

    def data(self, index, role):
        if role == Qt.DisplayRole:  # название файла
            return self.playlist.media(index.row()).canonicalUrl().fileName()

    def rowCount(self, arg):  # фикс (NotImplementedError: QAbstractListModel.rowCount()
        # is abstract and must be overridden)
        return self.playlist.mediaCount()


''' Медиаплеер '''
class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('player.ui', self)
        self.setWindowTitle('Медиаплеер')

        self.player = QMediaPlayer()  # объект меидиаплеера
        self.player.play()  # запуск

        ''' Кнопки и слайдер '''
        self.play_btn.clicked.connect(self.player.play)  # play
        self.pause_btn.clicked.connect(self.player.pause)  # pause
        self.time_slide.valueChanged.connect(
            self.player.setPosition)  # time slider
        self.player.durationChanged.connect(
            self.update_duration)  # обновление слайдера
        # обновление позиции ползунка на слайдере
        self.player.positionChanged.connect(self.update_position)
        self.view_btn.clicked.connect(self.viewer)  # view
        self.open_file.triggered.connect(self.open_f)  # открыть нужный файл

        ''' Плейлист '''
        self.playlist = QMediaPlaylist()  # объект QMediaPlaylist
        self.player.setPlaylist(self.playlist)  # вставка плейлиста
        # создаётся объект PlaylistModel с плейлистом
        self.projects = PlaylistModel(self.playlist)  # объект от PlaylistModel с плейлистом
        self.playlistView.setModel(self.projects)  # вставка проектов в интерфейс
        self.playlist.currentIndexChanged.connect(
            self.playlist_changed)  # выбор проекта
        self.playlistView.selectionModel().selectionChanged.connect(
            self.playlistView_changed)

    def open_f(self):  # открытие файла
        path = QFileDialog.getOpenFileName(  # запоминаем путь
            self, "Выбрать файл", "", "mp3 Audio (*.mp3);;mp4 Video \
            (*.mp4);;aac Audio (*.aac);;m4a Audio (*.m4a);;wav Audio (*.wav);;Все файлы (*)")[0]

        if path:  # проверка (вдруг ничего не выбрано)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.projects.layoutChanged.emit()  # обновление

    # обновление самого слайдера (т. к. изменятется длительность файла)
    def update_duration(self, duration):
        self.time_slide.setMaximum(duration)

    def playlistView_changed(self, arg):  # смена проекта в плейлисте
        if arg:  # фикс (IndexError: list index out of range)
            self.playlist.setCurrentIndex(arg.indexes()[0].row())

    def update_position(self, position):  # изменение позиции ползунка на слайдере
        self.time_slide.blockSignals(True)  # сначала True, потом False
        # но между меняется позиция ползунка на слайдере
        self.time_slide.setValue(position)
        self.time_slide.blockSignals(False)

    def playlist_changed(self, arg):  # смена проекта в интерфейсе 
        self.playlistView.setCurrentIndex(self.projects.index(arg))

    def viewer(self):  # видеопросмотр
        self.view = ViewerWindow()
        self.view.setMinimumSize(QSize(720, 480))
        video = QVideoWidget()
        self.view.setCentralWidget(video)
        self.player.setVideoOutput(video)
        self.view.show()

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_Escape:  # кнопка Escape для закрытия приложения
            exit()


class ViewerWindow(QMainWindow):  # окно просмотра видео
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медиаплеер')
