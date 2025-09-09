from fnc.fncBase import fncBase,gestionnaire
from librairy.openSoftware import OpenSoftware
import webbrowser as wb

class fonctionOpen(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__softopen = OpenSoftware()
        self.__socket = self._gestionnaire.getSocketObjet()
        if self.__socket is not None and self.__socket.getServeurOn():
            self.__socketEnabled = True
        else:
            self.__socketEnabled = False

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

    def openSoftSocket(self,name:str) -> bool:
        if not self.__socketEnabled:
            return False

        if name == "":
            return False

        return self.__socket.sendData("ouvre "+name)

    def openWebSite(self,name) -> bool:
        if name == "":
            return False

        dictWeb = self._gestionnaire.getDictionnaireWeb()
        if name in dictWeb:
            url = dictWeb[name]
        else :
            return False

        return wb.open(url)