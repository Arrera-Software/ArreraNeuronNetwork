from gestionnaire.gestion import gestionnaire


class gestGUI:
    def __init__(self, gest: gestionnaire):
        self.__gest = gest
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

    def activeCalculatriceNormal(self):
        self.__guiCalculatrice.activeCalcule()

    def activeCalculatriceComplex(self):
        self.__guiCalculatrice.activeComplex()

    def activeCalculatricePythagore(self):
        self.__guiCalculatrice.activePythagore()

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
        self.__guiWork.activeAcceuil()

    def activeWorkProject(self):
        self.__guiWork.activeProjet()

    def activeWorkTableur(self):
        self.__guiWork.activeTableur()

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

    def activeWorkWord(self):
        self.__guiWork.activeWord()

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