import datetime
import random
from librairy.dectectionOS import*
from librairy.travailJSON import *
from neuron.chatBots import*
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import *
from ObjetsNetwork.network import*
from neuron.main import*
from neuron.API import*
from neuron.software import*
from neuron.open import *
from neuron.search import*
from neuron.time import*
from ObjetsNetwork.chaineCarractere import *


class ArreraNetwork :
    def __init__(self,userFile:str,fichierConfiguration:str,fileFete:str):
        #Ouverture fichier de configuration
        self.fichierUtilisateur = jsonWork(userFile)
        self.configNeuron = jsonWork(fichierConfiguration)
        self.fichierVille = jsonWork(fileFete)
        #initilisation du gestionnaire du reseau de neuron
        self.detecteurOS = OS()
        self.gestionnaire = gestionNetwork(self.fichierUtilisateur,self.configNeuron,self.detecteurOS,self.fichierVille)
        self.network = network()
        #set des atribut
        self.gestionnaire.setAll()
        self.gestionnaire.setVilleMeteo()
        #initialisation objet
        self.formuleNeuron = formule(self.gestionnaire)
        self.fonctionAssistant = fncArreraNetwork(self.configNeuron,self.gestionnaire,self.detecteurOS,self.network)
        #recuperation etat du reseau
        self.etatReseau = self.network.getEtatInternet()
        #initilisation des neuron
        self.chatBot = neuroneDiscution(self.gestionnaire,self.formuleNeuron)
        self.main = neuroneMain(self.fonctionAssistant,self.gestionnaire)
        self.api = neuroneAPI(self.fonctionAssistant,self.gestionnaire)
        self.software = neuroneSoftware(self.fonctionAssistant,self.gestionnaire)
        self.open = neuroneOpen(self.fonctionAssistant,self.gestionnaire)
        self.search = neuroneSearch(self.fonctionAssistant,self.gestionnaire)
        self.time = neuroneTime(self.fonctionAssistant,self.gestionnaire)
    
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
            #api
            if self.etatReseau == True :
                valeur,text = self.api.neurone(requette,self.oldSorti,self.oldRequette)
            else :
                valeur = 0 
            if valeur == 0 :
                #software
                valeur,text = self.software.neurone(requette,self.oldSorti,self.oldRequette)
                if valeur == 0 :
                    #time
                    valeur,text = self.time.neurone(requette,self.oldSorti,self.oldRequette)
                    if valeur == 0 :
                        #open
                        valeur,text = self.open.neurone(requette,self.oldSorti,self.oldRequette)
                        if valeur == 0 :
                            #search
                            if self.etatReseau == True :
                                valeur,text = self.search.neurone(requette,self.oldSorti,self.oldSorti)
                            else :
                                valeur = 0
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