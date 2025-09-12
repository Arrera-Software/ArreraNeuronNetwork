import random

from gestionnaire.gestSTR import*
from neuron.CNeuronBase import neuronBase,gestionnaire

class neuroneAPI(neuronBase) :
    def __init__(self,gestionnaire:gestionnaire ):
        super().__init__(gestionnaire)
        self.__fncMeteo = self._gestFNC.getFNCMeteo()
        self.__fncBreef = self._gestFNC.getFNCBreef()

    def __texteMeteo(self,state:bool,a:int,b:int):
        if state:
            return self._language.getPhraseMeteo(str(random.randint(a, b)),
                                                  self.__fncMeteo.getNameTown(),
                                                  self.__fncMeteo.getDescription(),
                                                  self.__fncMeteo.getTemperature()
                                                 )[random.randint(0, 1)]
        else :
            return self._language.getPhraseMeteoError(str(random.randint(a, b)))

    def __texteBreef(self,outList:list,texte:str):
        self._listSortie = outList
        self._listSortie.append(texte)


    def __meteo(self,requette:str)->int:
        townHouse = self._userConf.getLieuDomicile()
        townWork = self._userConf.getLieuTravail()

        if self._keyword.checkAPI(requette,"meteo"):
            if self._keyword.checkAPI(requette, "meteoDemainMatin"):
                if self._keyword.checkAPI(townHouse,"lieuDomicile"):
                    state = self.__fncMeteo.getMeteoTowmorowMorning(town=townHouse)
                elif self._keyword.checkAPI(townWork,"lieuTravail"):
                    state = self.__fncMeteo.getMeteoTowmorowMorning(town=townWork)
                else :
                    state = self.__fncMeteo.getMeteoTowmorowMorning()

                self._listSortie = [self.__texteMeteo(state,3,4),""]
                return 4

            elif self._keyword.checkAPI(requette, "meteoDemainApresMidi"):
                # Recuperation de la meteo de demain apres midi
                if self._keyword.checkAPI(requette,"lieuDomicile"):
                    state = self.__fncMeteo.getMeteoTowmorowNoon(town=townHouse)
                elif self._keyword.checkAPI(requette,"lieuTravail"):
                    state = self.__fncMeteo.getMeteoTowmorowNoon(town=townWork)
                else :
                    state = self.__fncMeteo.getMeteoTowmorowNoon()

                # Mise en place du texte de sortie
                self._listSortie = [self.__texteMeteo(state, 1, 2), ""]
                return 4

            else :
                if self._keyword.checkAPI(requette, "lieuDomicile"):
                    state = self.__fncMeteo.getMeteoCurrentHour(town=townHouse)
                elif self._keyword.checkAPI(requette, "lieuTravail"):
                    state = self.__fncMeteo.getMeteoCurrentHour(town=townWork)
                else:
                    state = self.__fncMeteo.getMeteoCurrentHour()

                self._listSortie = [self.__texteMeteo(state, 5, 6), ""]
                return 4
        elif self._keyword.checkAPI(requette,"temperature"):
            if self._keyword.checkAPI(requette, "lieuDomicile"):
                state = self.__fncMeteo.getMeteoCurrentHour(town=townHouse)
            elif self._keyword.checkAPI(requette, "lieuTravail"):
                state = self.__fncMeteo.getMeteoCurrentHour(town=townWork)
            else:
                state = self.__fncMeteo.getMeteoCurrentHour()

            if state:
                texte = self._language.getPhraseTemperature(self.__fncMeteo.getTemperature())
            else :
                texte = self._language.getPhraseMeteoError(str(random.randint(0, 1)))

            self._listSortie = [texte,""]
            return 4
        return 0

    def __breef(self,requette:str):
        """
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        18 : Resumer tache / agenda
        19 : Resumer all ok
        20 : Resumer all fail
        """
        if self._keyword.checkAPI(requette,"resumer"):
            if self._keyword.checkAPI(requette,"actualite") or self._keyword.checkAPI(requette,"meteo"):
                out = self.__fncBreef.summarizeActuAndMeteo(self._userConf.getLieuDomicile())
                texte = self._language.getPhraseResumerActu()
                if out is not None:
                    outInt = 12
                    self._gestGUI.activeViewResumer(dict=out,list=None,intIn=outInt)
                else :
                    outInt = 11
            elif self._keyword.checkAPI(requette,"taches"):
                out = self.__fncBreef.summarizeTask()
                texte = self._language.getPhraseResumerTask()
                if out is not None:
                    outInt = 18
                    self._gestGUI.activeViewResumer(dict=None,list=out,intIn=outInt)
                else :
                    outInt = 11
            else:
                out = self.__fncBreef.summarizeAll()
                texte = self._language.getPhraseResumerAll("2")
                if out is not None:
                    outInt = 19
                    self._gestGUI.activeViewResumer(dict=out,list=None,intIn=outInt)
                else :
                    outInt = 20

            if outInt == 12 or outInt == 18 or outInt == 19:
                self._listSortie = [texte,""]
            else :
                self._listSortie = [self._language.getPhraseResumerAll("1"),""]
            return outInt
        return 0

    def neurone(self,requette:str):
        self._listSortie = ["", ""]
        self._valeurOut = 0
        self._valeurOut = self.__breef(requette)
        if self._valeurOut == 0:
            self._valeurOut = self.__meteo(requette)
        """
        listeLang = ["anglais","francais","espagnol","allemand", "chinois simplifie","chinois traditionnel",
                            "arabe", "russe","japonais","coreen","italien","portugais","neerlandais",
                            "suedois","danois","norvegien","finnois","grec","hebreu","indonesien"]

        dictLang = {"anglais":"en","francais":"fr","espagnol":"es","allemand":"de", "chinois simplifie":"zh-CN",
                           "chinois traditionnel":"zh-TW","arabe":"ar", "russe":"ru","japonais":"ja",
                           "coreen":"ko","italien":"it","portugais":"pt","neerlandais":"nl","suedois":"sv",
                           "danois":"da","norvegien":"no","finnois":"fi","grec":"el","hebreu":"he","indonesien":"id"}

        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0


        if self._gestNeuron.getAPI():
            #reponse du neuron main
            if ("resumer actualites" in requette) or ("resumer actu" in requette):
                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieResumerActualite()
                self._objHistorique.setAction("Resumer actualiter")
            elif ("resumer" in requette) and (("jour" in requette) or ("aujourd'hui" in requette)):
                nb,listout = self._fonctionArreraNetwork.sortieResumerAll()
                self._listSortie = listout
                self._valeurOut = nb
                self._objHistorique.setAction("Resumer complete de la journee")
            elif "actualites" in requette or "actu" in requette:
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieActualités()
                    self._objHistorique.setAction("Actualités")
            elif "meteo" in requette :
                   self._valeurOut = self.__meteo(requette)
            elif "temperature" in requette :
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieTemperature()
                    self._objHistorique.setAction("Temperature")
            elif "coordonnee gps" in requette or "position gps" in requette :
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieGPS()
                    self._objHistorique.setAction("Possition gps")
            elif ((("indique moi l'itineraire de" in requette)and("sur le gps" in requette))
                    or(("lance le gps pour un trajet de" in requette )and("a" in requette))):
                    self._listSortie = [self._fonctionArreraNetwork.sortieItineraire(requette), ""]
                    self._valeurOut = 1
                    self._objHistorique.setAction("Ouverture d'un itineraire sur google map")
            elif "gps aide" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieHelpItineraire(), ""]
                    self._valeurOut = 1
            elif "traduis" in requette or "traduction" in requette or "traduire" in requette :
                    chaineCarractere = str(requette).lower()
                    presenceLang = False
                    self._objHistorique.setAction("Outil de traduction")
                    for i in range(0,len(listeLang)-1):
                        if listeLang[i] in chaineCarractere :
                            presenceLang = True
                            break
                    if presenceLang:
                        presenceLang = False
                        firstLang = chaine.firstMots(chaineCarractere,listeLang)
                        chaineCarractere = chaineCarractere.replace(firstLang,"")
                        for i in range(0,len(listeLang)-1):
                            if listeLang[i] in chaineCarractere :
                                presenceLang = True
                                break
                        if presenceLang:
                            secondLang = chaine.firstMots(chaineCarractere,listeLang)
                            self._listSortie= [
                                self._fonctionArreraNetwork.sortieTraducteur(dictLang[firstLang], dictLang[secondLang])
                                ,""]
                            self._valeurOut = 3
                        else :
                            self._listSortie = [self._fonctionArreraNetwork.sortieErrorLangue(), ""]
                            self._valeurOut = 1
                    else :
                        self._listSortie = [self._fonctionArreraNetwork.sortieErrorLangue(), ""]
                        self._valeurOut = 1
            """
