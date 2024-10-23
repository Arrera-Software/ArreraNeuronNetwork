from librairy.travailJSON import *

class CAlanguage:
    def __init__(self,configFile:jsonWork):
        emplacement = configFile.lectureJSON("moduleLanguage")
        index = jsonWork(emplacement+"index.json")
        self.__formule = jsonWork(emplacement+index.lectureJSON("formule"))
        print(self.__formule.getContenuJSON())