from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project_kirka.ui', self)
        self.setWindowTitle('Проект')
 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
