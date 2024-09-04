from datetime import datetime, timedelta
from librairy.travailJSON import *
from librairy.dectectionOS import*

class gestionNetwork:
    def __init__(self,fileUser:jsonWork,ConfigFile:jsonWork,detecteurOS:OS,fileFete:jsonWork):
        self.__fileUser = fileUser
        self.__configFile = ConfigFile
        self.__fichierFete = fileFete
        self.__vous = False
        self.__lieuDomicile = False
        self.__lieuTravail = False
        self.__genre =""
        self.__name  =""
        self.__user =""
        self.__bute =""
        self.__listFonction = []
        self.__createur =""
        self.__adresseDomicile = ""
        self.__adresseTravail = ""
        self.__nbDiscution =0
        self.__nbVilleMeteo = 0
        self.__listVille = []
        self.__detecteurOS = detecteurOS
        self.__moteurRechercheDefault = ""
        self.__workEmplacement = ""
        self.__downloadEmplacment = ""
        self.__oldRequette = str
        self.__oldSorti = str
        
    def addDiscution(self):
        self.__nbDiscution =+ 1
    
    def setAll(self):
        if self.__configFile.lectureJSON("utilisationVous") == "1":
            self.__vous = True
        else :
            self.__vous = False
        if self.__configFile.lectureJSON("lieuDomicile") == "1":
            self.__lieuDomicile = True
        else :
            self.__lieuDomicile = False
        if self.__configFile.lectureJSON("lieuTravail") == "1":
            self.__lieuTravail = True
        else :
            self.__lieuTravail = False
        self.__genre =  self.__fileUser.lectureJSON("genre")
        self.__name =  str(self.__configFile.lectureJSON("name")).lower()
        self.__user =  str(self.__fileUser.lectureJSON("user"))
        self.__bute =   self.__configFile.lectureJSON("bute")
        self.__createur =   str(self.__configFile.lectureJSON("createur"))
        self.__listFonction = self.__configFile.lectureJSONList("listFonction")
        self.__nbVilleMeteo = int(self.__configFile.lectureJSON("nombreVilleMeteo"))
        self.__moteurRechercheDefault = str(self.__configFile.lectureJSON("moteurRechercheDefault"))
        self.__listVille = self.__fileUser.lectureJSONList("listVille")
        self.__adresseDomicile = self.__fileUser.lectureJSON("adresseDomicile")
        self.__adresseTravail = self.__fileUser.lectureJSON("adresseTravail")
        self.__workEmplacement = self.__fileUser.lectureJSON("wordFolder")
        self.__downloadEmplacment = self.__fileUser.lectureJSON("videoDownloadFolder")
    
    def getVous(self):
        return bool(self.__vous)
    
    def getGenre(self):
        return str(self.__genre) 
        
    def getName(self):
        return  str(self.__name )
        
    def getUser(self):
        return  str(self.__user )
    
    def getBute(self):
        return  str(self.__bute )
    
    def getCreateur(self):
        return  str(self.__createur )
        
    def getDiscution(self):
        return  str(self.__nbDiscution)

    def getNbDiscution(self):
        return int(self.__nbDiscution)
    
    def getNbListFonction(self):
        return len(self.__listFonction)
    
    def getListFonction(self):
        return self.__listFonction
    
    def getnbVilleMeteo(self):
        return self.__nbVilleMeteo
    
    def getListVilleMeteo(self):
        return self.__listVille

    def getEtatLieuDomicile(self):
        return self.__lieuDomicile

    def getEtatLieuTravail(self):
        return self.__lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.__fileUser.lectureJSON(flag)
    
    def getMoteurRechercheDefault(self):
        return self.__moteurRechercheDefault

    def getEmplacementFileAgenda(self)->str :
        return self.__fileUser.lectureJSON("emplacementEvenenement")

    def getEmplacemntfileTache(self)->str:
        return self.__fileUser.lectureJSON("emplacementTache")
    
    def getDictionnaireLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return self.__fileUser.lectureJSONDict("dictSoftWindows")
        else :
            if etatWindows == False and etatLinux == True :
                return self.__fileUser.lectureJSONDict("dictSoftLinux")
    
    def getListLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return list(self.__fileUser.lectureJSONDict("dictSoftWindows").keys())
        else :
            if etatWindows == False and etatLinux == True :
                return list(self.__fileUser.lectureJSONDict("dictSoftLinux").keys())
            
    def getListWeb(self):
        return list(self.__fileUser.lectureJSONDict("dictSite").keys())
    
    def getDictionnaireWeb(self):
        return self.__fileUser.lectureJSONDict("dictSite")

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1 
    
    def getFeteJour(self):
        date= datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.__fichierFete.lectureJSONMultiFlag(mois,jours)
    
    def getEmplacementSoftwareWindows(self):
        return self.__configFile.lectureJSON("emplacementSoftWindows")
    
    def setOld(self,output:str,input:str):
        """
        Methode qui peremt de sauvegarder oldSortie et oldRequette
        """
        self.__oldRequette = input 
        self.__oldSorti = output 
    
    def getOld(self):
        """
        Methode qui retourne une liste qui se presente comme sa [oldRequette,self.__oldSorti]
        """
        return [self.__oldRequette,self.__oldSorti]

    def getLinkDoc(self):
        """
        Methode pour donner le lien de la doc 
        """
        return self.__configFile.lectureJSON("lienDoc")
    
    def getTokenGithub(self):
        """
        Methode qui permet de recuperer les token github
        """
        return self.__fileUser.lectureJSON("tokenGithub")

    def getAdresseDomicile(self):
        """
        Methode pour retourner l'adresse du domicile
        """
        return  self.__adresseDomicile 
    
    def getAdresseTravil(self) :
        """
        Methode pour retourner l'adresse du lieu de travail
        """
        return  self.__adresseTravail 

    def getWorkEmplacement(self):
        return self.__workEmplacement
    
    def getEmplacementDownload(self):
        return self.__downloadEmplacment