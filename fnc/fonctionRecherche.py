from fnc.fncBase import fncBase,gestionnaire
import webbrowser
import requests
import time

class fncArreraSearch(fncBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__objNetwork = self._gestionnaire.getNetworkObjet()
        
    def __verifConnexion(self):
        self.__etatConnexion = self.__objNetwork.getEtatInternet()

    def search(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            # Recherche avec l'interface Arrera
            if self._gestionnaire.getGestNeuron().getSocket():
                return self._gestSocket.sendData("recherche "+query)
            else :
                moteurUser = self._gestionnaire.getUserConf().getMoteurRecherche()
                if moteurUser == "google":
                    return self.googleSearch(query)
                elif moteurUser == "brave":
                    return self.braveSearch(query)
                elif moteurUser == "duckduckgo":
                    return self.duckduckgoSearch(query)
                elif moteurUser == "qwant":
                    return self.qwantSearch(query)
                elif moteurUser == "ecosia":
                    return self.ecosiaSearch(query)
                elif moteurUser == "bing":
                    return self.bingSearch(query)
                elif moteurUser == "perplexity":
                    return self.perplexitySearch(query)
                else:
                    moteurDefault = self._gestionnaire.getConfigFile().moteurderecherche
                    if moteurDefault == "google":
                        return self.googleSearch(query)
                    elif moteurDefault == "brave":
                        return self.braveSearch(query)
                    elif moteurDefault == "duckduckgo":
                        return self.duckduckgoSearch(query)
                    elif moteurDefault == "qwant":
                        return self.qwantSearch(query)
                    elif moteurDefault == "ecosia":
                        return self.ecosiaSearch(query)
                    elif moteurDefault == "bing":
                        return self.bingSearch(query)
                    elif moteurDefault == "perplexity":
                        return self.perplexitySearch(query)
                    else :
                        return self.googleSearch(query)
        else:
            return False

    def braveSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://search.brave.com/search?q='
            urllink = requests.get(url+query+"&source=web")
            lienBrave = urllink.url
            webbrowser.open(lienBrave)
            return True
        else :
            return False

    def amazonSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://www.amazon.fr/s?k='
            urllink = requests.get(url+query)
            lienAmazon = urllink.url
            webbrowser.open(lienAmazon)
            return True
        else :
            return False

    def googleSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://www.google.com/search?q'
            query = {'q': query}
            urllink = requests.get(url, params=query)
            liengoogle = urllink.url
            webbrowser.open(liengoogle)
            return True
        else :
            return False

    def duckduckgoSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://duckduckgo.com/?q='
            lienduck = url+query
            webbrowser.open(lienduck) 
            return True
        else :
            return False 

    def qwantSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://www.qwant.com/?l=fr&q'
            query = {'q': query}
            urllink = requests.get(url, params=query)
            lienQwant = urllink.url
            webbrowser.open(lienQwant)
            return True
        else :
            return False


    def ecosiaSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = 'https://www.ecosia.org/search'
            query = {'q': query}
            urllink = requests.get(url,query)
            lienEcosia = urllink.url
            webbrowser.open(lienEcosia) 
            return True
        else :
            return False

    def bingSearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = "https://www.bing.com/search"
            query = {'q': query}
            urllink = requests.get(url, params=query)
            lienbing = urllink.url
            webbrowser.open(lienbing)
            return True
        else :
            return False
    
    def perplexitySearch(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            url = "https://www.perplexity.ai/search/new?q"
            webbrowser.open(url+"="+query+". Repond en francais")
            return True
        else :
            return False
    
    def bigRecherche(self,query:str):
        self.__verifConnexion()
        if self.__etatConnexion:
            i = 0
            while(i!=6):
                if (i==1) :
                    self.googleSearch(query)
                    time.sleep(1.5)
                else :
                    if (i==2):                
                        self.qwantSearch(query)
                        time.sleep(1.5)
                    else :
                        if(i==3):
                            self.duckduckgoSearch(query)
                            time.sleep(1.5)
                        else :
                            if(i==4):
                                self.bingSearch(query)
                                time.sleep(1.5)
                            else :
                                if(i==5):
                                    self.perplexitySearch(query)
                                    time.sleep(1.5)
                                        
                i = i + 1
            return True
        else :
            return False