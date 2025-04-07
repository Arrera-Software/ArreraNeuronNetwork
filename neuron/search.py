from neuron.CNeuronBase import *

class neuroneSearch(neuronBase) :

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self.__valeurOut = 0
        if self._gestNeuron.getSearch() == True :
            #reponse neuron search
            if (("bigsearch" in requette )or ("grand recherche" in requette)) :
                text,recherche = self._fonctionArreraNetwork.sortieGrandRecherche(requette)
                self._listSortie = [text, ""]
                self._objHistorique.setAction("bigrecherche " + recherche)
            elif (("search" in requette) or ("recherche" in requette)) :
                    text,recherche = self._fonctionArreraNetwork.sortieRechercheSimple(requette)
                    self._listSortie = [text, ""]
                    self._objHistorique.setAction("recherche " + recherche)
            #Mise a jour de la valeur                                                               
            self.__valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])