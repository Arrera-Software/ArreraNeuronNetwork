import requests
import geocoder

class Actu :
    def __init__(self,keyActu:str,nbPage:int,pay:str,lang:str):
        self.nbPage = int(nbPage)
        self.pay = pay
        self.keyActu = keyActu
        self.langue = lang
        self.URLActu = "https://newsapi.org/v2/top-headlines?"+"apiKey="+self.keyActu+"&country="+self.pay+"&category=general"+"&pageSize="+str(self.nbPage)+"&language="+self.langue
        
    def Actu(self):
        retourActu = requests.get(self.URLActu).json()["articles"]
        listeDescription = []
        for i in range(0,self.nbPage) :
            listeDescription.append(retourActu[i]["title"])
        
        return listeDescription
    
    
class Meteo : 
    def __init__(self,keyAPI : str):
        self.keyApi= keyAPI
        self.url="https://api.openweathermap.org/data/2.5/weather?"
        
        self.temperature = ""
        self.humiditer =  ""
        self.description =  ""
        self.icon =  ""
    
    def recuperationDataMeteo(self,latitude:str,longitude:str):
        self.latitude = latitude
        self.longitude = longitude
        reponse=requests.get(self.url+"lat="+str(self.latitude)+"&lon="+str(self.longitude)+"&lang=fr&units=metric&appid="+self.keyApi).json()
        if reponse["cod"] == "401" or reponse["cod"] == "400" :
            return False
        else :
            reponseData = reponse["main"]
            reponseDescription = reponse["weather"][0]
            self.temperature = str(reponseData["temp"])
            self.humiditer =  str(reponseData["humidity"])
            self.description =  str(reponseDescription["description"])
            self.icon =  str(reponseDescription['icon'])
            return True
            
       
    def gettemperature(self):#permet de recuperé la temperature
        return self.temperature
    
    def gethumiditer(self):#permet de recuperé le taux d'humiditer en %
       return self.humiditer
    
    def getdescription(self):#permet de recuperé la description de temp en fr
        return self.description
        
    def geticon(self):
        return self.icon