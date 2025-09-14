import json

class gestKeyword:
    def __init__(self,emplacement:str):
        self.__listFileKeyword = ["api.json","chatbot.json","codehelp.json",
                                  "open.json","search.json","service.json",
                                  "software.json","time.json","work.json"]
        self.__directoryKeyword = emplacement
        self.__keyWordLoaded = False
        self.__apiFile = None
        self.__chatbotFile = None
        self.__codehelpFile = None
        self.__openFile = None
        self.__searchFile = None
        self.__serviceFile = None
        self.__softwareFile = None
        self.__timeFile = None
        self.__workFile = None

    def __loadKeyword(self)->bool:
        try :
            with open(self.__directoryKeyword+self.__listFileKeyword[0],"r",encoding="utf-8") as f:
                self.__apiFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[1],"r",encoding="utf-8") as f:
                self.__chatbotFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[2],"r",encoding="utf-8") as f:
                self.__codehelpFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[3],"r",encoding="utf-8") as f:
                self.__openFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[4],"r",encoding="utf-8") as f:
                self.__searchFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[5],"r",encoding="utf-8") as f:
                self.__serviceFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[6],"r",encoding="utf-8") as f:
                self.__softwareFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[7],"r",encoding="utf-8") as f:
                self.__timeFile = json.load(f)
            with open(self.__directoryKeyword+self.__listFileKeyword[8],"r",encoding="utf-8") as f:
                self.__workFile = json.load(f)
            self.__keyWordLoaded = True
            return True
        except Exception as e:
            print(f"Erreur lors du chargement des fichiers de mots-clés : {e}")
            self.__keyWordLoaded = False
            return False


    def __getKeyWork(self,neuron:str,fonction:str)->list:
        if not self.__keyWordLoaded:
            if not self.__loadKeyword():
                return []

        if neuron == "api":
            if fonction in self.__apiFile:
                return self.__apiFile[fonction]
        elif neuron == "chatbot":
            if fonction in self.__chatbotFile:
                return self.__chatbotFile[fonction]
        elif neuron == "codehelp":
            if fonction in self.__codehelpFile:
                return self.__codehelpFile[fonction]
        elif neuron == "open":
            if fonction in self.__openFile:
                return self.__openFile[fonction]
        elif neuron == "search":
            if fonction in self.__searchFile:
                return self.__searchFile[fonction]
        elif neuron == "service":
            if fonction in self.__serviceFile:
                return self.__serviceFile[fonction]
        elif neuron == "software":
            if fonction in self.__softwareFile:
                return self.__softwareFile[fonction]
        elif neuron == "time":
            if fonction in self.__timeFile:
                return self.__timeFile[fonction]
        elif neuron == "work":
            if fonction in self.__workFile:
                return self.__workFile[fonction]
        return []

    def __checkContainWord(self,texte:str,listWord:list)->bool:
        texte = texte.lower()
        for word in listWord:
            if word.lower() in texte:
                return True
        return False

    def checkAPI(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("api",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkChatBot(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("chatbot",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkCodeHelp(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("codehelp",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkOpen(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("open",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkSearch(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("search",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkService(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("service",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkSoftware(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("software",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkTime(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("time",fonction)
        return self.__checkContainWord(texte,listWord)

    def checkWork(self,texte:str,fonction:str)->bool:
        listWord = self.__getKeyWork("work",fonction)
        return self.__checkContainWord(texte,listWord)

    def getListKeyword(self,neuron:str,fonction:str)->list:
        if neuron not in ["api","chatbot","codehelp","open","search","service","software","time","work"]:
            return []
        if neuron == "" or fonction == "":
            return []
        return self.__getKeyWork(neuron,fonction)