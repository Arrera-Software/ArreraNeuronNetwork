from abc import abstractmethod

from gestionnaire.gestion import*
from librairy.arrera_tk import *
from fnc.fncBase import fncBase

class GuiBase:
    def __init__(self,gestionnaire:gestionnaire,fnc:fncBase,name:str):
        # Init objet
        self.__gestionnaire = gestionnaire
        self.__titleGUI = self.__gestionnaire.getName()+" "+ name
        self.__icon = self.__gestionnaire.getIcon()
        # Arrera TK
        self.__arrtk = CArreraTK()
        # Init de la var de la fenetre
        self.__gui = None
        # Recuperation de la fonction
        self.__fnc = fnc

    @abstractmethod
    def __mainframe(self):
        pass

    def active(self):
        self.screen = self.__arrtk.aTopLevel(
            title=self.__titleGUI,
            width=800,
            height=600,
            resizable=True,
            icon=self.__icon,
        )
        self.__mainframe()
