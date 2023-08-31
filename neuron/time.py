from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneTime :
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
        #reponse neuron time
        if "heure" in requette :
            text = self.fonctionArreraNetwork.sortieHeure()
        else :
            if "date" in requette :
                text = self.fonctionArreraNetwork.sortieDate()
            else :
                if "chronometre" in requette or "chrono" in requette :
                    text = self.fonctionArreraNetwork.sortieOpenChrono()
                else :
                    if "horloge" in requette :
                        text = self.fonctionArreraNetwork.sortieOpenHorloge()
                    else :
                        if "minuteur" in requette :
                            text = self.fonctionArreraNetwork.sortieOpenSimpleMinuteur()
                        else :
                            if "ajouter un rendez-vous" in requette or "ajout un rendez-vous"  in requette or "ajout evenement" in requette or "ajout rappel" in requette or "ajout un evenement" in requette or "ajout un rappel" in requette or "ajouter un evenement" in requette or "ajouter  un rappel" in requette:
                                text = self.fonctionArreraNetwork.sortieAjoutEvent()
                            else :
                                if "suppr un rendez-vous" in requette or "supprimer un rendez-vous"  in requette or "suppr evenement" in requette or "suppr rappel" in requette or "suppr un evenement" in requette or "suppr un rappel" in requette or "supprimer un evenement" in requette or "supprimer un rappel" in requette:
                                    text = self.fonctionArreraNetwork.sortieSupprEvent()
                                else :
                                    if "evenement d'aujourd'hui" in requette or "evenement du jour" in requette or "rendez-vous d'aujourd'hui" in requette or "rappel aujourd'hui" in requette:
                                        text = self.fonctionArreraNetwork.sortieEvenementDay()
                                    
            
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text