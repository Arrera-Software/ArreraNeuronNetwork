from librairy.travailJSON import *

class CAlanguage:
    def __init__(self,configFile:jsonWork):
        emplacement = configFile.lectureJSON("moduleLanguage")
        index = jsonWork(emplacement+"index.json")
        self.__formule = jsonWork(emplacement+index.lectureJSON("formule"))

    def getNoComprehension(self):
        return self.__formule.lectureJSON("nc")

    def getPhraseBootNormale(self,nb:str,genre:str,user:str):
        phrases = self.__formule.lectureJSONList("bootN" + nb)
        return [phrase.format(genre=genre, user=user) for phrase in phrases]