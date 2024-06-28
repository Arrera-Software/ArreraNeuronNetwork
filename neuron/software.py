from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneSoftware :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__listSortie = ["",""]
        self.__valeurOut = int 

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getSoftware() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__listSortie = ["",""]
            self.__valeurOut = 0
            #Recuperation atribut de l'assistant
            etatVous = self.__gestionNeuron.getVous()
            genre = self.__gestionNeuron.getGenre()
            user = self.__gestionNeuron.getUser()
            #reponse neuron software
            if ("telecharge" in requette) :
                if "video" in requette :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieDownload("video"),""]
                else :
                    if ("musique" in requette) :
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieDownload("music"),""]
                    else :
                        if (etatVous == True) :
                            self.__listSortie = ["Je suis désoler "+genre+" mais je ne peux télécharger que des vidéo ou de musique",""]
                        else :
                            self.__listSortie = [user+" je ne peux télécharger que de video ou de musique. ",""]
            if (("calculatrice" in requette) or ("calculette" in requette)) :
                if "nombre complex" in requette or "nb complex" in requette :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieCalculatrice("1"),""]
                else :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieCalculatrice("0"),""]
            else :
                if ("pythagore" in requette) :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieCalculatrice("2"),""]
                    
                                        
            #Mise a jour de la valeur                                                               
            self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])