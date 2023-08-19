from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneSoftware :
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
        #reponse neuron software
        if "telecharge" in requette :
            if "video" in requette :
                text = self.fonctionArreraNetwork.sortieDownload("video")
            else :
                if "musique" in requette :
                    text = self.fonctionArreraNetwork.sortieDownload("music")
                else :
                    if self.etatVous == True :
                        text = "Je suis désoler "+self.genre+" mais je ne peux télécharger que des vidéo ou de musique"
                    else :
                        text = self.user+" je ne peux télécharger que de video ou de musique. "
        if "calculatrice" in requette or "calculette" in requette :
            if "nombre complex" in requette or "nb complex" in requette :
                text = self.fonctionArreraNetwork.sortieCalculatrice("1")
            else :
                text = self.fonctionArreraNetwork.sortieCalculatrice("0")
        else :
            if "pythagore" in requette :
                text = self.fonctionArreraNetwork.sortieCalculatrice("2")
                
                                    
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text