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