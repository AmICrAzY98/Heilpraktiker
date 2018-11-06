# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Patientenverwaltung.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Patientenverwaltung(object):
    def setupUi(self, Patientenverwaltung):
        Patientenverwaltung.setObjectName("Patientenverwaltung")
        Patientenverwaltung.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Patientenverwaltung)
        self.centralwidget.setObjectName("centralwidget")
        self.Patienteubersicht = QtWidgets.QTableWidget(self.centralwidget)
        self.Patienteubersicht.setGeometry(QtCore.QRect(490, 20, 301, 431))
        self.Patienteubersicht.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Patienteubersicht.setObjectName("Patienteubersicht")
        self.Patienteubersicht.setColumnCount(3)
        self.Patienteubersicht.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Patienteubersicht.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Patienteubersicht.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Patienteubersicht.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Patienteubersicht.setHorizontalHeaderItem(2, item)
        self.Patienteubersicht.horizontalHeader().setVisible(True)
        self.Patienteubersicht.verticalHeader().setVisible(False)
        self.Patienteubersicht.verticalHeader().setHighlightSections(True)
        self.addNew = QtWidgets.QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(10, 100, 301, 61))
        self.addNew.setObjectName("addNew")
        self.Back = QtWidgets.QToolButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(10, 10, 221, 51))
        self.Back.setObjectName("Back")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(490, 470, 301, 61))
        self.delete_2.setObjectName("delete_2")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(10, 170, 301, 61))
        self.open.setObjectName("open")
        Patientenverwaltung.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Patientenverwaltung)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Patientenverwaltung.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Patientenverwaltung)
        self.statusbar.setObjectName("statusbar")
        Patientenverwaltung.setStatusBar(self.statusbar)

        self.retranslateUi(Patientenverwaltung)
        QtCore.QMetaObject.connectSlotsByName(Patientenverwaltung)

    def retranslateUi(self, Patientenverwaltung):
        _translate = QtCore.QCoreApplication.translate
        Patientenverwaltung.setWindowTitle(_translate("Patientenverwaltung", "MainWindow"))
        item = self.Patienteubersicht.verticalHeaderItem(0)
        item.setText(_translate("Patientenverwaltung", "Neue Zeile"))
        item = self.Patienteubersicht.horizontalHeaderItem(0)
        item.setText(_translate("Patientenverwaltung", "ID"))
        item = self.Patienteubersicht.horizontalHeaderItem(1)
        item.setText(_translate("Patientenverwaltung", "Name"))
        item = self.Patienteubersicht.horizontalHeaderItem(2)
        item.setText(_translate("Patientenverwaltung", "Vorname"))
        self.addNew.setText(_translate("Patientenverwaltung", "Neuen Patienten hinzufügen"))
        self.Back.setText(_translate("Patientenverwaltung", "Zurück zum Hauptmenü"))
        self.delete_2.setText(_translate("Patientenverwaltung", "Patienten löschen"))
        self.open.setText(_translate("Patientenverwaltung", "Patienten öffnen"))

