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

    def activeHorloge(self):
        self.__guiHorloge.active()

    def activeMinuteur(self):
        self.__guiHorloge.activeMinuteur()

    def activeChrono(self):
        self.__guiHorloge.activeChrono()

    def activeLecture(self):
        self.__guiLecture.active()