# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.head = QtWidgets.QLabel(self.centralwidget)
        self.head.setGeometry(QtCore.QRect(100, 0, 600, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.head.setFont(font)
        self.head.setObjectName("head")
        self.Open_Pat = QtWidgets.QPushButton(self.centralwidget)
        self.Open_Pat.setGeometry(QtCore.QRect(10, 120, 301, 61))
        self.Open_Pat.setObjectName("Open_Pat")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(690, 490, 101, 61))
        self.Exit.setObjectName("Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.head.setText(_translate("MainWindow", "Heilpraktiker Software Version 1.0.0"))
        self.Open_Pat.setText(_translate("MainWindow", "Patientenverwaltung öffnen"))
        self.Exit.setText(_translate("MainWindow", "EXIT"))

