from fnc.fncBase import fncBase,gestionnaire
from datetime import datetime, timedelta
from meteofrance_api import MeteoFranceClient
from fnc.fonctionGPS import fncGPS

class fncMeteo(fncBase) :
    def __init__(self,gestionnaire:gestionnaire,gpsFnc:fncGPS):
        super().__init__(gestionnaire)
        self.__client = MeteoFranceClient()
        self.__fncGPS = gpsFnc
        self.__nameTown = None
        self.__temperature = None
        self.__humidity = None
        self.__description = None
        self.__date = None
        self.__warming = None


    def getMeteoCurrentHour(self,town:str="",latitude:str="",longitude:str=""):
        """
        Récupère la météo actuelle pour une ville ou des coordonnées géographiques.
        :param town: Nom de la ville (optionnel)
        :param latitude: Latitude (optionnel)
        :param longitude: Longitude (optionnel)
        :return: True si les données sont récupérées avec succès, False sinon.
        """
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            if town:
                try:
                    townWeather = self.__client.search_places(town)
                    place = townWeather[0]
                    if not place:
                        return False
                    weather = self.__client.get_forecast_for_place(place)
                    dictMeteo = weather.current_forecast
                    self.__nameTown = place.name
                    self.__temperature = dictMeteo['T']['value']
                    self.__humidity = dictMeteo["humidity"]
                    self.__description = dictMeteo['weather']['desc']
                    return True
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            elif latitude and longitude:
                try:
                    town = self.__fncGPS.getTownWithLatitudeAndLongitude(latitude,longitude)
                    if town is None:
                        return False
                    else:
                        townWeather = self.__client.search_places(town)
                        place = townWeather[0]
                        if not place:
                            return False
                        weather = self.__client.get_forecast_for_place(place)
                        dictMeteo = weather.current_forecast
                        self.__nameTown = place.name
                        self.__temperature = dictMeteo['T']['value']
                        self.__humidity = dictMeteo["humidity"]
                        self.__description = dictMeteo['weather']['desc']
                        return True
                except Exception as e:
                    # print(f"Erreur lors de la récupération des données météo : {e}")
                    return False
            else :
                if self.__fncGPS.locate():
                    try :
                        townWeather = self.__client.search_places(self.__fncGPS.getTown())
                        place = townWeather[0]
                        if not place:
                            return False
                        weather = self.__client.get_forecast_for_place(place)
                        dictMeteo = weather.current_forecast
                        self.__nameTown = place.name
                        self.__temperature = dictMeteo['T']['value']
                        self.__humidity = dictMeteo["humidity"]
                        self.__description = dictMeteo['weather']['desc']
                        return True
                    except Exception as e:
                        # print(f"Erreur lors de la récupération des données météo : {e}")
                        return False
                else :
                    return False
        else :
            return False

    # def getDateMetoTowmorowMorning(self,latitude:str,longitude:str):
    # def getDateMetoTowmorowNoon(self,latitude:str,longitude:str):

    def getNameTown(self):
        return self.__nameTown

    def getTemperature(self):
        return self.__temperature

    def getHumidity(self):#permet de recuperé le taux d'humiditer en %
        return self.__humidity

    def getDescription(self):
        return self.__description

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