from fnc.fncBase import fncBase,gestionnaire
from pyradios import RadioBrowser
import threading as th
import vlc

class fncRadio(fncBase) :
    def __init__(self, gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__rdBrowser = RadioBrowser()
        self.__etatNetwork = self._gestionnaire.getNetworkObjet().getEtatInternet()
        self.__stations = []
        self.__player = None
        self.__isRunning = False
        self.__thread = None

    def __searchRadio(self, radio):
        self.__stations = []
        self.__stations = self.__rdBrowser.search(name=radio, country="France")
        return bool(self.__stations)

    def __launchRadioThread(self):
        if not self.__isRunning and self.__stations and self.__etatNetwork:
            url = self.__stations[0]['url']
            self.__player = vlc.MediaPlayer(url)
            self.__isRunning = True
            self.__player.play()

    def __launchRadio(self):
        if not self.__isRunning:
            self.__thread = th.Thread(target=self.__launchRadioThread)
            self.__thread.start()

    def stopRadio(self):
        if self.__player and self.__isRunning:
            self.__player.stop()
            self.__player = None
            self.__isRunning = False
            if self.__thread:
                self.__thread.join(timeout=1)

    
    def startEurope1(self):
        if self.__etatNetwork:

            return True
        else :
            return False
       
    def startEurope2(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/europe-2/")
            return True
        else :
            return False
    
    def startFranceInfo(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-info/")
            return True
        else :
            return False
    
    def startFranceInter(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-inter/")
            return True
        else :
            return False
    
    def startFranceMusique(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/france-musique/")
            return True
        else :
            return False
    
    def startFranceCulture(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-culture/ ")
            return True
        else :
            return False
    
    def startFranceBleu(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/france-bleu-ile-de-france/")
            return True
        else :
            return False
    
    def startFunRadio(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/fun-radio/")
            return True
        else :
            return False
    
    def startNRJ(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/nrj/")
            return True
        else :
            return False
    
    def startRFM(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/rfm/")
            return True
        else :
            return False
    
    def startNostalgi(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-nostalgie/")
            return True
        else :
            return False
    
    def startSkyrock(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/skyrock/")
            return True
        else :
            return False
    
    def startRTL(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/rtl/")
            return True
        else :
            return False