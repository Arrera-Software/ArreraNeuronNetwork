import json
from librairy.resource_lib import resource_lib

class gestKeyword:
    def __init__(self, emplacement: str):
        self.__directoryKeyword = emplacement
        self.__keyWordLoaded = False
        self.__interface_file = None
        self.__r_lib = resource_lib()

    def __loadKeyword(self) -> bool:
        try:
            with open(self.__r_lib.resource_path(self.__directoryKeyword + "interface.json"), "r", encoding="utf-8") as f:
                self.__interface_file = json.load(f)
            self.__keyWordLoaded = True
            return True
        except Exception as e:
            print(f"Erreur lors du chargement des fichiers de mots-clés : {e}")
            self.__keyWordLoaded = False
            return False

    def __getKeyWork(self, neuron: str, fonction: str) -> list:
        if not self.__keyWordLoaded:
            if not self.__loadKeyword():
                return []

        if neuron == "interface" and self.__interface_file:
            if fonction in self.__interface_file:
                return self.__interface_file[fonction]
        return []

    def __checkContainWord(self, texte: str, listWord: list) -> bool:
        texte = texte.lower()
        for word in listWord:
            if word.lower() in texte:
                return True
        return False

    def checkInterface(self, texte: str, fonction: str) -> bool:
        listWord = self.__getKeyWork("interface", fonction)
        return self.__checkContainWord(texte, listWord)

    def getListKeyword(self, neuron: str, fonction: str) -> list:
        if neuron != "interface" or not fonction:
            return []
        return self.__getKeyWork(neuron, fonction)