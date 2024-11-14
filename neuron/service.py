from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*
class neuroneService :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork, objHist:CHistorique) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
        self.__objHistorique = objHist
        self.__listSortie = ["",""]
        self.__valeurOut = 0

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut
        
    def neurone(self,requette:str):
        if self.__gestNeuron.getService() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            #reponse du neuron main
            if "lire un truc" in requette or  "lit un truc" in requette :
                self.__listSortie = [self.__fonctionArreraNetwork.reading(),""]
                self.__objHistorique.setAction("Lecture")
                self.__valeurOut = 5
            else :
                if "calcule" in requette :
                    requette = requette.replace("calcule","")
                    requette = requette.replace(" ","")
                    if (("1" in requette) or ("2" in requette)  or ("3" in requette) 
                        or ("4" in requette) or ("5" in requette) or ("6" in requette)  
                        or ("7" in requette) or ("8" in requette) or ("9" in requette) 
                        or( "0" in requette) and ("+" in requette) or ("-" in requette) 
                        or ( "*" in requette) or ("/" in requette)) :
                        resultat =  eval(requette)
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieResultatCalcule(resultat),""]
                        self.__objHistorique.setAction("Calcule par texte")
                    else :
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieErrorCalcule(),""]
                else :
                    if (("ouvre la documentation" in requette)or("montre la documentation" in requette)):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenDocumentation(),""]
                        webbrowser.open(self.__gestionNeuron.getLinkDoc())
                    else :
                        if ("corrige" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieCorrection(requette),""]
            #Mise a jour de la valeur 
            if (self.__valeurOut==0):                                                            
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])