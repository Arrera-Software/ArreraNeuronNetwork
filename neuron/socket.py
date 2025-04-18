from neuron.CNeuronBase import *
from objet.parreraclient import *

class neuroneSocket(neuronBase):
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique):
        #Init objet
        self.__socket = PArreraClient(gestionnaire.getName())
        self.__serverOn = self.__socket.connectToServeur("ws://127.0.0.1:6666")
        self.__sortieMessage = ""
        self.__language = gestionnaire.getLanguageObjet()
        super().__init__(fncArreraNetwork, gestionnaire,objHist)

    def neurone(self,requette:str):
        if self._gestNeuron.getTime() == True  and self.__serverOn == True :
            if ("recherche" in requette):
                recherche = requette.replace("recherche","").strip()
                self.__socket.sendMessage("recherche " + recherche)
                self._listSortie = [self.__language.getPhraseSearch("3"),""]
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

    def stopSocket(self):
        self.__socket.disconnect()
        self.__serverOn = False