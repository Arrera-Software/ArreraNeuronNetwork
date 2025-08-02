from abc import abstractmethod

from gestionnaire.gestion import*
from librairy.arrera_tk import *
from fnc.fncBase import fncBase

class GuiBase:
    def __init__(self,gestionnaire:gestionnaire,name:str):
        # Init objet
        self._gestionnaire = gestionnaire
        self._titleGUI = self._gestionnaire.getName() + " : " + name
        self.__icon = self._gestionnaire.getIcon()
        self.__btnColor = self._gestionnaire.getConfigFile().assistant_color
        self.__btnTexteColor = self._gestionnaire.getConfigFile().assistant_text_color
        # Arrera TK
        self.__arrtk = CArreraTK()
        # Init de la var de la fenetre
        self.__gui = None
        self._screen = None

    @abstractmethod
    def __mainframe(self):
        pass

    def active(self):
        self._screen = self.__arrtk.aTopLevel(
            title=self._titleGUI,
            width=800,
            height=600,
            resizable=True,
            icon=self.__icon,
        )
        self.__mainframe()
