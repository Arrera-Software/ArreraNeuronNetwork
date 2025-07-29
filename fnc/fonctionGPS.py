from fnc.fncBase import fncBase,gestionnaire
import requests
import webbrowser
import urllib.parse

class fncGPS(fncBase):
    def __init__(self,gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        self.__latitude = None
        self.__longitude = None

    def locate(self):
        api_url = 'https://ipinfo.io/json'
        if self._gestionnaire.getNetworkObjet().getEtatInternet() :
            try:
                response = requests.get(api_url, timeout=5)
                response.raise_for_status()
                data = response.json()
                loc = tuple(map(float, data['loc'].split(',')))
                self.__latitude = loc[0]
                self.__longitude = loc[1]
                return True
            except Exception as e:
                return False
        else :
            return False

    def getLatitude(self):
        return self.__latitude

    def getLongitude(self):
        return self.__longitude

    def getTown(self):
        url = 'https://nominatim.openstreetmap.org/reverse'
        params = {
            'lat': str(self.__latitude),
            'lon': str(self.__longitude),
            'format': 'json',
            'zoom': 10,  # Niveau de détail (10 = ville)
            'addressdetails': 1,
        }
        headers = {
            'User-Agent': 'my-geocoder'
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        city = data.get('address', {}).get('city') \
               or data.get('address', {}).get('town') \
               or data.get('address', {}).get('village')
        return city

    def launchGoogleMapItinerary(self, depart: str, arrivee: str):
        if depart != "" and arrivee != "":
            base_url = "https://www.google.com/maps/dir/?api=1"
            params = {
                "origin": depart,
                "destination": arrivee
            }

            # Encoder les paramètres pour les inclure dans l'URL
            url_params = urllib.parse.urlencode(params)
            full_url = f"{base_url}&{url_params}"

            # Ouvrir l'URL dans le navigateur par défaut
            return webbrowser.open(full_url)
        else:
            return False

    def getTownWithLatitudeAndLongitude(self,latitude:str,longitude:str):
        if self._gestionnaire.getNetworkObjet().getEtatInternet() :
            url = 'https://nominatim.openstreetmap.org/reverse'
            params = {
                'lat': str(latitude),
                'lon': str(longitude),
                'format': 'json',
                'zoom': 10,  # Niveau de détail (10 = ville)
                'addressdetails': 1,
            }
            headers = {
                'User-Agent': 'my-geocoder'
            }
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            city = data.get('address', {}).get('city') \
                   or data.get('address', {}).get('town') \
                   or data.get('address', {}).get('village')
            return city
        else :
            return None