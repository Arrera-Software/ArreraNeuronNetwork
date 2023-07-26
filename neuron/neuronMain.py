from ObjetsNetwork.gestion import*
from arreraSoftware.lecteurText import*
class neuroneMain :
    def __init__(self,gestionnaireNeuron:gestionNetwork,json:jsonWork) :
        #Init objet
        self.gestionNeuron = gestionnaireNeuron
        self.objetJSON = json
        
    def neurone(self,requette):
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
        if "tu peux me lire un truc" in requette or "vous pouvez lire un truc" in requette or  "lit un truc" in requette :
            if self.etatVous == True :
                text = "Voici "+self.genre
            else :
                text = "Voici"
            Reading(self.objetJSON,self.gestionNeuron)
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Sauvegarde des sortie                         
        self.gestionNeuron.setHistory(text,requette)
        #Ajout d'une discution
        self.gestionNeuron.addDiscution()
        #Retour des valeur
        return valeur , text