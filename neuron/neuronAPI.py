from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*

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
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Sauvegarde des sortie                         
        self.gestionNeuron.setHistory(text,requette)
        #Ajout d'une discution
        self.gestionNeuron.addDiscution()
        #Retour des valeur
        return valeur , text