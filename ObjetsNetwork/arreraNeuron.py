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
    def __init__(self,name:str,user:str,genre:str,createur:str,bute:str,vous:bool,listFonction:list[str],fichierConfiguration:str,nbVille:int,listVille:str):
        #initilisation du gestionnaire du reseau de neuron 
        self.gestionnaire = gestionNetwork()
        #set des atribut
        self.gestionnaire.setAll(vous,genre,name,user,bute,createur,listFonction,nbVille)
        self.gestionnaire.setVilleMeteo(listVille)
        #initialisation objet
        self.formuleNeuron = formule(self.gestionnaire)
        self.FichierJSON = jsonWork(fichierConfiguration)
        self.arreraSoftware = fncArreraNetwork(self.FichierJSON,self.gestionnaire,"image/icon.png")
        #initilisation des neuron
        self.chatBot = neuroneDiscution(self.gestionnaire,self.formuleNeuron)
        self.main = neuroneMain(self.arreraSoftware,self.gestionnaire)
        self.api = neuroneAPI(self.arreraSoftware,self.gestionnaire)
    
    def boot(self):
        hour = datetime.datetime.now().hour
        text= self.formuleNeuron.salutation(hour)
        self.gestionnaire.setHistory(text,"boot")
        return str(text)
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.formuleNeuron.aurevoir(hour)
        return str(text)
    
    
    def neuron(self,var:str) :
        requette = chaine.netoyage(str(var))
        valeur = 0
        valeur,text = self.main.neurone(requette)
        if valeur == 0 :
            valeur,text = self.api.neurone(requette)
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
                                valeur,text = self.chatBot.neurone(requette)
                                if valeur == 0 :
                                    if "stop" in requette or "au revoir" in requette or "quitter" in requette or "bonne nuit" in requette or "adieu" in requette or "bonne soirée" in requette :
                                        text = self.formuleNeuron.aurevoir(datetime.datetime.now().hour)
                                        valeur = 15
                                    else : 
                                        valeur = 0 
                                        text = self.formuleNeuron.nocomprehension()   
        
        return valeur , text