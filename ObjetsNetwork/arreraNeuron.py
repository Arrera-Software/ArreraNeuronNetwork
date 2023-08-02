import datetime
import random
from librairy.travailJSON import *
from neuron.chatBots import*
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import *
from neuron.neuronMain import*
from neuron.neuronAPI import*
from ObjetsNetwork.chaineCarractere import *

class ArreraNetwork :
    def __init__(self,userFile:str,fichierConfiguration:str):
        #Ouverture fichier de configuration
        self.fichierUtilisateur = jsonWork(userFile)
        self.configNeuron = jsonWork(fichierConfiguration)
        #initilisation du gestionnaire du reseau de neuron 
        self.gestionnaire = gestionNetwork(self.fichierUtilisateur,self.configNeuron)
        #set des atribut
        self.gestionnaire.setAll()
        self.gestionnaire.setVilleMeteo()
        #initialisation objet
        self.formuleNeuron = formule(self.gestionnaire)
        self.fonctionAssistant = fncArreraNetwork(self.configNeuron,self.gestionnaire,)
        #initilisation des neuron
        self.chatBot = neuroneDiscution(self.gestionnaire,self.formuleNeuron)
        self.main = neuroneMain(self.fonctionAssistant,self.gestionnaire)
        self.api = neuroneAPI(self.fonctionAssistant,self.gestionnaire)
    
    def boot(self):
        hour = datetime.datetime.now().hour
        text= self.formuleNeuron.salutation(hour)
        self.oldRequette = "boot"
        self.oldSorti = text
        return str(text)
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.formuleNeuron.aurevoir(hour)
        return str(text)
    
    
    def neuron(self,var:str) :
        requette = chaine.netoyage(str(var))
        valeur = 0
        valeur,text = self.main.neurone(requette,self.oldSorti,self.oldRequette)
        if valeur == 0 :
            valeur,text = self.api.neurone(requette,self.oldSorti,self.oldRequette)
            if valeur == 0 :
                #software
                valeur = 0
                text = ""
                if valeur == 0 :
                    #time
                    valeur = 0
                    text = ""
                    if valeur == 0 :
                        #internet
                        valeur = 0
                        text = ""
                        if valeur == 0 :
                            #search
                            valeur = 0
                            text = ""
                            if valeur == 0 :
                                valeur,text = self.chatBot.neurone(requette,self.oldSorti,self.oldRequette)
                                if valeur == 0 :
                                    if "stop" in requette or "au revoir" in requette or "quitter" in requette or "bonne nuit" in requette or "adieu" in requette or "bonne soirée" in requette :
                                        text = self.formuleNeuron.aurevoir(datetime.datetime.now().hour)
                                        valeur = 15
                                    else : 
                                        valeur = 0 
                                        text = self.formuleNeuron.nocomprehension()
                                        self.gestionnaire.addDiscution()
                                
        #Sauvegarde des sortie                         
        self.oldRequette = requette
        self.oldSorti = text
        #Ajout d'une discution
        self.gestionnaire.addDiscution() 
        return valeur , text