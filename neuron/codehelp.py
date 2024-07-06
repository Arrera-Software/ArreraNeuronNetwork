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
            self.__listSortie = []
            self.__valeurOut = 0

            if ("ouvre" in requette):
                if (("organisateur de varriable" in requette)or("orga var" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenOrgaVar(),""]
                    self.__valeurOut = 5
            
            #Mise a jour de la valeur                                                               
            self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])