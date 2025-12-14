import datetime
from neuron.CNeuronBase import *


class neuroneChatbot(neuronBase) :
    def __init__(self, gestionnaire:gestionnaire):
        #Init objet
        super().__init__(gestionnaire)
        # self.__formule = self._gestNeuro
        self.__language = self._gestionnaire.getLanguageObjet()
        self.__gestIA = self._gestionnaire.getGestIA()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self.__gestIA.get_ia_is_enable():
            if self.__gestIA.send_request_ia(requette):
                if self.__gestIA.get_state_ia_reponse():
                    self._listSortie = [self.__gestIA.get_reponse_ia(),""]
                    self._valeurOut = 1
                else :
                    self._valeurOut = 0
            else :
                self._valeurOut = 0
        else :
            self._valeurOut = 0