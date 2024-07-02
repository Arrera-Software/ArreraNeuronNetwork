from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneTime :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__listSortie = ["",""]
        self.__valeurOut = int

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getTime() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            etatVous = self.__gestionNeuron.getVous()
            genre = self.__gestionNeuron.getGenre()
            #reponse neuron time
            if ("heure" in requette) :
                self.__listSortie = [self.fonctionArreraNetwork.sortieHeure(),""]
            else :
                if ("date" in requette) :
                    self.__listSortie = [self.fonctionArreraNetwork.sortieDate(),""]
                else :
                    if (("chronometre" in requette) or ("chrono" in requette)) :
                        self.__listSortie = [self.fonctionArreraNetwork.sortieOpenChrono(),""]
                        self.__valeurOut = 5
                    else :
                        if ("horloge" in requette) :
                            self.__listSortie = [self.fonctionArreraNetwork.sortieOpenHorloge(),""]
                            self.__valeurOut = 5
                        else :
                            if ("minuteur" in requette) :
                                self.__listSortie = [self.fonctionArreraNetwork.sortieOpenSimpleMinuteur(),""]
                                self.__valeurOut = 5
                            else :
                                if (("ajouter un rendez-vous" in requette) or ("ajout un rendez-vous"  in requette) 
                                    or ("ajout evenement" in requette) or ("ajout rappel" in requette) 
                                    or ("ajout un evenement" in requette) or ("ajout un rappel" in requette) 
                                    or ("ajouter un evenement" in requette) or ("ajouter  un rappel" in requette)):
                                    self.__listSortie = [self.fonctionArreraNetwork.sortieAjoutEvent(),""]
                                    self.__valeurOut = 5
                                else :
                                    if (("suppr un rendez-vous" in requette) or ("supprimer un rendez-vous"  in requette) 
                                        or ("suppr evenement" in requette) or ("suppr rappel" in requette) 
                                        or ("suppr un evenement" in requette) or ("suppr un rappel" in requette) 
                                        or ("supprimer un evenement" in requette) or ("supprimer un rappel" in requette) 
                                        or ("supprime un rendez-vous" in requette)):
                                        self.__listSortie = [self.fonctionArreraNetwork.sortieSupprEvent(),""]
                                        self.__valeurOut = 5
                                    else :
                                        if (("evenement d'aujourd'hui" in requette) or ("evenement du jour" in requette) 
                                            or ("rendez-vous d'aujourd'hui" in requette) or ("rappel aujourd'hui" in requette)):
                                            self.__listSortie = [self.fonctionArreraNetwork.sortieEvenementDay(),""]
                                            self.__valeurOut = 5
                                        else :
                                            if(("ouvre l'agenda" in requette) or ("ouvre le calendrier" in requette)):
                                                self.__listSortie = [self.fonctionArreraNetwork.sortieOpenAgenda(),""]
                                                self.__valeurOut = 5
                                            else :
                                                if(("montre mes taches"in requette)or("fais voir mes taches"in requette) 
                                                   or ("montre mes tache"in requette)or("fais voir mes tache"in requette)):
                                                    self.__listSortie = [self.fonctionArreraNetwork.sortieViewTache(),""]
                                                    self.__valeurOut = 5 
                                                else :
                                                    if(("ajoute une tache"in requette) or ("ajouter une tache" in requette) 
                                                       or ("ajout tache" in requette) or ("add tache" in requette)):
                                                        self.__listSortie = [self.fonctionArreraNetwork.sortieViewTacheAdd(),""]
                                                        self.__valeurOut = 5
                                                    else :
                                                        if(("supprime une tache" in requette)or ("supprimer une tache" in requette) 
                                                       or ("suppr une tache" in requette) or ("suppr tache" in requette)):
                                                            self.__listSortie = [self.fonctionArreraNetwork.sortieViewTacheSuppr(),""]
                                                            self.__valeurOut = 5
                                                        else :
                                                            if(("finir une tache" in requette) or ("terminer une tache" in requette) 
                                                               or ("termine une tache" in requette) or ("fini une tache" in requette)):
                                                                self.__listSortie = [self.fonctionArreraNetwork.sortieViewTacheCheck(),""]
                                                                self.__valeurOut = 5
                                                            else :
                                                                if (((("dit moi" in requette) and ("nombre" in requette)) or ("j'ai combien" in requette)) 
                                                                    and (("tache" in requette) or ("taches" in requette))) :
                                                                    self.__listSortie = [self.fonctionArreraNetwork.sortieNbSpeakTache(),""]
                                                                else :
                                                                    if  ((("dit moi" in requette) and ("tache" in requette) or ("taches" in requette)  
                                                                          and (("jour" in requette) or ("aujourd'hui" in requette))))  :
                                                                        self.__listSortie = [self.fonctionArreraNetwork.sortieSpeakTacheToday(),""]   
                
            #Mise a jour de la valeur 
            if (self.__valeurOut==0):                                                              
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])