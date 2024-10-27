from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuroneTime :
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
        if self.__gestNeuron.getTime() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            #reponse neuron time
            if ("heure" in requette) :
                self.__listSortie = [self.__fonctionArreraNetwork.sortieHeure(),""]
            else :
                if ("date" in requette) :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieDate(),""]
                else :
                    if (("chronometre" in requette) or ("chrono" in requette)) :
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenChrono(),""]
                        self.__valeurOut = 5
                    else :
                        if ("horloge" in requette) :
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenHorloge(),""]
                            self.__valeurOut = 5
                        else :
                            if ("minuteur" in requette) :
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSimpleMinuteur(),""]
                                self.__valeurOut = 5
                            else :
                                if (("ajouter un rendez-vous" in requette) or ("ajout un rendez-vous"  in requette) 
                                    or ("ajout evenement" in requette) or ("ajout rappel" in requette) 
                                    or ("ajout un evenement" in requette) or ("ajout un rappel" in requette) 
                                    or ("ajouter un evenement" in requette) or ("ajouter  un rappel" in requette)):
                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieAjoutEvent(),""]
                                    self.__objHistorique.setAction("Ajout d'un rendez-vous dans l'agenda")
                                    self.__valeurOut = 5
                                else :
                                    if (("suppr un rendez-vous" in requette) or ("supprimer un rendez-vous"  in requette) 
                                        or ("suppr evenement" in requette) or ("suppr rappel" in requette) 
                                        or ("suppr un evenement" in requette) or ("suppr un rappel" in requette) 
                                        or ("supprimer un evenement" in requette) or ("supprimer un rappel" in requette) 
                                        or ("supprime un rendez-vous" in requette)):
                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieSupprEvent(),""]
                                        self.__objHistorique.setAction("Suppression d'un rendez-vous dans l'agenda")
                                        self.__valeurOut = 5
                                    else :
                                        if (("evenement d'aujourd'hui" in requette) or ("evenement du jour" in requette) 
                                            or ("rendez-vous d'aujourd'hui" in requette) or ("rappel aujourd'hui" in requette)):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieEvenementDay(),""]
                                            self.__objHistorique.setAction("Consulation des rendez-vous enregistrer dans l'agenda")
                                            self.__valeurOut = 5
                                        else :
                                            if(("ouvre l'agenda" in requette) or ("ouvre le calendrier" in requette)):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenAgenda(),""]
                                                self.__objHistorique.setAction("Ouverture de l'interface agenda")
                                                self.__valeurOut = 5
                                            else :
                                                if((("montre mes taches"in requette)or("fais voir mes taches"in requette) 
                                                   or ("montre mes tache"in requette)or("fais voir mes tache"in requette))
                                                   and ("projet" not in requette)):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieViewTache(),""]
                                                    self.__objHistorique.setAction("Consulation des taches enregistrer")
                                                    self.__valeurOut = 5 
                                                else :
                                                    if((("ajoute une tache"in requette) or ("ajouter une tache" in requette) 
                                                       or ("ajout tache" in requette) or ("add tache" in requette))
                                                       and ("projet" not in requette)):
                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieViewTacheAdd(),""]
                                                        self.__objHistorique.setAction("Ajout d'une tache dans l'assistant")
                                                        self.__valeurOut = 5
                                                    else :
                                                        if((("supprime une tache" in requette)or ("supprimer une tache" in requette) 
                                                       or ("suppr une tache" in requette) or ("suppr tache" in requette))
                                                       and ("projet" not in requette)):
                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieViewTacheSuppr(),""]
                                                            self.__objHistorique.setAction("Suppression d'une tache dans l'assistant")
                                                            self.__valeurOut = 5
                                                        else :
                                                            if((("finir une tache" in requette) or ("terminer une tache" in requette) 
                                                               or ("termine une tache" in requette) or ("fini une tache" in requette))
                                                               and ("projet" not in requette)):
                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieViewTacheCheck(),""]
                                                                self.__objHistorique.setAction("Mise d'une tache a fini dans l'assistant")
                                                                self.__valeurOut = 5
                                                            else :
                                                                if ((((("dit moi" in requette) and ("nombre" in requette)) or ("j'ai combien" in requette)) 
                                                                    and (("tache" in requette) or ("taches" in requette)))and ("projet" not in requette)) :
                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieNbSpeakTache(),""]
                                                                    self.__objHistorique.setAction("Consultation du nombre de tache enregistrer")
                                                                else :
                                                                    if  (((("dit moi" in requette) and (("tache" in requette) or ("taches" in requette)) 
                                                                          and (("jour" in requette) or ("aujourd'hui" in requette))))and ("projet" not in requette))  :
                                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieSpeakTacheToday(),""]  
                                                                        self.__objHistorique.setAction("Consultation du nombre de tache enregistrer pour aujourd'hui")
                                                                    else :
                                                                        if  (((("dit moi" in requette) and (("tache" in requette) or ("taches" in requette))  
                                                                          and ("demain" in requette)))and ("projet" not in requette))  :
                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieSpeakTacheTowmorow(),""] 
                                                                            self.__objHistorique.setAction("Consultation du nombre de tache enregistrer pour demain")
                                                                        else :
                                                                            if ((("resumer" in requette) and ("tache" in requette)) or 
                                                                                (("resumer" in requette) and ("agenda" in requette))):
                                                                                nb,listout = self.__fonctionArreraNetwork.sortieResumerTacheAgenda()
                                                                                self.__listSortie = listout
                                                                                self.__valeurOut = nb
                                                                                self.__objHistorique.setAction("Resumer des tache et des evenement du jour")
                                                                    
                
            #Mise a jour de la valeur 
            if (self.__valeurOut==0):                                                              
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])