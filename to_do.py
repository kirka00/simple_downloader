from PyQt5 import uic
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtWidgets import QMainWindow
import sqlite3
from json import load, dump  # удобный обмен данными между todo.txt и self.tasks.todo
from history_todo import DBSample


class TodoModel(QAbstractListModel):  # структура данных модели дел
    def __init__(self):
        super().__init__()
        self.todo = []  # список задач

    def data(self, index, role):  # текст задачи
        if role == Qt.DisplayRole:
            return self.todo[index.row()][1]

        if role == Qt.DecorationRole:  # метка выполненной задачи
            if self.todo[index.row()][0]:  # если True, то отметка в виде галочки
                return QImage('tick.png')

    def rowCount(self, arg):  # фикс (NotImplementedError: QAbstractListModel.rowCount()
        # is abstract and must be overridden)
        return len(self.todo)


class To_do_list(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('to_do.ui', self)
        self.setWindowTitle('Планировщик')

        self.tasks = TodoModel()  # объект от TodoModel
        self.loading()  # подрузка задач из todo.txt
        self.todo_list.setModel(self.tasks)  # вставка задач в лист

        ''' Кнопки '''
        self.add_btn.clicked.connect(self.add)  # добавление
        self.del_btn.clicked.connect(self.delete)  # удаление
        self.com_btn.clicked.connect(self.complete)  # выполнение
        self.history.triggered.connect(
            self.history_view)  # открыть нужный файл

    def history_view(self):  # история задач
        self.DB = DBSample()
        self.DB.show()

    def add(self):  # добавление задачи
        text_task = self.todo_text.text()  # текст задачи
        if text_task:  # проверяем на наличие текста
            # пока задача не выполнена
            self.tasks.todo.append((False, text_task))
            self.save_db(False, text_task)  # сохрание в историю
            self.tasks.layoutChanged.emit()  # обновление
            self.todo_text.setText('')  # чистка
            self.save_in_todo()  # сохранение в todo.txt

    def delete(self):  # удаление задачи
        indexes = self.todo_list.selectedIndexes()  # выбор задачи
        if indexes:  # фикс IndexError: list index out of range
            del self.tasks.todo[indexes[0].row()]  # удаление
            self.tasks.layoutChanged.emit()  # обновление модели
            self.todo_list.clearSelection()   # чистка листа задач
            self.save_db(True, indexes)  # сохрание в историю
            self.save_in_todo()  # сохранение в todo.txt

    def complete(self):  # выполнение задачи
        indexes = self.todo_list.selectedIndexes()  # выбор задачи
        if indexes:  # фикс IndexError: list index out of range
            row = indexes[0].row()
            # смена статуса на True (задача выполнена)
            self.tasks.todo[row] = (True, self.tasks.todo[row][1])
            self.tasks.dataChanged.emit(indexes[0], indexes[0])
            self.todo_list.clearSelection()   # чистка листа задач
            self.save_in_todo()  # сохранение в todo.txt

    def save_db(self, bool, text):  # история задач в БД
        con = sqlite3.connect('DB_simple.db')  # подключение к БД
        cur = con.cursor()  # cоздание курсора
        cur.execute(  # вставка нужных данных в БД
            f'''INSERT INTO to_do_db (content, status) 
            VALUES ('{text}', '{bool}')
            ''')
        con.commit()  # сохранение
        con.close()  # закрытие

    def loading(self):  # подгрузка из todo.txt
        with open('todo.txt', encoding='utf8', mode='r') as file:
            self.tasks.todo = load(file)

    def save_in_todo(self):  # сохранение в todo.txt
        with open('todo.txt', encoding='utf8', mode='w') as file:
            dump(self.tasks.todo, file)

    def keyPressEvent(self, event):  # обработка клавиш
        if event.key() == Qt.Key_Delete:  # клавиша Delete удаляет выбранную задачу
            self.delete()
