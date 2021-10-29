import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QComboBox, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTime, QTimer
from PyQt5.QtGui import QFont


''' Пока БД не подключена, планировщика нет, медиаплеера нет, браузер работает, время идёт '''
''' Главное окно '''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.setWindowTitle('Главная страница')
        self.browser_btn.clicked.connect(self.browser_view)  # браузер
        self.downloader_btn.clicked.connect(self.downloader_view)  # загрузчик
        self.to_do_btn.clicked.connect(self.to_do_view)  # планировщик
        self.player_btn.clicked.connect(self.player_view)  # медиаплеер

        ''' Время '''
        time = QTimer(self)  # сщдание объекта
        font = QFont('Open Sans', 20, QFont.Bold)  # увеличение шрифт
        self.label.setFont(font)
        time.timeout.connect(self.showtime)  # добавление метода
        time.start(1000)  # обновление времени каждую секунду

    def browser_view(self):  # бразуер
        self.browser = BrowserWindow()
        self.browser.setWindowTitle('Браузер')

    def downloader_view(self):  # загрузчик
        self.downloader = DowloaderWindow()
        self.downloader.show()

    def to_do_view(self):  # планировщик
        self.to_do = To_do_list()
        self.to_do.show()

    def player_view(self):  # проигрывание медиафайлов
        self.player = Player()
        self.player.show()

    def showtime(self):  # время
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label.setText(label_time)


''' Браузер '''
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))

        self.browser.urlChanged.connect(self.update_url)

        url = QToolBar("Navigation")
        self.addToolBar(url)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.to_url)
        url.addWidget(self.urlbar)

        self.setCentralWidget(self.browser)
        self.show()

    def to_url(self):
        line = QUrl(self.urlbar.text())
        if line == '':
            line.setText('http')
        self.browser.setUrl(line)

    def update_url(self, line):
        self.urlbar.setText(line.toString())
        self.urlbar.setCursorPosition(0)


''' Загрузчик '''
class DowloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('downloader.ui', self)
        self.setWindowTitle('Загрузчик')
        self.comboBox.addItems(['test1', 'test2', 'test3', 'test4'])


''' Планировщик '''
class To_do_list(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


''' Медиаплеер '''
class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())