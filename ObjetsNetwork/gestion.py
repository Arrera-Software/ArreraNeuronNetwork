import datetime
from librairy.travailJSON import *
from librairy.dectectionOS import*

class gestionNetwork:
    def __init__(self,fileUser:jsonWork,ConfigFile:jsonWork,detecteurOS:OS,fileFete:jsonWork):
        self.fileUser = fileUser
        self.ConfigFile = ConfigFile
        self.fichierVille = fileFete
        self.vous = False
        self.lieuDomicile = False
        self.lieuTravail = False
        self.genre =""
        self.name  =""
        self.user =""
        self.bute =""
        self.listFonction = []
        self.createur =""
        self.nbDiscution =0
        self.nbVilleMeteo = 0
        self.listVille = []
        self.detecteurOS = detecteurOS
        self.moteurRechercheDefault = ""
    
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
      
    def setLieu(self):
        if self.ConfigFile.lectureJSON("lieuDomicile") == "1":
            self.lieuDomicile = True
        else :
            self.lieuDomicile = False
        if self.ConfigFile.lectureJSON("lieuTravail") == "1":
            self.lieuTravail = True
        else :
            self.lieuTravail = False
        
    def addDiscution(self):
        self.nbDiscution =+ 1
    
    
    def setAll(self):
        if self.ConfigFile.lectureJSON("utilisationVous") == "1":
            self.vous = True
        else :
            self.vous = False
        if self.ConfigFile.lectureJSON("lieuDomicile") == "1":
            self.lieuDomicile = True
        else :
            self.lieuDomicile = False
        if self.ConfigFile.lectureJSON("lieuTravail") == "1":
            self.lieuTravail = True
        else :
            self.lieuTravail = False
        self.genre =  self.fileUser.lectureJSON("genre")
        self.name =  str(self.ConfigFile.lectureJSON("name")).lower()
        self.user =  str(self.fileUser.lectureJSON("user"))
        self.bute =   self.ConfigFile.lectureJSON("bute")
        self.createur =   str(self.ConfigFile.lectureJSON("createur"))
        self.listFonction = self.ConfigFile.lectureJSON("listFonction")
        self.nbVilleMeteo = int(self.ConfigFile.lectureJSON("nombreVilleMeteo"))
        self.moteurRechercheDefault = str(self.ConfigFile.lectureJSON("moteurRechercheDefault"))
    
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

    def getEtatLieuDomicile(self):
        return self.lieuDomicile

    def getEtatLieuTravail(self):
        return self.lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.fileUser.lectureJSON(flag)
    
    def getMoteurRechercheDefault(self):
        return self.moteurRechercheDefault
    
    def getDictionnaireLogiciel(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return self.fileUser.lectureJSONDict("dictSoftWindows")
        else :
            if etatWindows == False and etatLinux == True :
                return self.fileUser.lectureJSONDict("dictSoftLinux")
    
    def getListLogiciel(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return list(self.fileUser.lectureJSONDict("dictSoftWindows").keys())
        else :
            if etatWindows == False and etatLinux == True :
                return list(self.fileUser.lectureJSONDict("dictSoftLinux").keys())
            
    def getListWeb(self):
        return list(self.fileUser.lectureJSONDict("dictSite").keys())
    
    def getDictionnaireWeb(self):
        return self.fileUser.lectureJSONDict("dictSite")

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1 
    
    def getFeteJour(self):
        date= datetime.datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.fichierVille.lectureJSONMultiFlag(mois,jours)
    
    def getEmplacementSoftwareWindows(self):
        return self.ConfigFile.lectureJSON("emplacementSoftWindows")