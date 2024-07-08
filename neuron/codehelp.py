from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneCodehelp :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron):
        self.__gestNeuron = neuronGest
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestionNeuron= gestionnaire
    
    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getCodeHelp() == True:
            #Initilisation des variable nbRand et text et valeur
            self.__listSortie = ["",""]
            self.__valeurOut = 0

            if ("ouvre" in requette):
                if (("organisateur de variable" in requette)or("orga var" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenOrgaVar(),""]
                    self.__valeurOut = 5
                else :
                    if (("color selecteur" in requette) or ("couleur selecteur" in requette) 
                        or ("selecteur de couleur" in requette)):
                        self.__listSortie=[self.__fonctionArreraNetwork.sortieOpenColorSelecteur(),""]
                        self.__valeurOut = 5
                    else :
                        if ("site github" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSiteGithub(),""]
                        else :
                            if (("gestion github" in requette) or ("gest github" in requette)):
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenGuiGithub(),""]
                                self.__valeurOut = 5
                            else :
                                if ("librairy" in requette):
                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenLibrairy(),""]
                                    self.__valeurOut = 5
            else :
                if (("recherche devdoc" in requette) or ("rdevdoc" in requette)
                     or ("sdevdoc" in requette) or ("recherche microsoft" in requette) 
                     or ("rmicrosoft" in requette) or ("smicrosoft" in requette) 
                     or ("recheche python" in requette) or ("rpython" in requette) 
                     or ("spython" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieSearchDoc(requette),""]
                else :
                    if (("recherche github" in requette) or ("rgithub" in requette) or
                        ("sgithub" in requette) or ("search github" in requette)):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieSearchGithub(requette),""]

            
            #Mise a jour de la valeur
            if (self.__valeurOut == 0):                                                               
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])