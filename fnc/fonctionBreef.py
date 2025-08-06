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

    def summarizeActuAndMeteo(self,ville:str = ""):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            actuFNC = self._gestionnaire.getGestFNC().getFNCActu()
            meteoFNC = self._gestionnaire.getGestFNC().getFNCMeteo()
            if actuFNC.setActu(5,"fr") and meteoFNC.getMeteoCurrentHour(town=ville):
                return {"actu":actuFNC.getActu(),
                        "meteo":{
                            "ville":meteoFNC.getNameTown(),
                            "temperature":meteoFNC.getTemperature(),
                            "weather":meteoFNC.getDescription(),
                            "icon":meteoFNC.getIcon(),
                            "redAlert":meteoFNC.getRedAlert(),
                            "yellowAlert":meteoFNC.getYellowAlert(),
                            "orangeAlert":meteoFNC.getOrangeAlert(),
                            "greenAlert":meteoFNC.getGreenAlert(),
                        }}
            else :
                return None
        else :
            return None

    def summarizeTaskToday(self):
        task = self._gestionnaire.getGestFNC().getFNCTask()
        return task.getListTaskToday()

    def summarizeAll(self, ville:str = ""):
        try :
            actu = []
            taskToday = []
            meteo = {}
            if self._gestionnaire.getNetworkObjet().getEtatInternet():
                actuFNC = self._gestionnaire.getGestFNC().getFNCActu()
                meteoFNC = self._gestionnaire.getGestFNC().getFNCMeteo()
                if actuFNC.setActu(3, "fr") and meteoFNC.getMeteoCurrentHour(town=ville):
                    actu = actuFNC.getActu()
                    meteo = {"ville": meteoFNC.getNameTown(),
                             "temperature": meteoFNC.getTemperature(),
                             "weather": meteoFNC.getDescription(),
                             "icon": meteoFNC.getIcon(),
                             "redAlert": meteoFNC.getRedAlert(),
                             "yellowAlert": meteoFNC.getYellowAlert(),
                             "orangeAlert": meteoFNC.getOrangeAlert(),
                             "greenAlert": meteoFNC.getGreenAlert()}

            task = self._gestionnaire.getGestFNC().getFNCTask()
            taskToday = task.getListTaskToday()

            return {"actu" : actu,"meteo": meteo,"task":taskToday}

        except Exception as e:
            return None

    # def morningBreef(self):