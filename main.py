import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from qt.main_window import Ui_MainWindow

# модули с классами
from download import DowloaderWindow  # загрузчик
from browser import BrowserWindow  # ьраузер
from to_do import To_do_list  # планировщик
from play import Player  # медиаплеер

''' Главное окно '''
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Главаня страница | Simple Downloader')
        self.browser_btn.clicked.connect(self.browser_view)  # браузер
        self.downloader_btn.clicked.connect(self.downloader_view)  # загрузчик
        self.to_do_btn.clicked.connect(self.to_do_view)  # планировщик
        self.player_btn.clicked.connect(self.player_view)  # медиаплеер


        self.setStyleSheet(
            '.QWidget {background-image: url(image/background.jpg)}')  # фон

        ''' Время '''
        time = QTimer(self)  # создание объекта от QTimer
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

    def player_view(self):  # медиаплеер
        self.player = Player()
        self.player.show()

    def showtime(self):  # время
        current_time = QTime.currentTime()  # объект QTime
        label_time = current_time.toString('hh:mm:ss')  # нужный формат
        self.label.setText(label_time)  # вывод

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_1:  # клавиша  1 для вызова браузера
            self.browser_view()
        elif event.key() == Qt.Key_2:  # клавиша 2 для вызова загрузчика
            self.downloader_view()
        if event.key() == Qt.Key_3:  # клавиша 3 для вызова браузера
            self.to_do_view()
        if event.key() == Qt.Key_4:  # клавиша 4 для вызова медиаплеера
            self.player_view()
        if event.key() == Qt.Key_Escape:  # кнопка Escape для закрытия приложения
            exit()

def except_hook(cls, exception, traceback):  # обработка ошибок
    sys.__excepthook__(cls, exception, traceback)


''' Запуск '''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('image/icon.png'))
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())