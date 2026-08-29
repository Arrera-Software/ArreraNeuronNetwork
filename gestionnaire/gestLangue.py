import random
from librairy.travailJSON import *
from gestionnaire.gestion import gestionnaire
from datetime import datetime
from librairy.resource_lib import resource_lib


class gestLangue:
    def __init__(self,emplacement:str,gestion:gestionnaire,listVar:list,listFonc:list):
        ressource_lib = resource_lib()
        self.__formule = jsonWork(ressource_lib.resource_path(emplacement + "formule.json"))
        self.__personnalite = jsonWork(ressource_lib.resource_path(emplacement + "personnalite.json"))
        self.__fncHist = gestion.getGestHist()
        # Variable
        self.__listFonction = listFonc
        self.__nbFonction = len(self.__listFonction)
        # Fichier JSON
        self.__userData = gestion.getUserConf()
        # Atribut
        self.__userFirstname = ""
        self.__genre = ""
        self.__nameAssistant = listVar[0]
        self.__bute = listVar[1]
        self.__createur = listVar[2]
        self.setVarUser()

    # Partie des formule

    def nocomprehension(self):
        return self.getNoComprehension()

    def bootNoHist(self):
        hour = datetime.now().hour
        nbrand = random.randrange(0, 1)
        if 0 <= hour < 3:
            formule = self.getPhraseBootNormale("1")
            return formule[nbrand]
        elif 3 <= hour <= 6:
            formule = self.getPhraseBootNormale("2")
            return formule[nbrand]
        elif 6 <= hour <= 10:
            formule = self.getPhraseBootNormale("3")
            return formule[nbrand]
        elif 10 <= hour <= 12:
            formule = self.getPhraseBootNormale("4")
            return formule[nbrand]
        elif 13 <= hour <= 14:
            formule = self.getPhraseBootNormale("5")
            return formule[nbrand]
        elif 15 <= hour <= 18:
            formule = self.getPhraseBootNormale("6")
            return formule[nbrand]
        elif 18 <= hour <= 20:
            formule = self.getPhraseBootNormale("7")
            return formule[nbrand]
        elif 20 <= hour <= 23:
            formule = self.getPhraseBootNormale("8")
            return formule[nbrand]
        elif 0 <= hour < 3:
            formule = self.getPhraseBootNormale("9")
            return formule[nbrand]
        else:
            formule = self.getPhraseBootNormale("10")
            return formule

    def aurevoir(self, hour):
        nbrand = random.randrange(0, 1)
        if 0 <= hour < 3:
            formule = self.getPhraseAurevoir("1")
            return formule[nbrand]
        elif 3 <= hour <= 6:
            formule = self.getPhraseAurevoir("2")
            return formule[nbrand]
        elif 6 <= hour <= 10:
            formule = self.getPhraseAurevoir("3")
            return formule[nbrand]
        elif 10 <= hour <= 12:
            formule = self.getPhraseAurevoir("4")
            return formule[nbrand]
        elif 13 <= hour <= 16:
            formule = self.getPhraseAurevoir("5")
            return formule[nbrand]
        elif 16 <= hour <= 18:
            formule = self.getPhraseAurevoir("6")
            return formule[nbrand]
        elif 18 <= hour <= 20:
            formule = self.getPhraseAurevoir("7")
            return formule[nbrand]
        elif 20 <= hour <= 23:
            formule = self.getPhraseAurevoir("8")
            return formule[nbrand]
        elif 0 <= hour < 3:
            formule = self.getPhraseAurevoir("9")
            return formule[nbrand]
        else:
            formule = self.getPhraseAurevoir("10")
            return formule[nbrand]

    def bootWithHist(self):
        hour = datetime.now().hour
        if 0 <= hour < 3:
            formule = self.getPhraseBootHist("1")
            return formule
        elif 3 <= hour <= 6:
            formule = self.getPhraseBootHist("2")
            return formule
        elif 6 <= hour <= 10:
            formule = self.getPhraseBootHist("3")
            return formule
        elif 10 <= hour <= 12:
            formule = self.getPhraseBootHist("4")
            return formule
        elif 13 <= hour <= 14:
            formule = self.getPhraseBootHist("5")
            return formule
        elif 15 <= hour <= 18:
            formule = self.getPhraseBootHist("6")
            return formule
        elif 18 <= hour <= 20:
            formule = self.getPhraseBootHist("7")
            return formule
        elif 20 <= hour <= 23:
            formule = self.getPhraseBootHist("8")
            return formule
        elif 0 <= hour < 3:
            formule = self.getPhraseBootHist("9")
            return formule
        else:
            formule = self.getPhraseBootHist("10")
            return formule

    def setVarUser(self):
        self.__userFirstname = self.__userData.getFirstnameUser()
        self.__userLastname = self.__userData.getLastnameUser()
        self.__genre = self.__userData.getGenre()

    def getDataUser(self):
        return [self.__userFirstname,self.__userLastname,self.__genre]

    def getNoComprehension(self):
        return self.__formule.getContentJsonFlag("nc")

    def getPhraseBootNormale(self,nb:str):
        phrases = self.__formule.getFlagListJson("bootN" + nb)
        return [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname) for phrase in phrases]

    def getPhraseAurevoir(self,nb:str):
        phrases = self.__formule.getFlagListJson("stop" + nb)
        return [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname) for phrase in phrases]

    def getPhraseBootHist(self,nb:str):
        phrase = self.__formule.getContentJsonFlag("bootHist" + nb)
        return phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                             user_lastname=self.__userLastname)

    def getPersonnalite(self) -> str:
        try:
            role = self.__personnalite.getContentJsonFlag("role")
            ton = self.__personnalite.getContentJsonFlag("ton")
            politesse = self.__personnalite.getContentJsonFlag("politesse")
            style = self.__personnalite.getContentJsonFlag("style_reponse")
            return f"Rôle : {role}\nTon : {ton}\nPolitesse : {politesse}\nStyle de réponse : {style}"
        except:
            return ""