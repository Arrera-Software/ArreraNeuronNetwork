from config.confNeuron import confNeuron
from gestionnaire.gestion import *
from neuron.API import *
from neuron.chatBots import *
from neuron.codehelp import *
from neuron.open import *
from neuron.search import *
from neuron.service import *
from neuron.software import *
from neuron.time import *
from neuron.work import *

class gestNeuron :
    def __init__(self,gestionnaire:gestionnaire, objHist:gestHistorique) -> None:
        # Recuperation des etat de chaque neurone
        self.__etatService = gestionnaire.getConfigFile().etatService
        self.__etatSoftware = gestionnaire.getConfigFile().etatSoftware
        self.__etatTime = gestionnaire.getConfigFile().etatTime
        self.__etatOpen = gestionnaire.getConfigFile().etatOpen
        self.__etatSearch = gestionnaire.getConfigFile().etatSearch
        self.__etatChatbot = gestionnaire.getConfigFile().etatChatbot
        self.__etatApi = gestionnaire.getConfigFile().etatApi
        self.__etatCodehelp = gestionnaire.getConfigFile().etatCodehelp
        self.__etatWork = gestionnaire.getConfigFile().etatWork
        self.__etatSocket = gestionnaire.getConfigFile().etatSocket
        # Creation des varriable des neurones
        self.napi = None
        self.nchatbot = None
        self.ncodehelp = None
        self.nopen = None
        self.nsearch = None
        self.nservice = None
        self.nsoftware = None
        self.ntime = None
        self.nwork = None
        # Init des neurones
        if self.__etatService == 1 :
            self.nservice = neuroneService(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatSoftware == 1 :
            self.nsoftware = neuroneSoftware(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatTime == 1 :
            self.ntime = neuroneTime(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatOpen == 1 :
            self.nopen = neuroneOpen(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatSearch == 1 :
            self.nsearch = neuroneSearch(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatChatbot == 1 :
            self.nchatbot = neuroneChatbot(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatApi == 1 :
            self.napi = neuroneAPI(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatCodehelp == 1 :
            self.ncodehelp = neuroneCodehelp(fncArreraNetwork, gestionnaire, objHist)
        if self.__etatWork == 1 :
            self.nwork = neuroneWork(fncArreraNetwork, gestionnaire, objHist)


    def getSocket(self):
        if self.__etatSocket == 1 :
            return True
        else :
            return False