# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/patver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_partient(object):
    def setupUi(self, partient):
        partient.setObjectName("partient")
        partient.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(partient)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 150, 800, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 801, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.vorname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.vorname.setObjectName("vorname")
        self.horizontalLayout.addWidget(self.vorname)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gebdat = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gebdat.setObjectName("gebdat")
        self.horizontalLayout.addWidget(self.gebdat)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.stra = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stra.setObjectName("stra")
        self.horizontalLayout_2.addWidget(self.stra)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.ort = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ort.setObjectName("ort")
        self.horizontalLayout_2.addWidget(self.ort)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 800, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(490, 490, 301, 61))
        self.exit.setObjectName("exit")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 490, 301, 61))
        self.add.setObjectName("add")
        self.akte_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.akte_out.setGeometry(QtCore.QRect(10, 160, 771, 311))
        self.akte_out.setReadOnly(True)
        self.akte_out.setObjectName("akte_out")
        partient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(partient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        partient.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(partient)
        self.statusbar.setObjectName("statusbar")
        partient.setStatusBar(self.statusbar)

        self.retranslateUi(partient)
        QtCore.QMetaObject.connectSlotsByName(partient)

    def retranslateUi(self, partient):
        _translate = QtCore.QCoreApplication.translate
        partient.setWindowTitle(_translate("partient", "MainWindow"))
        self.label.setText(_translate("partient", "Name:"))
        self.name.setText(_translate("partient", "<name>"))
        self.label_3.setText(_translate("partient", "Vorname:"))
        self.vorname.setText(_translate("partient", "<vorname>"))
        self.label_5.setText(_translate("partient", "Geburtsdatum"))
        self.gebdat.setText(_translate("partient", "<gebdat>"))
        self.label_7.setText(_translate("partient", "Straße:"))
        self.stra.setText(_translate("partient", "<straße+hausnr>"))
        self.label_9.setText(_translate("partient", "Ort"))
        self.ort.setText(_translate("partient", "<plz+ort>"))
        self.exit.setText(_translate("partient", "Zurück zum Menü"))
        self.add.setText(_translate("partient", "Neuen Akten Eintrag"))

