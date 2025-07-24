from abc import abstractmethod
from gestionnaire.gestion import*
from fnc.fncArreraNetwork import*
from gestionnaire.gestSTR import*
from gestionnaire.gestNeuron import*
from gestionnaire.gestHistorique import*

class neuronBase :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionnaire, objHist:gestHistorique):
        #Init objet
        self._gestionNeuron = gestionnaire
        self._fonctionArreraNetwork = fncArreraNetwork
        self._gestNeuron = self._gestionNeuron.getGestNeuron()
        self._objHistorique = objHist
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