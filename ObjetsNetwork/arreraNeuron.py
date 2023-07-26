import datetime
import random
from librairy.travailJSON import *
from neuron.chatBots import*
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import *
from neuron.neuronMain import*

class ArreraNetwork :
    def __init__(self,name:str,user:str,genre:str,createur:str,bute:str,vous:bool,listFonction:list[str],fichierConfiguration:str):
        #initilisation objet 
        self.gestionnaire = gestionNetwork()
        self.FichierJSON = jsonWork(fichierConfiguration)
        #set des atribut
        self.gestionnaire.setAll(vous,genre,name,user,bute,createur,listFonction)
        #initilisation objet secondaire
        self.formuleNeuron = formule(self.gestionnaire)
        #initilisation des neuron
        self.chatBot = neuroneDiscution(self.gestionnaire,self.formuleNeuron)
        self.main = neuroneMain(self.gestionnaire,self.FichierJSON)
    
    def boot(self):
        hour = datetime.datetime.now().hour
        text= self.formuleNeuron.salutation(hour)
        self.gestionnaire.setHistory(text,"boot")
        return str(text)
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.formuleNeuron.aurevoir(hour)
        return str(text)
    
    def netoyage(self,chaine):
        chaine = str(chaine)
        chaine.replace("-"," ")
        chaine.replace('"'," ")
        chaine.replace("_"," ")
        chaine.replace('/'," ")
        chaine.replace("é","e")
        chaine.replace("è","e")
        chaine.replace("à","a")
        chaine.replace("ç","c")
        return chaine
    
    def neuron(self,var:str) :
        requette = self.netoyage(str(var).lower())
        valeur = 0
        self.main.neurone(requette)
        if valeur == 0 :
            #software
            valeur = 0
            text = ""
            if valeur == 0 :
                #api
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
                    else :
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