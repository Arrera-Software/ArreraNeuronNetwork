from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.enabledNeuron import*
class neuroneService :
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
        if self.__gestNeuron.getService() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            #Recuperation atribut de l'assistant
            etatVous = self.__gestionNeuron.getVous()
            genre = self.__gestionNeuron.getGenre()
            user = self.__gestionNeuron.getUser()
            #reponse du neuron main
            if "lire un truc" in requette or  "lit un truc" in requette :
                self.__listSortie = [self.__fonctionArreraNetwork.reading(),""]
                self.__valeurOut = 52 
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
                        if etatVous == True :
                            self.__listSortie = ["Voici le resultat de votre calcule "+genre+" est "+str(resultat),""]
                        else :
                            self.__listSortie = ["Voici le resultat de ton calcule "+user+" est "+str(resultat),""]
                    else :
                        if etatVous == True :
                            self.__listSortie = ["Le calcule que vous me demander de faire "+genre+" est imposible a faire.",""]
                        else :
                            self.__listSortie = ["Le calcule que tu me demande de faire est imposible.",""]
            #Mise a jour de la valeur 
            if (self.__valeurOut==0):                                                            
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])