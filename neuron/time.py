from neuron.CNeuronBase import *

class neuroneTime(neuronBase):

    def neurone(self,requette:str):
        if self._gestNeuron.getTime() == True :
            #Initilisation des variable nbRand et text et valeur
            self._valeurOut = 0
            self._listSortie = ["", ""]
            #reponse neuron time
            if ("heure" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieHeure(), ""]
            elif ("date" in requette) :
                    self._listSortie = [self._fonctionArreraNetwork.sortieDate(), ""]
            elif ("chronometre" in requette or "chrono" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenChrono(), ""]
                self._valeurOut = 5
            elif ("horloge" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenHorloge(), ""]
                self._valeurOut = 5
            elif ("minuteur" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenSimpleMinuteur(), ""]
                self._valeurOut = 5
            elif (("ajouter un rendez-vous" in requette) or ("ajout un rendez-vous"  in requette)
                    or ("ajout evenement" in requette) or ("ajout rappel" in requette)
                    or ("ajout un evenement" in requette) or ("ajout un rappel" in requette)
                    or ("ajouter un evenement" in requette) or ("ajouter  un rappel" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieAjoutEvent(), ""]
                    self._objHistorique.setAction("Ajout d'un rendez-vous dans l'agenda")
                    self._valeurOut = 5
            elif (("suppr un rendez-vous" in requette) or ("supprimer un rendez-vous"  in requette)
                    or ("suppr evenement" in requette) or ("suppr rappel" in requette)
                    or ("suppr un evenement" in requette) or ("suppr un rappel" in requette)
                    or ("supprimer un evenement" in requette) or ("supprimer un rappel" in requette)
                    or ("supprime un rendez-vous" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieSupprEvent(), ""]
                    self._objHistorique.setAction("Suppression d'un rendez-vous dans l'agenda")
                    self._valeurOut = 5
            elif (("evenement d'aujourd'hui" in requette) or ("evenement du jour" in requette)
                    or ("rendez-vous d'aujourd'hui" in requette) or ("rappel aujourd'hui" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieEvenementDay(), ""]
                    self._objHistorique.setAction("Consulation des rendez-vous enregistrer dans l'agenda")
                    self._valeurOut = 5
            elif(("ouvre l'agenda" in requette) or ("ouvre le calendrier" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenAgenda(), ""]
                    self._objHistorique.setAction("Ouverture de l'interface agenda")
                    self._valeurOut = 5
            elif((("montre mes taches"in requette)or("fais voir mes taches"in requette)
                   or ("montre mes tache"in requette)or("fais voir mes tache"in requette))
                   and ("projet" not in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieViewTache(), ""]
                    self._objHistorique.setAction("Consulation des taches enregistrer")
                    self._valeurOut = 5
            elif((("ajoute une tache"in requette) or ("ajouter une tache" in requette)
                   or ("ajout tache" in requette) or ("add tache" in requette))
                   and ("projet" not in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheAdd(), ""]
                    self._objHistorique.setAction("Ajout d'une tache dans l'assistant")
                    self._valeurOut = 5
            elif((("supprime une tache" in requette)or ("supprimer une tache" in requette)
               or ("suppr une tache" in requette) or ("suppr tache" in requette))
               and ("projet" not in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheSuppr(), ""]
                    self._objHistorique.setAction("Suppression d'une tache dans l'assistant")
                    self._valeurOut = 5
            elif((("finir une tache" in requette) or ("terminer une tache" in requette)
                   or ("termine une tache" in requette) or ("fini une tache" in requette))
                   and ("projet" not in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheCheck(), ""]
                    self._objHistorique.setAction("Mise d'une tache a fini dans l'assistant")
                    self._valeurOut = 5
            elif ((((("dit moi" in requette) and ("nombre" in requette)) or ("j'ai combien" in requette))
                    and (("tache" in requette) or ("taches" in requette)))and ("projet" not in requette)) :
                    self._listSortie = [self._fonctionArreraNetwork.sortieNbSpeakTache(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer")
            elif  (((("dit moi" in requette) and (("tache" in requette) or ("taches" in requette))
                      and (("jour" in requette) or ("aujourd'hui" in requette))))and ("projet" not in requette))  :
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheToday(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour aujourd'hui")
            elif  (((("dit moi" in requette) and (("tache" in requette) or ("taches" in requette))
                  and ("demain" in requette)))and ("projet" not in requette))  :
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheTowmorow(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour demain")
            elif ((("resumer" in requette) and ("tache" in requette)) or
                    (("resumer" in requette) and ("agenda" in requette))):
                    nb,listout = self._fonctionArreraNetwork.sortieResumerTacheAgenda()
                    self._listSortie = listout
                    self._valeurOut = nb
                    self._objHistorique.setAction("Resumer des tache et des evenement du jour")
                                                                    
                
            #Mise a jour de la valeur 
            if (self._valeurOut==0):
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])