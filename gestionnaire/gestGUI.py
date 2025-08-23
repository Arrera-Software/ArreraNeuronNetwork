from gestionnaire.gestion import gestionnaire


class gestGUI:
    def __init__(self, gest: gestionnaire):
        self.__gest = gest
        # Importation des GUI
        from gui.GUICalculatrice import GUICalculatrice
        from gui.GUIorthographe import GUIOrthographe

        # Calculatrice
        self.__guiCalculatrice = GUICalculatrice(self.__gest)
        # Correcteur d'orthographe
        self.__guiOrthographe = GUIOrthographe(self.__gest)

    def activeCalculatriceNormal(self):
        self.__guiCalculatrice.activeCalcule()

    def activeCalculatriceComplex(self):
        self.__guiCalculatrice.activeComplex()

    def activeCalculatricePythagore(self):
        self.__guiCalculatrice.activePythagore()

    def activeOrthographe(self):
        self.__guiOrthographe.active()