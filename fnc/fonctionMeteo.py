from fnc.fncBase import fncBase,gestionnaire
from datetime import datetime, timedelta
from meteofrance_api import MeteoFranceClient

class fncMete(fncBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__client = MeteoFranceClient()

    
    # def getDataMeteoNow(self,latitude:str,longitude:str):
    # def getDateMetoTowmorowMorning(self,latitude:str,longitude:str):
    # def getDateMetoTowmorowNoon(self,latitude:str,longitude:str):
    # def gettemperature(self):#permet de recuperé la temperature
    # def gethumiditer(self):#permet de recuperé le taux d'humiditer en %
    # def getdescription(self):#permet de recuperé la description de temp en fr
    # def geticon(self):
    """
    Ville : {'dt': 1753732800, 
    'T': {'value': 20.7, 'windchill': 22.9}, 
    'humidity': 55, 
    'sea_level': 1021, 
    'wind': {'speed': 3, 'gust': 0, 'direction': 340, 'icon': 'NNO'}, 
    'rain': {'1h': 0}, 
    'snow': {'1h': 0}, 
    'iso0': 2900, 
    'rain snow limit': 'Non pertinent', 
    'clouds': 10, 
    'weather': {'icon': 'p1j', 
    'desc': 'Ensoleillé'}}
    """