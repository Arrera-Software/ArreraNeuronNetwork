from neuron.CNeuronBase import neuronBase,gestionnaire
from tkinter.filedialog import askopenfilename


class neuroneWork(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fonctionWork = self._gestionnaire.getGestFNC().getFNCWork()
        self.__fileProjectCreate = False
        self.__nameFileProjectCreate = ""
        self.__typeFileProjectCreate = ""

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0
        if self.__neuronTableur(requette) == 1:
            return
        elif self.__neuronProjet(requette) == 1:
            return
        elif self.__neuronWord(requette) == 1:
            return
        elif self._keyword.checkWork(requette,"help-work"):

            self._listSortie = [self._language.getPhraseHelpArreraWork("5"),"work"]
            self._valeurOut = 17
        elif self._keyword.checkWork(requette,"question-open") and self._keyword.checkOpen(requette,"open") and self._keyword.checkWork(requette,"open-file"):
            word = self.__fonctionWork.getEtatWord()
            tableur = self.__fonctionWork.getEtatTableur()

            if word and tableur:
                self._listSortie = [self._language.getPhraseWork("21"),""]
            elif tableur and not word:
                self._listSortie = [self._language.getPhraseWork("22"),""]
            elif word and not tableur:
                self._listSortie = [self._language.getPhraseWork("23"),""]
            else :
                self._listSortie = [self._language.getPhraseWork("24"),""]

            self._valeurOut = 1



    def __neuronTableur(self,requette:str):
        if not self.__fonctionWork.getEtatTableur():
            if (self._keyword.checkOpen(requette,"open") and
                    self._keyword.checkWork(requette,"tableur-file")):

                if self.__fonctionWork.openTableur():
                    self._listSortie = [self._language.getPhraseWork("5"),""]
                else :
                    self._listSortie = [self._language.getPhraseWork("6"),""]

                self._valeurOut = 7
                return 1
            elif self._keyword.checkWork(requette,"help-tableur"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("1")
                    ,"tableur"]
                self._valeurOut = 17
                return 1
            else :
                return 0
        else:
            if (self._keyword.checkOpen(requette,"open") and
                        self._keyword.checkWork(requette,"tableur-file") and
                        self._keyword.checkOpen(requette,"computer")):

                    if self.__fonctionWork.openTableurOs():
                        self._listSortie = [self._language.getPhraseWork("1"), ""]
                    else :
                        self._listSortie = [self._language.getPhraseWork("2"), ""]

                    self._valeurOut = 1
                    return 1
            elif (self._keyword.checkWork(requette,"close") and
                  self._keyword.checkWork(requette,"tableur-file")):

                if self.__fonctionWork.closeTableur():
                    self._listSortie = [self._language.getPhraseWork("10"), ""]
                else :
                    self._listSortie = [self._language.getPhraseWork("11"), ""]

                self._valeurOut = 8
                return 1
            elif self._keyword.checkWork(requette,"add") and self._keyword.checkWork(requette,"tableur-file"):
                if self._keyword.checkWork(requette,"valeur"):
                    if self._gestGUI.activeManageTableur(1):
                        self._listSortie = [self._language.getPhraseWork("25"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("29"),""]
                        self._valeurOut = 1
                    return 1
                elif self._keyword.checkWork(requette,"somme"):
                    if self._gestGUI.activeManageTableur(2):
                        self._listSortie = [self._language.getPhraseWork("27"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("28"),""]
                        self._valeurOut = 1
                    return 1
                elif self._keyword.checkWork(requette,"moyenne"):
                    if self._gestGUI.activeManageTableur(3):
                        self._listSortie = [self._language.getPhraseWork("29"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("30"),""]
                        self._valeurOut = 1
                    return 1
                elif self._keyword.checkWork(requette,"comptage"):
                    if self._gestGUI.activeManageTableur(4):
                        self._listSortie = [self._language.getPhraseWork("64"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("65"),""]
                        self._valeurOut = 1
                    return 1
                elif self._keyword.checkWork(requette,"min"):
                    if self._gestGUI.activeManageTableur(5):
                        self._listSortie = [self._language.getPhraseWork("31"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("32"),""]
                        self._valeurOut = 1
                    return 1
                elif self._keyword.checkWork(requette,"max"):
                    if self._gestGUI.activeManageTableur(6):
                        self._listSortie = [self._language.getPhraseWork("33"),""]
                        self._valeurOut = 5
                    else :
                        self._listSortie = [self._language.getPhraseWork("34"),""]
                        self._valeurOut = 1
                    return 1
                else :
                    return 0
            elif self._keyword.checkWork(requette,"del") and self._keyword.checkWork(requette,"tableur-file"):
                if self._gestGUI.activeManageTableur(7):
                    self._listSortie = [self._language.getPhraseWork("41"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("42"),""]
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkWork(requette,"read") and self._keyword.checkWork(requette,"tableur-file"):
                if self._gestGUI.activeReadTableur():
                    self._listSortie = [self._language.getPhraseWork("36"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("37"),""]
                    self._valeurOut = 1
                return 1
            else :
                return 0

    def __neuronProjet(self,requette:str):
        if not self.__fonctionWork.getEtatProject():
            if self._keyword.checkWork(requette,"open-project"):
                listKeyword = self._keyword.getListKeyword("work","open-project")
                for mot in listKeyword:
                    requette = requette.replace(mot,"")
                project = requette.strip()
                if self.__fonctionWork.openProjet(project):
                    self._listSortie = [self._language.getPhraseProjetFileOpen("6",project),""]
                    self._valeurOut = 14
                else :
                    self._listSortie = [self._language.getPhraseProjetFileOpen("7",project),""]
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkWork(requette, "create-project"):
                listKeyword = self._keyword.getListKeyword("work","create-project")
                for mot in listKeyword:
                    requette = requette.replace(mot,"")
                project = requette.strip()
                if self.__fonctionWork.createProjet(project):
                    self._listSortie = [self._language.getPhraseProjetFileOpen("4",project),""]
                    self._valeurOut = 10
                else :
                    self._listSortie = [self._language.getPhraseProjetFileOpen("5",project),""]
                    self._valeurOut = 1
                return 1
            elif (self._keyword.checkWork(requette,"liste") and
                  self._keyword.checkWork(requette,"project-file")):
                listProject = self.__fonctionWork.getListProjet()
                nbProject = len(listProject)
                if nbProject == 0:
                    debutPhrase = self._language.getPhraseWork("68")

                elif nbProject == 1:
                    debutPhrase = self._language.getPhraseWork("67")

                else :
                    debutPhrase = self._language.getPhraseWork("66")

                self._valeurOut = 1
                text = ""

                for i in range(0,nbProject):
                    if i == nbProject-1:
                        if nbProject == 1:
                            text = debutPhrase + " " + listProject[i] + "."
                        else :
                            text = text + " et " + listProject[i] + "."
                    elif i == 0:
                        text = debutPhrase + " " + listProject[i]
                    else :
                        text = text + ", " + listProject[i]

                self._listSortie = [text,"liste project"]
                return 1
            elif self._keyword.checkWork(requette,"help-project"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("3"),
                                    "project"]
                self._valeurOut = 17
                return 1
        else :
            if (self._keyword.checkWork(requette,"project-file") and
                    self._keyword.checkWork(requette,"close")):
                if self.__fonctionWork.closeProjet():
                    self._listSortie = [self._language.getPhraseWork("14"),""]
                    self.__fileProjectCreate = False
                    self.__nameFileProjectCreate = ""
                    self.__typeFileProjectCreate = ""
                    self._valeurOut = 21
                else :
                    self._listSortie = [self._language.getPhraseWork("15"),""]
                    self._valeurOut = 1
                return 1
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkWork(requette,"file") and
                  self._keyword.checkWork(requette,"liste")):
                self._listSortie = [self._language.getPhraseHelpArreraWork("4"),""]
                self._valeurOut = 17
                return 1
            elif (self._keyword.checkWork(requette,"project-file") and
                  (self._keyword.checkTime(requette,"montre") or
                   self._keyword.checkTime(requette,"open")) and
                  self._keyword.checkTime(requette,"tache")):

                if self._gestGUI.activeTaskProject(3):
                    self._listSortie = [
                        self._language.getPhraseProjetFileOpen("10",
                                                               self.__fonctionWork.getNameProjet()),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("51"),""]
                    self._valeurOut = 1
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkTime(requette,"add") and
                  self._keyword.checkTime(requette,"tache")):

                if self._gestGUI.activeTaskProject(1):
                    self._listSortie = [
                        self._language.getPhraseProjetFileOpen("11",
                                                               self.__fonctionWork.getNameProjet()),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("52"),""]
                    self._valeurOut = 1
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkTime(requette,"delete") and
                  self._keyword.checkTime(requette,"tache")):

                if self._gestGUI.activeTaskProject(2):
                    self._listSortie = [
                        self._language.getPhraseProjetFileOpen("12",
                                                               self.__fonctionWork.getNameProjet()),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("53"),""]
                    self._valeurOut = 1

            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkWork(requette,"file") and
                  self._keyword.checkWork(requette,"create")):
                self._listSortie = [self._language.getPhraseWork("72")
                    ,""]
                self._valeurOut = 1
                self.__fileProjectCreate = True
                self.__nameFileProjectCreate = ""
                self.__typeFileProjectCreate = ""
                return 1

            elif self.__fileProjectCreate:
                if self._keyword.checkWork(requette,"name-file"):
                    listKeyword = self._keyword.getListKeyword("work","name-file")
                    for mot in listKeyword:
                        requette = requette.replace(mot,"")

                    self.__nameFileProjectCreate = requette.strip()

                    if self.__nameFileProjectCreate != "":
                        if self.__typeFileProjectCreate == "":
                            self._listSortie = [self._language.getPhraseWork("45")
                                ,""]
                            self._valeurOut = 1
                        elif self.__fonctionWork.createFileProject(self.__nameFileProjectCreate,
                                                                     self.__typeFileProjectCreate):
                            nameTypeFile = self.__nameFileProjectCreate+"."+self.__typeFileProjectCreate
                            self._listSortie = [
                                self._language.getPhraseProjetFileOpen("8",
                                                                       nameTypeFile),""]
                            self._valeurOut = 1
                            self.__fileProjectCreate = False
                            self.__nameFileProjectCreate = ""
                            self.__typeFileProjectCreate = ""
                        else :
                            self._listSortie = [self._language.getPhraseWork("63")
                                ,""]
                            self._valeurOut = 1
                    else :
                        self._listSortie = [self._language.getPhraseWork("62")
                            ,""]
                        self._valeurOut = 1

                    return 1

                elif self._keyword.checkWork(requette,"type-file"):
                    listKeyword = self._keyword.getListKeyword("work","type-file")
                    for mot in listKeyword:
                        requette = requette.replace(mot,"")

                    self.__typeFileProjectCreate = requette.strip().replace(" ","")

                    if (self.__typeFileProjectCreate in self.__fonctionWork.getListTypeFileName()
                        or self.__typeFileProjectCreate in self.__fonctionWork.getListTypeFileExtension() or
                            self.__typeFileProjectCreate != ""):

                        if self.__nameFileProjectCreate == "":
                            self._listSortie = [
                                self._language.getPhraseWork("70")
                                ,""]
                            self._valeurOut = 1
                        elif self.__fonctionWork.createFileProject(self.__nameFileProjectCreate,
                                                                   self.__typeFileProjectCreate):
                            nameTypeFile = self.__nameFileProjectCreate+"."+self.__typeFileProjectCreate
                            self._listSortie = [
                                self._language.getPhraseProjetFileOpen("8",
                                                                       nameTypeFile),""]
                            self._valeurOut = 1
                            self.__fileProjectCreate = False
                            self.__nameFileProjectCreate = ""
                            self.__typeFileProjectCreate = ""
                        else :
                            self._listSortie = [self._language.getPhraseWork("63")
                                ,""]
                            self._valeurOut = 1

                    else :
                        self._listSortie = [
                            self._language.getPhraseWork("71")
                            ,""]
                        self._valeurOut = 1

                    return 1

    def __neuronWord(self,requette:str):
        if not self.__fonctionWork.getEtatWord():
            if (self._keyword.checkOpen(requette,"open") and
                    self._keyword.checkWork(requette,"word-file")):
                if self.__fonctionWork.openWord():
                    self._listSortie = [self._language.getPhraseWork("7"),""]
                    self._valeurOut = 7
                else :
                    self._listSortie = [self._language.getPhraseWork("8"),""]
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkWork(requette,"help-word"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("2"),"word"]
                self._valeurOut = 17
                return 1
        else :
            if (self._keyword.checkOpen(requette,"open") and
                    self._keyword.checkWork(requette,"word-file") and
                    self._keyword.checkOpen(requette,"computer")):

                if self.__fonctionWork.openWordOs():
                    self._listSortie = [self._language.getPhraseWork("3"), ""]
                else :
                    self._listSortie = [self._language.getPhraseWork("4"), ""]

                self._valeurOut = 1
                return 1
            elif (self._keyword.checkWork(requette,"close") and
                  self._keyword.checkWork(requette,"word-file")):

                if self.__fonctionWork.closeTableur():
                    self._listSortie = [self._language.getPhraseWork("12"), ""]
                else :
                    self._listSortie = [self._language.getPhraseWork("13"), ""]

                self._valeurOut = 8
                return 1
            elif self._keyword.checkWork(requette,"help-word"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("2"),"word"]
                self._valeurOut = 17
                return 1
            elif (self._keyword.checkWork(requette,"write") and
                  self._keyword.checkWork(requette,"word-file")):
                if self._gestGUI.activeWriteWord():
                    self._listSortie = [self._language.getPhraseWork("18"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("19"),""]
                    self._valeurOut = 1
                return 1
            elif (self._keyword.checkWork(requette,"read") and
                  self._keyword.checkWork(requette,"word-file")):
                if self._gestGUI.activeReadWord():
                    self._listSortie = [self._language.getPhraseWork("61"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseWork("16"),""]
                    self._valeurOut = 1
                return 1

    def __neuronGUI(self,requette):
        if self._keyword.checkOpen(requette,"open") and self._keyword.checkWork(requette,"gui-work"):# open
            if self._keyword.checkwork(requette,"project-file"): # projet
                if self._gestGUI.activeWorkProject():
                    self._listSortie = []
                    self._valeurOut = 5
                else :
                    self._listSortie = []
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkwork(requette,"tableur-file"): # tableur
                if self._gestGUI.activeWorkTableur():
                    self._listSortie = []
                    self._valeurOut = 5
                else :
                    self._listSortie = []
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkwork(requette,"word-file"): # word
                if self._gestGUI.activeWorkWord():
                    self._listSortie = []
                    self._valeurOut = 5
                else :
                    self._listSortie = []
                    self._valeurOut = 1
                return 1
            else :
                if self._gestGUI.activeWork():
                    self._listSortie = []
                    self._valeurOut = 5
                else :
                    self._listSortie = []
                    self._valeurOut = 1



