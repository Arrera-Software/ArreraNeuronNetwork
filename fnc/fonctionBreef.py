from librairy.arrera_date import *
from fnc.fncBase import fncBase,gestionnaire

class fncBreef(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        # FNC
        fncObjet = self._gestionnaire.getGestFNC()
        self.__actuFNC = fncObjet.getFNCActu()
        self.__meteoFNC = fncObjet.getFNCMeteo()
        self.__work = fncObjet.getFNCWork()
        # Librairie
        self.__date = CArreraDate()

    # def summarizeActu(self):
    # def summarizeTask(self):
    # def summarizeAll(self):
    # def morningBreef(self):