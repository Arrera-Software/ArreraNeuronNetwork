from gestionnaire.gestion import *
from gestionnaire.gestSocket import *

class fncBase:
    def __init__(self, gestionnaire:gestionnaire):
        self.__gestionnaire = gestionnaire
        self.__gestSocket = self.__gestionnaire.getSocketObjet()
        self.__gestLang = self.__gestionnaire.getLanguageObjet()
        # Librairy
        self.__dectOS = self.__gestionnaire.getOSObjet()