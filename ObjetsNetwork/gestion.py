class gestionNetwork:
    def __init__(self):
        self.vous = False
        self.genre =""
        self.name  =""
        self.user =""
        self.bute =""
        self.createur =""
        self.nbDiscution =""
        self.oldRequette =""
        self.oldSortie =""
    
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
        self.vous = bool(vous)
        self.genre =  str(genre)
        self.name =  str(name)
        self.user =  str(user) 
        self.bute =  str(bute)
        self.createur =  str(createur)
    
    def getVous(self):
        return bool(self.vous)
    
    def getGenre(self):
        print(self.genre)
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

        