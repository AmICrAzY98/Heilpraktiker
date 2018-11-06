import sys
from qtpy import QtWidgets
from UI.MainWindow import Ui_MainWindow
from UI.Patientenverwaltung import Ui_Patientenverwaltung
from UI.addPat import Ui_AddNewPat
from UI.patver import Ui_partient
from patienten import Patientenliste
from UI.openPat import Ui_openPat
app = QtWidgets.QApplication(sys.argv)

PatientenVerwaltung = Patientenliste()
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Exit.clicked.connect(self.onExit)
        self.ui.Open_Pat.clicked.connect(self.onOpenPat)
        self.setWindowTitle("Heilpraktiker Software Version 1.0.0")

    def onOpenPat(self):
        self.pat = PatVerWindow()
        self.pat.show()
        window.hide()

    def onExit(self):
        PatientenVerwaltung.listespeichern()
        sys.exit()


class PatVerWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_Patientenverwaltung()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.onBack)
        self.ui.addNew.clicked.connect(self.onAddNew)
        self.ui.open.clicked.connect(self.onOpen)
        self.load("./Patienten/Ids.txt")

        self.setWindowTitle("Patientenverwaltung")

    def load(self, filen):
        self.ui.Patienteubersicht.setRowCount(0)
        with open(filen, "r", newline='')as file:
            for line in file:
                row = self.ui.Patienteubersicht.rowCount()
                self.ui.Patienteubersicht.insertRow(row)
                self.ui.Patienteubersicht.setItem(row, 0, QtWidgets.QTableWidgetItem(line.split("_")[0]))
                self.ui.Patienteubersicht.setItem(row, 1, QtWidgets.QTableWidgetItem(line.split("_")[1]))
                self.ui.Patienteubersicht.setItem(row, 2, QtWidgets.QTableWidgetItem(line.split("_")[2]))

    def onOpen(self):
        self.open = openPati()
        self.open.show()
        self.hide()
    def onAddNew(self):
        self.add = addNewPatient()
        self.add.show()
        self.hide()

    def onBack(self):
        window.show()
        self.hide()


class patient(QtWidgets.QMainWindow):
    def __init__(self, x,parent = None):
        super().__init__(parent)

        self.ui = Ui_partient()
        self.ui.setupUi(self)
        self.id = x
        self.load()

        self.setWindowTitle("Patient "+self.ui.name.text()+"_"+self.ui.vorname.text())

    def load(self):
        inpu = PatientenVerwaltung.getPatientX(self.id).getKopf()
        self.ui.name.setText(inpu[0])
        self.ui.vorname.setText(inpu[1])
        self.ui.gebdat.setText(inpu[2])
        self.ui.stra.setText(inpu[3]+" "+inpu[4])
        self.ui.ort.setText(inpu[5]+ " "+inpu[6])
        self.ui.akte_out.setPlainText(PatientenVerwaltung.getPatientX(self.id).readakte())




class openPati(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_openPat()
        self.ui.setupUi(self)
        self.load()
        self.ui.exit.clicked.connect(self.OnExit)
        self.ui.open.clicked.connect(self.onOpen)

    def onOpen(self):
        self.pat = patient(self.ui.comboBox.currentIndex())
        self.hide()
        self.pat.show()
    def load(self):
        with open("./Patienten/Ids.txt","r") as file:
            for line in file:
                temp = line.split("_")
                self.ui.comboBox.insertItem(int(temp[0]),temp[1]+" "+temp[2])

    def OnExit(self):
        self.hide()
        self.back = PatVerWindow()
        self.back.show()



class addNewPatient(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_AddNewPat()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.onSave)
        self.ui.quit.clicked.connect(self.onBrake)
        self.setWindowTitle("Neuen Patienten hinzufügen")

    def onBrake(self):
        self.hide()
        self.back = PatVerWindow()
        self.back.show()

    def onSave(self):
        global PatientenVerwaltung
        anr = self.ui.herrfrau.currentText()
        nam = self.ui.name.text()
        vorn = self.ui.vorname.text()
        geb = self.ui.gebdat.text()
        stra = self.ui.stra.text()
        nr = self.ui.hausnummer.text()
        plz = self.ui.plz.text()
        ort = self.ui.ort.text()
        tel = self.ui.telef.text()
        PatientenVerwaltung.neuenpatienten(anr, nam , vorn, geb, stra, nr, plz, ort, tel)
        self.hide()
        self.back = PatVerWindow()
        self.back.show()
        PatientenVerwaltung.listespeichern()




window = MainWindow()
window.show()

sys.exit(app.exec_())