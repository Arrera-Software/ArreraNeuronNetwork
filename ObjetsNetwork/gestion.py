from datetime import datetime, timedelta
from librairy.travailJSON import *
from librairy.dectectionOS import*

class gestionNetwork:
    def __init__(self,fileUser:jsonWork,ConfigFile:jsonWork,detecteurOS:OS,fileFete:jsonWork):
        self.__fileUser = fileUser
        self.__configFile = ConfigFile
        self.__fichierFete = fileFete
        self.__nbDiscution =0
        self.__detecteurOS = detecteurOS
        self.__oldRequette = str
        self.__oldSorti = str
        
    def addDiscution(self):
        self.__nbDiscution =+ 1
    
    def getVous(self):
        if self.__configFile.lectureJSON("utilisationVous") == "1":
            vous = True
        else :
            vous = False
        
        return bool(vous)
    
    def getGenre(self):
        return str(self.__fileUser.lectureJSON("genre")) 
        
    def getName(self):
        return  str(self.__configFile.lectureJSON("name"))
        
    def getUser(self):
        return str(self.__fileUser.lectureJSON("user"))
    
    def getBute(self):
        return  str(self.__configFile.lectureJSON("bute"))
    
    def getCreateur(self):
        return  str(self.__configFile.lectureJSON("createur"))

    def getNbDiscution(self):
        return int(self.__nbDiscution)
    
    def getNbListFonction(self):
        return len(self.__configFile.lectureJSONList("listFonction"))
    
    def getListFonction(self):
        return self.__configFile.lectureJSONList("listFonction")
    
    def getnbVilleMeteo(self):
        return int(self.__configFile.lectureJSON("nombreVilleMeteo"))
    
    def getListVilleMeteo(self):
        
        return self.__fileUser.lectureJSONList("listVille")

    def getEtatLieuDomicile(self):
        if self.__configFile.lectureJSON("lieuDomicile") == "1":
            lieuDomicile = True
        else :
            lieuDomicile = False
        return lieuDomicile

    def getEtatLieuTravail(self):
        if self.__configFile.lectureJSON("lieuTravail") == "1":
            lieuTravail = True
        else :
            lieuTravail = False
        return lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.__fileUser.lectureJSON(flag)
    
    def getMoteurRechercheDefault(self):
        return str(self.__configFile.lectureJSON("moteurRechercheDefault"))

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
        return  self.__fileUser.lectureJSON("adresseDomicile")
    
    def getAdresseTravil(self) :
        """
        Methode pour retourner l'adresse du lieu de travail
        """
        return  self.__fileUser.lectureJSON("adresseTravail")

    def getWorkEmplacement(self):
        return self.__fileUser.lectureJSON("wordFolder")
    
    def getEmplacementDownload(self):
        return self.__fileUser.lectureJSON("videoDownloadFolder")