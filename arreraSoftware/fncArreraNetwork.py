#module pyhon
import random
import re
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
from arreraSoftware.fonctionTache import*
from arreraSoftware.fonctionCodeHelp import*
from arreraSoftware.fonctionArreraWork import*
from arreraSoftware.fonctionRadio import*
from arreraSoftware.fonctionArreraPenseBete import*
from arreraSoftware.fncOrthographe import*

class fncArreraNetwork:
    def __init__(self,fichierConfigurationNeuron:jsonWork,gestionNeuron:gestionNetwork,decteurOS:OS,network:network):
        #Recuperation des objet
        self.__configNeuron = fichierConfigurationNeuron
        self.__gestionNeuron = gestionNeuron
        self.__detecteurOS = decteurOS
        self.__objetNetwork =  network
        #Recuperation varriable
        self.__etatVous = self.__gestionNeuron.getVous()
        self.__user = self.__gestionNeuron.getUser()
        self.__genre = self.__gestionNeuron.getGenre()
        #Recuperation etat de la connextion internet
        etatConnextion = self.__objetNetwork.getEtatInternet()
        #initialisation objet 
        self.__fncReading = fncLecture(self.__configNeuron,self.__detecteurOS)
        self.__actu = Actu("3b43e18afcf945888748071d177b8513")
        self.__gps = GPS("19bfbee6112be5b3d9a64d4ccec72602",etatConnextion)
        self.__meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        self.__traducteur = fncArreraTrad(self.__configNeuron,)
        self.__downloader = fncArreraVideoDownload(self.__configNeuron,self.__gestionNeuron)
        self.__calculatrice = fncCalculatrice(self.__configNeuron)  
        self.__objetRecherche = fncArreraSearch(etatConnextion)
        self.__objetDate = fncDate()
        self.__objetHorloge = fncArreraHorloge()
        self.__objetCalendar = fncArreraAgenda(self.__configNeuron,self.__gestionNeuron)
        self.__objetTache = fncArreraTache(self.__objetDate,self.__configNeuron,self.__gestionNeuron.getEmplacemntfileTache())
        self.__objetCodehelp = fncCodehelp(self.__configNeuron,self.__detecteurOS,self.__gestionNeuron)
        self.__objetArreraWork = fncArreraWork(self.__objetDate,self.__gestionNeuron,self.__configNeuron,self.__detecteurOS)
        self.__objetHorloge.setAtributJSON(self.__configNeuron)    
        self.__objetOpenSoft = OpenSoftware(self.__gestionNeuron)
        self.__objRadio = fncRadio(self.__objetNetwork)
        self.__objPenseBete = fncArreraPostite(self.__configNeuron)
        self.__objOrthographe = fncOrthagraphe(self.__configNeuron.lectureJSON("interfaceColor"),
                                               self.__configNeuron.lectureJSON("interfaceTextColor"))
        
    def reading(self):
        self.__fncReading.fenetreLecture()
        if self.__etatVous == True :
            text = "Voila "+self.__genre+" J'éspére que sa vous sera utile"
        else :
            text = "Voila "+self.__user+".Je suis toujour la si tu as besoin de moi."
        return text

    def sortieActualités(self):
        sortie = self.__actu.setActu("6","fr")
        if (sortie == True):
            listActu = self.__actu.getActu()
            if ((listActu[0]=="error") and (listActu[1] == "error")):
                return 6 , ["Désoler une erreur c'est produite pour la récupération des actulités",""]
            else :
                nbrand1 = random.randint(0,1)
                nbrand2 = random.randint(2,3)
                nbrand3 = random.randint(4,5)
                return 3, [listActu[nbrand1],listActu[nbrand2],listActu[nbrand3]]
        else :
            return 6 , ["Désoler une erreur c'est produite pour la récupération des actulités",""]
        
    
    def sortieMeteoTowmoroMorning(self,ville):
        if ville == "" :
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True :
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True :
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDateMetoTowmorowMorning(lat,lon)
                    if sortiMeteo == True :
                        if self.__etatVous == True :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" pour demain matin est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a votre localisation pour demain matin est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                            text =  listReponse[nbrand]
                        else :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" pour demain matin est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a ta localisation pour demain matin est de "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                        
                            text =  listReponse[nbrand]
                    else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain matin"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain matin."  
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain matin."
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain matin."
            else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain matin"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain matin."
        else :
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True :
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDateMetoTowmorowMorning(lat,lon)
                if  sortiMeteo == True:
                    nameVille =  ville
                    if self.__etatVous == True :
                        text= "La meteo a "+nameVille+"  pour demain matin est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"             
                    else :
                        text = "La meteo a "+nameVille+" pour demain matin est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"            
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain matin."
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain matin."  
            else :
                if self.__etatVous == True :
                    text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain matin."
                else :
                    text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain matin."  
        
        return 4 , [text,""]
    
    def sortieMeteoTowmorNoon(self,ville):
        if ville == "" :
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True :
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True :
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDateMetoTowmorowNoon(lat,lon)
                    if sortiMeteo == True :
                        if self.__etatVous == True :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" pour demain midi est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a votre localisation pour demain midi est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                            text =  listReponse[nbrand]
                        else :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" pour demain midi est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a ta localisation pour demain midi est de "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                        
                            text =  listReponse[nbrand]
                    else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain midi"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain midi."  
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain midi."
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain midi."
            else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain midi"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain midi."
        else :
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True :
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDateMetoTowmorowNoon(lat,lon)
                if  sortiMeteo == True:
                    nameVille =  ville
                    if self.__etatVous == True :
                        text= "La meteo a "+nameVille+"  pour demain midi est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"             
                    else :
                        text = "La meteo a "+nameVille+" pour demain midi est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"            
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain midi."
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain midi."  
            else :
                if self.__etatVous == True :
                    text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo pour demain midi."
                else :
                    text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo pour demain midi."  
        
        return 4 , [text,""]
    
    def sortieMeteoToday(self,ville):
        if ville == "" :
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True :
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True :
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDataMeteoNow(lat,lon)
                    if sortiMeteo == True :
                        if self.__etatVous == True :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a votre localisation est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                            text =  listReponse[nbrand]
                        else :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a ta localisation est de "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                        
                            text =  listReponse[nbrand]
                    else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."
            else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."
        else :
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True :
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDataMeteoNow(lat,lon)
                if  sortiMeteo == True:
                    nameVille =  ville
                    if self.__etatVous == True :
                        text= "La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"             
                    else :
                        text = "La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"            
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
            else :
                if self.__etatVous == True :
                    text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                else :
                    text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
        
        return 4 , [text,""]
    
    def sortieTemperature(self):
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True :
            lat = self.__gps.getlatPossition()
            lon = self.__gps.getlonPossition()
            sortieMeteo = self.__meteo.getDataMeteoNow(lat,lon)
            if sortieMeteo == True :
                if self.__etatVous == True :
                    text = ["La temperature actuel dehors et de "+self.__meteo.gettemperature()+"°C",""]
                else :
                    text = ["Il fais "+self.__meteo.gettemperature()+"°C",""]     
        return 4 , text
    
    def sortieGPS(self):
        text = []
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True :
            sortieGPS = self.__gps.recuperationNameVillePosition()
            if sortieGPS == True :
                lat = self.__gps.getlatPossition()
                lon = self.__gps.getlonPossition()
                nameVille = self.__gps.getNameVille()
                if self.__etatVous == True :
                    text = ["Votre localisation est latitude "+lat+" longitude "+lon+" Ce qui correspond a la ville de "+nameVille+".",""]
                else :
                    text = ["Tu es localiser a la latitude "+lat+" longitude "+lon+" .Ce qui correspond a la ville de "+nameVille+" .",""]
        return 4,text
    
    def sortieItineraire(self,phrase):
        """
        Extrait les adresses de départ et d'arrivée d'une phrase donnée.
        
        Parameters:
        phrase (str): La phrase contenant les adresses de départ et d'arrivée.
        
        Returns:
        tuple: Une paire (départ, arrivée) des adresses extraites.

        Phrase a utiliser :
            indique-moi l'itineraire de [depart] a [arrive] sur le GPS, s'il te plait.

            lance le GPS pour un trajet de [depart] a [arrive], s'il te plaît.
        Mots qui peuvent compter comme ville : 
            domicile,residence,maison,appartement,chez moi,foyer,maison,foyer,demeure
            bureau,lieu de travail,entreprise,societe,boulot,cabinet",college,lycee,ecole,campus,universite
            la ou je suis , ma localisation
        """
        reusite = bool
        # Expressions régulières pour extraire les parties de la phrase
        pattern = re.compile(r"de\s+(.*?)\s+(?:a|comme|et)\s+(.*?)\s+(?:comme|et|s'il|destination|aller|sur|,|\.|$)", re.IGNORECASE)
        match = pattern.search(phrase)
        
        if match:
            depart = match.group(1).strip()
            arrivee = match.group(2).strip()
            reusite = True
        else:
            reusite = False
        if (reusite == True ) :
            if ((depart == "domicile") or (depart =="residence") 
                or (depart =="maison") or (depart == "appartement") 
                or (depart =="chez moi") or (depart =="foyer") 
                or (depart =="maison") or (depart == "foyer") 
                or (depart =="demeure")):
                depart = self.__gestionNeuron.getAdresseDomicile()
            else : 
                if ((depart =="bureau")or (depart =="lieu de travail")
                    or (depart =="entreprise")or (depart =="societe")
                    or (depart =="boulot") or (depart == "cabinet")
                    or (depart =="college")or (depart =="lycee")
                    or (depart =="ecole") or (depart =="campus")
                    or (depart =="universite")):
                    depart = self.__gestionNeuron.getAdresseTravil()
                else :
                    if ((depart =="la ou je suis")or (depart =="ma localisation")) :
                        if (self.__gps.recuperationNameVillePosition()!= False) :
                            if (self.__etatVous == True) :
                                return "Une erreur c'est produite qui m'empeche de vous faire cette itineraire"
                            else :
                                return "Une erreur c'est produite qui m'empeche de te faire cette itineraire"
                        else :
                            depart = self.__gps.getNameVille()
            
            if ((arrivee == "domicile") or (arrivee =="residence") 
                or (arrivee =="maison") or (arrivee == "appartement") 
                or (arrivee =="chez moi") or (arrivee =="foyer") 
                or (arrivee =="maison") or (arrivee == "foyer") 
                or (arrivee =="demeure")):
                arrivee = self.__gestionNeuron.getAdresseDomicile()
            else : 
                if ((arrivee =="bureau")or (arrivee =="lieu de travail")
                    or (arrivee =="entreprise")or (arrivee =="societe")
                    or (arrivee =="boulot") or (arrivee == "cabinet")
                    or (arrivee =="college")or (arrivee =="lycee")
                    or (arrivee =="ecole") or (arrivee =="campus")
                    or (arrivee =="universite")):
                    arrivee = self.__gestionNeuron.getAdresseTravil()
                else :
                    if ((arrivee =="la ou je suis")or (arrivee =="ma localisation")) :
                        if (self.__gps.recuperationNameVillePosition()!= False) :
                            if (self.__etatVous == True) :
                                return "Une erreur c'est produite qui m'empéche de vous faire cette itineraire"
                            else :
                                return "Une erreur c'est produite qui m'empéche de te faire cette itineraire"
                        else :
                            arrivee = self.__gps.getNameVille()
            

            sortieGMap = self.__gps.launchGoogleMapItineraire(depart,arrivee)
            if (sortieGMap == True) :
                if (self.__etatVous==True) :
                    return "Voici votre itineraire sur google map. J'espére que sa vous sera utile "+self.__genre+" "+self.__user
                else :
                    return "Je t'ai fais ton itinaire sur google map"
            else :
                if (self.__etatVous==True) :
                    return "Désolé "+self.__genre+" "+self.__user+". Il a un probleme qui m'empéche de faire l'itineraires."
                else :
                    return "Désolé il a un souci qui m'empéche de te donne cette route"
        else :
            if (self.__etatVous==True):
                return "Désoler "+self.__genre+" mais je n'arrive pas a savoir ou vous aller et ou vous allez partir"
            else :
                return "Désoler "+self.__user+" mais je n'arrive pas a savoir ou tu veux te rendre et de ou tu part"     
            

                    
            
    
    def sortieResumerActualite(self):
        """

        Returns:
            meteoHome,meteoWork,feteJour,Actu 1,Actu 2,Actu 3,textSpeak
        """
        #var 
        verif = False
        meteoHome = ""
        meteoWork =  ""
        feteJour = ""
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        listOut = []

        if (self.__etatVous == True):
            textSpeak = "Voici un tour d'horizon des nouvelles du jour et des prévisions météorologiques."
        else : 
            textSpeak = "Voici un résumé des dernières actualités et de la météo pour aujourd'hui."

        # Partie Meteo 

        domicile = self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile")
        travail = self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail")

        # Meteo a domicile
        if (domicile != ""):
            verif = self.__gps.recuperationCordonneeVille(domicile)
            if (verif == True) :
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatVille(),self.__gps.getLonVille())
                if (verif == True) :
                    if self.__etatVous == True :
                        textSpeak = textSpeak + "La météo a votre domicile est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+"°C. "
                    else :
                        textSpeak = textSpeak + "La météo chez toi est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+"°C. "
                    
                    meteoHome = "Meteo lieu de residence :\nDescription : "+self.__meteo.getdescription()+"\nTemperature : "+self.__meteo.gettemperature()+"°C"
                else :
                   meteoHome = "error" 
            else :
                meteoHome = "error"
        else :
            meteoHome = "error"
        
        # Meteo sur le lieu de travail
        if (travail != "") :
            verif = self.__gps.recuperationCordonneeVille(travail)
            if (verif==True) :
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatVille(),self.__gps.getLonVille())
                if (verif == True) :
                    if self.__etatVous == True :
                        textSpeak = textSpeak +"La météo a votre lieu de travail est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+"°C. "
                    else :
                        textSpeak = textSpeak +"La météo a ton boulot est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+"°C. "
                    
                    meteoWork = "Meteo lieu de travail :\nDescription : "+self.__meteo.getdescription()+"\nTemperature : "+self.__meteo.gettemperature()+"°C"
                else :
                    meteoWork = "error" 
            else :
                meteoWork = "error" 
        else :
            meteoWork = "error" 

        # Meteo sur la position que si la meteo au lieu de travail et au domicile a echouer
        if (meteoHome == "error" and meteoWork == "error") :
            verif = self.__gps.recuperationCordonneePossition()
            if (verif == True):
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatPossition(),self.__gps.getlonPossition())
                if (verif == True) :
                    if self.__etatVous == True :
                        textSpeak = textSpeak + "La meteo a votre localisation est "+self.__meteo.getdescription+" avec une temperature de "+self.__meteo.gettemperature()+"°C. "
                    else :
                        textSpeak = textSpeak + "La meteo a ta localisation est "+self.__meteo.getdescription+" avec une temperature de "+self.__meteo.gettemperature()+"°C. "
                
                    meteoWork = "Meteo a votre position :\nDescription : "+self.__meteo.getdescription()
                    +"\nTemperature : "+self.__meteo.gettemperature()+"°C"
                else :
                    meteoWork = "error" 
            else :
                meteoWork = "error"  
                
        #fete du jour
        feteJour = self.__gestionNeuron.getFeteJour()
        textSpeak = textSpeak + "La fête du jour est "+feteJour+". "

        #Liste des actu
        verif = self.__actu.setActu("6","fr","fr")
        if (verif == True) :
            listeActu = self.__actu.getActu()
            textSpeak = textSpeak + "Et enfin les actualités sont "+listeActu[nbrand1]+", "+listeActu[nbrand2]+" et "+listeActu[nbrand3]
            #Construction de la liste
            listOut = [meteoHome,meteoWork,feteJour,listeActu[nbrand1],listeActu[nbrand2],listeActu[nbrand3],textSpeak]
            return 12 , listOut
        else :
            return 11 , ["error","error"]

    def sortieTraducteur(self,langInt:str,langOut:int):
        self.__traducteur.fenetreTrad(langInt,langOut)
    
    def sortieCalculatrice(self,mode):
        if mode == "0":
            if self.__etatVous == True :
                text = "Voila votre calculatrice "+self.__genre
            else :
                text = "Voici la calculatrice"
        else :
            if mode == "1":
                if self.__etatVous == True :
                    text = "Voila votre calculatrice en mode nombre complex "+self.__genre
                else :
                    text = "Voici la calculatrice en mode complexe" 
            else :
                if self.__etatVous == True :
                    text = "Voila votre calculatrice en mode pythagore "+self.__genre
                else :
                    text = "Voici la calculatrice en mode pythagore" 
        self.__calculatrice.calculatrice(mode)
        return text
    
    def sortieOpenSoftware(self,soft):
        dictionnaireSoft = self.__gestionNeuron.getDictionnaireLogiciel()
        sortie = self.__objetOpenSoft.setName(dictionnaireSoft[soft])
        if sortie == True :
            if self.__etatVous == True :
                text = "Ok je vous ouvre "+soft+" "+self.__genre
            else :
                text = "Voici "+soft
            self.__objetOpenSoft.open()
        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir "+soft
            else :
                text = "Il un probleme qui m'empeche d'ouvrir "+soft
        return text
    
    
    def sortieOpenDiapo(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("diapoWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("diapoLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de diaporama "+self.__genre+" "+self.__user,
                               "Je vous ai ouvert votre logiciel de présentation. En quoi puis-je vous aider de plus "+self.__genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de présentation " +self.__user,
                                "Je t'ai ouvert ton logiciel de diaporama. En quoi puis-je t'aider de plus " + self.__user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel de présentation"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel de présentation"
        return text
    
    def sortieOpenBrowser(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("browserWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("browserLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,5)
                listReponse = ["Voici votre navigateur web "+self.__genre+" "+self.__user,
                               "Ok je vous ouvre votre explorateur web "+self.__genre+" "+self.__user,
                               "Voila votre explorateur web "+self.__genre,
                               "Voici votre navigateur internet "+self.__genre+" "+self.__user,
                               "Ok je vous ouvre votre explorateur internet "+self.__genre+" "+self.__user,
                               "Voila votre explorateur internet "+self.__genre,]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,5)
                listReponse = ["Voici ton navigateur web "+self.__genre+" "+self.__user,
                               "Ok je t'ouvre ton explorateur web "+self.__genre+" "+self.__user,
                               "Voila ton explorateur web "+self.__genre,
                               "Voici ton navigateur internet "+self.__genre+" "+self.__user,
                               "Ok je t'ouvre ton explorateur internet "+self.__genre+" "+self.__user,
                               "Voila ton explorateur internet "+self.__genre,]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre navigateur internet"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton navigateur internet"
        return text
    
    def sortieOpenNote(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("noteWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("noteLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
               text = "Voici vos notes "+self.__genre
            else :
                text = "Voici tes notes "+self.__user

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir vos notes"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir tes notes"
        return text
    
    def sortieOpenMusic(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("musicWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("musicLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
               text = "Voici "+self.__genre+" ,bonne écoute"
            else :
                text = "Voici "+self.__user+" ,bonne écoute"

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel d'écoute musicale"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel d'écoute musicale"
        return text
    
    def sortieOpenYoutube(self):
        webbrowser.open("https://www.youtube.com/")
        if self.__etatVous == True :
            text = "Ok, je vous ai ouvert YouTube."
        else :
            text = "Ok, je t'ai ouvert YouTube."
        
        return text
    
    def sortieOpenCloud(self):
        lien= self.__gestionNeuron.getValeurfichierUtilisateur("lienCloud")
        webbrowser.open(lien)
        if self.__etatVous == True :
            text = "Ok, je vous ai ouvert votre stokage distant."
        else :
            text = "Ok, je t'ai ouvert ton stokage distant."
        
        return text
    
    def sortieOpenSite(self,site):
        dictionnaireSoft = self.__gestionNeuron.getDictionnaireWeb()
        webbrowser.open(dictionnaireSoft[site])
        if self.__etatVous == True :
            text = "Ok je vous ouvre "+site+" "+self.__genre
        else :
            text = "Voici "+site  
            
    def sortieRechercheSimple(self,requette:str):
        moteurDefault = self.__gestionNeuron.getMoteurRechercheDefault()
        moteurUser = self.__gestionNeuron.getValeurfichierUtilisateur("moteurRecherche")
        recherche = requette.replace("search","")
        recherche = recherche.replace("recherche","")
        if moteurUser == "":
            moteur = moteurDefault
        else :
            moteur = moteurUser
    
        match moteur :
            case "duckduckgo" :
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
            case "google" :
                sortieRecherche = self.__objetRecherche.googleSearch(recherche)
            case "qwant" :
                sortieRecherche = self.__objetRecherche.qwantSearch(recherche)
            case "ecosia" :
                sortieRecherche = self.__objetRecherche.ecosiaSearch(recherche)
            case "brave" :
                sortieRecherche = self.__objetRecherche.braveSearch(recherche)
            case "bing":
                sortieRecherche = self.__objetRecherche.bingSearch(recherche)
            case "perplexity":
                sortieRecherche = self.__objetRecherche.perplexitySearch(recherche)
            case other :
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
        if sortieRecherche == False :
            if self.__etatVous ==  True:
                return "Je suis désoler "+self.__genre+" . Mais je peux pas faire votre recherche si je ne suis pas connecter a internet"
            else :
                return "Désoler "+self.__user+" je suis pas connecter a internet"
        else :
            if self.__etatVous ==  True:
                text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
            else :
                text = "Voici ta recherche "
       
        return text,recherche
    
    def sortieGrandRecherche(self,requette:str):
        recherche = requette.replace("bigsearch","")
        recherche = recherche.replace("grand recherche","")
        sortieRecheche = self.__objetRecherche.bigRecherche(recherche)
        if sortieRecheche == True :
            if self.__etatVous == True :
                text = "Voici le resultat de votre recherche sur plusieur moteur de recherche "+self.__genre
            else :
                text = "Voici ton resultat " 
        else :
            if self.__etatVous == True :
                text = "Votre appareil n'est pas connecter internet "+self.__genre
            else :
                text = "Je suis desoler mais je suis pas connecter a internet"
                
        return text,recherche
    
    def sortieHeure(self):
        self.__objetDate.rafraichisement()
        heure = self.__objetDate.heure()
        minute = self.__objetDate.minute()
        return "Il est "+heure+" heure "+minute + "  minute" 
    
    def sortieDate(self):
        self.__objetDate.rafraichisement()
        jour = self.__objetDate.jour()
        mois = self.__objetDate.mois()
        annes = self.__objetDate.annes()
        return "On est le "+jour+" "+mois+" "+annes
    
    def sortieOpenChrono(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance le chronométre "+self.__genre
        else :
            text = "Okay je te lance le chronométre"
        self.__objetHorloge.modeChrono()
        return text

    def sortieOpenHorloge(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance l'horloge "+self.__genre
        else :
            text = "Okay je te lance l'horloge"
        self.__objetHorloge.modeHorloge()
        return text
    
    def sortieOpenSimpleMinuteur(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance l'application minuteur "+self.__genre
        else :
            text = "Okay je te lance l'application minuteur"
        self.__objetHorloge.modeMinuteur()
        return text   
    
    def sortieAjoutEvent(self):
        self.__objetCalendar.activeAddWindows()
        if (self.__etatVous==True):
            text = "Ok, je vous ouvre la fenetre de l'agenda pour ajouter un événement"
        else :
            text = "Ok, je t'ouvre la fenetre de l'agenda pour ajouter un événement"
        return text  
    
    def sortieSupprEvent(self):
        self.__objetCalendar.activeSupprWindows()
        if (self.__etatVous==True):
            text = "Ok, je vous ouvre la fenetre de l'agenda pour supprimer un événement"
        else :
            text = "Ok, je t'ouvre la fenetre de l'agenda pour supprimer un événement"
        return text   
    
    def sortieEvenementDay(self):
        nbEvent= self.__objetCalendar.getNbEventToday()
        if (nbEvent==0):
            if (self.__etatVous==True):
                text = "Vous n'avez pas d'événement enregister pour aujourd'hui"
            else :
                text = "Tu as rien de prévu aujourd'hui"
        else :
            listEvent = self.__objetCalendar.getEventToday()
            if(nbEvent==1):
                if (self.__etatVous==True):
                    text = "Vous avez qu'un seul événement pour aujourd'hui qui est "+listEvent[0]
                else :
                    text = "Tu as qu'un seul événement aujourd'hui qui est "+listEvent[0]
            else :
                if (self.__etatVous==True):
                    baseTexte = "Vous avez "+str(nbEvent)+" pour aujourd'hui qui sont "
                else :
                    baseTexte = "Tu as "+str(nbEvent)+" pour aujourd'hui qui sont "
                for i in range(0,nbEvent):
                    if (i==0):
                        text = baseTexte+listEvent[i]
                    else :
                        if (i==(nbEvent-1)):
                            text = text+" et "+listEvent[i]
                        else :
                            text = text +", "+listEvent[i]
            
        return text
    
    def sortieOpenAgenda(self):
        if (self.__etatVous==True):
            text = "Je vous ai ouvert l'agenda. J'espére que sa vous sera utile."
        else :
            text = "Okay, je t'ouvre l'application agenda."
        
        self.__objetCalendar.activeAgenda()
        return text
    
    def sortieListLogiciel(self,nb:int,listSoft:list):
        if (nb==0):
            if (self.__etatVous == True) :
                return "Vous n'avez pas de logiciel enregisté. Ouvrez les paramétres pour en enregistrer un."
            else :
                return "Tu n'as pas de logiciel enregisté. Ouvre les paramétres pour en enregister un"
        else :
            if (nb == 1) :
                if (self.__etatVous == True) :
                    return "Vous avez qu'un seul logiciel enregisté. Qui est "+listSoft[0]
                else :
                    return "Tu as un seul logiciel enregisté. Qui est "+listSoft[0]
            else :
                if (self.__etatVous == True) :
                    baseTexte = "Vous avez "+str(nb)+" de logiciels enregistré. Qui sont"
                else :
                    baseTexte = "Tu as "+str(nb)+" de logiciels enregistré. Qui sont"
                
                for i in range(0,nb):
                    if (i == 0):
                        texte = baseTexte+" "+listSoft[i]
                    else :
                        if (i == (nb-1)):
                            texte = texte + " et "+ listSoft[i]
                        else :
                            texte = texte +", "+ listSoft[i]
                
                return texte 

    def sortieListSite(self,nb:int,listSite:list):
        if (nb==0):
            if (self.__etatVous == True) :
                return "Vous n'avez pas de site internet enregisté dans l'assistant. Ouvrez les paramétres pour en enregistrer un."
            else :
                return "Tu n'as pas de site internet enregisté dans l'assistant. Ouvre les paramétres pour en enregister un"
        else :
            if (nb == 1) :
                if (self.__etatVous == True) :
                    return "Vous avez qu'un seul site internet enregisté. Qui est "+listSite[0]
                else :
                    return "Tu as un seul site internet enregisté. Qui est "+listSite[0]
            else :
                if (self.__etatVous == True) :
                    baseTexte = "Vous avez "+str(nb)+" de site internet enregistré. Qui sont"
                else :
                    baseTexte = "Tu as "+str(nb)+" de site internet enregistré. Qui sont"
                
                for i in range(0,nb):
                    if (i == 0):
                        texte = baseTexte+" "+listSite[i]
                    else :
                        if (i == (nb-1)):
                            texte = texte + " et "+ listSite[i]
                        else :
                            texte = texte +", "+ listSite[i]
                
                return texte
    
    def sortieViewTache(self):
        if (self.__etatVous==True) :
            text = "Trés bien je vous ouvre l'application tache "+self.__genre 
        else :
            text = "Okay je t'ouvre l'application tache "+self.__user
        
        self.__objetTache.activeViewTask()
        return text
    
    def sortieViewTacheAdd(self):
        if (self.__etatVous==True) :
            text = "Je vous ouvre le programme d'ajout de tache. Suivez bien l'interface "+self.__genre 
        else :
            text = "Okay je t'ouvre l'application pour ajouter une nouvelle tache "+self.__user
        
        self.__objetTache.activeViewAdd()
        return text
    
    def sortieViewTacheSuppr(self):
        sortie = self.__objetTache.activeViewSuppr()
        if (sortie==True):
            if (self.__etatVous==True) :
                text = "Je vous ouvre le programme de suppression de tache. Suivez bien l'interface "+self.__genre 
            else :
                text = "Okay je t'ouvre l'application pour supprimer une nouvelle tache "+self.__user
        else :
            if (self.__etatVous==True) :
                text = "Désoler "+self.__genre+". Il est imposible de supprimer un tache si il en a aucun de crée " 
            else :
                text = "Désoler "+self.__user+". Il est imposible de supprimer un tache si il en a aucun de crée " 
        
        return text
    
    def sortieViewTacheCheck(self):
        sortie = self.__objetTache.activeViewCheck()
        if (sortie==True):
            if (self.__etatVous==True) :
                text = "Je vous ouvre le programme qui vous permet de définir un tache fini" 
            else :
                text = "Okay je t'ouvre l'application pour finir une tache "
        else :
            if (self.__etatVous==True) :
                text = "Désoler "+self.__genre+". Il est imposible de finir un tache si il en a aucun de crée " 
            else :
                text = "Désoler "+self.__user+". Il est imposible de finir un tache si il en a aucun de crée "
        
        return text

    def sortieNbSpeakTache(self):
        nbTache = self.__objetTache.getNbTache()
        nbToday = self.__objetTache.getNbTacheToday()
        if (nbTache==0) :
            if (self.__etatVous==True):
                text = "Vous avez aucune tache enregister"
            else :
                text = "Tu as aucune tache enregistrer"
        else :
            if (nbTache == 1) :
                if (nbToday == 1) :
                    if (self.__etatVous==True):
                        text = "Vous avez une tache enregistrer et elle est à finir aujourd'hui"
                    else :
                        text = "Tu as une seul tache . Et tu dois l'avoir fini ce soir."
                else :
                    if (self.__etatVous==True):
                        text = "Vous avez une tache enregistrer."
                    else :
                        text = "Tu as une seul tache. "
            else :
                if (self.__etatVous==True):
                    baseText = "Vous avec "+str(nbTache)+" enregistrer."
                else :
                    baseText = "Tu as "+str(nbTache)+" enregistrer."
                if (nbTache==1) :
                    if (self.__etatVous==True):
                        text = baseText+" Dont une tache a finir aujourd'hui."
                    else :
                        text = baseText+" Avec une tache que tu dois finir aujourd'hui."
                else :
                    if (nbTache>1):
                        if (self.__etatVous==True):
                            text = baseText+" Dont "+str(nbToday)+" tache a finir aujourd'hui."
                        else :
                            text = baseText+" Avec "+str(nbToday)+" tache que tu dois finir aujourd'hui."
                    else :
                        if (self.__etatVous==True):
                            text = baseText + " Et aucune tache aujourd'hui."
                        else :
                            text = baseText + " Et aucune tache aujourd'hui."

        return text
    
    def sortieSpeakTacheToday(self):
        listTache = self.__objetTache.getTacheToday()
        nbTache = len(listTache)
        if (nbTache==0) :
            if (self.__etatVous==True):
                text = "Vous avez aucune tache aujourd'hui "+self.__genre+"."
            else :
                text = "Tu as aucune tache a faire aujourd'hui"
        else :
            if (nbTache==1):
                if (self.__etatVous==True):
                    baseText = "Vous avez une seul tache à faire aujourd'hui qui est "
                else :
                    baseText = "Tu as uns seul tache à finir pour aujourd'hui qui est "
            else :
                if (self.__etatVous==True):
                    baseText = "Vous avez "+str(nbTache)+" tache à faire aujourd'hui qui sont "
                else :
                    baseText = "Tu as "+str(nbTache)+" à finir pour aujourd'hui qui sont "
            
            for i in range(0,nbTache):
                if (i == 0):
                    text = baseText + listTache[i]
                else :
                    if ( i == (nbTache-1)):
                        text = text + " et " + listTache[i]
                    else :
                        text = text+", "+listTache[i]
        
        return text
    
    def sortieSpeakTacheTowmorow(self):
        listTache = self.__objetTache.getTacheTowmorow()
        nbTache = len(listTache)
        if (nbTache==0) :
            if (self.__etatVous==True):
                text = "Vous avez aucune tache pour demain "+self.__genre+"."
            else :
                text = "Tu as aucune tache a faire demain"
        else :
            if (nbTache==1):
                if (self.__etatVous==True):
                    baseText = "Vous avez une seul tache à faire pour demain qui est "
                else :
                    baseText = "Tu as uns seul tache à finir pour demain qui est "
            else :
                if (self.__etatVous==True):
                    baseText = "Vous avez "+str(nbTache)+" tache à faire pour demain qui sont "
                else :
                    baseText = "Tu as "+str(nbTache)+" à finir pour demain qui sont "
            
            for i in range(0,nbTache):
                if (i == 0):
                    text = baseText + listTache[i]
                else :
                    if ( i == (nbTache-1)):
                        text = text + " et " + listTache[i]
                    else :
                        text = text+", "+listTache[i]
        
        return text
    
    def sortieOpenOrgaVar(self):
        if (self.__etatVous==True):
            text = "Ok je vous ouvre l'organisateur de varriable "+self.__genre+"."
        else :
            text = "Okay je t'ouvre l'organisateur de varriable j'espére que sa t'aidera sur ton projet de programation."
        
        self.__objetCodehelp.activeOrgaVar()
        
        return text
    
    def sortieSearchDoc(self,requette:str):
        """
        Flag recherche : 
            - recherche devdoc / rdevdoc / sdevdoc : Recherche dans sur devdoc 
            - recherche microsoft / rmicrosoft / smicrosoft : recherche microsoft learn
            - recheche python / rpython / spython : recherche sur le site python.org
        """
        if (("recherche devdoc" in requette) or ("rdevdoc" in requette) or ("sdevdoc" in requette)):
            recherche = requette.replace("recherche devdoc","")
            recherche = recherche.replace("rdevdoc","")
            recherche = recherche.replace("sdevdoc","")
            self.__objetCodehelp.rechercheDoc(1,recherche)
            if (self.__etatVous==True):
                text = "Tres bien je vous fais la recherche sur le site DevDoc."
            else :
                text = "Okay je t'ai ouvert la recherche sur le site DevDoc dans ton navigateur."
            r = "devdoc "+recherche
        else :
            if (("recherche microsoft" in requette) or ("rmicrosoft" in requette) or ("smicrosoft" in requette)):
                recherche = requette.replace("recherche microsoft","")
                recherche = recherche.replace("rmicrosoft","")
                recherche = recherche.replace("smicrosoft","")
                self.__objetCodehelp.rechercheDoc(2,recherche)
                if (self.__etatVous==True):
                    text = "Tres bien je vous fais la recherche sur la documentation Learn de microsoft."
                else :
                    text = "Okay je t'ai ouvert la recherche dans la documentation Learn de microsoft dans ton navigateur."
                r = "microsoft "+recherche
            else :
                if (("recheche python" in requette) or ("rpython" in requette) or ("spython" in requette)):
                    recherche = requette.replace("recheche python","")
                    recherche = recherche.replace("rpython","")
                    recherche = recherche.replace("spython","")
                    self.__objetCodehelp.rechercheDoc(3,recherche)
                    if (self.__etatVous==True):
                        text = "Tres bien je vous fais la recherche sur le site du language de programation python."
                    else :
                        text = "Okay je t'ai ouvert la recherche dans le site du language de programation python dans ton navigateur."
                    r = "python "+recherche
        
        return text,r
    
    def sortieOpenColorSelecteur(self):
        if (self.__etatVous == True):
            text = "Ok je vous ouvre la fonctionnalité codehelp Color Selecteur."
        else :
            text = "Okay voici ton color sélecteur"
        
        self.__objetCodehelp.activeColorSelecteur()

        return text

    def sortieSearchGithub(self,requette:str):
        """
        Flag de recherche : 
            recherche github 
            rgithub
            sgithub
            search github
        """
        if (self.__etatVous==True):
            text = "Ok je vous fais la recherche sur github "+self.__genre+"."
        else :
            text = "Okay voici ta recherche github."

        recherche = requette.replace("recherche github","")
        recherche = recherche.replace("rgithub","")
        recherche = recherche.replace("sgithub","")
        recherche = recherche.replace("search github","")

        self.__objetCodehelp.searchGithub(recherche)

        return text,recherche
    
    def sortieOpenSiteGithub(self):
        if (self.__etatVous == True):
            text = "Voici le site github "+self.__genre+" j'espére que sa vous sera utile."
        else :
            text = "Voila le site github"

        self.__objetCodehelp.openSiteGithub()
        return text 
    
    def sortieOpenGuiGithub(self):
        if (self.__etatVous==True):
            text = "Voci mon outil de gestion github "+self.__genre+" "+self.__user+"."
        else :
            text = "Voila le logiciel de gestion github"
        
        self.__objetCodehelp.openGestionGithub()

        return text

    def sortieOpenLibrairy(self):
        if (self.__etatVous==True):
            text = "Je vous es ouvert le l'interface qui vous permet d'acceder au librairy Codehelp"
        else :
            text = "Je t'ai ouvert la librairy github"
        
        self.__objetCodehelp.openOutilLibrairy()

        return text

    # Partie Arrera Work 
    def getWordOpen(self):
        return self.__objetArreraWork.getEtatWord()
    
    def getTableurOpen(self):
        return self.__objetArreraWork.getEtatTableur()
    
    def getFileTableur(self):
        return self.__objetArreraWork.getNameFileTableur()
    
    def getFileWord(self):
        return self.__objetArreraWork.getNameFileWord()
    
    def sortieOpenTableur(self):
        sortie = self.__objetArreraWork.openTableur()
        if (sortie == True) :
            if (self.__etatVous == True) :
                text = "Votre fichier Exel a bien etais ouvert correctement "+self.__genre+". Il nous reste plus qu'a travailler dessus."
            else :
                text = "Je t'ai bien ouvert ton fichier exel. Aller travaillons dessus."
        else :
            if (self.__etatVous == True) :
                text = "Désoler "+self.__genre+" mais il met imposible de t'ouvrir un fichier exel"
            else :
                text = "Un probléme est survenu j'arrive pas a t'ouvrir ton fichier Exel."
        
        return text
    
    def sortieOpenWord(self):
        sortie = self.__objetArreraWork.openWord()
        if (sortie == True) :
            if (self.__etatVous == True) :
                text = "Votre fichier de traitement de texte a bien etais ouvert correctement "+self.__genre+". Il nous reste plus qu'a ecrire dessus."
            else :
                text = "Je t'ai bien ouvert ton fichier Word. Aller travaillons dessus."
        else :
            if (self.__etatVous == True) :
                text = "Désoler "+self.__genre+" mais il met imposible de t'ouvrir un fichier Word"
            else :
                text = "Un probléme est survenu j'arrive pas a t'ouvrir ton fichier Word."
        
        return text
    
    def sortieCloseTableur(self):
        sortie = self.__objetArreraWork.closeTableur()
        if (sortie == True) :
            if (self.__etatVous == True):
                text = "Je vous es bien fermé votre fichier Exel."
            else :
                text ="Je t'ai fermée ton Exel."
        else:
            if (self.__etatVous == True):
                text = "Il imposible de femer un fichier Exel. Si vous en avez pas ouvert un."
            else :
                text ="Il n'a pas de fichier exel ouvert. Il en a aucun ouvert."
        
        return text
    
    def sortieCloseDocx(self):
        sortie = self.__objetArreraWork.closeDocx()
        if (sortie == True) :
            if (self.__etatVous == True):
                text = "Je vous es bien fermé votre fichier word."
            else :
                text ="Je t'ai fermée ton word."
        else:
            if (self.__etatVous == True):
                text = "Il imposible de femer un fichier word. Si vous en avez pas ouvert un."
            else :
                text ="Il n'a pas de fichier word ouvert. Il en a aucun ouvert."
        
        return text
    
    def sortieWriteDocx(self,texte:str):
        if (texte != ""):
            ligne = texte.replace("ecrit dans le word","")
            ligne = ligne.replace("ecrit" ,"")
            
            sortie = self.__objetArreraWork.writeDocxFile(ligne)
            
            if (sortie == True):
                if (self.__etatVous == True):
                    text = "Je vous es bien écrit ce que vous voulez dans le fichier .docx"
                else :
                    text ="Tout c'est bien passé j'ai pu écrire ce que vous voulez dans le fichier."
            else :
                if (self.__etatVous == True):
                    text = "Il a un probleme qui m'a empeché d'écrire dans le fichier ce que vous m'avez demandé. Il peut etre pas ouvert."
                else :
                    text = "Un probleme est survenu. Tu n'a surment pas ouvert un fichier word."
        else :
            if (self.__etatVous == True):
                text = "Je ne pas ecrire dans le fichier si vous me disais pas ce que je dois ecrire."
            else :
                text ="Il es impossible pour moi d'écrire si tu me donne pas ce que je dois écrire."
        
        return text
    
    def sortieReadDocx(self):
        sortie = self.__objetArreraWork.readDocxFile()

        if (sortie == "error"):
            if (self.__etatVous == True):
                text = "Je pense que le fichier dois etre fermé je peux pas le lire "+self.__genre+". Essayez de le reouvrir"
            else :
                text ="Je ne peux pas lire le fichier . Vérifie si tu la bien ouvert "+self.__user+"."
            
        else :
            text = sortie
        
        return text
    
    def sortieFileOpen(self):
        tableur = self.getTableurOpen()
        word = self.getWordOpen()

        if ((tableur == True) and (word == True)):
            if (self.__etatVous) :
                text = "Vous avez un fichier de traitement de texte ouvert ainsi q'un tableur"
            else :
                text = "Tu as un tableur d'ouvert et un traitement de texte"
        else :
            if ((tableur == True) and (word == False)):
                if (self.__etatVous) :
                    text = "Vous avez juste ouvert un fichier tableur"
                else :
                    text = "Tu as juste un fichier tableur d'ouvert"
            else :
                if ((tableur == False) and (word == True)):
                    if (self.__etatVous) :
                        text = "Vous avez qu'un fichier de traitement de texte ouvert."
                    else :
                        text = "Tu as qu'un traitement de texte ouvert."
                else :
                    if (self.__etatVous) :
                        text = "Vous avez aucun fichier d'ouvert"
                    else :
                        text = "Tu as aucun fichier d'ouvert"
        
        return text
    
    def sortieReadTableur(self):
        return self.__objetArreraWork.readTableur()
    
    def sortieAddValeurTableur(self):
        sortie = self.__objetArreraWork.tkAddValeurParole()
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Suivez bien l'interface graphique pour ajouter une valeur au tableur."
            else :
                text = "Suis bien l'interface pour ajouter une valeur au tableur."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+" mais je ne peux pas ajouter une valeur."
            else :
                text = "Désoler il a probleme qui m'empéche d'ajouter ta valeur."

        return text
    
    def sortieSupprValeurTableur(self):
        sortie = self.__objetArreraWork.tkSuppValeurParole()
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Suivez bien l'interface graphique pour supprimer une valeur au tableur."
            else :
                text = "Suis bien l'interface pour supprimer une valeur au tableur."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+" mais je ne peux pas supprimer une valeur."
            else :
                text = "Désoler il a probleme qui m'empéche de supprimer ta valeur."

        return text
    
    def sortieAddFormuleTableur(self,mode:int):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        match mode :
            case 1 :
                sortie = self.__objetArreraWork.tkAddFormuleParole(1)
                if (sortie == True) :
                    if (self.__etatVous == True) :
                        text = "Trés bien je vous ouvre l'interface pour ajouter une somme a votre tableur."
                    else :
                        text = "Okay , je t'ouvre l'interface pour que tu ajoute une somme au tableur"
                else :
                    if (self.__etatVous == True) :
                        text = "Désoler "+self.__genre+" mais il a un probleme."
                    else :
                        text = "Désoler "+self.__user+" mais je rancontre un probléme "
            case 2 :
                sortie = self.__objetArreraWork.tkAddFormuleParole(2)
                if (sortie == True) :
                    if (self.__etatVous == True) :
                        text = "Trés bien je vous ouvre l'interface pour ajouter une moyenne a votre tableur."
                    else :
                        text = "Okay , je t'ouvre l'interface pour que tu ajoute une moyenne au tableur"
                else :
                    if (self.__etatVous == True) :
                        text = "Désoler "+self.__genre+" mais il a un probleme."
                    else :
                        text = "Désoler "+self.__user+" mais je rancontre un probléme "
            case 3 :
                sortie = self.__objetArreraWork.tkAddFormuleParole(3)
                if (sortie == True) :
                    if (self.__etatVous == True) :
                        text = "Trés bien je vous ouvre l'interface pour ajouter un comptage de valeur a votre tableur."
                    else :
                        text = "Okay , je t'ouvre l'interface pour que tu ajoute un comptage de valeur au tableur"
                else :
                    if (self.__etatVous == True) :
                        text = "Désoler "+self.__genre+" mais il a un probleme."
                    else :
                        text = "Désoler "+self.__user+" mais je rancontre un probléme "
            case 4 :
                sortie = self.__objetArreraWork.tkAddFormuleParole(4)
                if (sortie == True) :
                    if (self.__etatVous == True) :
                        text = "Trés bien je vous ouvre l'interface pour ajouter un minimun a votre tableur."
                    else :
                        text = "Okay , je t'ouvre l'interface pour que tu ajoute un minimun au tableur"
                else :
                    if (self.__etatVous == True) :
                        text = "Désoler "+self.__genre+" mais il a un probleme."
                    else :
                        text = "Désoler "+self.__user+" mais je rancontre un probléme "
            case 5 :
                sortie = self.__objetArreraWork.tkAddFormuleParole(5)
                if (sortie == True) :
                    if (self.__etatVous == True) :
                        text = "Trés bien je vous ouvre l'interface pour ajouter un maximun a votre tableur."
                    else :
                        text = "Okay , je t'ouvre l'interface pour que tu ajoute un maximun au tableur"
                else :
                    if (self.__etatVous == True) :
                        text = "Désoler "+self.__genre+" mais il a un probleme."
                    else :
                        text = "Désoler "+self.__user+" mais je rancontre un probléme "
            case other :
                if (self.__etatVous == True) :
                    text = "Désoler "+self.__genre+" mais il a un probleme."
                else :
                    text = "Désoler "+self.__user+" mais je rancontre un probléme "
        
        return text
    
    def sortieOpenSoftTableurFile(self):
        sortie = self.__objetArreraWork.openTableurOs()
        if (sortie==True):
            if (self.__etatVous == True):
                text = "Je vous es ouvert votre fichier tableur avec logiciel par défault de votre ordinateur."
            else :
                text = "Trés bien votre tableur est ouvert dans le logiciel par défault de votre ordinateur."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas ouvrir le tableur dans le logiciel par défault de votre ordinateur"
            else :
                text = "Désoler "+self.__user+". Je ne peux pas ouvrir le tableur dans le logiciel par défault de votre ordinateur"
        return text
    
    def sortieOpenSoftWorkFile(self):
        sortie = self.__objetArreraWork.openWordOs()
        if (sortie==True):
            if (self.__etatVous == True):
                text = "Je vous es ouvert votre fichier word avec logiciel par défault de votre ordinateur."
            else :
                text = "Trés bien votre word est ouvert dans le logiciel par défault de votre ordinateur."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas ouvrir le word dans le logiciel par défault de votre ordinateur"
            else :
                text = "Désoler "+self.__user+". Je ne peux pas ouvrir le word dans le logiciel par défault de votre ordinateur"
        return text
    
    def sortieOpenTableurGUI(self):
        sortie = self.__objetArreraWork.guiTableurWork()
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous es ouvert mon interface pour travailler sur un tableur"
            else :
                text = "Je t'ai bien ouvert le tableur avec mon interface"
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Il est impossible pour moi de vous ouvrir le tableur avec mon interface"
            else :
                text = "Désoler "+self.__user+". Il est impossible pour moi de t'ouvrir le tableur avec mon interface"
        return text
    
    def sortieOpenWordGUI(self):
        sortie = self.__objetArreraWork.guiWordWork()
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous es ouvert mon interface pour travailler sur votre fichier de traitement de texte"
            else :
                text = "Je t'ai bien ouvert ton traitement de texte avec mon interface de travail"
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Il est impossible pour moi de vous ouvrir le traitement de texte avec mon interface"
            else :
                text = "Désoler "+self.__user+". Il est impossible pour moi de t'ouvrir le traitement de texte avec mon interface"
        return text

    def sortieCreateFolder(self,requette:str):
        tampon = requette.replace("cree un projet nommer","")
        tampon = tampon.replace("cree un nouveau projet nommer","")
        tampon = tampon.replace("cree un projet nomme","")
        name = tampon.replace("cree un nouveau projet nomme","")
        name = name.replace(" ","")
        sortie = self.__objetArreraWork.createProject(name)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous es bien crée votre projet "+name+". Quelle est le type de projet ?"
            else :
                text  = "Ton projet nommer "+name+" a bien etais crée. Quelle est le type de projet ?"
        else :
            if (self.__etatVous == True):
                text = "Désoler mais un probleme m'empéche de crée ton projet "+name
            else :
                text  = "Désoler mais un probleme m'empéche de crée ton projet "+name
        
        return text
    
    def sortieSetTypeProjet(self,requette:str):
        type = requette.replace("le type est","")
        type = type.replace("le type du projet est","")
        sortie = self.__objetArreraWork.setTypeProject(type)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai bien mit le type sur votre projet."
            else :
                text  = "Je t'ai bien mit le type sur ton projet."
        else :
            if (self.__etatVous == True):
                text = "Désoler mais un probleme m'empéche de mettre le type sur votre projet."
            else :
                text  = "Désoler mais un probleme m'empéche de mettre le type sur ton projet."
        return text
    
    def sortieOpenProjet(self,requette:str):
        projet = requette.replace("ouvre le projet nommer","")
        projet = projet.replace("ouvre le projet nomme","")
        projet = projet.replace("ouvre le projet","")
        projet = projet.replace(" ","")
        sortie = self.__objetArreraWork.openProjet(projet)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai bien ouvert le projet "+projet+" "+self.__genre+". Que voulez vous faire ?"
            else :
                text = "Le projet "+projet+" est bien ouvert. Que veux-tu faire ?"
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+" mais je ne peux pas t'ouvrir le projet "+projet+". Il n'existe peut-étre pas"
            else :
                text = "Désoler mais je trouve pas le projet "+projet+"."
        return projet,text
    
    def sortieCloseProject(self):
        sortie = self.__objetArreraWork.closeProject()

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai bien fermer votre projet "+self.__genre+"."
            else :
                text  = "Je t'ai bien fermer ton projet"
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+" mais il semble pas avoir de projet ouvert"
            else :
                text  = "Désoler "+self.__name+" mais il semble pas avoir de projet ouvert"
        
        return text
    
    def sortieAddfile(self,type:str,name:str):
        """
        Type:
            exel 
            word
            odt
            txt
            python 
            h 
            json
            html
            css
            md
            cpp
            c
            php
            js
            java
            kt
        """
        mode = int 
        typeName = ""
        match type :
            case "exel" :
                mode  = 1
                typeName = "exel"
            case "word" :
                mode = 2
                typeName = "word"
            case "odt" :
                mode = 3
                typeName = "open document texte"
            case "txt":
                mode = 4
                typeName = "texte"
            case "python" :
                mode = 5 
                typeName = "python"
            case "h" :
                mode = 6
                typeName = "en tête c++"
            case "json":
                mode = 7
                typeName = "json"
            case "html":
                mode = 8
                typeName = "html"
            case "css":
                mode = 9 
                typeName = "css"
            case "md":
                mode = 10
                typeName = "md"
            case "cpp":
                mode = 11
                typeName = "laguage c++"
            case "c" :
                mode = 12
                typeName = "language c"
            case "php" :
                mode = 13 
                typeName = "PHP"
            case "js" :
                mode = 14 
                typeName = "JavaScript"
            case "java" :
                mode = 15
                typeName = "Java"
            case "kt" :
                mode = 16
                typeName = "Kotlin"
            
        sortie = self.__objetArreraWork.createFileProject(mode,name)

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai bien crée votre fichier "+typeName+". Voulez-vous l'ouvrir ?"
            else : 
                text = "Je t'ai bien crée ton fichier "+typeName+". Es que tu veux que je te l'ouvre ?"
        else :
            if (self.__etatVous == True):
                text = "Je pense que vous avez pas de projet d'ouvert. Car je ne peux pas crée votre fichier."
            else :
                text = "Je pense que tu n'a pas ouvert un projet. Je ne peux pas crée ton fichier."
        
        return text

    def sortieCreateFileDirect(self,requette:str):
        """
        Phrase possible : 
            cree un fichier #type#  #nom#
        """
        nom = requette.replace("cree un fichier","").replace("word","").replace("odt","").replace("txt","").replace("python","")
        nom = nom.replace("json","").replace("html","").replace("css","").replace("md","").replace("cpp","").replace("language c","")
        nom = nom.replace("exel","").replace("nommer","").replace("texte","").replace("en tete","").replace("open","").replace("tableur","")
        nom = nom.replace("language c++","").replace("php","").replace("javascript","").replace("java script","").replace("java","").replace("kotlin","")
        nom = nom.replace("kt","").replace("js","").replace("document","")
        nom = nom.replace(" ","") # Pas touche

        if ("word" in requette):
            typeFile = "word"
        else :
            if (("odt"in requette) or ("open texte document" in requette)):
                typeFile = "odt"
            else :
                if (("txt"in requette) or ("texte" in requette)):
                    typeFile = "txt"
                else :
                    if ("python"in requette):
                        typeFile = "python"
                    else :
                        if (("en tete" in requette)):
                            typeFile = "h"
                        else :
                            if ("json" in requette):
                                typeFile ="json"
                            else :
                                if ("html" in requette):
                                    typeFile = "html"
                                else :
                                    if ("css" in requette):
                                        typeFile = "css"
                                    else :
                                        if ("md" in requette):
                                            typeFile = "md"
                                        else :
                                            if (("cpp" in requette )or ("language c++" in requette)):
                                                typeFile = "cpp"
                                            else :
                                                if (("language c" in requette) ):
                                                    typeFile = "c"
                                                else :
                                                    if (("exel" in requette) or ("tableur" in requette)):
                                                        typeFile = "exel"
                                                    else :
                                                        if ("php" in requette):
                                                            typeFile = "php"
                                                        else :
                                                            if (("javascript" in requette) or ("java script" in requette) or ("js" in requette)):
                                                                typeFile = "js"
                                                            else :
                                                                if ("java" in requette):
                                                                    typeFile = "java"
                                                                else :
                                                                    if (("kotlin" in requette )or ("kt" in requette)):
                                                                        typeFile = "kt"
                                                                    else :
                                                                        typeFile = ""
        return self.sortieAddfile(typeFile,nom)
    
    def getNameProjetOpen(self):
        return self.__objetArreraWork.getNameProjet()

    def getNameLastFile(self):
        return self.__objetArreraWork.getNameLastFileCreate()
    
    def sortieopenFileCreated(self):
        sortie = self.__objetArreraWork.openLastFileCreate()
        print(sortie)
        if (sortie == 1) :
            if (self.__etatVous == True):
                text = "Je vous ai bien ouvert votre fichier avec le logiciel par default de votre ordinateur "+self.__genre+"."
            else :
                text = "Je t'ai bien ouvert ton fichier."
        else :
            if (sortie == 2):
                if (self.__etatVous == True):
                    text = "Je vous ai ouvert votre fichier de traitement texte. Que voulez-vous ecrire ?"
                else :
                    text = "Je t'ai bien ouvert ton fichier. Que veux-tu faire ?"
            else :
                if (sortie == 3):
                    if (self.__etatVous == True):
                        text = "Votre a tableur a bien été ouvert que voulez-vous ajouter."
                    else :
                        text = "Ton tableur est ouvert que veux-tu faire avec ?"
                else :
                    if (sortie == 0):
                        if (self.__etatVous == True):
                            text = "Désoler mais il semble avoir un probleme."
                        else :
                            text = "Désoler mais il semble avoir un probleme."
        
        return text    

    def sortieListFileProject(self):
        sortie = self.__objetArreraWork.setlistFileProject()

        if (sortie == True):
            liste = self.__objetArreraWork.getListFileProjet()
            finTexte = ""
            for i in range(0,len(liste)):
                if (i == 0):
                    finTexte = liste[i]
                else :
                    if (i==(len(liste)-1)):
                        finTexte = finTexte + " et " + liste[i]
                    else :
                        finTexte = finTexte+", "+liste[i]
            if (self.__etatVous == True):
                text = "Les fichier de votre projet sont "+finTexte+"."
            else :
                text = "Les fichier present dans votre projet sont "+finTexte+"."
        else :
            if (self.__etatVous == True):
                text = "Pardonner moi "+self.__genre+" mais je ne peux pas lister les fichiers de votre projet."
            else :
                text = "Pardonne moi "+self.__name+" mais je ne peux pas lister les fichiers de ton projet." 

        return text 

    def sortieOpenFileProject(self,requette:str):
        """
        Phrase  :
            ouvre le fichier du projet nommer #name#
            ouvre le fichier nommer #name#
        """
        nameFile = requette.replace("ouvre le fichier du projet nommer","")
        nameFile = nameFile.replace("ouvre le fichier nommer","")
        nameFile = nameFile.replace(" ","")

        sortie = self.__objetArreraWork.openFileOtherProjet(nameFile)

        if (sortie == 1):
            if (self.__etatVous == True):
                text = "Je vous ai bien le fichier "+nameFile+". Je reste a votre service "+self.__genre+". "
            else :
                text = "Le fichier "+nameFile+" est bien ouvert."
        else :
            if (sortie == 0):
                if (self.__etatVous == True):
                    text = "Désoler "+self.__genre+". Mais je ne peux pas ouvrir ce que vous demmander. Il a peux être pas un projet ouvert."
                else :
                    text = "Il a probleme je ne peux pas t'ouvrir ce que tu veux. Il a peux être pas un projet ouvert."
            else :
                if (sortie == 2):
                    if (self.__etatVous == True):
                        text = "Je vous ai bien ouvert ton fichier de traitement de texte "+nameFile+". Je suis prêt à travailler dessus "+self.__genre+"."
                    else :
                        text = "Ton fichier "+nameFile+" est bien ouvert. Que veux tu ecrire dessus."
                else :
                    if (sortie == 3):
                        if (self.__etatVous == True):
                            text = "Votre fichier "+nameFile+" est bien ouvert. Quelle formule voulez-vous dessus "+self.__genre+"."
                        else :
                            text = "Ton fichier exel "+nameFile+" est bien ouvert."
        
        return text,nameFile

    def sortieShowTacheProjet(self):
        sortie = self.__objetArreraWork.showTacheProjet()

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert mon interface pour voir vos taches sur le projet "+self.getNameProjetOpen()+"."
            else :
                text = "Je t'ai ouvert l'interface pour voir les taches du projet "+self.getNameProjetOpen()+"."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas montrer les tache de votre projet."
            else :
                text = "Pardonne moi "+self.__user+". Je ne peux pas te montrer tes taches."
        
        return text
    
    def sortieAddTacheProjet(self):
        sortie = self.__objetArreraWork.addTacheProjet()

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert mon interface pour ajouter une tache au projet "+self.getNameProjetOpen()+"."
            else :
                text = "Je t'ai ouvert l'interface pour que tu ajoute une tache au projet "+self.getNameProjetOpen()+"."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas ajouter une tache de votre projet."
            else :
                text = "Pardonne moi "+self.__user+". Je ne peux pas te ajouter une tache."
        
        return text
    
    def sortieSupprTacheProjet(self):
        sortie = self.__objetArreraWork.supprTacheProjet()

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert mon interface pour supprimer une tache au projet "+self.getNameProjetOpen()+"."
            else :
                text = "Je t'ai ouvert l'interface pour que tu supprime une tache au projet "+self.getNameProjetOpen()+"."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas supprimer une tache de votre projet."
            else :
                text = "Pardonne moi "+self.__user+". Je ne peux pas te supprimer une tache."
        
        return text
    
    def sortieSupprTacheProjet(self):
        sortie = self.__objetArreraWork.supprTacheProjet()

        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert mon interface pour terminer une tache au projet "+self.getNameProjetOpen()+"."
            else :
                text = "Je t'ai ouvert l'interface pour que tu termine une tache au projet "+self.getNameProjetOpen()+"."
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+". Je ne peux pas terminer une tache de votre projet."
            else :
                text = "Pardonne moi "+self.__user+". Je ne peux pas te terminer une tache."
        
        return text
    
    def sortieNbTacheProjet(self):
        sortie = self.__objetArreraWork.getNbTacheProjet()
        sortie2 = self.__objetArreraWork.getNBTacheToday()

        if ((sortie != -1) and (sortie2 != -1) and (sortie != 0)):
            if (self.__etatVous == True):
                text = "Dans le projet "+self.getNameProjetOpen()+" vous avez "+str(sortie)+" tache enregistrer dont "+str(sortie2)+" a finir aujourd'hui."
            else :
                text = "Tu as "+str(sortie)+" tache enregistrer dont "+str(sortie2)+" a finir aujourd'hui dans le projet"+self.getNameProjetOpen()
        else :
            if (sortie == 0) :
                if (self.__etatVous == True):
                    text = "Vous avez aucune tache enregistrer dans le projet "+self.getNameProjetOpen()+"."
                else :
                    text = "Tu as aucune tache dans le projet "+self.getNameProjetOpen()+"."
            else :
                if (self.__etatVous == True):
                    text = "Pardonner-moi "+self.__genre+" mais je ne pas vous donner le nombre de tache dans votre projet."
                else :
                    text = "Désoler "+self.__user+" un probleme est survenu qui m'empéche de te donner le nombre de tache dans votre projet."
        
        return text

    def sortieListeTacheTodayProjet(self):
        sortie = self.__objetArreraWork.setListTacheTodayProjet()

        if (sortie == True) :
            listTache = self.__objetArreraWork.getListTacheTodayProjet()
            nbTache = len(listTache)

            if (nbTache==0) :
                if (self.__etatVous==True):
                    text = "Vous avez aucune tache aujourd'hui pour le projet "+self.getNameProjetOpen()+"."
                else :
                    text = "Tu as aucune tache a faire aujourd'hui pour le projet "+self.getNameProjetOpen()+"."
            else :
                if (nbTache==1):
                    if (self.__etatVous==True):
                        baseText = "Vous avez une seul tache à faire aujourd'hui pour le projet "+self.getNameProjetOpen()+" qui est "
                    else :
                        baseText = "Tu as uns seul tache à finir pour aujourd'hui pour le projet "+self.getNameProjetOpen()+" qui est "
                else :
                    if (self.__etatVous==True):
                        baseText = "Vous avez "+str(nbTache)+" tache à faire aujourd'hui pour le projet "+self.getNameProjetOpen()+" qui sont "
                    else :
                        baseText = "Tu as "+str(nbTache)+" à finir pour aujourd'hui pour le projet "+self.getNameProjetOpen()+" qui sont "
                
                for i in range(0,nbTache):
                    if (i == 0):
                        text = baseText + listTache[i]
                    else :
                        if ( i == (nbTache-1)):
                            text = text + " et " + listTache[i]
                        else :
                            text = text+", "+listTache[i]
        else :
            if (self.__etatVous==True) :
                text = "Excuser moi "+self.__genre+" mais je peux pas vous donner les taches d'aujourd'hui pour le projet."
            else :
                text = "Pardonne moi mais je peux pas te donner les taches d'aujourd'hui pour le projet"
        
        return text
    
    def sortieListTacheTowmorowProjet(self):
        sortie = self.__objetArreraWork.setListTacheTowmorowProjet()

        if (sortie == True) :
            listTache = self.__objetArreraWork.getListTacheTowmorowProjet()
            nbTache = len(listTache)

            if (nbTache==0) :
                if (self.__etatVous==True):
                    text = "Vous avez aucune tache a faire pour demain pour le projet "+self.getNameProjetOpen()+"."
                else :
                    text = "Tu as aucune tache a faire pour demain pour le projet "+self.getNameProjetOpen()+"."
            else :
                if (nbTache==1):
                    if (self.__etatVous==True):
                        baseText = "Vous avez une seul tache a faire pour demain pour le projet "+self.getNameProjetOpen()+" qui est "
                    else :
                        baseText = "Tu as uns seul tache à finir pour demain pour le projet "+self.getNameProjetOpen()+" qui est "
                else :
                    if (self.__etatVous==True):
                        baseText = "Vous avez "+str(nbTache)+" tache à faire pour demain le projet "+self.getNameProjetOpen()+" qui sont "
                    else :
                        baseText = "Tu as "+str(nbTache)+" à finir pour demain le projet "+self.getNameProjetOpen()+" qui sont "
                
                for i in range(0,nbTache):
                    if (i == 0):
                        text = baseText + listTache[i]
                    else :
                        if ( i == (nbTache-1)):
                            text = text + " et " + listTache[i]
                        else :
                            text = text+", "+listTache[i]
        else :
            if (self.__etatVous==True) :
                text = "Excuser moi "+self.__genre+" mais je peux pas vous donner les taches pour demain pour le projet."
            else :
                text = "Pardonne moi mais je peux pas te donner les taches pour demain pour le projet."
        
        return text
    
    def sortieResumerTacheAgenda(self):
        """
        Return  : tache,agenda
        
        """
        # Recuperation des liste
        listEvent = self.__objetCalendar.getEventToday()
        listTache = self.__objetTache.getTacheToday()
        # Recuperation du nombre de tache et event
        nbEvent = self.__objetCalendar.getNbEventToday()
        nbTache = len(listTache)
        
        if (self.__etatVous == True):
            if (nbTache == 0):
                tacheTXT = "Vous avez aucune tache pour aujourd'hui" 
            else :
                if (nbTache == 1):
                    tacheTXT = "Vous avez "+str(nbTache)+" tache qui est "+listTache[0]+"."
                else :
                    tacheTXT = "Vous avez "+str(nbTache)+" taches qui sont "
                    for i in range(0,nbTache):
                        if (i == 0):
                            tacheTXT = tacheTXT+listTache[i]
                        else :
                            if (i == (nbTache-1)):
                                tacheTXT = tacheTXT+" et "+listTache[i]    
                            else :
                                tacheTXT = tacheTXT+", "+listTache[i]      
            if (nbEvent == 0):
                eventTXT = "Vous avez aucun événement aujourd'hui" 
            else :
                if (nbEvent == 1):
                    eventTXT = "Vous avez "+str(nbEvent)+" evénement aujourd'hui qui est "+listEvent[0]+"."
                else :
                    eventTXT = "Vous avez "+str(nbEvent)+" evénement aujourd'hui qui sont "
                    for i in range(0,nbEvent):
                        if (i == 0):
                            eventTXT = eventTXT +listEvent[i]
                        else :
                            if (i == (nbEvent-1)):
                                eventTXT = eventTXT+" et "+listEvent[i]    
                            else :
                                eventTXT = eventTXT+", "+listEvent[i]
            
        else :
            if (nbTache == 0):
                tacheTXT = "Vous avez aucune tache pour aujourd'hui" 
            else :
                if (nbTache == 1):
                    tacheTXT = "Tu as "+str(nbTache)+" tache qui est "+listTache[0]+"."
                else :
                    tacheTXT = "Tu as "+str(nbTache)+" taches qui sont "
                    for i in range(0,nbTache):
                        if (i == 0):
                            tacheTXT = tacheTXT+listTache[i]
                        else :
                            if (i == (nbTache-1)):
                                tacheTXT = tacheTXT+" et "+listTache[i]    
                            else :
                                tacheTXT = tacheTXT+", "+listTache[i]
            if (nbEvent == 0):
                eventTXT = "Tu as aucun événement aujourd'hui" 
            else :
                if (nbEvent == 1):
                    eventTXT = "Tu as "+str(nbEvent)+" evénement aujourd'hui qui est "+listEvent[0]+"."
                else :
                    eventTXT = "Tu as "+str(nbEvent)+" evénement aujourd'hui qui sont "
                    for i in range(0,nbEvent):
                        if (i == 0):
                            eventTXT = eventTXT +listEvent[i]
                        else :
                            if (i == (nbEvent-1)):
                                eventTXT = eventTXT+" et "+listEvent[i]    
                            else :
                                eventTXT = eventTXT+", "+listEvent[i]
        
        return 18,[tacheTXT,eventTXT]
    
    def sortieResumerAll(self):
        """
        Sortie NB  :
        - 19 -> OK
        - 20 -> Fail
        Sortie list : 
            [Meteo home , Meteo Work , fete , Actu 1 , Actu 2 , Actu 3 , textSpeak , tache , agenda]
        """
        nb1,listAgendaTache = self.sortieResumerTacheAgenda()
        nb2,listActuMeto = self.sortieResumerActualite()
        
        if (nb2 == 11):
            if (self.__etatVous == True) :
                text = "Imposible de vous faire le résumer "+self.__genre
            else :
                text = "Imposible de te faire le resumer "+self.__user
            return 20,[text,""]
        else :
            listOut = listActuMeto+listAgendaTache
            if (self.__etatVous == True) :
                listOut[6]= "Voici votre résumer des actulitée du jour avec la meteo ainsi des taches que vous avez a faire et des événement du jour."
            else :
                listOut[6]= "Voici ton résumer des actulitée du jour avec la meteo ainsi des taches que tu as faire et des événement du jour."
            
            return 19,listOut 
    
    def sortieStartRadio(self,radio:int):
        """
        1 = Europe 1 
        2 = Europe 2 
        3 = France Info
        4 = France Inter
        5 = France Musique
        6 = France Culture
        7 = France Bleu
        8 = Fun Radio
        9 = NRJ
        10 = RFM 
        11 = Nostalgi 
        12 = Skyrock
        13 = RTL
        """    
        if (self.__etatVous == True):
            text1 = "Je vous lance la radio "
            text2 = ". Bonne ecoute "+self.__genre
        else :
            text1 = "Voici la radio "
            text2 = ". Profite bien de ton ecoute "+self.__user
        
        match radio :
            case 1 :
                txtRadio = "Europe 1"
                sortieRadio = self.__objRadio.startEurope1()
            case 2 :
                sortieRadio = self.__objRadio.startEurope2()
                txtRadio = "Europe 2"
            case 3 :
                sortieRadio = self.__objRadio.startFranceInfo()
                txtRadio = "France Info"
            case 4 :
                sortieRadio = self.__objRadio.startFranceInter()
                txtRadio = "France Inter"
            case 5 :
                sortieRadio = self.__objRadio.startFranceMusique()
                txtRadio = "France Musique"
            case 6 :
                sortieRadio = self.__objRadio.startFranceCulture()
                txtRadio = "France culture"
            case 7 :
                sortieRadio = self.__objRadio.startFranceBleu()
                txtRadio = "France Bleu"
            case 8 :
                sortieRadio = self.__objRadio.startFunRadio()
                txtRadio = "Fun Radio"
            case 9 :
                sortieRadio = self.__objRadio.startNRJ()
                txtRadio = "NRJ"
            case 10 :
                sortieRadio = self.__objRadio.startRFM()
                txtRadio = "RFM"
            case 11 :
                sortieRadio = self.__objRadio.startNostalgi()
                txtRadio = "Nostalgi"
            case 12 :
                sortieRadio = self.__objRadio.startSkyrock()
                txtRadio = "Skyrock"
            case 13 :
                sortieRadio = self.__objRadio.startRTL()
                txtRadio = "RTL"
        
        
        if (sortieRadio == True):
            return text1+txtRadio+text2
        else :
            return "Je ne peux pas lancer une radio. Un probléme est survenu."
    
    def sortieDownloadMusic(self):
        self.__downloader.activeMusique()
        if (self.__etatVous == True):
            text = "Okay je vous ouvre l'interface pour télécharger une video youtube en musique."
        else :
            text = "Okay je t'ouvre l'interface pour télécharger une video youtube en musique."
        return text
    
    def sortieDownloadVideo(self):
        self.__downloader.activeVideo()
        if (self.__etatVous == True):
            text = "Okay je vous ouvre l'interface pour télécharger une video youtube."
        else :
            text = "Okay je t'ouvre l'interface pour télécharger une video youtube."
        return text
    
    def sortieOpenProjetDirect(self,projet:str):
        sortie = self.__objetArreraWork.openProjet(projet)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai bien ouvert le projet "+projet+" "+self.__genre+". Que voulez vous faire ?"
            else :
                text = "Le projet "+projet+" est bien ouvert. Que veux-tu faire ?"
        else :
            if (self.__etatVous == True):
                text = "Désoler "+self.__genre+" mais je ne peux pas t'ouvrir le projet "+projet+". Il n'existe peut-étre pas"
            else :
                text = "Désoler mais je trouve pas le projet "+projet+"."
        return projet,text
    
    def sortieOpenTableurDirect(self,file:str):
        sortie = self.__objetArreraWork.openTableurDirectly(file)
        if (sortie == True) :
            if (self.__etatVous == True) :
                text = "Votre fichier Exel a bien etais ouvert correctement "+self.__genre+". Il nous reste plus qu'a travailler dessus."
            else :
                text = "Je t'ai bien ouvert ton fichier exel. Aller travaillons dessus."
        else :
            if (self.__etatVous == True) :
                text = "Désoler "+self.__genre+" mais il met imposible de t'ouvrir un fichier exel"
            else :
                text = "Un probléme est survenu j'arrive pas a t'ouvrir ton fichier Exel."
        
        return text
    
    def sortieOpenWordDirect(self,file:str):
        sortie = self.__objetArreraWork.openWordDirectly(file)
        if (sortie == True) :
            if (self.__etatVous == True) :
                text = "Votre fichier de traitement de texte a bien etais ouvert correctement "+self.__genre+". Il nous reste plus qu'a ecrire dessus."
            else :
                text = "Je t'ai bien ouvert ton fichier Word. Aller travaillons dessus."
        else :
            if (self.__etatVous == True) :
                text = "Désoler "+self.__genre+" mais il met imposible de t'ouvrir un fichier Word"
            else :
                text = "Un probléme est survenu j'arrive pas a t'ouvrir ton fichier Word."
        
        return text

    def sortieOpenPostiteWithFile(self):
        sortie = self.__objPenseBete.activePenseBete(1)
        if (sortie == True):
            nameFile = self.__objPenseBete.getNamefile()
            if (self.__etatVous == True):
                text = "Je vous ai ouvert votre pense bete "+nameFile+" "+self.__genre+" "+self.__user
            else :
                text = "Je t'ai l'outil le pense bete "+nameFile
        else :
            if (self.__etatVous == True):
                text = "Un probleme est survenu je ne peux pas vous ouvrir l'outil de pense bete"
            else :
                text = "Il est imposible pour moi de d'ouvrir l'outil de pense bete"

        return sortie,text

    def sortieOpenPostiteNoFile(self):
        sortie = self.__objPenseBete.activePenseBete(2)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert l'outil de pense bete "+self.__genre+" "+self.__user
            else :
                text = "Je t'ai l'outil de pense bete"
        else :
            if (self.__etatVous == True):
                text = "Un probleme est survenu je ne peux pas vous ouvrir l'outil de pense bete"
            else :
                text = "Il est imposible pour moi de d'ouvrir l'outil de pense bete"

        return text

    def getNamePenseBete(self):
        return self.__objPenseBete.getNamefile()
    
    def sortieCorrection(self,requette:str):
        texte = requette.replace("corrige","").strip()
        sortie = self.__objOrthographe.active(texte)
        if (sortie == True):
            if (self.__etatVous == True):
                text = "Je vous ai ouvert l'outil pour corriger votre phrase."
            else :
                text = "Je t'ai ouvert l'outil pour corriger votre phrase."
        else :
            if (self.__etatVous == True):
                text = "Il est imposible d'ouvrir l'outil"
            else :
                text = "Il est imposible d'ouvrir l'outil"
        return text