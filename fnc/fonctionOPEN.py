from fnc.fncBase import fncBase,gestionnaire
from librairy.openSoftware import OpenSoftware

class fonctionOpen(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__softopen = OpenSoftware()

    def openSoft(self,name:str) -> bool:
        if name == "":
            return False

        dictSoft = self._gestionnaire.getUserConf().getSoft()

        if name in dictSoft:
            emplacement = dictSoft[name]
            if self.__softopen.setLocation(emplacement):
                return self.__softopen.open()
            else:
                return False
        else:
            return False