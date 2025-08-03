from gui.codehelp.CHGithub import*

from fnc.fncBase import fncBase,gestionnaire

class fncCodehelp(fncBase) :
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)
        # self.__orgaVar = CHOrgraVarriable(configNeuron,dectOs)
        # self.__searchDoc = CHsearchDoc()
        # self.__colorSelector = CCHcolorSelector(configNeuron)
        self.__githubObjet = CHGithub(gestionnaire)
        # self.__librairyCodehelp = CHLibrairy(configNeuron,gestNeuron)

    """
    def activeOrgaVar(self):
        self.__orgaVar.bootOrganisateur()

    
    def rechercheDoc(self,mode:int,recherche:str):
        
        1 : DevDoc
        2 : Microsoft
        3 : Python 
        
        match mode :
            case 1 :
                # DevDoc
                self.__searchDoc.rechercheDevDoc(recherche)
            case 2 : 
                # Microsoft 
                self.__searchDoc.rechercheMicrosoft(recherche)
            case 3 :
                # Python 
                self.__searchDoc.recherchePython(recherche)
    
    
    def activeColorSelecteur(self):
        self.__colorSelector.bootSelecteur()
    """
    def searchGithub(self,requette:str):
        self.__githubObjet.search(requette)
    
    def openSiteGithub(self):
        w.open("https://github.com/")

    def openGestionGithub(self):
        self.__githubObjet.active()

    """
    def openOutilLibrairy(self):
        self.__librairyCodehelp.active()
    """