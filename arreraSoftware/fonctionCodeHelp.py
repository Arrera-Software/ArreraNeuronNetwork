from objet.CHOrgraVarriable import*
from objet.CHsearchDoc import*
from objet.CCHcolorSelector import*
from librairy.dectectionOS import*

class fncCodehelp :
    def __init__(self,configNeuron:jsonWork,dectOs:OS) -> None:
        self.__orgaVar = CHOrgraVarriable(configNeuron,dectOs)
        self.__searchDoc = CHsearchDoc()
        self.__colorSelector = CCHcolorSelector(configNeuron)
    
    def activeOrgaVar(self):
        self.__orgaVar.bootOrganisateur()

    def rechercheDoc(self,mode:int,recherche:str):
        """
        1 : DevDoc
        2 : Microsoft
        3 : Python 
        """
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