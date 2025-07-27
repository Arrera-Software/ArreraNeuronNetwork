from fnc.fncBase import fncBase,gestionnaire
import geocoder
import requests
import webbrowser
import subprocess

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

        """
        self.__url = "http://api.openweathermap.org/geo/1.0/"
        self.__key = KeyGPS
        if etatConnextion == True :
            self.__g = geocoder.ip('me')
        else :
            self.__g = ""
            
    def recuperationCordonneePossition(self):
        if self.__g.ok:
            self.loc = self.__g.latlng
            return True
        else:
            return False
    
    def getlatPossition(self):
        return str(self.loc[0])

    def getlonPossition(self):
        return str(self.loc[1]) 
    
    def recuperationCordonneeVille(self,ville:str):
        reponse = requests.get(self.__url+"direct?q="+ville+"&appid="+self.__key+"&limit=1")
        if reponse.status_code == 400 :
            return False
        else :
            self.loc = reponse.json()[0]
            return True
    
    def getlatVille(self):
        return self.loc["lat"]

    def getLonVille(self):
        return self.loc["lon"]  
    
    def recuperationNameVillePosition(self):
        reponse = requests.get(self.__url+"reverse?"+"lat="+str(self.loc[0])+"&lon="+str(self.loc[1])+"&appid="+self.__key)
        if reponse.status_code == 400 :
            return False
        else :
            self.nameVille = reponse.json()[0]["name"]
            return True
    
    def getNameVille(self):
        return self.nameVille
    
    def launchGoogleMapItineraire(self,depart:str, arrivee:str):
        if (depart!="" and arrivee!=""):
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
        else :
            return False
    """