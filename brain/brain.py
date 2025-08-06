import threading as th
from gestionnaire.gestion import *
from gestionnaire.gestLangue import*


class ABrain :
    def __init__(self,config:confNeuron):
        # Declaration des diferente var 
        self.__listOut =  [] 
        self.__valeurOut = 0
        self.__networkRunning = True
        self.__neuronUsed = str
        self.__listNeuron = ["chatBot","service","api",
                             "software","open","search",
                             "time","codehelp","word"]
        #Ouverture fichier de configuration
        #self.__configNeuron = jsonWork(fichierConfiguration)
        #self.__fichierUtilisateur = jsonWork(self.__configNeuron.lectureJSON("fileUser"))
        #self.__fichierVille = jsonWork(self.__configNeuron.lectureJSON("fileFete"))
        # Gestionnaire
        self.__gestionnaire = gestionnaire(config)
        self.__gestNeuron = self.__gestionnaire.getGestNeuron()
        # Partie serveur
        self.__socket = self.__gestionnaire.getSocketObjet()
        #initilisation du gestionnaire du reseau de neuron
        self.__gestLangue = self.__gestionnaire.getLanguageObjet()
        #recuperation etat du reseau
        self.__etatReseau = self.__gestionnaire.getNetworkObjet().getEtatInternet()
        #initilisation des neuron

    def getNeuronRunning(self):
        return self.__networkRunning

    def boot(self,mode:int):
        """_summary_

        Args:
            mode (int): 1.no hist | 2. Hist

        Returns:
            _type_: _description_
        """
        hour = datetime.now().hour
        if mode == 1 :
            text= self.__gestLangue.bootNoHist(hour)
        else :
            text= self.__gestLangue.bootWithHist(hour)
        self.__gestionnaire.setOld("boot","boot")
        return str(text)
    
    def shutdown(self):
        #self.__historique.saveHistorique()
        hour = datetime.now().hour
        text = self.__gestLangue.aurevoir(hour)
        if self.__gestionnaire.getGestNeuron().getSocket():
            if self.__socket.getServeurOn():
                self.__socket.stopSocket()
        return str(text)
    
    def getListSortie(self)->list :
        return self.__listOut

    def getNeuronUsed(self)-> type[str]:
        return self.__neuronUsed

    def getValeurSortie(self)->int :
        """
        0 : Aucun sortie
        1 : Sortie normale
        3 : Sortie actu
        4 : Meteo / temperature / GPS
        5 : Sortie avec fenetre tkinter
        6 : Erreur actu
        7 : Ouverture de fichier
        8 : Fermeture de fichier
        9 : Lecture fichier
        10 : Creation d'un projet
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        13 : Lecture tableur
        14 : Ouverture d'un projet
        15 : Arret de l'assistant
        16 : Creation d'un fichier dans un projet
        17 : Affichage aide
        18 : Resumer tache / agenda
        19 : Resumer all ok 
        20 : Resumer all fail
        21 : Close projet
        """
        return self.__valeurOut
    
    def getTableur(self):
        return self.__fonctionAssistant.getTableurOpen()
    
    def getWord(self):
        return self.__fonctionAssistant.getWordOpen()

    def getProject(self):
        return self.__fonctionAssistant.getProjectOpen()

    def getUserData(self):
        return self.__gestionnaire.getLanguageObjet().getDataUser()

    def neuron(self,var:str) :
        # Var local
        requette = self.__gestionnaire.netoyageChaine(str(var))
        # Var de l'objet
        self.__valeurOut = 0
        self.__listOut =  []
        self.__neuronUsed = "none"
        # Service
        if self.__gestNeuron.nservice is None:
            self.__valeurOut = 0
        else :
            self.__gestNeuron.nservice.neurone(requette)
            self.__valeurOut = self.__gestNeuron.nservice.getValeurSortie()
        if self.__valeurOut == 0 :
            #software
            if self.__gestNeuron.nsoftware is None:
                self.__valeurOut = 0
            else :
                self.__gestNeuron.nsoftware.neurone(requette)
                self.__valeurOut = self.__gestNeuron.nsoftware.getValeurSortie()

            if self.__valeurOut == 0 :
                #time
                if self.__gestNeuron.ntime is None:
                    self.__valeurOut = 0
                else :
                    self.__gestNeuron.ntime.neurone(requette)
                    self.__valeurOut = self.__gestNeuron.ntime.getValeurSortie()

                if self.__valeurOut == 0 :
                    #code help
                    if self.__gestNeuron.ncodehelp is None:
                        self.__valeurOut = 0
                    else :
                        self.__gestNeuron.ncodehelp.neurone(requette)
                        self.__valeurOut = self.__gestNeuron.ncodehelp.getValeurSortie()

                    if self.__valeurOut == 0:
                        #work
                        if self.__gestNeuron.nwork is None:
                            self.__valeurOut = 0
                        else :
                            self.__gestNeuron.nwork.neurone(requette)
                            self.__valeurOut = self.__gestNeuron.nwork.getValeurSortie()

                        if self.__valeurOut == 0:
                            #open
                            if self.__gestNeuron.nopen is None:
                                self.__valeurOut = 0
                            else :
                                self.__gestNeuron.nopen.neurone(requette)
                                self.__valeurOut = self.__gestNeuron.nopen.getValeurSortie()

                            if self.__valeurOut == 0 :
                                #search
                                if not self.__etatReseau and self.__gestNeuron.nsearch is None :
                                    self.__valeurOut = 0
                                else :
                                    self.__gestNeuron.nsearch.neurone(requette)
                                    self.__valeurOut = self.__gestNeuron.nsearch.getValeurSortie()

                                if self.__valeurOut == 0 :
                                    #chatBot
                                    if self.__gestNeuron.nchatbot is None:
                                        self.__valeurOut = 0
                                    else :
                                        self.__gestNeuron.nchatbot.neurone(requette)
                                        self.__valeurOut = self.__gestNeuron.nchatbot.getValeurSortie()

                                    if self.__valeurOut == 0 :
                                        #api
                                        if not self.__etatReseau  and self.__gestNeuron.napi is None :
                                            self.__valeurOut = 0
                                        else :
                                            self.__gestNeuron.napi.neurone(requette)
                                            self.__valeurOut = self.__gestNeuron.napi.getValeurSortie()

                                        if self.__valeurOut == 0 :
                                            if (("stop" in requette) or ("au revoir" in requette)
                                                or ("quitter" in requette) or ("bonne nuit" in requette)
                                                or ("adieu" in requette) or ("bonne soirée" in requette)
                                                or ("arreter" in requette)) :
                                                self.__listOut = [self.shutdown(),""]
                                                self.__valeurOut = 15
                                            else :
                                                self.__valeurOut = 0
                                                self.__listOut = [self.__gestLangue.nocomprehension(), ""]
                                        else :
                                            self.__listOut = self.__gestNeuron.napi.getListSortie()
                                            self.__neuronUsed = self.__listNeuron[2]
                                    else :
                                        self.__listOut = self.__gestNeuron.nchatbot.getListSortie()
                                        self.__neuronUsed = self.__listNeuron[0]
                                else :
                                    self.__listOut = self.__gestNeuron.nsearch.getListSortie()
                                    self.__neuronUsed = self.__listNeuron[5]
                            else :
                                self.__listOut = self.__gestNeuron.nopen.getListSortie()
                                self.__neuronUsed = self.__listNeuron[4]
                        else :
                            self.__listOut = self.__gestNeuron.nwork.getListSortie()
                            self.__neuronUsed = self.__listNeuron[8]
                    else :
                        self.__listOut = self.__gestNeuron.ncodehelp.getListSortie()
                        self.__neuronUsed = self.__listNeuron[7]
                else :
                    self.__listOut = self.__gestNeuron.ntime.getListSortie()
                    self.__neuronUsed = self.__listNeuron[6]
            else :
                self.__listOut = self.__gestNeuron.nsoftware.getListSortie()
                self.__neuronUsed = self.__listNeuron[3]
        else :
            self.__listOut = self.__gestNeuron.nservice.getListSortie()
            self.__neuronUsed = self.__listNeuron[1]

        #Sauvegarde de la sortie et de l'entrée
        if (self.__valeurOut == 3) or (self.__valeurOut == 12) or (self.__valeurOut == 11):
            self.__gestionnaire.setOld("requette api",requette)
        else :
            self.__gestionnaire.setOld(self.__listOut[0],requette)