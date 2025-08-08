from abc import abstractmethod
from gestionnaire.gestion import gestionnaire

class neuronBase :
    def __init__(self,gestionnaire:gestionnaire):
        #Init objet
        self._gestionNeuron = gestionnaire
        self._gestFNC = self._gestionNeuron.getGestFNC()
        self._objHistorique = None
        self._listSortie = ["",""]
        self._socket = self._gestionNeuron.getSocketObjet()
        self._language = self._gestionNeuron.getLanguageObjet()
        self._valeurOut = 0

    def getListSortie(self)->list:
        return self._listSortie

    def getValeurSortie(self)->int :
        return self._valeurOut

    @abstractmethod
    def neurone(self,requette:str):
        pass