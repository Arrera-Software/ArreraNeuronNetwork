import geocoder
import requests

class GPS:
    def __init__(self,KeyGPS:str):
        self.g = geocoder.ip('me')
        self.url = "http://api.openweathermap.org/geo/1.0/"
        self.key = KeyGPS
            
    def recuperationCordonneePossition(self):
        if self.g.ok:
            self.loc = self.g.latlng
            return True
        else:
            return False
    
    def getlatPossition(self):
        return str(self.loc[0])

    def getlonPossition(self):
        return str(self.loc[1]) 
    
    def recuperationCordonneeVille(self,ville:str):
        reponse = requests.get(self.url+"direct?q="+ville+"&appid="+self.key+"&limit=1")
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
        reponse = requests.get(self.url+"reverse?"+"lat="+str(self.loc[0])+"&lon="+str(self.loc[1])+"&appid="+self.key)
        if reponse.status_code == 400 :
            return False
        else :
            self.nameVille = reponse.json()[0]["local_names"]["fr"]
            return True
    
    def getNameVille(self):
        return self.nameVille