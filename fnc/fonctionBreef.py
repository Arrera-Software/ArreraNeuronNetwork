from librairy.arrera_date import *
from fnc.fncBase import fncBase,gestionnaire

class fncBreef(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        # FNC
        # fncObjet = self._gestionnaire.getGestFNC()
        # self.__task = fncObjet.getFNCTask()
        # self.__meteoFNC = fncObjet.getFNCMeteo()
        # self.__work = fncObjet.getFNCWork()
        # Librairie
        self.__date = CArreraDate()

    def summarizeActu(self):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            actuFNC = self._gestionnaire.getGestFNC().getFNCActu()
            if actuFNC.setActu(5,"fr"):
                return actuFNC.getActu()
            else :
                return None
        else :
            return None

    def summarizeTaskToday(self):
        task = self._gestionnaire.getGestFNC().getFNCTask()
        return task.getListTaskToday()

    def summarizeAll(self):
        try :
            actu = []
            taskToday = []
            if self._gestionnaire.getNetworkObjet().getEtatInternet():
                actuFNC = self._gestionnaire.getGestFNC().getFNCActu()
                if actuFNC.setActu(3, "fr"):
                    actu = actuFNC.getActu()

            task = self._gestionnaire.getGestFNC().getFNCTask()
            taskToday = task.getListTaskToday()

            return {"actu" : actu,"task":taskToday}

        except Exception as e:
            return None

    # def morningBreef(self):