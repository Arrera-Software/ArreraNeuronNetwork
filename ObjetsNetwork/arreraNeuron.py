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
        self.__fichierUtilisateur = jsonWork(userFile)
        self.__configNeuron = jsonWork(fichierConfiguration)
        self.__fichierVille = jsonWork(fileFete)
        #initilisation du gestionnaire du reseau de neuron
        self.__detecteurOS = OS()
        self.__gestionnaire = gestionNetwork(self.__fichierUtilisateur,self.__configNeuron,self.__detecteurOS,self.__fichierVille)
        self.__network = network()
        #set des atribut
        self.__gestionnaire.setAll()
        self.__gestionnaire.setVilleMeteo()
        #initialisation objet
        self.__formuleNeuron = formule(self.__gestionnaire)
        self.__fonctionAssistant = fncArreraNetwork(self.__configNeuron,self.__gestionnaire,self.__detecteurOS,self.__network)
        #recuperation etat du reseau
        self.__etatReseau = self.__network.getEtatInternet()
        #initilisation des neuron
        self.__etatNeuron = [self.__configNeuron.lectureJSON("chatBot"),
                         self.__configNeuron.lectureJSON("main"),
                         self.__configNeuron.lectureJSON("API"),
                         self.__configNeuron.lectureJSON("software"),
                         self.__configNeuron.lectureJSON("open"),
                         self.__configNeuron.lectureJSON("search"),
                         self.__configNeuron.lectureJSON("time")]
        if self.__etatNeuron[0] == "1":
            self.__chatBot = neuroneDiscution(self.__gestionnaire,self.__formuleNeuron)
        if self.__etatNeuron[1] == "1":
            self.__main = neuroneMain(self.__fonctionAssistant,self.__gestionnaire)
        if self.__etatNeuron[2] == "1":
            self.__api = neuroneAPI(self.__fonctionAssistant,self.__gestionnaire)
        if self.__etatNeuron[3] == "1":
            self.__software = neuroneSoftware(self.__fonctionAssistant,self.__gestionnaire)
        if self.__etatNeuron[4] == "1":
            self.__open = neuroneOpen(self.__fonctionAssistant,self.__gestionnaire)
        if self.__etatNeuron[5] == "1":
            self.__search = neuroneSearch(self.__fonctionAssistant,self.__gestionnaire)
        if self.__etatNeuron[6] == "1":
            self.__time = neuroneTime(self.__fonctionAssistant,self.__gestionnaire)
    
    def boot(self):
        hour = datetime.datetime.now().hour
        text= self.__formuleNeuron.salutation(hour)
        self.__oldRequette = "boot"
        self.__oldSorti = text
        return str(text)
    
    def setOld(self,requette:str,sortie:str):
        self.__oldRequette = requette
        self.__oldSorti = sortie
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.__formuleNeuron.aurevoir(hour)
        return str(text)

    def transformeListSTR(self,list:list)->str:
        return str(list[0])
    
    def phraseActu(self,actu1:str,actu2:str,actu3:str):
        if self.__gestionnaire.getVous() == True :
            return str("Les actualités du jour sont "+actu1+" "+actu2+" "+actu3+".")
        else :
            return str("Les actu du jour sont "+actu1+" "+actu2+" "+actu3+".")
    
    def neuron(self,var:str) :
        requette = chaine.netoyage(str(var))
        valeur = 0
        listOut =  []
        valeur,text = self.__main.neurone(requette,self.__oldSorti,self.__oldRequette)
        if valeur == 0  and self.__etatNeuron[0] == "1":
            #software
            valeur,text = self.__software.neurone(requette,self.__oldSorti,self.__oldRequette)
            if valeur == 0  and self.__etatNeuron[1] == "1":
                #time
                valeur,text = self.__time.neurone(requette,self.__oldSorti,self.__oldRequette)
                if valeur == 0 :
                    #open
                    valeur,text = self.__open.neurone(requette,self.__oldSorti,self.__oldRequette)
                    if valeur == 0 and self.__etatNeuron[2] == "1" :
                        #search
                        if self.__etatReseau == True :
                            valeur,text = self.__search.neurone(requette,self.__oldSorti,self.__oldSorti)
                        else :
                            valeur = 0
                        if valeur == 0 and self.__etatNeuron[3] == "1" :
                            valeur,text = self.__chatBot.neurone(requette,self.__oldSorti,self.__oldRequette)
                            if valeur == 0 and self.__etatNeuron[4] == "1" :
                                #api
                                if self.__etatReseau == True :
                                    valeur,listOut = self.__api.neurone(requette,self.__oldSorti,self.__oldRequette)
                                else :
                                    valeur = 0
                                if valeur == 0  nd self.__etatNeuron[1] == "1":
                                    if "stop" in requette or "au revoir" in requette or "quitter" in requette or "bonne nuit" in requette or "adieu" in requette or "bonne soirée" in requette or "arreter" in requette :
                                        text = self.__formuleNeuron.aurevoir(datetime.datetime.now().hour)
                                        valeur = 15
                                    else : 
                                        valeur = 0 
                                        text = self.__formuleNeuron.nocomprehension()
                                        self.__gestionnaire.addDiscution()
        #Creation de la liste de sortie
        if ((valeur  != 3) and (valeur != 12) and (valeur != 11) and (valeur!=4)) :
            listOut =  [text,""]
        #Sauvegarde des sortie                         
        self.__oldRequette = requette
        #Sauvegarde de la sortie 
        if ((valeur  == 3) or (valeur == 12) or (valeur == 11)) :
            self.__oldSorti = "requette api"      
        else :
            self.__oldSorti = listOut[0]
        #Ajout d'une discution
        self.__gestionnaire.addDiscution() 
        return valeur , listOut