from fnc.fncBase import fncBase,gestionnaire
import threading as th

class fncLecture(fncBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__arrVoice = self._gestionnaire.getArrVoice()
        self.__thRead = None
        
    def __readText(self, texte:str):
        self.__thRead = th.Thread(target=self.__readText, args=(texte,))

    def read(self,texte:str):
        self.__readText(texte)