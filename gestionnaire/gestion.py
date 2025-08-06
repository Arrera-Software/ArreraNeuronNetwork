from librairy.dectectionOS import*
from librairy.network import*
from librairy.travailJSON import jsonWork
from config.confNeuron import confNeuron
from datetime import datetime

class gestionnaire:
    def __init__(self,confAssistant:confNeuron):
        # Importation des gestionnaires
        from gestionnaire.gestSocket import gestSocket
        from gestionnaire.gestLangue import gestLangue
        from gestionnaire.gestNeuron import gestNeuron
        from gestionnaire.gestHistorique import gestHistorique
        from gestionnaire.gestSTR import gestSTR
        from gestionnaire.gestFNC import gestFNC
        # Librairy
        # Importation des librairies
        from librairy.arrera_voice import CArreraVoice
        # Declaration des librairies
        self.__detecteurOS = OS()
        self.__network = network()
        self.__arrVoice = CArreraVoice(self)
        # Fichier JSON
        self.__config = confAssistant
        self.__fileUser = jsonWork("JSON/configUser.json") # A faire
        self.__fichierFete = jsonWork("config/listFete.json")
        # Temporaire
        # Initialisation des tout les gestionnaires
        #self.__gestFNC

        self.__gestLang = gestLangue(self.__config.fichierLangue,
                                     self.__fileUser, [self.__config.name,
                                                       self.__config.bute,
                                                       self.__config.createur],
                                     self.__config.listFonction)
        #if self.__gestNeuron.getSocket():
        #    self.__gestSocket = gestSocket(self.__config.name)
        # else :
        #    self.__gestSocket = None
        self.__gestSocket = gestSocket(self.__config.name) # Temporaire, a faire plus tard
        self.__gestSTR = gestSTR()

        self.__fnc = gestFNC(self)

        self.__gestHist = gestHistorique(self.__fnc, self)
        self.__gestNeuron = gestNeuron(self.__fnc, self, self.__gestHist)

        # Varriable
        self.__oldRequette = ""
        self.__oldSorti = ""

    def getConfigFile(self):
        return self.__config

    def getOSObjet(self):
        return self.__detecteurOS

    def getArrVoice(self):
        """
        Methode qui retourne l'objet de la librairie de voice
        """
        return self.__arrVoice

    def getLanguageObjet(self):
        return self.__gestLang

    def getGestNeuron(self):
        return self.__gestNeuron

    def getNetworkObjet(self):
        return self.__network

    def getSocketObjet(self):
        return self.__gestSocket
        
    def getName(self):
        return  self.__config.name

    def getIcon(self):
        return self.__config.icon

    def getGestFNC(self):
        """
        Methode qui retourne l'objet gestFNC
        """
        return self.__fnc

    def getListVilleMeteo(self):
        return self.__fileUser.getFlagListJson("listVille")

    def getEtatLieuDomicile(self):
        if not self.__fileUser.getContentJsonFlag("lieuDomicile"):
            lieuDomicile = True
        else :
            lieuDomicile = False
        return lieuDomicile

    def getEtatLieuTravail(self):
        if not self.__fileUser.getContentJsonFlag("lieuTravail"):
            lieuTravail = True
        else :
            lieuTravail = False
        return lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.__fileUser.getContentJsonFlag(flag)
    
    def getMoteurRechercheDefault(self):
        return self.__config.moteurderecherche

    def getEmplacementFileAgenda(self)->str :
        return self.__fileUser.getContentJsonFlag("emplacementEvenenement")

    def getEmplacemntfileTache(self)->str:
        return self.__fileUser.getContentJsonFlag("emplacementTache")

    def getEmplacementFileHist(self)->str:
        return self.__fileUser.getContentJsonFlag("emplacementHistorique")
    
    def getDictionnaireLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        etatMac = self.__detecteurOS.osMac()
        if etatWindows == True and etatLinux == False :
            return self.__fileUser.getFlagDictJson("dictSoftWindows")
        elif etatWindows == False and etatLinux == True or etatMac == True:
            return self.__fileUser.getFlagDictJson("dictSoftLinux")
        else :
            return None

    def getListLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        etatMac = self.__detecteurOS.osMac()
        if etatWindows == True and etatLinux == False and etatMac == False:
            return list(self.__fileUser.getFlagDictJson("dictSoftWindows").keys())
        elif etatWindows == False and etatLinux == True or etatMac == True :
            return list(self.__fileUser.getFlagDictJson("dictSoftLinux").keys())
        else :
            return None

    def getListWeb(self):
        return list(self.__fileUser.getFlagDictJson("dictSite").keys())
    
    def getDictionnaireWeb(self):
        return self.__fileUser.getFlagDictJson("dictSite")

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1 
    
    def getFeteJour(self):
        date= datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.__fichierFete.getContentJsonMultiFlag(mois, jours)
    
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
        return self.__config.lienDoc
    
    def getTokenGithub(self):
        """
        Methode qui permet de recuperer les token github
        """
        return self.__fileUser.getContentJsonFlag("tokenGithub")

    def getAdresseDomicile(self):
        """
        Methode pour retourner l'adresse du domicile
        """
        return  self.__fileUser.getContentJsonFlag("adresseDomicile")
    
    def getAdresseTravil(self) :
        """
        Methode pour retourner l'adresse du lieu de travail
        """
        return  self.__fileUser.getContentJsonFlag("adresseTravail")

    def getWorkEmplacement(self):
        return self.__fileUser.getContentJsonFlag("wordFolder")
    
    def getEmplacementDownload(self):
        return self.__fileUser.getContentJsonFlag("videoDownloadFolder")

    def netoyageChaine(self,chaine:str):
        """
        Methode qui permet de netoyer une chaine de caractere
        """
        return self.__gestSTR.netoyage(carractere=chaine)

    def emplacementTaskFile(self):
        """
        Methode qui retourne l'emplacement du fichier de tache
        """
        return self.__fileUser.getContentJsonFlag("emplacementTache")