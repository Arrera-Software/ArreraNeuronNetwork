from neuron.CNeuronBase import *

class neuroneService(neuronBase) :
        
    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        self._keyword.checkService(requette,"read")
        if (self._keyword.checkService(requette,"read") and
                self._keyword.checkService(requette,"lecture-contenu")) :
            self._gestGUI.activeLecture()
            self._listSortie = [self._language.getPhraseService("6"), ""]
            self._valeurOut = 5
        elif self._keyword.checkService(requette,"calcule"):
            listKeyword = self._keyword.getListKeyword("service","calcule")
            for word in listKeyword:
                requette = requette.replace(word,"")

            requette = requette.strip()

            if self._keyword.checkService(requette,"nombre") :
                resultat =  eval(requette)
                self._listSortie = [self._language.getPhraseResultatCalcule(resultat),
                                    ""]
            else :
                self._listSortie = [self._language.getPhraseService("1"), ""]
            self._valeurOut = 1

        elif (self._keyword.checkOpen(requette,"open") and
              self._keyword.checkService(requette,"doc")) :
            if self._gestFNC.getFNCOpen().openWebSite(self._gestionnaire.getLinkDoc()):
                self._listSortie = [self._language.getPhraseService("2"), ""]
            else :
                self._listSortie = [self._language.getPhraseService("8"), ""]
            self._valeurOut = 1

        elif self._keyword.checkService(requette,"corige"):
            if self._gestionnaire.getNetworkObjet().getEtatInternet():
                if self._gestFNC.getFNCOrthographe().getToolLaunched():
                    listKeyword = self._keyword.getListKeyword("service","corige")

                    for word in listKeyword:
                        requette = requette.replace(word,"")
                    requette = requette.strip()

                    self._gestGUI.activeOrthographe(requette)
                    self._listSortie = [self._language.getPhraseService("3"), ""]
                else :
                    self._listSortie = [self._language.getPhraseService("4"), ""]
            else :
                self._listSortie = [self._language.getPhraseService("7"), ""]
            self._valeurOut = 1