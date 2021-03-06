import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from qt.history_downloads_qt import Ui_Form

''' Вывод БД в таблице '''
class DB_down(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('История задач')
        self.connection = sqlite3.connect("DB_simple.db")
        self.select_data()

    def select_data(self):
        # По умолчанию будем выводить все данные из таблицы to_do_db
        res = self.connection.cursor().execute("SELECT * FROM downloads").fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        self.connection.close()

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_Escape:  # клавиша Escape для закрытия приложения
            exit()