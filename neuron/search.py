from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneSearch:
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__gestNeuron = neuronGest
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__listSortie = ["",""]

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        if self.__gestNeuron.getSearch() == True :
            #Initilisation des variable nbRand et text et valeur
            valeur = 0
            self.__listSortie = ["",""]
            #reponse neuron search
            if (("bigsearch" in requette )or ("grand recherche" in requette)) :
                self.__listSortie = [self.__fonctionArreraNetwork.sortieGrandRecherche(requette),""]
            else :
                if (("search" in requette) or ("recherche" in requette)) :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieRechercheSimple(requette),""]    
            #Mise a jour de la valeur                                                               
            valeur = self.__gestionNeuron.verrifSortie(self.__listSortie[0])
            #Retour des valeur
            return valeur , self.__listSortie
        else :
            return 0 , ""
            