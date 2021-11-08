from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QToolBar, QLineEdit
from PyQt5.QtCore import QUrl, Qt


''' Браузер '''
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()  # 'движок'
        self.browser.setUrl(QUrl('http://google.com'))  # стартовое окно

        self.browser.urlChanged.connect(self.update_url)  # обновление адресной строки

        url = QToolBar('Navigation') # место адресной строки
        self.addToolBar(url)

        self.urlbar = QLineEdit() # адресная строка
        self.urlbar.returnPressed.connect(self.to_url)  # переход по url 
        url.addWidget(self.urlbar)
        self.setCentralWidget(self.browser)  # само окно
        self.show()

    def to_url(self):  # переход по url
        self.browser.setUrl(QUrl(self.urlbar.text()))

    def update_url(self, line):  # обновление url 
        self.urlbar.setText(line.toString())
        self.urlbar.setCursorPosition(0)

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_Escape:  # клавиша Escape для закрытия приложения
            exit()