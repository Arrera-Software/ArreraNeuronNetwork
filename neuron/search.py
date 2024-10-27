from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuroneSearch:
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork, objHist:CHistorique) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__objHistorique = objHist
        self.__listSortie = ["",""]

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getSearch() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            #reponse neuron search
            if (("bigsearch" in requette )or ("grand recherche" in requette)) :
                text,recherche = self.__fonctionArreraNetwork.sortieGrandRecherche(requette)
                self.__listSortie = [text,""]
                self.__objHistorique.setAction("bigrecherche "+recherche)
            else :
                if (("search" in requette) or ("recherche" in requette)) :
                    text,recherche = self.__fonctionArreraNetwork.sortieRechercheSimple(requette)
                    self.__listSortie = [text,""] 
                    self.__objHistorique.setAction("recherche "+recherche)   
            #Mise a jour de la valeur                                                               
            self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])