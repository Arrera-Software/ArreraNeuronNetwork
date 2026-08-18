from gestionnaire.gestion import gestionnaire
from neuron.IARouter import IARouter
from neuron.interface import interface
from neuron.core_neuron import core_neuron
from neuron.markdown import neuroneMarkdown

class gestNeuron :
    def __init__(self,gestionnaire:gestionnaire) -> None:
        # Recuperation de l'etat du socket
        self.__etatSocket = gestionnaire.getConfigFile().etatSocket
        self.__brief_is_enabled = gestionnaire.getConfigFile().brief_enable
        # Creation du routeur principal (remplace les anciens neurones)
        self.iarouter = IARouter(gestionnaire)
        # Neurones socket
        self.ninterface = None
        self.nmarkdown = None
        self.ncore = core_neuron(gestionnaire)
        
        # Init des neurones socket
        if self.__etatSocket == 1 :
            self.ninterface = interface(gestionnaire)
            self.nmarkdown = neuroneMarkdown(gestionnaire)

    def getSocket(self):
        if self.__etatSocket == 1 :
            return True
        else :
            return False

    def getBrief(self):
        if self.__brief_is_enabled == 1 :
            return True
        else :
            return False