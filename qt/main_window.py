# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(601, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(5, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 581, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.player = QtWidgets.QLabel(self.gridLayoutWidget)
        self.player.setStyleSheet("font-size: 16px")
        self.player.setObjectName("player")
        self.gridLayout.addWidget(self.player, 3, 1, 1, 1)
        self.download = QtWidgets.QLabel(self.gridLayoutWidget)
        self.download.setStyleSheet("font-size: 16px")
        self.download.setObjectName("download")
        self.gridLayout.addWidget(self.download, 1, 1, 1, 1)
        self.to_do = QtWidgets.QLabel(self.gridLayoutWidget)
        self.to_do.setStyleSheet("font-size: 16px")
        self.to_do.setObjectName("to_do")
        self.gridLayout.addWidget(self.to_do, 2, 1, 1, 1)
        self.browser_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.browser_btn.setStyleSheet("font-size: 14px")
        self.browser_btn.setObjectName("browser_btn")
        self.gridLayout.addWidget(self.browser_btn, 0, 0, 1, 1)
        self.player_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.player_btn.setStyleSheet("font-size: 14px")
        self.player_btn.setObjectName("player_btn")
        self.gridLayout.addWidget(self.player_btn, 3, 0, 1, 1)
        self.go_search = QtWidgets.QLabel(self.gridLayoutWidget)
        self.go_search.setStyleSheet("font-size: 16px")
        self.go_search.setObjectName("go_search")
        self.gridLayout.addWidget(self.go_search, 0, 1, 1, 1)
        self.downloader_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.downloader_btn.setStyleSheet("font-size: 14px")
        self.downloader_btn.setObjectName("downloader_btn")
        self.gridLayout.addWidget(self.downloader_btn, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.to_do_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.to_do_btn.setStyleSheet("font-size: 14px")
        self.to_do_btn.setObjectName("to_do_btn")
        self.gridLayout.addWidget(self.to_do_btn, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setAutoRepeat(False)
        self.actionTest.setVisible(False)
        self.actionTest.setIconVisibleInMenu(False)
        self.actionTest.setShortcutVisibleInContextMenu(False)
        self.actionTest.setObjectName("actionTest")
        self.actionsdsfs = QtWidgets.QAction(MainWindow)
        self.actionsdsfs.setObjectName("actionsdsfs")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.player.setText(_translate("MainWindow", "<- Проигрывание медиафайлов"))
        self.download.setText(_translate("MainWindow", "<- Загрузка файлов"))
        self.to_do.setText(_translate("MainWindow", "<- Простой to do list"))
        self.browser_btn.setText(_translate("MainWindow", "Браузер (1)"))
        self.player_btn.setText(_translate("MainWindow", "Медиаплеер (4)"))
        self.go_search.setText(_translate("MainWindow", "<-  Google Search"))
        self.downloader_btn.setText(_translate("MainWindow", "Загрузчик (2)"))
        self.to_do_btn.setText(_translate("MainWindow", "Планировщик (3)"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionsdsfs.setText(_translate("MainWindow", "sdsfs"))