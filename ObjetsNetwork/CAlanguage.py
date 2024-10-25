from lxml.html.defs import phrase_tags

from librairy.travailJSON import *
from ObjetsNetwork.gestion import *

class CAlanguage:
    def __init__(self,configFile:jsonWork,gestionnaire:gestionNetwork):
        emplacement = configFile.lectureJSON("moduleLanguage")
        index = jsonWork(emplacement+"index.json")
        self.__formule = jsonWork(emplacement+index.lectureJSON("formule"))
        self.__chatbot = jsonWork(emplacement+index.lectureJSON("chatbot"))
        self.__codeHelp = jsonWork(emplacement+index.lectureJSON("codeHelp"))
        self.__open = jsonWork(emplacement+index.lectureJSON("open"))
        self.__search = jsonWork(emplacement+index.lectureJSON("search"))
        self.__service = jsonWork(emplacement+index.lectureJSON("service"))
        self.__software = jsonWork(emplacement+index.lectureJSON("software"))
        self.__gestionnaire = gestionnaire
        self.__user = self.__gestionnaire.getUser()
        self.__genre = self.__gestionnaire.getGenre()
        self.__createur = self.__gestionnaire.getCreateur()
        self.__bute = self.__gestionnaire.getBute()
        self.__nameAssistant = self.__gestionnaire.getName()

    def setUserGenre(self,genre:str):
        self.__user = self.__gestionnaire.getUser()
        self.__genre = self.__gestionnaire.getGenre()


    def getNoComprehension(self):
        return self.__formule.lectureJSON("nc")

    def getPhraseBootNormale(self,nb:str):
        phrases = self.__formule.lectureJSONList("bootN" + nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseAurevoir(self,nb:str):
        phrases = self.__formule.lectureJSONList("stop"+ nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseBootHist(self,nb:str):
        phrase = self.__formule.lectureJSON("bootHist"+nb)
        return phrase.format(genre=self.__genre, user=self.__user)

    def getBlague(self,nb:int):
        """
        :param nb: Max 9
        :return:
        """
        return self.__formule.lectureJSONList("blague")[nb]

    def getReponseBlague(self,nb:int):
        """
        :param nb: Max 9
        :return:
        """
        return self.__formule.lectureJSONList("reponse")[nb]

    def getPhraseChatBotNormal(self, index:str):
        phrases = self.__chatbot.lectureJSON(index)
        return phrases.format(genre=self.__genre, user=self.__user,bute = self.__bute,name=self.__nameAssistant,createur=self.__createur)

    def getPhraseChatBotList(self, index:str):
        phrases = self.__formule.lectureJSONList(index)
        return [phrase.format(genre=self.__genre, user=self.__user,bute = self.__bute,name=self.__nameAssistant,createur=self.__createur) for phrase in phrases]

    def getPhraseListeFonction(self):
        listFonction = self.__gestionnaire.getListFonction()
        nbFonction = self.__gestionnaire.getNbListFonction()
        nb = nbFonction - 1
        text = self.__chatbot.lectureJSON("phListFonc")
        for i in range(0, nbFonction):
            if i == nb:
                text = text + " et " + listFonction[i]
            else:
                if i == 0:
                    text = text + listFonction[i]
                else:
                    text = text + ", " + listFonction[i]
        return text + " ."

    def getPhraseCodehelp(self,nb:str):
        formule = self.__codeHelp.lectureJSON("ph"+nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpen(self,nb:str):
        formule = self.__open.lectureJSON("ph"+nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenList(self,nb:str):
        phrases = self.__open.lectureJSON("ph"+nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

    def getPhraseOpenError(self,nb:str):
        formule = self.__open.lectureJSON("phError"+nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseOpenRadio(self, radio:str, etat:bool):
        if etat:
            formule = self.__open.lectureJSON("phRadio")
            return formule.format(genre=self.__genre, user=self.__user, radio=radio)
        else:
            formule = self.__open.lectureJSON("phRadioError")
            return formule.format(genre=self.__genre, user=self.__user, radio=radio)

    def getPhraseOpenSite(self,site:str,etat:bool):
        if etat :
            formule = self.__open.lectureJSON("phSite")
            return formule.format(genre=self.__genre,user=self.__user,site=site)
        else :
            formule = self.__open.lectureJSON("phSiteError")
            return formule.format(genre=self.__genre,user=self.__user,site=site)

    def getPhraseNbOpenSoftware(self, nb:str):
        formule = self.__open.lectureJSON("phNbSite")
        return formule.format(genre=self.__genre,user=self.__user,nombre=nb)

    def getPhraseNbOpenSite(self, nb: str):
        formule = self.__open.lectureJSON("phNbSoftware")
        return formule.format(genre=self.__genre, user=self.__user, nombre=nb)

    def getPhraseListeRadio(self):
        listRadio = self.__open.lectureJSONList("phListRadion")
        text = listRadio[0]
        for i in range(1, len(listRadio)):
            text = text + "\n- " + listRadio[i]
        return text

    def getPhraseSearch(self,nb:str):
        formule = self.__search.lectureJSON("ph"+nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseResultatCalcule(self,resultat:str):
        formule = self.__service.lectureJSON("phcalcule")
        return formule.format(genre=self.__genre,user=self.__user,resultat=resultat)

    def getPhraseService(self,nb:str):
        formule = self.__service.lectureJSON("ph"+nb)
        return formule.format(genre=self.__genre,user=self.__user)

    def getPhraseSoftware(self,nb:str):
        formule = self.__software.lectureJSON("ph"+nb)
        return formule.format(genre=self.__genre,user=self.__user)