import requests
from datetime import datetime, timedelta

class Actu :
    def __init__(self,keyActu:str):
        self.__keyActu = keyActu
        self.__nbPage = 0
        self.__URLbase = "https://newsapi.org/v2/everything?apiKey="

    def setActu(self,nbPage:str,lang:str):
        listFlag = ["&language="+lang,
                    "&pageSize="+nbPage,"&q=France"]
        self.__jsonActu = requests.get(self.__URLbase+self.__keyActu+
                                     listFlag[0]+
                                     listFlag[1]+
                                     listFlag[2]).json()
        sortieRequest = self.__jsonActu["status"]
        nomResute = self.__jsonActu["totalResults"]
        if (sortieRequest=="ok" and nomResute != 0):
            self.__nbPage = int(nbPage)
            return True
        else :
            self.__nbPage = 0
            return False


    def getActu(self):
        if (self.__nbPage!=0):
            listeDescription = []
            retourActu = self.__jsonActu["articles"]
            for i in range(0,self.__nbPage) :
                listeDescription.append(retourActu[i]["title"])
            return listeDescription
        else :
            return ["error","error"]