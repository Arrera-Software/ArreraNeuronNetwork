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

    def setUserGenre(self,genre:str):
        self.__user = self.__gestionnaire.getUser()
        self.__genre = self.__gestionnaire.getGenre()


    def getNoComprehension(self):
        return self.__formule.lectureJSON("nc")

    def getPhraseBootNormale(self,nb:str):
        phrases = self.__formule.lectureJSONList("bootN" + nb)
        return [phrase.format(genre=self.__genre, user=self.__user) for phrase in phrases]

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