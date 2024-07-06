from objet.CHOrgraVarriable import*
from librairy.dectectionOS import*

class fncCodehelp :
    def __init__(self,configNeuron:jsonWork,dectOs:OS) -> None:
        self.__orgaVar = CHOrgraVarriable(configNeuron,dectOs)
    
    def activeOrgaVar(self):
        self.__orgaVar.bootOrganisateur()

