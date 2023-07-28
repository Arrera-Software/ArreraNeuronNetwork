class gestionNetwork:
    def __init__(self):
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
    
    def setVous(self,vous:bool):
        self.vous = vous
    
    def setGenre(self,genre:str):
        self.genre = genre
        
    def setName(self,name:str):
        self.name = name.lower()
        
    def setUser(self,user:str):
        self.user = user 
    
    def setBute(self,bute:str):
        self.bute = bute
    
    def setCreateur(self,createur:str):
        self.createur = createur
    
    def setListFonction(self,liste:list[str]):
        self.listFonction = liste
        
    def addDiscution(self):
        self.nbDiscution =+ 1
    
    def setAll(self,vous:bool,genre:str,name:str,user:str,bute:str,createur:str,liste:list[str],nbVille:int):
        self.vous = bool(vous)
        self.genre =  str(genre)
        self.name =  str(name)
        self.user =  str(user) 
        self.bute =  str(bute)
        self.createur =  str(createur)
        self.listFonction = liste
        self.nbVilleMeteo = nbVille
    
    def setVilleMeteo(self,listVille:list[str]):
        self.listVille = listVille
    
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