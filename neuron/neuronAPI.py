from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneAPI :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork
        
    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #Recuperation atribut de l'assistant
        self.oldrequette = self.gestionNeuron.getOldrequette()
        self.oldsortie = self.gestionNeuron.getOldSortie()
        self.nbDiscution = self.gestionNeuron.getNbDiscution()
        self.name = self.gestionNeuron.getName()
        self.etatVous = self.gestionNeuron.getVous()
        self.genre = self.gestionNeuron.getGenre()
        self.user = self.gestionNeuron.getUser()
        self.bute = self.gestionNeuron.getBute()
        self.createur = self.gestionNeuron.getCreateur()
        #reponse du neuron main
        if "actualites" in requette :
            text = self.fonctionArreraNetwork.sortieActualités()
        else :
            if "meteo" in requette :
                nb = self.gestionNeuron.getnbVilleMeteo()
                villes = self.gestionNeuron.getListVilleMeteo()
                resultat = 0 
                for i in range(0,nb):
                    ville = chaine.netoyage(villes[i])
                    if ville in requette :
                        text = self.fonctionArreraNetwork.sortieMeteo(villes[i])
                        resultat = 1
                        break
                    else :
                        resultat = 0
                if resultat == 0 :
                    text = self.fonctionArreraNetwork.sortieMeteo("")  
                    
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Sauvegarde des sortie                         
        self.gestionNeuron.setHistory(text,requette)
        #Ajout d'une discution
        self.gestionNeuron.addDiscution()
        #Retour des valeur
        return valeur , text