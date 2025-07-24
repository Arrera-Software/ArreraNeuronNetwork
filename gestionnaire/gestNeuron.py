from config.confNeuron import confassistant
from gestionnaire.gestion import *
from gestionnaire.gestHistorique import *
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
    def __init__(self,fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionnaire, objHist:gestHistorique) -> None:
        # Recuperation des etat de chaque neurone
        self.__etatService = confassistant.etatService
        self.__etatSoftware = confassistant.etatSoftware
        self.__etatTime = confassistant.etatTime
        self.__etatOpen = confassistant.etatOpen
        self.__etatSearch = confassistant.etatSearch
        self.__etatChatbot = confassistant.etatChatbot
        self.__etatApi = confassistant.etatApi
        self.__etatCodehelp = confassistant.etatCodehelp
        self.__etatWork = confassistant.etatWork
        self.__etatSocket = confassistant.etatSocket
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