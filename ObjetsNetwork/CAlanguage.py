from lxml.html.defs import phrase_tags

from librairy.travailJSON import *
from ObjetsNetwork.gestion import *

class CAlanguage:
    def __init__(self,configFile:jsonWork,gestionnaire:gestionNetwork):
        emplacement = configFile.lectureJSON("moduleLanguage")
        index = jsonWork(emplacement+"index.json")
        self.__formule = jsonWork(emplacement+index.lectureJSON("formule"))
        self.__chatbot = jsonWork(emplacement+index.lectureJSON("chatbot"))
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