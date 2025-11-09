from neuron.CNeuronBase import neuronBase,gestionnaire
import random
from datetime import time,datetime

class interface(neuronBase):
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)

    def neurone(self,requette:str):
        if self._keyword.checkInterface(requette,"erreuropensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("2"),""]
        elif self._keyword.checkInterface(requette,"noopensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("3"),""]
        elif self._keyword.checkInterface(requette,"opensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("1"),""]
        elif self._keyword.checkInterface(requette,"breef"):
            if time(6,0) <= datetime.now().time() < time(11,0):
                texte = self._language.getPhraseMorningBreef("1")
                self._gestGUI.activeBreef()
                outInt = 19
            else :
                out = self._gestFNC.getFNCBreef().summarizeAll()
                texte = self._language.getPhraseResumerAll("2")
                if out is not None:
                    outInt = 19
                    self._gestGUI.activeViewResumer(dict=out,list=None,intIn=outInt)
                else :
                    outInt = 20
            self._listSortie = [texte,""]
            self._valeurOut = outInt

        elif self._keyword.checkInterface(requette,"meteo"):
            state = self._gestFNC.getFNCMeteo().getMeteoCurrentHour()
            if state:
                texte =  self._language.getPhraseMeteo(str(random.randint(5, 6)),
                                                       self._gestFNC.getFNCMeteo().getNameTown(),
                                                       self._gestFNC.getFNCMeteo().getDescription(),
                                                       self._gestFNC.getFNCMeteo().getTemperature()
                                                     )[random.randint(0, 1)]
            else :
                texte =  self._language.getPhraseMeteoError(str(random.randint(5, 6)))
            self._valeurOut = 0
            self._listSortie = [texte,""]
        elif self._keyword.checkInterface(requette,"task"):
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseTime("9"), ""]
            self._gestGUI.activeTache()
        elif self._keyword.checkInterface(requette,"agenda"):
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseTime("8"), ""]
            self._gestGUI.activeAgenda()