# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'to_do_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 351, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.com_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.com_btn.setObjectName("com_btn")
        self.gridLayout.addWidget(self.com_btn, 0, 1, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 7, 4, 1, 1)
        self.del_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.del_btn.setObjectName("del_btn")
        self.gridLayout.addWidget(self.del_btn, 7, 1, 1, 1)
        self.todo_list = QtWidgets.QListView(self.gridLayoutWidget)
        self.todo_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.todo_list.setObjectName("todo_list")
        self.gridLayout.addWidget(self.todo_list, 0, 4, 1, 1)
        self.todo_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.todo_text.setObjectName("todo_text")
        self.gridLayout.addWidget(self.todo_text, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.history = QtWidgets.QAction(MainWindow)
        self.history.setObjectName("history")
        self.menu.addAction(self.history)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.com_btn.setText(_translate("MainWindow", "??????????????????"))
        self.add_btn.setText(_translate("MainWindow", "????????????????"))
        self.del_btn.setText(_translate("MainWindow", "??????????????"))
        self.label.setText(_translate("MainWindow", "???????????? ->"))
        self.menu.setTitle(_translate("MainWindow", "????????????"))
        self.history.setText(_translate("MainWindow", "?????????????? ??????????"))
