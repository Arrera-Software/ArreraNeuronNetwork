from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuronWork :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron,objHist:CHistorique):
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__objHistorique = objHist
        self.__listSortie = ["",""]
        self.__valeurOut = int
    
    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut
    
    def neurone(self,requette:str):
        if (self.__gestNeuron.getWork() == True):
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]

            if (("ouvre" in requette) and ("fichier" in requette)):
                if ("exel" in requette):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTableur(),""]
                    self.__objHistorique.setAction("Ouverture d'un fichier exel "+self.__fonctionArreraNetwork.getFileTableur())
                    self.__valeurOut = 7 
                else :
                    if ("word" in requette):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenWord(),""]
                        self.__objHistorique.setAction("Ouverture d'un fichier word "+self.__fonctionArreraNetwork.getFileWord())
                        self.__valeurOut = 7
            else :
                if ("ferme" in requette) :
                    if ("exel" in requette):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseTableur(),""]
                        self.__objHistorique.setAction("Fermeture d'un fichier exel")
                        self.__valeurOut = 8
                    else :
                        if ("word" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseDocx(),""]
                            self.__objHistorique.setAction("Fermeture d'un fichier word")
                            self.__valeurOut = 8
                else :
                    if ("lit" in requette):
                        if ("word" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieReadDocx(),""]
                            self.__objHistorique.setAction("Lecture du fichier word "+self.__fonctionArreraNetwork.getFileWord())
                            self.__valeurOut = 9
                    else :
                        if ("ecrit dans le word" in requette) :
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieWriteDocx(requette),""]
                            self.__objHistorique.setAction("Ecriture dans le fichier docx"+self.__fonctionArreraNetwork.getFileWord())
                            self.__valeurOut = 1