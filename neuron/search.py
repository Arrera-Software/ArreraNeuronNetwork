from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneSearch:
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #Recuperation atribut de l'assistant
        self.oldrequette = oldRequette
        self.oldsortie = oldSortie
        self.nbDiscution = self.gestionNeuron.getNbDiscution()
        self.name = self.gestionNeuron.getName()
        self.etatVous = self.gestionNeuron.getVous()
        self.genre = self.gestionNeuron.getGenre()
        self.user = self.gestionNeuron.getUser()
        self.bute = self.gestionNeuron.getBute()
        self.createur = self.gestionNeuron.getCreateur()
        #reponse neuron search
        if "bigsearch" in requette or "grand recherche" in requette :
            text = self.fonctionArreraNetwork.sortieGrandRecherche(requette)
        else :
            if "search" in requette or "recherche" in requette :
                text = self.fonctionArreraNetwork.sortieRechercheSimple(requette)
            
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text
            