class gestionNetwork:
    def __init__(self):
        self.vous = bool
        self.genre = str
        self.name = str
        self.user = str
        self.bute = str
        self.createur = str
        self.nbDiscution = int
        self.oldRequette = str 
        self.oldSortie = str
    
    def setVous(self,vous:bool):
        self.vous = vous
    
    def setGenre(self,genre:str):
        self.genre = genre
        
    def setName(self,name:str):
        self.name = name
        
    def setUser(self,user:str):
        self.user = user 
    
    def setBute(self,bute:str):
        self.bute = bute
    
    def setCreateur(self,createur:str):
        self.createur = createur
        
    def addDiscution(self):
        self.nbDiscution =+ 1
    
    def setAll(self,vous:bool,genre:str,name:str,user:str,bute:str,createur:str):
        self.vous = vous
        self.genre = genre
        self.name = name
        self.user = user 
        self.bute = bute
        self.createur = createur
    
    def getVous(self):
        return self.vous
    
    def getGenre(self):
        return self.genre 
        
    def getName(self):
        return self.name 
        
    def getUser(self):
        return self.user 
    
    def getBute(self):
        return self.bute 
    
    def getCreateur(self):
        return self.createur 
        
    def getDiscution(self):
        return self.nbDiscution
    
    def setHistory(self,text,requette):
        self.oldRequette = requette
        self.oldSortie = text
        
    def getOldrequette(self):
        return self.oldRequette
    
    def getOldSortie(self):
        return self.oldSortie

        