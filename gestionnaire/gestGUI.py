from gestionnaire.gestion import gestionnaire


class gestGUI:
    def __init__(self, gest: gestionnaire):
        self.__gest = gest
        # Importation des GUI
        from gui.GUICalculatrice import GUICalculatrice

        # Calculatrice
        self.__guiCalculatrice = GUICalculatrice(self.__gest)

    def activeCalculatrice(self):
        self.__guiCalculatrice.active()

