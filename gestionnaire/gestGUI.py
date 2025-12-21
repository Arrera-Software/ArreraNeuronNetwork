from gestionnaire.gestion import gestionnaire


class gestGUI:
    def __init__(self, gest: gestionnaire):
        self.__name_gui = None
        self.__gest = gest
        self.__liste_gui = ["calculatrice_normal","calculatrice_pythagore",
                            "calculatrice_complex","orthographe",
                            "arrera_download","agenda",
                            "agenda_add","agenda_delete",
                            "horloge","minuteur",
                            "chrono","lecture",
                            "tache","tache_finish",
                            "tache_del","work",
                            "work_projet","work_tableur",
                            "work_manage_tableur","work_read_tableur",
                            "work_word","work_word_read","work_word_write",
                            "tache_projet","tache_projet_add","tache_projet_del",
                            "traducteur","resumer",
                            "aide","breef"]
        self.__parms = None
        self.__textOut = None
        self.__valOut = 0
        # Importation des GUI
        from gui.GUICalculatrice import GUICalculatrice
        from gui.GUIorthographe import GUIOrthographe
        from gui.GUIArreraDownload import GUIArreraDownload
        from gui.GUIAgenda import GUIAgenda
        from gui.GUIHorloge import GUIHorloge
        from gui.GUILecture import GUILecture
        from gui.GUITache import GUITache
        from gui.GUIArreraWork import GUIWork
        from gui.GUITraducteur import GuiTraducteur
        from gui.GUIViewResumer import GUIViewResumer
        from gui.GUIHelp import GUIHelp
        from gui.GUIViewBreef import GUIViewBreef

        # Calculatrice
        self.__guiCalculatrice = GUICalculatrice(self.__gest)
        # Correcteur d'orthographe
        self.__guiOrthographe = GUIOrthographe(self.__gest)
        # Arrera Download
        self.__guiArreraDownload = GUIArreraDownload(self.__gest)
        # Agenda
        self.__guiAgenda = GUIAgenda(self.__gest)
        # Horloge
        self.__guiHorloge = GUIHorloge(self.__gest)
        # Lecture
        self.__guiLecture = GUILecture(self.__gest)
        # Tâche
        self.__guiTache = GUITache(self.__gest)
        # Work
        self.__guiWork = GUIWork(self.__gest)
        # Traducteur
        self.__guiTraducteur = GuiTraducteur(self.__gest)
        # Resumer
        self.__guiResumer = GUIViewResumer(self.__gest)
        # Aide
        self.__guiHelp = GUIHelp(self.__gest)
        # Breef
        self.__guiBreef = GUIViewBreef(self.__gest)

    def setGUIActive(self,gui:str,parms=None):
        if gui in self.__liste_gui:
            self.__name_gui = gui
            self.__parms = parms
            return True
        else :
            return False

    def launch_gui(self):
        if self.__name_gui is not None:
            if self.__name_gui == self.__liste_gui[0]:
                try :
                    self.__guiCalculatrice.activeCalcule()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("7")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("8")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[1]:
                try :
                    self.__guiCalculatrice.activePythagore()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("5")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("6")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[2]:
                try :
                    self.__guiCalculatrice.activeComplex()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("3")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("4")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[3]:
                if self.__parms != "" and self.__gest.getGestFNC().getFNCOrthographe().getToolLaunched():
                    self.__guiOrthographe.active()
                    self.__guiOrthographe.setTexte(self.__parms)
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseService("3")
                    self.__valOut = 5
                    return True
                else :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseService("4")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[4]:
                try :
                    self.__guiArreraDownload.active()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("1")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("2")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[5]:
                self.__guiAgenda.active()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("8")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[6]:
                self.__guiAgenda.activeAdd()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("4")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[7]:
                self.__guiAgenda.activeDel()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("5")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[8]:
                self.__guiHorloge.active()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("2")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[9]:
                self.__guiHorloge.activeMinuteur()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("3")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[10]:
                self.__guiHorloge.activeChrono()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("1")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[11]:
                self.__guiLecture.active()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseService("6")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[12]:
                self.__guiTache.active()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("9")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[13]:
                self.__guiTache.activeFinish()
                self.__textOut =  self.__gest.getLanguageObjet().getPhraseTime("11")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[14]:
                self.__guiTache.activeDel()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseTime("12")
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[15]:
                try :
                    self.__guiWork.activeAcceuil()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("7")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("8")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[16]:
                try :
                    self.__guiWork.activeProjet()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("1")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("2")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[17]:
                try :
                    self.__guiWork.activeTableur()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("3")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("4")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[18]:
                return  self.__guiManageTableur(self.__parms)
            elif self.__name_gui == self.__liste_gui[19]:
                if self.__guiWork.activeReadTableur():
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("21")
                    self.__valOut = 5
                    return True
                else :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("22")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[20]:
                try:
                    self.__guiWork.activeWord()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("5")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenGUIWork("6")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[21]:
                try:
                    self.__guiWork.activeReadWord()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkWord("9")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkWord("10")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[22]:
                try:
                    self.__guiWork.activeWriteWord()
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkWord("7")
                    self.__valOut = 5
                    return True
                except Exception as e:
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkWord("8")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[23]:
                if self.__guiWork.openTaskProjet() :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("10",
                                                                                  self.__gest.getGestFNC().getFNCWork().getNameProjet())
                    self.__valOut = 5
                    return True
                else :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("11")
                    self.__valOut = 1
                    return False

            elif self.__name_gui == self.__liste_gui[24]:
                if self.__guiWork.openTaskProjetAdd() :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("12",
                                                                                              self.__gest.getGestFNC().getFNCWork().getNameProjet())
                    self.__valOut = 5
                    return True
                else :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("13")
                    self.__valOut = 1
                    return False

            elif self.__name_gui == self.__liste_gui[25]:
                if self.__guiWork.openTaskProjetdel() :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("14",
                                                                                              self.__gest.getGestFNC().getFNCWork().getNameProjet())
                    self.__valOut = 5
                    return True
                else :
                    self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("15")
                    self.__valOut = 1
                    return False
            elif self.__name_gui == self.__liste_gui[26]:
                self.__guiTraducteur.active()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenTraducteur()
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[27]:
                dicte = self.__parms[0]
                liste = self.__parms[1]
                intIn = self.__parms[2]
                self.__guiResumer.activeView(dict=dicte,list=liste,intIn=intIn)
                self.__textOut = self.__gest.getLanguageObjet().getPhraseOpenTraducteur()
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[28]:
                self.__guiHelp.activeHelp(self.__parms[0])
                self.__textOut = self.__parms[1]
                self.__valOut = 5
                return True
            elif self.__name_gui == self.__liste_gui[29]:
                self.__guiBreef.activeBreef()
                self.__textOut = self.__gest.getLanguageObjet().getPhraseMorningBreef("1")
                self.__valOut = 5
                return True
            else :
                return False
        else :
            return False

    def __guiManageTableur(self,param:int):
        try :
            out = self.__guiWork.activeManageTableur(int(param))
        except Exception as e:
            self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("8")
            self.__valOut = 1
            return False

        if param == 1:
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("7")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("8")
                self.__valOut = 1
                return False
        elif param == 2 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("9")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("10")
                self.__valOut = 1
                return False
        elif param == 3 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("11")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("12")
                self.__valOut = 1
                return False
        elif param == 4 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("13")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("14")
                self.__valOut = 1
                return False
        elif param == 5 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("15")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("16")
                self.__valOut = 1
                return False
        elif param == 6 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("17")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("18")
                self.__valOut = 1
                return False
        elif param == 7 :
            if out :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("19")
                self.__valOut = 5
                return True
            else :
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("20")
                self.__valOut = 1
                return False
        else :
            self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("8")
            self.__valOut = 1
            return False


    def textOut(self):
        return self.__textOut

    def valOut(self):
        return self.__valOut


    def activeCalculatriceNormal(self):
        try :
            self.__guiCalculatrice.activeCalcule()
            return True
        except Exception as e:
            return False

    def activeCalculatriceComplex(self):
        try :
            self.__guiCalculatrice.activeComplex()
            return True
        except Exception as e:
            return False

    def activeCalculatricePythagore(self):
        try :
            self.__guiCalculatrice.activePythagore()
            return True
        except Exception as e:
            return False

    def activeOrthographe(self,texte:str):
        if texte != "":
            self.__guiOrthographe.active()
            self.__guiOrthographe.setTexte(texte)
        else :
            return

    def activeArreraDownload(self):
        self.__guiArreraDownload.active()

    def activeAgenda(self):
        self.__guiAgenda.active()

    def activeAgendaAdd(self):
        self.__guiAgenda.activeAdd()

    def activeAgendaDel(self):
        self.__guiAgenda.activeDel()

    def activeHorloge(self):
        self.__guiHorloge.active()

    def activeMinuteur(self):
        self.__guiHorloge.activeMinuteur()

    def activeChrono(self):
        self.__guiHorloge.activeChrono()

    def activeLecture(self):
        self.__guiLecture.active()

    def activeTache(self):
        self.__guiTache.active()

    def activeTaskFinish(self):
        self.__guiTache.activeFinish()

    def activeDelTask(self):
        self.__guiTache.activeDel()

    def activeWork(self):
        try :
            self.__guiWork.activeAcceuil()
            return True
        except Exception as e:
            return False

    def activeWorkProject(self):
        try :
            self.__guiWork.activeProjet()
            return True
        except Exception as e:
            return False

    def activeWorkTableur(self):
        try :
            self.__guiWork.activeTableur()
            return True
        except Exception as e:
            return False

    def activeManageTableur(self,mode:int):
        """
        1. Add Valeur
        2. Add Somme
        3. Add Moyenne
        4. Add Comptage
        5. Add Minimum
        6. Add Maximum
        7. Suppr valeur
        """
        return  self.__guiWork.activeManageTableur(mode)

    def activeReadTableur(self):
        return self.__guiWork.activeReadTableur()

    def activeWorkWord(self):
        try:
            self.__guiWork.activeWord()
            return True
        except Exception as e:
            return False

    def activeReadWord(self):
        return self.__guiWork.activeReadWord()

    def activeWriteWord(self):
        return self.__guiWork.activeWriteWord()

    def activeTaskProject(self,mode:int):
        """
        1. Add Projet
        2. Del Projet
        3. View Projet
        """
        match mode :
            case 1:
                return self.__guiWork.openTaskProjetAdd()
            case 2:
                return self.__guiWork.openTaskProjetdel()
            case 3:
                return self.__guiWork.openTaskProjet()
            case _ :
                return False

    def activeTraducteur(self):
        self.__guiTraducteur.active()

    def activeResumer(self):
        self.__guiResumer.active()

    def activeViewResumer(self,dict:dict=None,list:list=None, intIn:int=0):
        self.__guiResumer.activeView(dict=dict,list=list,intIn=intIn)

    def activeHelp(self, texte:str):
        self.__guiHelp.activeHelp(texte)

    def activeBreef(self):
        self.__guiBreef.activeBreef()