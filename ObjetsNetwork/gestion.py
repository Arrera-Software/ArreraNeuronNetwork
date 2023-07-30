from librairy.travailJSON import *

class gestionNetwork:
    def __init__(self,fileUser:jsonWork,ConfigFile:jsonWork):
        self.fileUser = fileUser
        self.ConfigFile = ConfigFile
        self.vous = False
        self.genre =""
        self.name  =""
        self.user =""
        self.bute =""
        self.listFonction = []
        self.createur =""
        self.nbDiscution =0
        self.oldRequette =""
        self.oldSortie =""
        self.nbVilleMeteo = 0
        self.listVille = []
    
    def setVous(self):
        if self.ConfigFile.lectureJSON("utilisationVous") == "1":
            self.vous = True
        else :
            self.vous = False
    
    def setGenre(self):
        self.genre =  self.fileUser.lectureJSON("genre")
        
    def setName(self):
        self.name =  self.ConfigFile.lectureJSON("name").lower
        
    def setUser(self):
        self.user =  self.fileUser.lectureJSON("user")
    
    def setBute(self):
        self.bute =   self.ConfigFile.lectureJSON("bute")
    
    def setCreateur(self):
        self.createur = self.ConfigFile.lectureJSON("createur")
    
    def setListFonction(self):
        self.listFonction = self.ConfigFile.lectureJSON("listFonction")
        
    def addDiscution(self):
        self.nbDiscution =+ 1
    
    def setAll(self):
        if self.ConfigFile.lectureJSON("utilisationVous") == "1":
            self.vous = True
        else :
            self.vous = False
        self.genre =  self.fileUser.lectureJSON("genre")
        self.name =  str(self.ConfigFile.lectureJSON("name")).lower()
        self.user =  str(self.fileUser.lectureJSON("user"))
        self.bute =   self.ConfigFile.lectureJSON("bute")
        self.createur =   str(self.ConfigFile.lectureJSON("createur"))
        self.listFonction = self.ConfigFile.lectureJSON("listFonction")
        self.nbVilleMeteo = int(self.ConfigFile.lectureJSON("nombreVilleMeteo"))
    
    def setVilleMeteo(self):
        self.listVille = self.fileUser.lectureJSONList("listVille")
    
    def getVous(self):
        return bool(self.vous)
    
    def getGenre(self):
        return str(self.genre) 
        
    def getName(self):
        return  str(self.name )
        
    def getUser(self):
        return  str(self.user )
    
    def getBute(self):
        return  str(self.bute )
    
    def getCreateur(self):
        return  str(self.createur )
        
    def getDiscution(self):
        return  str(self.nbDiscution)
    
    def setHistory(self,text,requette):
        self.oldRequette = requette
        self.oldSortie = text
        
    def getOldrequette(self):
        return self.oldRequette
    
    def getOldSortie(self):
        return self.oldSortie

    def getNbDiscution(self):
        return int(self.nbDiscution)
    
    def getNbListFonction(self):
        return len(self.listFonction)
    
    def getListFonction(self):
        return self.listFonction
    
    def getnbVilleMeteo(self):
        return self.nbVilleMeteo
    
    def getListVilleMeteo(self):
        return self.listVille

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1  