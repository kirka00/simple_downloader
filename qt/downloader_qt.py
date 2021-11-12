# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 389)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("font-size: 14px")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 481, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.link = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.link.setObjectName("link")
        self.gridLayout.addWidget(self.link, 0, 0, 1, 1)
        self.down_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_btn.setObjectName("down_btn")
        self.gridLayout.addWidget(self.down_btn, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 1)
        self.answer = QtWidgets.QLabel(self.gridLayoutWidget)
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.gridLayout.addWidget(self.answer, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 1, 0, 1, 1)
        self.quality = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.quality.setObjectName("quality")
        self.gridLayout.addWidget(self.quality, 3, 0, 1, 1)
        self.codec = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.codec.setObjectName("codec")
        self.gridLayout.addWidget(self.codec, 2, 0, 1, 1)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(90, 250, 151, 51))
        self.play_btn.setObjectName("play_btn")
        self.play_text = QtWidgets.QLabel(self.centralwidget)
        self.play_text.setGeometry(QtCore.QRect(260, 240, 311, 61))
        self.play_text.setObjectName("play_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.history_downloads = QtWidgets.QAction(MainWindow)
        self.history_downloads.setObjectName("history_downloads")
        self.menu.addAction(self.history_downloads)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<- Выбор кодека"))
        self.down_btn.setText(_translate("MainWindow", "Скачать"))
        self.label_4.setText(_translate("MainWindow", "<-Куда скачивать (путь)"))
        self.label.setText(_translate("MainWindow", "<- ссылка на видео"))
        self.label_3.setText(_translate("MainWindow", "<- Качество"))
        self.play_btn.setText(_translate("MainWindow", "Медиаплеер"))
        self.play_text.setText(_translate("MainWindow", "<- Можно посмотреть скаченные файлы"))
        self.menu.setTitle(_translate("MainWindow", "Итсория"))
        self.history_downloads.setText(_translate("MainWindow", "История скачиваний"))
