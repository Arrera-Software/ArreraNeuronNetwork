from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
class neuroneMain :
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
        #reponse du neuron main
        if "lire un truc" in requette or  "lit un truc" in requette :
            text = self.fonctionArreraNetwork.reading()
        else :
            if "calcule" in requette :
                requette = requette.replace("calcule","")
                requette = requette.replace(" ","")
                if "1" in requette or "2" in requette  or "3" in requette or "4" in requette or "5" in requette or "6" in requette  or "7" in requette or "8" in requette or "9" in requette or "0" in requette and "+" in requette or "-" in requette or "*" in requette or "/" in requette :
                    resultat =  eval(requette)
                    if self.etatVous == True :
                        text = "Voici le resultat de votre calcule "+self.genre+" est "+str(resultat)
                    else :
                        text = "Voici le resultat de ton calcule "+self.user+" est "+str(resultat)
                else :
                    if self.etatVous == True :
                        text = "Le calcule que vous me demander de faire "+self.genre+" est imposible a faire."
                    else :
                        text = "Le calcule que tu me demande de faire est imposible."
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text