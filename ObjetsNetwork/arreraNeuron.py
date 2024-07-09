from librairy.dectectionOS import*
from librairy.travailJSON import *
from neuron.chatBots import*
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import *
from ObjetsNetwork.network import*
from neuron.service import*
from neuron.API import*
from neuron.software import*
from neuron.open import *
from neuron.search import*
from neuron.time import*
from neuron.codehelp import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class ArreraNetwork :
    def __init__(self,userFile:str,fichierConfiguration:str,fileFete:str):
        # Declaration des diferente var 
        self.__listOut =  [] 
        self.__valeurOut = int
        #Ouverture fichier de configuration
        self.__fichierUtilisateur = jsonWork(userFile)
        self.__configNeuron = jsonWork(fichierConfiguration)
        self.__fichierVille = jsonWork(fileFete)
        #initilisation du gestionnaire du reseau de neuron
        self.__detecteurOS = OS()
        self.__etatNeuron = GestArreraNeuron(self.__configNeuron)
        self.__gestionnaire = gestionNetwork(self.__fichierUtilisateur,self.__configNeuron,self.__detecteurOS,self.__fichierVille)
        self.__network = network()
        #set des atribut
        self.__gestionnaire.setAll()
        #initialisation objet
        self.__formuleNeuron = formule(self.__gestionnaire)
        self.__fonctionAssistant = fncArreraNetwork(self.__configNeuron,self.__gestionnaire,self.__detecteurOS,self.__network)
        #recuperation etat du reseau
        self.__etatReseau = self.__network.getEtatInternet()
        #initilisation des neuron
        self.__chatBot = neuroneDiscution(self.__gestionnaire,self.__formuleNeuron,self.__etatNeuron)
        self.__service = neuroneService(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__api = neuroneAPI(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__software = neuroneSoftware(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__open = neuroneOpen(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__search = neuroneSearch(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__time = neuroneTime(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
        self.__codehelp = neuroneCodehelp(self.__fonctionAssistant,self.__gestionnaire,self.__etatNeuron)
    
    def realoadUserData(self):
        """
        Methode qui permet de recharger tout les donnée utilisateur
        """
        self.__gestionnaire.setAll()

    def boot(self):
        hour = datetime.now().hour
        text= self.__formuleNeuron.salutation(hour)
        self.__gestionnaire.setOld("boot","boot")
        return str(text)
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.__formuleNeuron.aurevoir(hour)
        return str(text)
    
    def getListSortie(self)->list :
        return self.__listOut 

    def getValeurSortie(self)->int :
        """
        0 : Aucun sortie
        1 : Sortie normale
        3 : Sortie actu
        4 : Meteo / temperature / GPS
        5 : Sortie avec fenetre tkinter
        11 : Erreur du resumer 
        12 : Reussite du resumer
        15 : Arret de l'assistant
        """
        return self.__valeurOut

    
    def neuron(self,var:str) :
        # Var local
        requette = chaine.netoyage(str(var))
        # Var de l'objet
        self.__valeurOut = 0
        self.__listOut =  []
        print (requette)

        # Service
        self.__service.neurone(requette)
        self.__valeurOut = self.__service.getValeurSortie()
         
        if self.__valeurOut == 0 :
            #software
            self.__software.neurone(requette)
            self.__valeurOut = self.__software.getValeurSortie()
            
            if self.__valeurOut == 0 :
                #time
                self.__time.neurone(requette)
                self.__valeurOut = self.__time.getValeurSortie()
                
                if self.__valeurOut == 0 :
                    #code help 
                    self.__codehelp.neurone(requette)
                    self.__valeurOut = self.__codehelp.getValeurSortie()
                    if (self.__valeurOut == 0 ):
                        #open
                        self.__open.neurone(requette)
                        self.__valeurOut = self.__open.getValeurSortie()
                        
                        if self.__valeurOut == 0 :
                            #search
                            if self.__etatReseau == True :
                                self.__search.neurone(requette)
                                self.__valeurOut = self.__search.getValeurSortie()
                            else :
                                self.__valeurOut = 0
                            
                            if self.__valeurOut == 0 :
                                self.__chatBot.neurone(requette)
                                self.__valeurOut = self.__chatBot.getValeurSortie()
                                
                                if self.__valeurOut == 0 :
                                    #api
                                    if self.__etatReseau == True :
                                        self.__api.neurone(requette)
                                        self.__valeurOut = self.__api.getValeurSortie()
                                    else :
                                        self.__valeurOut = 0
                                    
                                    if self.__valeurOut == 0 :
                                        if (("stop" in requette) or ("au revoir" in requette) 
                                            or ("quitter" in requette) or ("bonne nuit" in requette) 
                                            or ("adieu" in requette) or ("bonne soirée" in requette) 
                                            or ("arreter" in requette)) :
                                            self.__listOut = [self.__formuleNeuron.aurevoir(datetime.now().hour),""]
                                            self.__valeurOut = 15
                                        else : 
                                            self.__valeurOut = 0 
                                            self.__listOut = [self.__formuleNeuron.nocomprehension(),""]
                                            self.__gestionnaire.addDiscution()
                                    else :
                                        self.__listOut = self.__api.getListSortie()
                                else :
                                    self.__listOut = self.__chatBot.getListSortie()
                            else :
                                self.__listOut = self.__search.getListSortie()
                        else :
                            self.__listOut = self.__open.getListSortie()
                    else :
                        self.__listOut = self.__codehelp.getListSortie()
                else :
                    self.__listOut = self.__time.getListSortie()
            else :
                self.__listOut = self.__software.getListSortie()
        else :
            self.__listOut = self.__service.getListSortie()

        #Sauvegarde de la sortie et de l'entré 
        if ((self.__valeurOut  == 3) or (self.__valeurOut == 12) or (self.__valeurOut == 11)) :
            self.__gestionnaire.setOld("requette api",requette)     
        else :
            self.__gestionnaire.setOld(self.__listOut[0],requette)
        #Ajout d'une discution
        self.__gestionnaire.addDiscution() 