from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuroneCodehelp :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique):
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestionNeuron= gestionnaire
        self.__objHistorique = objHist
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
    
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
                    self.__objHistorique.setAction("Ouverture organisateur de varriable")
                    self.__valeurOut = 5
                else :
                    if (("color selecteur" in requette) or ("couleur selecteur" in requette) 
                        or ("selecteur de couleur" in requette)):
                        self.__listSortie=[self.__fonctionArreraNetwork.sortieOpenColorSelecteur(),""]
                        self.__objHistorique.setAction("Ouverture selecteur de couleur")
                        self.__valeurOut = 5
                    else :
                        if ("site github" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSiteGithub(),""]
                            self.__objHistorique.setAction("Ouverture du site github")
                        else :
                            if (("gestion github" in requette) or ("gest github" in requette)):
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenGuiGithub(),""]
                                self.__objHistorique.setAction("Ouverture de logiciel de gestion github")
                                self.__valeurOut = 5
                            else :
                                if ("librairy" in requette):
                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenLibrairy(),""]
                                    self.__objHistorique.setAction("Ouverture de la librairy codehelp")
                                    self.__valeurOut = 5
            else :
                if (("recherche devdoc" in requette) or ("rdevdoc" in requette)
                     or ("sdevdoc" in requette) or ("recherche microsoft" in requette) 
                     or ("rmicrosoft" in requette) or ("smicrosoft" in requette) 
                     or ("recheche python" in requette) or ("rpython" in requette) 
                     or ("spython" in requette)):
                    text , recherche = self.__fonctionArreraNetwork.sortieSearchDoc(requette)
                    self.__listSortie = [text,""]
                    self.__objHistorique.setAction("Recherche documentation "+recherche)
                else :
                    if (("recherche github" in requette) or ("rgithub" in requette) or
                        ("sgithub" in requette) or ("search github" in requette)):
                        text,recherche = self.__fonctionArreraNetwork.sortieSearchGithub(requette)
                        self.__listSortie = [text,""]
                        self.__objHistorique.setAction("Recherche github "+recherche)

            
            #Mise a jour de la valeur
            if (self.__valeurOut == 0):                                                               
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])