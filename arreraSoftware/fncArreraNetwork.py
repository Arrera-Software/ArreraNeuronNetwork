#module pyhon
from tkinter import*
import random
#librairy Arrera
from librairy.travailJSON import *
from librairy.openSoftware import*
#objet de fonctionement du reseau
from ObjetsNetwork.gestion import*
from ObjetsNetwork.network import*
#differente fonctionnalitée
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *
from arreraSoftware.fonctionGPS import*
from arreraSoftware.fonctionTraduction import*
from arreraSoftware.fonctionArreraDownload import *
from arreraSoftware.fonctionCalculatrice import * 
from arreraSoftware.fonctionRecherche import *
from arreraSoftware.fonctionDate import *
from arreraSoftware.fonctionHorloge import*
from arreraSoftware.fonctionCalendar import *

class fncArreraNetwork:
    def __init__(self,fichierConfigurationNeuron:jsonWork,gestionNeuron:gestionNetwork,decteurOS:OS,network:network):
        #Recuperation des objet
        self.configNeuron = fichierConfigurationNeuron
        self.gestionNeuron = gestionNeuron
        self.detecteurOS = decteurOS
        self.objetNetwork =  network
        self.icon = self.configNeuron.lectureJSON("iconAssistant")
        #Recuperation varriable
        self.color = self.configNeuron.lectureJSON("interfaceColor")
        self.textColor = self.configNeuron.lectureJSON("interfaceTextColor")
        self.etatVous = self.gestionNeuron.getVous()
        self.name = self.gestionNeuron.getName()
        self.user = self.gestionNeuron.getUser()
        self.genre = self.gestionNeuron.getGenre()
        #Recuperation etat de la connextion internet
        etatConnextion = self.objetNetwork.getEtatInternet()
        #initialisation objet 
        self.fncReading = fncLecture(self.configNeuron,self.detecteurOS)
        self.actu = Actu("3b43e18afcf945888748071d177b8513","6","fr","fr")
        self.gps = GPS("19bfbee6112be5b3d9a64d4ccec72602",etatConnextion)
        self.meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        self.itineraires = GPSItineraires()
        self.traducteur = fncArreraTrad(self.configNeuron)
        self.downloader = fncArreraVideoDownload(self.configNeuron)
        self.calculatrice = fncCalculatrice(self.configNeuron)  
        self.objetRecherche = fncArreraSearch(etatConnextion)
        self.objetDate = fncDate()
        self.objetHorloge = fncArreraHorloge()
        self.objetCalendar = fncArreraCalendar(self.configNeuron,self.gestionNeuron)
        self.objetHorloge.setAtributJSON(self.configNeuron)    
        
    def reading(self):
        self.fncReading.fenetreLecture()
        if self.etatVous == True :
            text = "Voila "+self.genre+" J'éspére que sa vous sera utile"
        else :
            text = "Voila "+self.user+".Je suis toujour la si tu as besoin de moi."
        return text

    def sortieActualités(self):
        listActu = self.actu.Actu()
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        if self.etatVous == True :
            text = "Les actualites du jour sont "+listActu[nbrand1]+" , "+listActu[nbrand2] + " et "+listActu[nbrand3]+"."
        else :
            text = "Les news du jour sont "+listActu[nbrand1]+" , "+listActu[nbrand2] + " et "+listActu[nbrand3]+"."
        return str(text)
    
    def sortieMeteo(self,ville):
        if ville == "" :
            sortieGPS = self.gps.recuperationCordonneePossition()
            if sortieGPS == True :
                sortieGPS = self.gps.recuperationNameVillePosition()
                if sortieGPS == True :
                    nameVille = self.gps.getNameVille()
                    lon = self.gps.getlonPossition()
                    lat = self.gps.getlatPossition()
                    sortiMeteo = self.meteo.recuperationDataMeteo(lat,lon)
                    if sortiMeteo == True :
                        if self.etatVous == True :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C",
                                            "La meteo a votre localisation est "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C"]
                            text =  listReponse[nbrand]
                        else :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C",
                                            "La meteo a ta localisation est de "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C"]
                        
                            text =  listReponse[nbrand]
                    else :
                        if self.etatVous == True :
                            text = "Je suis désoler "+self.genre+" "+self.user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.user+" je n'arrive pas a savoir la meteo."  
                else :
                        if self.etatVous == True :
                            text = "Je suis désoler "+self.genre+" "+self.user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.user+" je n'arrive pas a savoir la meteo."
            else :
                        if self.etatVous == True :
                            text = "Je suis désoler "+self.genre+" "+self.user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.user+" je n'arrive pas a savoir la meteo."
        else :
            sortieGPS = self.gps.recuperationCordonneeVille(ville)
            if sortieGPS == True :
                lat = self.gps.getlatVille()
                lon = self.gps.getLonVille()
                sortiMeteo = self.meteo.recuperationDataMeteo(lat,lon)
                if  sortiMeteo == True:
                    nameVille =  ville
                    if self.etatVous == True :
                        text= "La meteo a "+nameVille+" est "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C"             
                    else :
                        text = "La meteo a "+nameVille+" est "+self.meteo.getdescription()+" avec une température de "+self.meteo.gettemperature()+" °C"            
                else :
                        if self.etatVous == True :
                            text = "Je suis désoler "+self.genre+" "+self.user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.user+" je n'arrive pas a savoir la meteo."  
            else :
                if self.etatVous == True :
                    text = "Je suis désoler "+self.genre+" "+self.user+". Mais je ne parvien pas a recuperer la meteo"
                else :
                    text = "Je suis désoler "+self.user+" je n'arrive pas a savoir la meteo."  
        return text   
    
    def sortieTemperature(self):
        sortieGPS = self.gps.recuperationCordonneePossition()
        if sortieGPS == True :
            lat = self.gps.getlatPossition()
            lon = self.gps.getlonPossition()
            sortieMeteo = self.meteo.recuperationDataMeteo(lat,lon)
            if sortieMeteo == True :
                if self.etatVous == True :
                    text = "La temperature actuel dehors et de "+self.meteo.gettemperature()+"°C"
                else :
                    text = "If fais "+self.meteo.gettemperature()+"°C"     
        return text
    
    def sortieGPS(self):
        sortieGPS = self.gps.recuperationCordonneePossition()
        if sortieGPS == True :
            sortieGPS = self.gps.recuperationNameVillePosition()
            if sortieGPS == True :
                lat = self.gps.getlatPossition()
                lon = self.gps.getlonPossition()
                nameVille = self.gps.getNameVille()
                if self.etatVous == True :
                    text = "Votre localisation est latitude "+lat+" longitude "+lon+" Ce qui correspond a la ville de "+nameVille+"."
                else :
                    text = "Tu es localiser a la latitude "+lat+" longitude "+lon+" .Ce qui correspond a la ville de "+nameVille+" ."
        return text
    
    def sortieItineraires(self,loc1:str,loc2:str):
        if loc1 == "loc" :
            sortieGPS = self.gps.recuperationCordonneePossition()
            if sortieGPS == True :
                self.gps.recuperationNameVillePosition()
                loc = self.gps.getNameVille()
                sortieGPS = self.itineraires.ouvertureItineraires(loc,loc2)
        else :
            sortieGPS = self.itineraires.ouvertureItineraires(loc1,loc2)
        return sortieGPS
    
    def ResumerActualite(self):
        #Recuperation nom des villes
        domicile = self.gestionNeuron.getValeurfichierUtilisateur("lieuDomicile")
        travail = self.gestionNeuron.getValeurfichierUtilisateur("lieuTravail")
        #Recuperation coordonne GPS
        sortieGPS = self.gps.recuperationCordonneeVille(domicile)
        if sortieGPS == True :
            sortieMeteo = self.meteo.recuperationDataMeteo(self.gps.getlatVille(),self.gps.getLonVille())
            if sortieMeteo == True:
                tempDomicile = self.meteo.gettemperature()
                descripDomicile = self.meteo.getdescription()
                sortieGPS = self.gps.recuperationCordonneeVille(travail)
                if sortieGPS == True :
                    sortieMeteo = self.meteo.recuperationDataMeteo(self.gps.getlatVille(),self.gps.getLonVille())
                    if sortieMeteo == True:
                        tempTravail = self.meteo.gettemperature() 
                        descripTravail = self.meteo.getdescription()
                        if self.etatVous == True :
                            text = "Le meteo a votre domicile est "+descripDomicile+" avec une temperature "+tempDomicile+" °C .Celle a de votre lieu de travail est "+descripTravail+" avec une temperature de "+tempTravail+" °C ."
                        else :
                            text =  "Le meteo a ton domicile est "+descripDomicile+" avec une temperature "+tempDomicile+" °C .Celle de ton lieu de travail est "+descripTravail+" avec une temperature de "+tempTravail+" °C ."
                    else :
                        if self.etatVous == True :
                            return  "Desoler "+self.genre+" mais il a un probleme"
                        else :
                            return  "Desoler "+self.user+" mais il a un probleme"
                else :
                    if self.etatVous == True :
                        return  "Desoler "+self.genre+" mais il a un probleme"
                    else :
                        return  "Desoler "+self.user+" mais il a un probleme"
            else :
                if self.etatVous == True :
                    return  "Desoler "+self.genre+" mais il a un probleme"
                else :
                    return  "Desoler "+self.user+" mais il a un probleme"
        else :
            if self.etatVous == True :
                return  "Desoler "+self.genre+" mais il a un probleme"
            else :
                return "Desoler "+self.user+" mais il a un probleme"
        feteJour = self.gestionNeuron.getFeteJour()
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        listeActu = self.actu.Actu()
        text2 = text+" Les actualites son "+listeActu[nbrand1]+"."+listeActu[nbrand2]+"."+listeActu[nbrand3]
        text3 = text2+".Et aujourd'hui on fete les "+feteJour
        return text3
    
    def sortieTraducteur(self,langInt:str,langOut:int):
        self.traducteur.fenetreTrad(langInt,langOut)
        
    
    def sortieDownload(self,mode):
        self.downloader.fenetreDownload(mode)
        if self.etatVous == True:
            if mode == "music" :
                text = "J'espère que la musique que vous avez téléchargée vous rendra heureux "+self.genre+" ."
            else :
                text = "J'espère que la vidéo que vous avez téléchargée vous rendra heureux "+self.genre+" ."
        else :
            if mode == "music" :
                text =  "J'espère que la musique que vous avez téléchargée vous fera plaisir "+self.user+"."
            else :
                text =  "J'espère que la vidéo que vous avez téléchargée vous fera plaisir "+self.user+"."
        
        return text
    
    def sortieCalculatrice(self,mode):
        if mode == "0":
            if self.etatVous == True :
                text = "Voila votre calculatrice "+self.genre
            else :
                text = "Voici la calculatrice"
        else :
            if mode == "1":
                if self.etatVous == True :
                    text = "Voila votre calculatrice en mode nombre complex "+self.genre
                else :
                    text = "Voici la calculatrice en mode complexe" 
            else :
                if self.etatVous == True :
                    text = "Voila votre calculatrice en mode pythagore "+self.genre
                else :
                    text = "Voici la calculatrice en mode pythagore" 
        self.calculatrice.calculatrice(mode)
        return text
    
    def sortieOpenSoftware(self,soft):
        dictionnaireSoft = self.gestionNeuron.getDictionnaireLogiciel()
        objet = OpenSoftware(self.gestionNeuron,dictionnaireSoft[soft])
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
                text = "Ok je vous ouvre "+soft+" "+self.genre
            else :
                text = "Voici "+soft
        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir "+soft
            else :
                text = "Il un probleme qui m'empeche d'ouvrir "+soft
        return text
    
    def sortieOpenTraitementTexte(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("wordWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("wordLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de traitement de texte "+self.genre+" "+self.user,
                               "Je vous ai ouvert votre logiciel de traitement de texte. En quoi puis-je vous aider de plus "+self.genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de traitement de texte " +self.user,
                                "Je t'ai ouvert ton logiciel de traitement de texte. En quoi puis-je t'aider de plus " + self.user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel traitement de texte"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel traitement de texte"
        return text
    
    def sortieOpenTableur(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("exelWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("exelLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de tableur "+self.genre+" "+self.user,
                               "Je vous ai ouvert votre logiciel de tableur. En quoi puis-je vous aider de plus "+self.genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de tableur " +self.user,
                                "Je t'ai ouvert ton logiciel de tableur. En quoi puis-je t'aider de plus " + self.user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel tableur"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel tableur"
        return text
    
    def sortieOpenDiapo(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("diapoWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("diapoLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de diaporama "+self.genre+" "+self.user,
                               "Je vous ai ouvert votre logiciel de présentation. En quoi puis-je vous aider de plus "+self.genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de présentation " +self.user,
                                "Je t'ai ouvert ton logiciel de diaporama. En quoi puis-je t'aider de plus " + self.user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel de présentation"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel de présentation"
        return text
    
    def sortieOpenBrowser(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("browserWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("browserLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
                nbrand = random.randint(0,5)
                listReponse = ["Voici votre navigateur web "+self.genre+" "+self.user,
                               "Ok je vous ouvre votre explorateur web "+self.genre+" "+self.user,
                               "Voila votre explorateur web "+self.genre,
                               "Voici votre navigateur internet "+self.genre+" "+self.user,
                               "Ok je vous ouvre votre explorateur internet "+self.genre+" "+self.user,
                               "Voila votre explorateur internet "+self.genre,]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,5)
                listReponse = ["Voici ton navigateur web "+self.genre+" "+self.user,
                               "Ok je t'ouvre ton explorateur web "+self.genre+" "+self.user,
                               "Voila ton explorateur web "+self.genre,
                               "Voici ton navigateur internet "+self.genre+" "+self.user,
                               "Ok je t'ouvre ton explorateur internet "+self.genre+" "+self.user,
                               "Voila ton explorateur internet "+self.genre,]
                text = listReponse[nbrand]

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre navigateur internet"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton navigateur internet"
        return text
    
    def sortieOpenNote(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("noteWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("noteLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
               text = "Voici vos notes "+self.genre
            else :
                text = "Voici tes notes "+self.user

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir vos notes"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir tes notes"
        return text
    
    def sortieOpenMusic(self):
        etatWindows = self.detecteurOS.osWindows()
        etatLinux = self.detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.gestionNeuron.getValeurfichierUtilisateur("musicWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.gestionNeuron.getValeurfichierUtilisateur("musicLinux")
        objet = OpenSoftware(self.gestionNeuron,logiciel)
        sortie = objet.open()
        if sortie == True :
            if self.etatVous == True :
               text = "Voici "+self.genre+" ,bonne écoute"
            else :
                text = "Voici "+self.user+" ,bonne écoute"

        else :
            if self.etatVous == True :
                text = "Je suis desoler "+self.genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel d'écoute musicale"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel d'écoute musicale"
        return text
    
    def sortieOpenYoutube(self):
        webbrowser.open("https://www.youtube.com/")
        if self.etatVous == True :
            text = "Ok, je vous ai ouvert YouTube."
        else :
            text = "Ok, je t'ai ouvert YouTube."
        
        return text
    
    def sortieOpenCloud(self):
        lien= self.gestionNeuron.getValeurfichierUtilisateur("lienCloud")
        webbrowser.open(lien)
        if self.etatVous == True :
            text = "Ok, je vous ai ouvert votre stokage distant."
        else :
            text = "Ok, je t'ai ouvert ton stokage distant."
        
        return text
    
    def sortieOpenSite(self,site):
        dictionnaireSoft = self.gestionNeuron.getDictionnaireWeb()
        webbrowser.open(dictionnaireSoft[site])
        if self.etatVous == True :
            text = "Ok je vous ouvre "+site+" "+self.genre
        else :
            text = "Voici "+site  
            
    def sortieRechercheSimple(self,requette:str):
        moteurDefault = self.gestionNeuron.getMoteurRechercheDefault()
        moteurUser = self.gestionNeuron.getValeurfichierUtilisateur("moteurRecherche")
        recherche = requette.replace("search","")
        recherche = recherche.replace("recherche","")
        if moteurUser == "":
            moteur = moteurDefault
        else :
            moteur = moteurUser
    
        match moteur :
            case "duckduckgo" :
                sortieRecherche = self.objetRecherche.duckduckgoSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "google" :
                sortieRecherche = self.objetRecherche.googleSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "qwant" :
                sortieRecherche = self.objetRecherche.QwantSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "ecosia" :
                sortieRecherche = self.objetRecherche.EcosiaSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "brave" :
                sortieRecherche = self.objetRecherche.braveSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "bing":
                sortieRecherche = self.objetRecherche.bingSearch(recherche)
                if self.etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case other :
                sortieRecherche = self.objetRecherche.duckduckgoSearch(recherche)
                if self.etatVous ==  True:
                    text = "Je vous ai fais votre recherche sur duckduckgo car il un probleme avec mes fichier de configuration"
                else :
                    text = "Je t'ai fais ta recherche sur duckduckgo car il un probleme avec mes fichier de configuration"
        if sortieRecherche == False :
            if self.etatVous ==  True:
                return "Je suis désoler "+self.genre+" . Mais je peux pas faire votre recherche si je ne suis pas connecter a internet"
            else :
                return "Désoler "+self.user+" je suis pas connecter a internet"
        else :
            return text
    
    def sortieGrandRecherche(self,requette:str):
        recherche = requette.replace("bigsearch","")
        recherche = recherche.replace("grand recherche","")
        sortieRecheche = self.objetRecherche.GrandRecherche(recherche)
        if sortieRecheche == True :
            if self.etatVous == True :
                text = "Voici le resultat de votre recherche sur plusieur moteur de recherche "+self.genre
            else :
                text = "Voici ton resultat " 
        else :
            if self.etatVous == True :
                text = "Votre appareil n'est pas connecter internet "+self.genre
            else :
                text = "Je suis desoler mais je suis pas connecter a internet"
                
        return text
    
    def sortieHeure(self):
        self.objetDate.rafraichisement()
        heure = self.objetDate.heure()
        minute = self.objetDate.minute()
        return "Il est "+heure+" heure "+minute + "  minute" 
    
    def sortieDate(self):
        self.objetDate.rafraichisement()
        jour = self.objetDate.jour()
        mois = self.objetDate.mois()
        annes = self.objetDate.annes()
        return "On est le "+jour+" "+mois+" "+annes
    
    def sortieOpenChrono(self):
        if self.etatVous == True :
            text = "Tres bien je vous lance le chronométre "+self.genre
        else :
            text = "Okay je te lance le chronométre"
        self.objetHorloge.modeChrono()
        return text

    def sortieOpenHorloge(self):
        if self.etatVous == True :
            text = "Tres bien je vous lance l'horloge "+self.genre
        else :
            text = "Okay je te lance l'horloge"
        self.objetHorloge.modeHorloge()
        return text
    
    def sortieOpenSimpleMinuteur(self):
        if self.etatVous == True :
            text = "Tres bien je vous lance l'application minuteur "+self.genre
        else :
            text = "Okay je te lance l'application minuteur"
        self.objetHorloge.modeMinuteur()
        return text   
    
    def sortieAjoutEvent(self):
        self.objetCalendar.addEvenemnt()
        return "Ok"    
    
    def sortieSupprEvent(self):
        self.objetCalendar.supprEvenement()
        return "Ok"    
    
    def sortieEvenementDay(self):
        nb , listEvent = self.objetCalendar.checkEvenement()  
        if nb == 0 :
            if self.etatVous == True :
                return "Vous avez aucun évenement aujourd'hui"
            else :
                return "Tu as rien de prévu aujourd'hui"  
        else :
            if self.etatVous == True :
                text = "Vous avez "+str(nb)+" prévu évenement aujourd'hui "
            else :
                text = "Tu as "+str(nb)+" prévu évenement aujourd'hui "
            if nb > 1 :
                text = text + "qui sont "
            else :
                text = text + "qui est "
            for i in range(0,nb) :
                if i == nb-1:
                    text = text + listEvent[i] + "."  
                else :
                    if i == nb-2 :
                        text = text + listEvent[i] + " et "
                    else :
                        text = text + listEvent[i] + "," 
                
            
            return text