from fnc.fonctionTache import *
from tkinter import filedialog
from tkinter.messagebox import *
from objet.arreradocument import *
from objet.arreratableur import *
from librairy.travailJSON import *
import subprocess
import re
import os
from pathlib import Path


class fncArreraWork(fncBase):
    def __init__(self,gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        # Objet
        self.__dectOs = self._gestionnaire.getOSObjet()
        self.__fncDate = CArreraDate()
        # Variable etat ouverture fichier
        self.__tableurOpen = False
        self.__wordOpen = False
        self.__projectOpen = False
        # Varriable des objet 
        self.__objTableur = None
        self.__objWord = None
        # File JSON Project
        self.__jsonFileProject = None
        # Varriable de nom du fichier
        self.__fileTableur = ""
        self.__fileWord = ""
        # Chargement des variable
        self.__nameAssistant = gestionnaire.getConfigFile().name
        self.__iconAssistant = self._gestionnaire.getConfigFile().icon
        self.__guiColor = "White"
        self.__textColor = "Black"
        # Varriable Projet
        self.__folderProject = ""
        self.__lastCreateFile = ""
        self.__listFileProjet = []
        self.__fncTaskProjet = None  # Correspont au tache du projet
        self.__listTaskProjetToday = []
        self.__listTaskProjetTowmorow = []
        self.__listReadTableur = []
        self.__contentWork = ""

    # Partie Tableur

    def openTableur(self):
        if not self.__tableurOpen:
            # Demande de l'emplacement du fichier
            showinfo("Work", "Choisissez votre fichier exel")
            emplacementFile = filedialog.askopenfilename(
                defaultextension='.xlsx',
                filetypes=[("Fichiers Excel", "*.xlsx")])
            self.__fileTableur = emplacementFile
            if emplacementFile == "":
                showwarning("Work", "Aucun fichier selectionner")
                return False
            else:
                self.__objTableur = CArreraTableur(emplacementFile)
                showinfo("Work", "Exel ouvert")
                self.__tableurOpen = True
                return True
        else:
            return False

    def closeTableur(self):
        if self.__tableurOpen:
            self.__objTableur.saveFile()
            self.__objTableur.closeFile()
            del self.__objTableur
            self.__objTableur = None
            self.__fileTableur = ""
            self.__tableurOpen = False
            return True
        else:
            return False

    def readTableur(self):
        if self.__tableurOpen:
            self.__listReadTableur = []
            contenu = self.__objTableur.read()
            for cell_position, cell_value in contenu.items():
                self.__listReadTableur.append("Cellule " + str(cell_position) + " : " + str(cell_value))
            return True
        else:
            return False

    def getReadTableur(self):
        return self.__listReadTableur

    def addValeurOnTableur(self, case: str, valeur):
        if self.__tableurOpen  and (case != ""):
            if self.__objTableur.write(case, valeur):
                if self.__objTableur.saveFile():
                    return True
                else :
                    return False
            else :
                return False
        else:
            return False

    def getListFormuleTableur(self):
        return ["Somme","Moyenne","Comptage","Minimum","Maximum"]

    def addSommeOnTableur(self, case_start: str, case_stop: str, case_dest: str):
        if (self.__tableurOpen and case_start != "") and (case_stop != "") and (case_dest != ""):
            if self.__objTableur.somme(case1=case_start, case2=case_stop, caseDestination=case_dest):
                if self.__objTableur.saveFile() :
                    return True
                else :
                    return False
            else :
                return False
        else :
            return False

    def addMoyenneOnTableur(self, case_start: str, case_stop: str, case_dest: str):
        if (self.__tableurOpen and case_start != "") and (case_stop != "") and (case_dest != ""):
            if self.__objTableur.moyenne(case1=case_start, case2=case_stop, caseDestination=case_dest):
                if self.__objTableur.saveFile() :
                    return True
                else :
                    return False
            else :
                return False
        else :
            return False

    def addComptageOnTableur(self, case_start: str, case_stop: str, case_dest: str):
        if (self.__tableurOpen and case_start != "") and (case_stop != "") and (case_dest != ""):
            if self.__objTableur.comptage(case1=case_start, case2=case_stop, caseDestination=case_dest):
                if self.__objTableur.saveFile() :
                    return True
                else :
                    return False
            else :
                return False
        else :
            return False

    def addMinimumOnTableur(self, case_start: str, case_stop: str, case_dest: str):
        if (self.__tableurOpen and case_start != "") and (case_stop != "") and (case_dest != ""):
            if self.__objTableur.minimun(case1=case_start, case2=case_stop, caseDestination=case_dest):
                if self.__objTableur.saveFile():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def addMaximumOnTableur(self, case_start: str, case_stop: str, case_dest: str):
        if (self.__tableurOpen and case_start != "") and (case_stop != "") and (case_dest != ""):
            if self.__objTableur.maximun(case1=case_start, case2=case_stop, caseDestination=case_dest):
                if self.__objTableur.saveFile():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def delValeur(self, case: str):
        if self.__tableurOpen:
            if self.__verifTableurCase(case):
                if self.__objTableur.deleteValeur(case):
                    if self.__objTableur.saveFile():
                        return True
                    else:
                        return False
                else :
                    return False
            else:
                return False
        else:
            return False

    def __verifTableurCase(self, chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False

    def openTableurDirectly(self, file: str):
        if (self.__tableurOpen == False and file != ""):
            self.__fileTableur = file
            self.__objTableur = CArreraTableur(file)
            self.__tableurOpen = True
            return True
        else:
            return False

    def openTableurOs(self):
        if self.__tableurOpen:
            if self.__dectOs.osLinux() and not self.__dectOs.osWindows() :
                subprocess.call(["xdg-open", self.__fileTableur])
                return True
            elif not self.__dectOs.osLinux() and self.__dectOs.osWindows() == True:
                    os.startfile(self.__fileTableur)
                    return True
            elif self.__dectOs.osMac():  # <-- Ajout du support MacOS
                subprocess.call(["open", self.__fileTableur])
                return True
            else:
                return False
        else:
            return False

    # Partie Word

    def openWord(self):
        if not self.__wordOpen:
            # Demande de l'emplacement du fichier
            showinfo("Work", "Choisissez votre fichier word")
            emplacementFile = filedialog.askopenfilename(
                defaultextension='.docx',
                filetypes=[('Tout les fichier', '*.*'),
                           ('Fichiers Word', '*.docx'),
                           ("Texte OpenDocument", "*.odt")])
            self.__fileWord = emplacementFile
            if emplacementFile == "":
                showwarning("Work", "Aucun fichier selectionner")
                return False
            else:
                self.__objWord = CArreraDocx(emplacementFile)
                showinfo("Work", "Word ouvert")
                self.__wordOpen = True
                return True
        else:
            return False

    def openWordDirectly(self, file: str):
        if self.__wordOpen == False and file != "":
            self.__fileWord = file
            self.__objWord = CArreraDocx(file)
            self.__wordOpen = True
            return True
        else:
            return False

    def closeWord(self):
        if self.__wordOpen:
            del self.__objWord
            self.__objWord = None
            self.__fileWord = ""
            self.__wordOpen = False
            return True
        else:
            return False

    def writeWordEcrase(self,texte:str):
        if self.__wordOpen:
            if self.__objWord.writeEcrase(texte) :
                return True
            else:
                return False
        else:
            return False

    def writeWord(self, texte:str):
        if self.__wordOpen:
            if self.__objWord.writeNoEcrase(texte):
                return True
            else:
                return False
        else :
            return False

    def readWord(self):
        if self.__wordOpen:
            self.__contentWork = ""
            self.__contentWork = self.__objWord.read()
            return True
        else:
            return False

    def getReadWord(self):
        return self.__contentWork

    def openWordOs(self):
        if self.__wordOpen:
            if self.__dectOs.osLinux() and not self.__dectOs.osWindows():
                subprocess.call(["xdg-open", self.__fileWord])
                return True
            elif not self.__dectOs.osLinux() and self.__dectOs.osWindows() == True:
                os.startfile(self.__fileWord)
                return True
            elif self.__dectOs.osMac():  # <-- Ajout du support MacOS
                subprocess.call(["open", self.__fileWord])
                return True
            else:
                return False
        else:
            return False

    # Partie Projet

    def getListProjet(self):
        wordEmplacement = self._gestionnaire.getWorkEmplacement()
        if wordEmplacement != "":
            try :
                repertoir = Path(wordEmplacement)
                return [dossier.name for dossier in repertoir.iterdir() if dossier.is_dir()]
            except:
                return None
        else :
            return None

    def openProjet(self, project: str):
        if not self.__projectOpen:
            wordEmplacement = self._gestionnaire.getWorkEmplacement()
            repertoir = Path(wordEmplacement)
            dossier = [dossier.name for dossier in repertoir.iterdir() if dossier.is_dir()]
            for i in range(0, len(dossier)):
                if project == dossier[i]:
                    # Ecriture de l'emplacement du projet
                    self.__folderProject = wordEmplacement + "/" + project
                    # Ouverture du fichier de config
                    self.__jsonFileProject = jsonWork(
                        os.path.join(self.__folderProject + "/.arreraProjet", project + ".apr"))
                    # Mise de la var a true
                    self.__projectOpen = True
                    # Ouverture fichier de tache
                    self.__fncTaskProjet = self._gestionnaire.getGestFNC().initTaskProject(self.__folderProject + "/.arreraProjet/TaskProjet.json")
                    return True
            return False
        else:
            return False

    def createProjet(self, name: str):
        wordEmplacement = self._gestionnaire.getWorkEmplacement()
        if (self.__projectOpen == False) and (wordEmplacement != ""):
            dataJson = {"name": "", "type": ""}
            folder = (wordEmplacement + "/" + name)
            dataJson["name"] = name
            try:
                # Creation du projet
                os.makedirs(folder, exist_ok=True)
                # Creation du sous dossier de config du projet
                os.makedirs(folder + "/.arreraProjet")
                # Enregistrement de l'emplacement du projet
                self.__folderProject = folder
                # Creation du fichier de config
                configPath = os.path.join(folder + "/.arreraProjet", name + ".apr")
                # Creation du fichier de tache
                taskPath = os.path.join(folder + "/.arreraProjet", "TaskProjet.json")
                try:
                    # Ecriture dans les deux fichier
                    with open(configPath, "w", encoding="utf-8") as file:
                        json.dump(dataJson, file, ensure_ascii=False, indent=4)
                    with open(taskPath, "w", encoding="utf-8") as file:
                        json.dump({}, file, ensure_ascii=False, indent=4)
                    # Ouverture du fichier de config
                    self.__jsonFileProject = jsonWork(configPath)
                    # Mise a true de la var de projet ouvert
                    self.__projectOpen = True
                    # Ouverture fichier de tache
                    self.__fncTaskProjet = self._gestionnaire.getGestFNC().initTaskProject(taskPath)
                    return True
                except Exception as e:
                    return False
            except Exception as e:
                return False
        else:
            return False

    def closeProjet(self):
        if self.__projectOpen:
            self.__projectOpen = False
            self.__folderProject = ""
            self.__lastCreateFile = ""
            self.__jsonFileProject = None
            self.__fncTaskProjet = None
            self.__listFileProjet = []
            self.__listTaskProjetToday = []
            self.__listTaskProjetTowmorow = []
            return True
        else:
            return False

    def getViewTypeProjetAvailable(self):
        return ["Développement d'application web",
                 "Développement d'application desktop",
                 "Développement d'application mobile",
                 "Électronique",
                 "Électrique",
                 "Système embarqué",
                 "Développement de jeux vidéo",
                 "Écriture de livre"]


    def addTypeProjet(self, type: str):
        if (type != "") and self.__projectOpen == True and (type in self.getViewTypeProjetAvailable()):
            self.__jsonFileProject.EcritureJSON("type", type)
            return True
        else:
            return False

    def getTypeProjet(self):
        if self.__projectOpen:
            return self.__jsonFileProject.lectureJSON("type")
        else:
            return None

    def getNameProjet(self):
        if self.__projectOpen:
            return self.__jsonFileProject.lectureJSON("name")
        else:
            return None

    def getNameTypeFileWithExtension(self):
        return {"excel": "xlsx",
                "word": "docx",
                "Open Document Texte": "odt",
                "markdown": "md",
                "Arrera Postite":".ab"}

    def getListTypeFileName(self):
        return list(self.getNameTypeFileWithExtension().keys())

    def getListTypeFileExtension(self):
        return list(self.getNameTypeFileWithExtension().values())

    def createFileProject(self,name: str,type:str):
        if self.__projectOpen and name != "" and type != "":
            if type in self.getListTypeFileName() or type in self.getListTypeFileExtension():
                emplacement = self.__folderProject + "/"
                if type == "excel" or type == "xlsx":
                    try :
                        self.__lastCreateFile = name + ".xlsx"
                        wb = Workbook()
                        ws = wb.active
                        ws.title = name
                        ws['A1'] = ""
                        wb.save(emplacement + self.__lastCreateFile)
                        del ws
                        wb.close()
                        del wb
                        return True
                    except Exception as e:
                        # print(e)
                        return False
                elif type == "word" or type == "docx":
                    try :
                        self.__lastCreateFile = name + '.docx'
                        doc = Document()
                        doc.add_paragraph("")
                        doc.save(emplacement + self.__lastCreateFile)
                        return True
                    except Exception as e:
                        # print(e)
                        return False
                elif type == "Open Document Texte" or type == "odt":
                    try :
                        self.__lastCreateFile = name + ".odt"
                        doc = OpenDocumentText()
                        p1 = P(text="")
                        doc.text.addElement(p1)
                        doc.save(emplacement + self.__lastCreateFile)
                        return True
                    except Exception as e:
                        # print(e)
                        return False
                elif type == "markdown" or type == "md":
                    try :
                        self.__lastCreateFile = name + ".md"
                        filePath = os.path.join(emplacement, self.__lastCreateFile)
                        with open(filePath, "w", encoding="utf-8") as file:
                            file.write("File readme named " + name)
                        return True
                    except Exception as e:
                        # print(e)
                        return False
                elif type == "Arrera Postite" or type == ".ab":
                    try :
                        self.__lastCreateFile = name + ".ab"
                        filePath = os.path.join(emplacement, self.__lastCreateFile)
                        with open(filePath, "w", encoding="utf-8") as file:
                            file.write("# File Arrera Postiste named " + name)
                        return True
                    except Exception as e:
                        # print(e)
                        return False
                else :
                    return False
            else :
                return False
        else :
            return False

    def setlistFileProject(self):
        if self.__projectOpen:
            try:
                # Liste les fichiers et dossiers dans le répertoire
                self.__listFileProjet = os.listdir(self.__folderProject)
                self.__listFileProjet.remove(".arreraProjet")
                return True
            except FileNotFoundError:
                return False
            except PermissionError:
                return False
            except Exception as e:
                return False
        else:
            return False

    def getListFileProjet(self):
        return self.__listFileProjet

    def addTacheProjet(self,name: str, date: datetime = None, description: str = None):
        if self.__projectOpen:
            return self.__fncTaskProjet.addTask(name,date,description)
        else:
            return False

    def supprTacheProjet(self,name):
        if self.__projectOpen:
            return self.__fncTaskProjet.delTask(name)
        else:
            return False

    def finishTacheProjet(self,name:str):
        if self.__projectOpen:
            return self.__fncTaskProjet.finishTask(name)
        else:
            return False

    def checkTacheProjet(self,name):
        if self.__projectOpen:
            return self.__fncTaskProjet.checkDateTask(name)
        else:
            return False

    def setListTacheTodayProjet(self):
        if self.__projectOpen:
            self.__listTaskProjetToday = self.__fncTaskProjet.getListTaskToday()
            return True
        else:
            return False

    def getListTacheTodayProjet(self):
        return self.__listTaskProjetToday

    def setListTacheTowmorowProjet(self):
        if self.__projectOpen:
            self.__listTaskProjetTowmorow = self.__fncTaskProjet.getListTaskTowmorow()
            return True
        else:
            return False

    def getListTacheTowmorowProjet(self):
        return self.__listTaskProjetTowmorow

    # Getteur

    def getEtatTableur(self):
        return self.__tableurOpen

    def getEtatWord(self):
        return self.__wordOpen

    def getEtatProject(self):
        return self.__projectOpen

    def getNameFileTableur(self):
        return self.__fileTableur

    def getNameFileWord(self):
        return self.__fileWord