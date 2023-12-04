from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneSearch:
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #reponse neuron search
        if "bigsearch" in requette or "grand recherche" in requette :
            text = self.__fonctionArreraNetwork.sortieGrandRecherche(requette)
        else :
            if "search" in requette or "recherche" in requette :
                text = self.__fonctionArreraNetwork.sortieRechercheSimple(requette)
            
        #Mise a jour de la valeur                                                               
        valeur = self.__gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text
            