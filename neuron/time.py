from neuron.CNeuronBase import *

class neuroneTime(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__libTime = self._gestionnaire.getArrDate()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = self.__neuronTime(requette)
        if self._valeurOut == 0:
            self._valeurOut = self.__neuronAgenda(requette)
            if self._valeurOut == 0:
                self._valeurOut = self.__neuronTache(requette)


    def __neuronTime(self,requette:str):
        if self._keyword.checkTime(requette,"hour"):
            hour = self.__libTime.heure()
            minute = self.__libTime.minute()
            self._listSortie =  [self._language.getPhraseHeure(hour,minute),""]
            return 1
        elif self._keyword.checkTime(requette,"date"):
            day = self.__libTime.jourSimple()
            month = self.__libTime.mois()
            year = self.__libTime.annes()
            self._listSortie = [self._language.getPhraseDate(jour=day,
                                                             mois=month,
                                                             annee=year),""]
            return 1
        elif self._keyword.checkTime(requette,"chrono"):
            self._gestGUI.activeChrono()
            self._listSortie = [self._language.getPhraseTime("1"),""]
            return 1
        elif self._keyword.checkTime(requette,"clock"):
            self._gestGUI.activeHorloge()
            self._listSortie = [self._language.getPhraseTime("2"),""]
            return 1
        elif self._keyword.checkTime(requette,"clock"):
            self._gestGUI.activeHorloge()
            self._listSortie = [self._language.getPhraseTime("3"),""]
            return 1
        elif self._keyword.checkTime(requette,"timer"):
            self._gestGUI.activeMinuteur()
            self._listSortie = [self._language.getPhraseTime("4"),""]
            return 1
        else :
            return 0

    def __neuronAgenda(self,requette:str):
        """
        if "evenement" in requette or "agenda" in requette or "rendez vous" in requette or "rappel" in requette:
            if "ajoute" in requette or "ajouter" in requette or "add" in requette or "ajout" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieAjoutEvent(), ""]
                self._objHistorique.setAction("Ajout d'un rendez-vous dans l'agenda")
                self._valeurOut = 5
                return 1
            elif "supprime" in requette or "supprimer" in requette or "suppr" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieSupprEvent(), ""]
                self._objHistorique.setAction("Suppression d'un rendez-vous dans l'agenda")
                self._valeurOut = 5
                return 1
            elif ("montre" in requette or "fais voir" in requette) and ("aujourd'hui" in requette or "jour" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieEvenementDay(), ""]
                self._objHistorique.setAction("Consulation des rendez-vous enregistrer dans l'agenda")
                self._valeurOut = 5
                return 1
            elif "montre" in requette or "ouvre" in requette or "fais voir" in requette :
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenAgenda(), ""]
                self._objHistorique.setAction("Ouverture de l'interface agenda")
                self._valeurOut = 5
                return 1
            else :
                return 0
        else :
            return 0
        """
        return 0

    def __neuronTache(self, requette:str):
        """
        if ("taches" in requette or "tache" in requette) and "projet" not in requette:
            if ("montre" in requette or "fais voir" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTache(), ""]
                self._objHistorique.setAction("Consulation des taches enregistrer")
                self._valeurOut = 5
                return 1
            elif ("ajoute" in requette or "ajouter" in requette
                  or "ajout" in requette or "add" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheAdd(), ""]
                self._objHistorique.setAction("Ajout d'une tache dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("supprime" in requette or "supprimer" in requette or "suppr" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheSuppr(), ""]
                self._objHistorique.setAction("Suppression d'une tache dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("finir" in requette or "terminer" in requette or "termine" in requette or "fini" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheCheck(), ""]
                self._objHistorique.setAction("Mise d'une tache a fini dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("dit moi" in requette) and (("nombre" in requette) or ("combien" in requette)):
                if  (("jour" in requette) or ("aujourd'hui" in requette)) :
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheToday(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour aujourd'hui")
                    self._valeurOut = 1
                    return 1
                elif ("demain" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheTowmorow(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour demain")
                    self._valeurOut = 1
                    return 1
                else :
                    self._listSortie = [self._fonctionArreraNetwork.sortieNbSpeakTache(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer")
                    self._valeurOut = 1
                    return 1
            else :
                return 0
        else:
            return 0
        """
        return 0