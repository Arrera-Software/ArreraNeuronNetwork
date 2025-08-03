from fnc.fncBase import fncBase,gestionnaire
import webbrowser as wb
# Codehelp
from objet.CHsearchDoc import CHsearchDoc
from gui.codehelp.CHGithub import CHGithub
from gui.codehelp.CHLibrairy import CHLibrairy

class fncCodehelp(fncBase) :
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)
        # self.__orgaVar = CHOrgraVarriable(configNeuron,dectOs)
        self.__searchDoc = CHsearchDoc()
        # self.__colorSelector = CCHcolorSelector(configNeuron)
        self.__githubObjet = CHGithub(gestionnaire)
        self.__librairyCodehelp = CHLibrairy()

    def searchDocInDevDoc(self, recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchDevDoc(recherche)
        else :
            return False

    def searchDocInMicrosoft(self,recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchMicrosoft(recherche)
        else :
            return False

    def searchDocInPython(self,recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchPython(recherche)
        else :
            return False
    """
    def activeOrgaVar(self):
        self.__orgaVar.bootOrganisateur()

    
    def activeColorSelecteur(self):
        self.__colorSelector.bootSelecteur()
    """
    def searchGithub(self,requette:str):
        self.__githubObjet.search(requette)
    
    def openSiteGithub(self):
        wb.open("https://github.com/")

    def openGestionGithub(self):
        self.__githubObjet.active()

    def openOutilLibrairy(self):
        self.__librairyCodehelp.active()