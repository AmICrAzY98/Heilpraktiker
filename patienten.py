import datetime  # Für die Datumsanzeige
import pickle
import os        # Überprüft ob Datei schon vorhanden


""" Heilpraktiker Software Patient.py
    Version 1.0.0
    By JonasB
    Dieses Modul, hat den Sinn eine Klasse Patient zu erstellen die mehrere wichtige Eigenschaften speichern kann.
    Außerdem hat diese Klasse zugriff auf einen Writer/Reader welcher die Patientenakte beschreiben/lesen kann.
"""
# Klasse Patient:


class Patient:

    def __init__(self, a, b, c, d, e, f, g, h, i):

        self.persönlicheDaten=[a, b, c, d, e, f, g, h, i]
        # Anrede, Name, Vorname, Geburtsdatum, Straße, Hausnummer, Postleitzahl, Ort, Telefonnummer, Alter
        self.akten = []
        self.alterBerechnen()
        # self.filename = "./Patientenakten/"+b+"_"+c+".akte"
        # if os.path.exists(self.filename):
        #    print("Datei existiert bereits")
        # else:
        #    file = open(self.filename, 'w', encoding="utf-8")
        #    file.write(self.persönlicheDaten[1]+" "+self.persönlicheDaten[2]+"\n")
        #    file.close()
    def alterBerechnen(self):
        today = datetime.date.today()
        bday = datetime.date(
            int(self.persönlicheDaten[3].split(".")[2]),
            int(self.persönlicheDaten[3].split(".")[1]),
            int(self.persönlicheDaten[3].split(".")[0])
        )
        if today.month < bday.month or \
                (today.month == bday.month and today.day < bday.day):
            self.persönlicheDaten.append(str(today.year - bday.year - 1))
        else:
            self.persönlicheDaten.append(str(today.year - bday.year))

        print(self.persönlicheDaten)


    def writeinakte(self, text):
        self.akten.append(datetime.datetime.now().strftime("%A %d.%M.%Y    ")+self.textbearbeiten(text))

        # with open(self.filename, "a", encoding="utf-8") as file:
        #    file.write("\n\n")
        #    file.write(datetime.datetime.now().strftime("%A %d.%M.%Y    "))
        #    temp = 0
        #    for char in text:
        #        if temp == 100:
        #            file.write("-\n"+char)
        #            temp = 0
        #        else:
        #            file.write(char)
        #            temp += 1

    def textbearbeiten(self, text):
        string = ""
        counter = 0

        for char in text:
            if char != " ":
                string += char
            elif char == " ":
                counter += 1
                if counter == 9:
                    string += "\n"
                    counter = 0
                else:
                    string += char
                    counter += 1

        return string

    def readakte(self):
        for element in self.akten:
            # for char in element:
            #    if temp == 100:
            #        print("-\n"+char)
            #        temp = 1
            #    else:
            #        print(char)
            #        temp += 1
            return  element+"\n\n"
    def getKopf(self):
        out = []
        out.append(self.persönlicheDaten[1])
        out.append(self.persönlicheDaten[2])
        out.append(self.persönlicheDaten[3])
        out.append(self.persönlicheDaten[4])
        out.append(self.persönlicheDaten[5])
        out.append(self.persönlicheDaten[6])
        out.append(self.persönlicheDaten[7])
        return out
    def readeintrag(self, x):
        print(self.akten[x])


class Patientenliste:

    def __init__(self):
        if not os.path.exists("./Patienten/Liste.p"):
            self.liste = []
        else:
            self.liste = pickle.load(open("./Patienten/Liste.p", "rb"))
        if not os.path.exists("./Patienten/Ids.txt"):
            file = open("/Patienten/Ids.txt", 'w', encoding="utf-8")
            file.close()

    def neuenpatienten(self, anr, nam, vorn, geb, stra, nr, plz, ort, tel):
        file = open("./Patienten/Ids.txt", 'a', encoding="utf-8")
        file.write(str(len(self.liste))+"_"+nam+"_"+vorn+"\n")
        file.close()
        self.liste.append(Patient(anr, nam, vorn, geb, stra, nr, plz, ort, tel))

    def listespeichern(self):
        pickle.dump(self.liste, open("./Patienten/Liste.p", "wb"))

    def list(self):
        with open("./Patienten/Ids.txt", "r") as file:
            for line in file:
                print(line)

    def getPatientX(self, id):
        return self.liste[id]

    def addEintrag(self, p, text):
        p.writeinakte(text)
