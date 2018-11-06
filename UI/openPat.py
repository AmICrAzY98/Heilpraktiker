# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/openPat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_openPat(object):
    def setupUi(self, openPat):
        openPat.setObjectName("openPat")
        openPat.resize(400, 330)
        self.centralwidget = QtWidgets.QWidget(openPat)
        self.centralwidget.setObjectName("centralwidget")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(50, 100, 300, 61))
        self.open.setObjectName("open")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(50, 180, 301, 61))
        self.exit.setObjectName("exit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        openPat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(openPat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        openPat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(openPat)
        self.statusbar.setObjectName("statusbar")
        openPat.setStatusBar(self.statusbar)

        self.retranslateUi(openPat)
        QtCore.QMetaObject.connectSlotsByName(openPat)

    def retranslateUi(self, openPat):
        _translate = QtCore.QCoreApplication.translate
        openPat.setWindowTitle(_translate("openPat", "MainWindow"))
        self.open.setText(_translate("openPat", "Patienten öffnen"))
        self.exit.setText(_translate("openPat", "Abbrechen"))

