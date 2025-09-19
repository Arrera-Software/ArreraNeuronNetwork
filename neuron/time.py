from neuron.CNeuronBase import *

class neuroneTime(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__libTime = self._gestionnaire.getArrDate()
        self.__fncTask = self._gestFNC.getFNCTask()
        self.__taskAdd = False
        self.__taskEnd = False

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
        if self._keyword.checkTime(requette,"calendar"):
            if (self._keyword.checkTime(requette,"open") or
                    self._keyword.checkTime(requette,"montre")):
                self._listSortie = [self._language.getPhraseTime("8"), ""]
                self._gestGUI.activeAgenda()
                return 1
        else :
            return 0
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
        if self._keyword.checkTime(requette,"tache"):
            if (self._keyword.checkTime(requette, "open") or
                    self._keyword.checkTime(requette, "montre")):
                self._listSortie = [self._language.getPhraseTime("9"), ""]
                self._gestGUI.activeTache()
                return 1
            elif self._keyword.checkTime(requette,"add"):
                self._listSortie = [self._language.getPhraseTime("10"), ""]
                self.__taskAdd = True
                self.__taskEnd = False
                return 1
            elif self._keyword.checkTime(requette,"delete") :
                self._listSortie = [self._language.getPhraseTime("11"), ""]
                self._gestGUI.activeDelTask()
                return 1
            elif self._keyword.checkTime(requette,"finish") :
                self._listSortie = [self._language.getPhraseTime("12"), ""]
                self.__taskEnd = True
                self.__taskAdd = False
                return 1
            if self._keyword.checkTime(requette,"how-much"):
                if self._keyword.checkTime(requette,"today"):
                    nbTaskToday = self.__fncTask.getNbTaskToday()
                    if nbTaskToday == 0 :
                        self._listSortie = [self._language.getPhraseNBTache("6","",""), ""]
                    else :
                        if nbTaskToday == 1 :
                            self._listSortie = [self._language.getPhraseNBTache("5","",""), ""]
                        else :
                            self._listSortie = [self._language.getPhraseNBTache("4",str(nbTaskToday),""), ""]
                    return 1
                if self._keyword.checkTime(requette,"tomorrow"):
                    nbTaskTowmorow = self.__fncTask.getNbTaskTowmorow()
                    if nbTaskTowmorow == 0:
                        self._listSortie = [self._language.getPhraseNBTache("9", "", ""), ""]
                    else:
                        if nbTaskTowmorow == 1:
                            self._listSortie = [self._language.getPhraseNBTache("8", "", ""), ""]
                        else:
                            self._listSortie = [self._language.getPhraseNBTache("7", str(nbTaskTowmorow), ""), ""]
                    return 1
                else :
                    nbTask = len(self.__fncTask.getAllTask())
                    nbTaskToday = self.__fncTask.getNbTaskToday()
                    if nbTaskToday == 0 :
                        self._listSortie = [self._language.getPhraseNBTache("3",str(nbTask),str(nbTaskToday)), ""]
                    elif nbTaskToday == 1 :
                        self._listSortie = [self._language.getPhraseNBTache("1",str(nbTask),str(nbTaskToday)), ""]
                    else :
                        self._listSortie = [self._language.getPhraseNBTache("2",str(nbTask),str(nbTaskToday)), ""]
                    return 1
        elif self.__taskAdd:
            if self._keyword.checkTime(requette,"name-task"):
                self.__taskAdd = False
                listPhrase = self._keyword.getListKeyword("time","name-task")
                name = requette
                for phrase in listPhrase:
                    name = name.replace(phrase,"")
                name = name.strip()
                if name == "":
                    self._listSortie = [self._language.getPhraseTime("25"), ""]
                else :
                    if self.__fncTask.addTask(name):
                        self._listSortie = [self._language.getPhraseTime("24",task=name), ""]
                    else :
                        self._listSortie = [self._language.getPhraseTime("26"), ""]
                return 1
        elif self.__taskEnd:
            if self._keyword.checkTime(requette,"name-task"):
                self.__taskEnd = False
                listPhrase = self._keyword.getListKeyword("time","name-task")
                name = requette
                for phrase in listPhrase:
                    name = name.replace(phrase,"")
                name = name.strip()
                if name == "":
                    self._listSortie = [self._language.getPhraseTime("14"), ""]
                else :
                    if self.__fncTask.finishTask(name):
                        self._listSortie = [self._language.getPhraseTime("13",task=name), ""]
                    else :
                        self._listSortie = [self._language.getPhraseTime("27",task=name), ""]
                return 1
        else:
            return 0

        """
        if ("taches" in requette or "tache" in requette) and "projet" not in requette:
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