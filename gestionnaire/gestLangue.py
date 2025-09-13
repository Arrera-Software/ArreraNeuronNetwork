import random
from librairy.travailJSON import *
from gestionnaire.gestUserSetting import gestUserSetting

class gestLangue:
    def __init__(self,emplacement:str,user_data:gestUserSetting,listVar:list,listFonc:list):
        index = jsonWork(emplacement+"index.json")
        self.__formule = jsonWork(emplacement + index.getContentJsonFlag("formule"))
        self.__chatbot = jsonWork(emplacement + index.getContentJsonFlag("chatbot"))
        self.__codeHelp = jsonWork(emplacement + index.getContentJsonFlag("codeHelp"))
        self.__open = jsonWork(emplacement + index.getContentJsonFlag("open"))
        self.__search = jsonWork(emplacement + index.getContentJsonFlag("search"))
        self.__service = jsonWork(emplacement + index.getContentJsonFlag("service"))
        self.__software = jsonWork(emplacement + index.getContentJsonFlag("software"))
        self.__api = jsonWork(emplacement + index.getContentJsonFlag("api"))
        self.__time = jsonWork(emplacement + index.getContentJsonFlag("time"))
        self.__work = jsonWork(emplacement + index.getContentJsonFlag("work"))
        self.__socket = jsonWork(emplacement + index.getContentJsonFlag("socket"))
        # Variable
        self.__listFonction = listFonc
        self.__nbFonction = len(self.__listFonction)
        # Fichier JSON
        self.__userData = user_data
        # Atribut
        self.__user = ""
        self.__genre = ""
        self.__nameAssistant = listVar[0]
        self.__bute = listVar[1]
        self.__createur = listVar[2]
        self.setVarUser()

    # Partie des formule

    def nocomprehension(self):
        return self.getNoComprehension()

    def bootNoHist(self, hour):
        nbrand = random.randrange(0, 1)
        if 0 <= hour < 3:
            formule = self.getPhraseBootNormale("1")
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                formule = self.getPhraseBootNormale("2")
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    formule = self.getPhraseBootNormale("3")
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        formule = self.getPhraseBootNormale("4")
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 14:
                            formule = self.getPhraseBootNormale("5")
                            return formule[nbrand]
                        else:
                            if hour >= 15 and hour <= 18:
                                formule = self.getPhraseBootNormale("6")
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    formule = self.getPhraseBootNormale("7")
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        formule = self.getPhraseBootNormale("8")
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            formule = self.getPhraseBootNormale("9")
                                            return formule[nbrand]
                                        else:
                                            formule = self.getPhraseBootNormale("10")
                                            return formule

    def aurevoir(self, hour):
        nbrand = random.randrange(0, 1)
        if hour >= 0 and hour < 3:
            formule = self.getPhraseAurevoir("1")
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                formule = self.getPhraseAurevoir("2")
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    formule = self.getPhraseAurevoir("3")
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        formule = self.getPhraseAurevoir("4")
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 16:
                            formule = self.getPhraseAurevoir("5")
                            return formule[nbrand]
                        else:
                            if hour >= 16 and hour <= 18:
                                formule = self.getPhraseAurevoir("6")
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    formule = self.getPhraseAurevoir("7")
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        formule = self.getPhraseAurevoir("8")
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            formule = self.getPhraseAurevoir("9")
                                            return formule[nbrand]
                                        else:
                                            formule = self.getPhraseAurevoir("10")
                                            return formule[nbrand]

    def bootWithHist(self, hour):

        sortie = self.__fncHist.verfiHist()
        if (sortie == True):
            self.__fncHist.startHistAction()

            if hour >= 0 and hour < 3:
                formule = self.getPhraseBootHist("1")
                return formule
            else:
                if hour >= 3 and hour <= 6:
                    formule = self.getPhraseBootHist("2")
                    return formule
                else:
                    if hour >= 6 and hour <= 10:
                        formule = self.getPhraseBootHist("3")
                        return formule
                    else:
                        if hour >= 10 and hour <= 12:
                            formule = self.getPhraseBootHist("4")
                            return formule
                        else:
                            if hour >= 13 and hour <= 14:
                                formule = self.getPhraseBootHist("5")
                                return formule
                            else:
                                if hour >= 15 and hour <= 18:
                                    formule = self.getPhraseBootHist("6")
                                    return formule
                                else:
                                    if hour >= 18 and hour <= 20:
                                        formule = self.getPhraseBootHist("7")
                                        return formule
                                    else:
                                        if hour >= 20 and hour <= 23:
                                            formule = self.getPhraseBootHist("8")
                                            return formule
                                        else:
                                            if hour >= 0 and hour < 3:
                                                formule = self.getPhraseBootHist("9")
                                                return formule
                                            else:
                                                formule = self.getPhraseBootHist("10")
                                                return formule

        else :
            return self.bootNoHist(hour)


    def setVarUser(self):
        self.__user = self.__userData.getUser()
        self.__genre = self.__userData.getGenre()

    def getDataUser(self):
        return [self.__user,self.__genre]

    def getNoComprehension(self):
        return self.__formule.getContentJsonFlag("nc")

    def getPhraseBootNormale(self,nb:str):
        phrases = self.__formule.getFlagListJson("bootN" + nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseAurevoir(self,nb:str):
        phrases = self.__formule.getFlagListJson("stop" + nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseBootHist(self,nb:str):
        phrase = self.__formule.getContentJsonFlag("bootHist" + nb)
        return phrase.format(genre=self.__genre, user=self.__user)

    def getBlague(self,nb:int):
        """
        :param nb: Max 9
        :return:
        """
        return self.__chatbot.getFlagListJson("blague")[nb]

    def getReponseBlague(self,nb:int):
        """
        :param nb: Max 9
        :return:
        """
        return self.__chatbot.getFlagListJson("reponse")[nb]

    def getPhraseChatBotNormal(self, index:str):
        phrases = self.__chatbot.getContentJsonFlag(index)
        return phrases.format(genre=self.__genre, user=self.__user,bute = self.__bute,name=self.__nameAssistant,createur=self.__createur)

    def getPhraseChatBotList(self, index:str):
        phrases = self.__chatbot.getFlagListJson(index)
        return [phrase.format(genre=self.__genre, user=self.__user,bute = self.__bute,name=self.__nameAssistant,createur=self.__createur) for phrase in phrases]

    def getPhraseListeFonction(self):
        self.__nbFonction = 0
        nb = self.__nbFonction - 1
        text = self.__chatbot.getContentJsonFlag("phListFonc")
        for i in range(0, self.__nbFonction):
            if i == nb:
                text = text + " et " + self.__listFonction[i]
            else:
                if i == 0:
                    text = text + self.__listFonction[i]
                else:
                    text = text + ", " + self.__listFonction[i]
        return text + " ."

    def getPhraseCodehelp(self,nb:str):
        formule = self.__codeHelp.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpen(self,nb:str):
        formule = self.__open.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenList(self,nb:str):
        phrases = self.__open.getFlagListJson("ph" + nb)
        nb = random.randint(0, len(phrases) - 1)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseOpenError(self,nb:str):
        formule = self.__open.getContentJsonFlag("phError" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenRadio(self, radio:str, etat:bool):
        if etat:
            formule = self.__open.getContentJsonFlag("phRadio")
            return formule.format(genre=self.__genre, user=self.__user, radio=radio)
        else:
            formule = self.__open.getContentJsonFlag("phRadioError")
            return formule.format(genre=self.__genre, user=self.__user, radio=radio)

    def getPhraseOpenSite(self,site:str,etat:bool):
        if etat :
            formule = self.__open.getContentJsonFlag("phSite")
            return formule.format(genre=self.__genre,user=self.__user,site=site)
        else :
            formule = self.__open.getContentJsonFlag("phSiteError")
            return formule.format(genre=self.__genre,user=self.__user,site=site)

    def getPhraseNbOpenSoftware(self, nb:str):
        formule = self.__open.getContentJsonFlag("phNbSite")
        return formule.format(genre=self.__genre,user=self.__user,nombre=nb)

    def getPhraseNbOpenSite(self, nb: str):
        formule = self.__open.getContentJsonFlag("phNbSoftware")
        return formule.format(genre=self.__genre, user=self.__user, nombre=nb)

    def getPhraseListeRadio(self):
        listRadio = self.__open.getFlagListJson("phListRadion")
        text = listRadio[0]
        for i in range(1, len(listRadio)):
            text = text + "\n- " + listRadio[i]
        return text

    def getPhraseSearch(self,nb:str):
        formule = self.__search.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseResultatCalcule(self,resultat:str):
        formule = self.__service.getContentJsonFlag("phcalcule")
        return formule.format(genre=self.__genre,user=self.__user,resultat=resultat)

    def getPhraseService(self,nb:str):
        formule = self.__service.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseSoftware(self,nb:str):
        formule = self.__software.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenSoftware(self,nb:str,name:str):
        formule = self.__software.getContentJsonFlag("phOpen" + nb)
        return formule.format(genre=self.__genre,user=self.__user,name=name)

    def getPhraseResumerActu(self):
        formule = self.__api.getContentJsonFlag("phResumerActu")
        return formule.format(genre=self.__genre, user=self.__user)

    def getPhraseResumerTask(self):
        formule = self.__api.getContentJsonFlag("phResumerTask")
        return formule.format(genre=self.__genre, user=self.__user)

    def getPhraseResumerAll(self,nb:str):
        formule = self.__api.getContentJsonFlag("phResumerAll" + nb)
        return formule.format(genre=self.__genre, user=self.__user)

    def getPhraseApi(self,nb:str):
        formule = self.__api.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseMeteo(self,nb:str,ville:str,description:str,temperature:str):
        phrases = self.__api.getFlagListJson("phMeteo" + nb)
        return [phrase.format(genre=self.__genre,user=self.__user,ville=ville,description=description,temperature=temperature) for phrase in phrases]

    def getPhraseMeteoError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phMeteoError" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseCoordonnees(self,ville:str,latitude:str,longitude:str):
        phrases = self.__api.getContentJsonFlag("phCoordonnees")
        return phrases.format(genre=self.__genre,user=self.__user,ville=ville,latitude=latitude,longitude=longitude)

    def getPhraseTemperature(self,temperature:str):
        formule = self.__api.getContentJsonFlag("phTemperature")
        return formule.format(genre=self.__genre,user=self.__user,temperature=temperature)

    def getPhraseGPSError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phGPSError" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseIteneraireError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phIteneraireError" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseIteneraire(self):
        formule = self.__api.getContentJsonFlag("phIteneraire")
        return formule.format(genre=self.__genre,user=self.__user)

    def getTexteHelpIteneraire(self):
        formule = self.__api.getContentJsonFlag("phhelpIteneraire")
        return formule.format(genre=self.__genre,user=self.__user)

    def getOpenHelpIteneraire(self):
        formule = self.__api.getContentJsonFlag("phOpenHelpIteneraire")
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenTraducteur(self):
        formule = self.__api.getContentJsonFlag("phTraducteur")
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseErrorLangue(self):
        formule = self.__api.getContentJsonFlag("phErrorLangue")
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseHeure(self,heure:str,minute:str):
        formule = self.__time.getContentJsonFlag("phHeure")
        return formule.format(genre=self.__genre,user=self.__user,heure=heure,minute=minute)

    def getPhraseDate(self,jour:str,mois:str,annee:str):
        formule = self.__time.getContentJsonFlag("phDate")
        return formule.format(genre=self.__genre,user=self.__user,jour=jour,mois=mois,annee=annee)

    def getPhraseTime(self,nb:str):
        formule = self.__time.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre,user=self.__user)
    def getPhraseEvent(self,nb:str):
        formule = self.__time.getContentJsonFlag("phEvent")
        return formule.format(genre=self.__genre,user=self.__user,nombre=nb)

    def getPhraseNBTache(self,nb:str,nombre1:str,nombre2:str):
        formule = self.__time.getContentJsonFlag("phNBTache" + nb)
        return formule.format(genre=self.__genre,user=self.__user,nombre1=nombre1,nombre2=nombre2)

    def getPhraseWork(self, nb:str):
        formule = self.__work.getContentJsonFlag("phWork" + nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseProjetFileOpen(self,nb:str,nameFile:str):
        formule = self.__work.getContentJsonFlag("phProjetFileOpen" + nb)
        return formule.format(genre=self.__genre,user=self.__user,name=nameFile)

    def getPhraseProjetNbTache(self, nb:str, nombre1:str, nameProjet:str, nombre2:str=""):
        formule = self.__work.getContentJsonFlag("phProjetNbTache" + nb)
        return formule.format(genre=self.__genre, user=self.__user, nombre=nombre1, name=nameProjet, nombre2=nombre2)

    def getPhraseHelpArreraWork(self,nb:str):
        formule = self.__work.getFlagListJson("phHelpArreraWork" + nb)
        liste = [phrase.format(genre=self.__genre,user=self.__user) for phrase in formule]
        phraseOut = ""
        for i in range(0,len(liste)):
            if i == 0:
                phraseOut = liste[i]
            else:
                phraseOut = phraseOut + "\n\n- " + liste[i]
        return phraseOut

    def getPhraseSocket(self,name:str):
        return self.__socket.getContentJsonFlag(name)
