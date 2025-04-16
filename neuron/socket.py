from neuron.CNeuronBase import *
from objet.parreraclient import *

class neuroneSocket(neuronBase):
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique):
        #Init objet
        super().__init__(fncArreraNetwork, gestionnaire,objHist)
        self.__socket = PArreraClient(gestionnaire.getName())
        self.__serverOn = self.__socket.connectToServeur("ws://127.0.0.1:12345")
        self.__sortieMessage = ""

    def neurone(self,requette:str):
        if self._gestNeuron.getTime() == True  and self.__serverOn == True :
            if ("send" in requette):
                msg = requette.replace("send","").strip()
                self.__socket.sendMessage(msg)
                self._listSortie = ["Message envoyer",""]
                self._valeurOut = 1
            else :
                self._valeurOut = 0


    def receivedMessageServer(self):
        message = self.__socket.receiveMessage()
        if message:
            # Traitement du message reçu
            self.__sortieMessage = message
            return True
        else:
            return False

    def getMessageServer(self):
        return self.__sortieMessage