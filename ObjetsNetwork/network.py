import requests
class network:
    def __init__(self) :
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            self.etatConnexion = True
        except requests.ConnectionError :
            self.etatConnexion = False
    
    def getEtatInternet(self):
        return self.etatConnexion