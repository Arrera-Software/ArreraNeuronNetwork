import random

from neuron.CNeuronBase import gestionnaire,neuronBase

class neuroneOpen(neuronBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fncOpen = self._gestionnaire.getGestFNC().getFNCOpen()
        self.__fncRadio = self._gestionnaire.getGestFNC().getFNCRadio()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0

        if self.partUserRadio(requette) == 1:
            return

        if self._keyword.checkOpen(requette,"open"):

            if self.partPreSaved(requette) == 1:
                return

            if self.partArreraSoft(requette) == 1:
                return

            if self.partUserSoft(requette) == 1:
                return

        """
        if self._gestNeuron.getOpen():
            #fonction neuron Open
            if ("ouvre" in requette) or ("ouvrir" in requette):
                if self._fonctionArreraNetwork.openSoftwareAssistant(requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenSoftware(requette), ""]
                else :
                    if "youtube" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieOpenYoutube(), ""]
                        self._objHistorique.setAction("Ouverture de youtube")
                    else :
                        siteOpen = self._fonctionArreraNetwork.openSaveWebSiteAssistant(requette)
                        if siteOpen:
                            self._listSortie = [self._fonctionArreraNetwork.sortieOpenSite(requette,siteOpen), ""]
                        elif self._gestNeuron.getSocket():
                            if self._socket.getServeurOn():
                                soft = requette.replace("ouvre","").strip()
                                soft = soft.replace("ouvrir","").strip()
                                self._socket.sendData("ouvre " + soft)
                                self._listSortie = [self._language.getPhraseSocket("openSoftSocket").format(softSocket=soft)
                                    ,""]
                        elif self._gestNeuron.getSocket():
                            if self._socket.getServeurOn():
                                soft = requette.replace("ouvrir","").replace("ouvre","").strip()
                                if soft == "":
                                    self._listSortie = [self._fonctionArreraNetwork.sortieNoOpen(), ""]
                                elif soft == "arrera postite" or soft == "postite":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraPostite")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrerra postite")
                                elif soft == "arrera video download" or soft == "video download":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraVideoDownload")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrera video download")
                                elif soft == "arrera raccourci" or soft == "raccourci":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraRaccourci")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrera raccourci")
                                else :
                                    self._socket.sendData("ouvre " + soft)
                                    self._listSortie = [self._language.getPhraseSocket("openSoftSocket").format(softSocket=soft),""]
                        else :
                            self._listSortie = [self._fonctionArreraNetwork.sortieNoOpen(), ""]

            elif "lance" in requette:
                if "europe 1" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(1), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 1")
                elif "europe 2" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(2), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 2")
                elif "france info" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(3), ""]
                        self._objHistorique.setAction("Lancement de la radio france info")
                elif "france inter" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(4), ""]
                        self._objHistorique.setAction("Lancement de la radio france inter")
                elif "france musique" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(5), ""]
                        self._objHistorique.setAction("Lancement de la radio france musique")
                elif "france culture" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(6), ""]
                        self._objHistorique.setAction("Lancement de la radio france culture")
                elif "fun radio" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(8), ""]
                        self._objHistorique.setAction("Lancement de la radio fun radio")
                elif "nrj" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(9), ""]
                        self._objHistorique.setAction("Lancement de la radio nrj")
                elif "rfm" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(10), ""]
                        self._objHistorique.setAction("Lancement de la radio rfm")
                elif "nostalgi" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(11), ""]
                        self._objHistorique.setAction("Lancement de la radio nostalgi")
                elif "skyrock" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(12), ""]
                        self._objHistorique.setAction("Lancement de la radio skyrock")
                elif "rtl" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(13), ""]
                        self._objHistorique.setAction("Lancement de la radio rtl")

            elif (("liste les logiciels" in requette)or("quelles sont les logiciels enregister" in requette)
                    or("quelles sont les logiciel enregister" in requette) or("quelles sont les logiciels enregiste" in requette)
                    or("quelles sont les logiciels enregiste" in requette) or ("fais une liste des logiciel"in requette)
                    or ("fais une liste des logiciels"in requette) or ("liste les logiciel" in requette)):
                        self._listSortie = [self._fonctionArreraNetwork.sortieListLogiciel(), ""]
            elif (("liste les sites" in requette)or("quelles sont les sites enregister" in requette)
                or("quelles sont les site enregister" in requette) or("quelles sont les sites enregiste" in requette)
                or("quelles sont les sites enregiste" in requette) or ("fais une liste des site"in requette)
                or ("fais une liste des sites"in requette) or ("liste les site" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieListSite(), ""]
            elif ("liste" in requette) and ("radio" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieListRadio()
                                     ,"radio"]
                self._valeurOut = 17


            #Mise a jour de la valeur
            if self._valeurOut == 0:
                self._valeurOut = self._gestionnaire.verrifSortie(self._listSortie[0])
        """

    def partUserSoft(self, requette: str) -> int:
        listKeyword = self._keyword.getListKeyword("open","open")
        software = requette
        for keyword in listKeyword:
            software = software.replace(keyword, "")
        software = software.strip().replace(" ","")
        outfnc = self.__fncOpen.openSoft(software)

        if outfnc == 1:
            nbRand = str(random.randint(1,2))
            self._listSortie = [
                self._language.getPhraseUserSoft(nbRand,software)
                ,""]
            self._valeurOut = 1
            return 1
        elif outfnc == 2:
            nbRand = str(random.randint(3,4))
            self._listSortie = [
                self._language.getPhraseUserSoft(nbRand,software)
                ,""]
            self._valeurOut = 1
            return 1
        elif outfnc == 0:
            return self.partUserWeb(requette)


    def partUserWeb(self, requette: str) -> int:
        listKeyword = self._keyword.getListKeyword("open","open")
        site = requette
        for keyword in listKeyword:
            site = site.replace(keyword, "")
        site = site.strip()

        outfnc = self.__fncOpen.openSaveWebSite(site)

        if  outfnc == 1:
            nbRand = str(random.randint(1,2))
            self._listSortie = [self._language.getPhraseUserWeb(nbRand,site)]
            self._valeurOut = 1
            return 1
        elif outfnc == 2:
            nbRand = str(random.randint(3,4))
            self._listSortie = [self._language.getPhraseUserWeb(nbRand,site)]
            self._valeurOut = 1
            return 1
        elif outfnc == 0:
            self._listSortie = [self._language.getPhraseNoOpen("1")]
            self._valeurOut = 1
            return 0
        else :
            return 0


    def partUserRadio(self, requette: str) -> int:
        if (self._keyword.checkOpen(requette,"launch") and
                self._keyword.checkOpen(requette,"radio")):
            if not self.__fncRadio.getRadioRunning():
                nbRadom = str(random.randint(1,6))
                if "eupope 1" in requette:
                    try :
                        if self.__fncRadio.startEurope1():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Europe 1"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "europe 2" in requette:
                    try :
                        if self.__fncRadio.startEurope2():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Europe 2"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france info" in requette:
                    try :
                        if self.__fncRadio.startFranceInfo():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France info"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france inter" in requette:
                    try :
                        if self.__fncRadio.startFranceInter():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France inter"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france musique" in requette:
                    try :
                        if self.__fncRadio.startFranceMusique():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France Musique"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france culture" in requette:
                    try :
                        if self.__fncRadio.startFranceCulture():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France Culture"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france bleu" in requette:
                    try :
                        if self.__fncRadio.startFranceBleu():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France bleu"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "fun radio" in requette:
                    try :
                        if self.__fncRadio.startFunRadio():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Fun radio"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "nrj" in requette:
                    try :
                        if self.__fncRadio.startNRJ():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"NRJ"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "rfm" in requette:
                    try :
                        if self.__fncRadio.startRFM():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"RFM"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "nostalgi" in requette:
                    try :
                        if self.__fncRadio.startNostalgi():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Nostalgi"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "skyrock" in requette:
                    try :
                        if self.__fncRadio.startSkyrock():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Skyrock"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "rtl" in requette:
                    try :
                        if self.__fncRadio.startRTL():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"RTL"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                return 1
            else :
                self._listSortie = [self._language.getPhraseRadioLaunch("7"),""]
                self._valeurOut = 1
                return 1
        elif (self._keyword.checkOpen(requette,"stop") and
              self._keyword.checkOpen(requette,"radio")):
            if self.__fncRadio.stop():
                self._listSortie = [self._language.getPhraseRadioLaunch("9"),""]
            else :
                self._listSortie = [self._language.getPhraseRadioLaunch("10"),""]
            self._valeurOut = 1
            return 1
        else :
            return 0

    def partArreraSoft(self, requette: str) -> int:
        if (not self._keyword.checkOpen(requette,"youtube_music")
              and self._keyword.checkOpen(requette,"youtube_downloader")):
            if self._gestGUI.activeArreraDownload():
                self._listSortie = [self._language.getPhraseArreraSoftOpen("1"),""]
            else :
                self._listSortie = [self._language.getPhraseArreraSoftOpen("2"),""]

            self._valeurOut = 5
            return 1
        if self._keyword.checkOpen(requette,"calculator"):
            if self._keyword.checkOpen(requette,"complex_mode"):
                if self._gestGUI.activeCalculatriceComplex():
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("3"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("4"),""]
                    self._valeurOut = 1
            elif self._keyword.checkOpen(requette,"pythagore_mode"):
                if self._gestGUI.activeCalculatricePythagore():
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("5"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("6"),""]
                    self._valeurOut = 1
            else :
                if self._gestGUI.activeCalculatriceNormal():
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("7"),""]
                    self._valeurOut = 5
                else :
                    self._listSortie = [self._language.getPhraseArreraSoftOpen("8"),""]
                    self._valeurOut = 1
            return 1
        else :
            return 0

    def partPreSaved(self, requette: str) -> int:

        if (self._keyword.checkOpen(requette,"youtube")
                and not self._keyword.checkOpen(requette,"youtube_music")
                and not self._keyword.checkOpen(requette,"youtube_downloader")
                and not self._keyword.checkOpen(requette,"pythagore_mode")):
            outfnc = self.__fncOpen.openWebSite("https://www.youtube.com/")

            if  outfnc == 1:
                self._listSortie = [self._language.getPhrasePresavedOpen("1"),""]
            elif outfnc == 2:
                self._listSortie = [self._language.getPhrasePresavedOpen("2"),""]
            else :
                self._listSortie = [self._language.getPhrasePresavedOpen("3"),""]
            self._valeurOut = 1
            return 1

        elif (self._keyword.checkOpen(requette,"youtube_music")
              and not self._keyword.checkOpen(requette,"youtube_downloader")):
            outfnc = self.__fncOpen.openWebSite("https://music.youtube.com/")
            if  outfnc == 1:
                self._listSortie = [self._language.getPhrasePresavedOpen("4"),""]
            elif outfnc == 2:
                self._listSortie = [self._language.getPhrasePresavedOpen("5"),""]
            else :
                self._listSortie = [self._language.getPhrasePresavedOpen("6"),""]
            self._valeurOut = 1
            return 1

        else :
            return 0
