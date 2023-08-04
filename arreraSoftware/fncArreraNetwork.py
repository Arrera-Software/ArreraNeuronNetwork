from tkinter import*
import random
from librairy.travailJSON import *
from ObjetsNetwork.gestion import*
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *
from arreraSoftware.fonctionGPS import*
from arreraSoftware.fonctionTraduction import*

class fncArreraNetwork:
    def __init__(self,fichierConfigurationNeuron:jsonWork,gestionNeuron:gestionNetwork,decteurOS:OS):
        #Recuperation des objet
        self.configNeuron = fichierConfigurationNeuron
        self.gestionNeuron = gestionNeuron
        self.detecteurOS = decteurOS
        self.icon = self.configNeuron.lectureJSON("iconAssistant")
        #Recuperation varriable
        self.color = self.configNeuron.lectureJSON("interfaceColor")
        self.textColor = self.configNeuron.lectureJSON("interfaceTextColor")
        self.etatVous = self.gestionNeuron.getVous()
        self.name = self.gestionNeuron.getName()
        self.user = self.gestionNeuron.getUser()
        self.genre = self.gestionNeuron.getGenre()
        #initialisation objet 
        self.actu = Actu("3b43e18afcf945888748071d177b8513","6","fr","fr")
        self.gps = GPS("19bfbee6112be5b3d9a64d4ccec72602")
        self.meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        self.itineraires = GPSItineraires()
       
        
    def reading(self):
        fncLecture(self.configNeuron,self.detecteurOS)
        if self.etatVous == True :
            text = "J'espere que sa vous etais utile "+self.genre
        else :
            text = "J'espere que sa ta servie "+self.name
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
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        listeActu = self.actu.Actu()
        text2 = text+" Les actualites son "+listeActu[nbrand1]+"."+listeActu[nbrand2]+"."+listeActu[nbrand3]
        
        return text2
    
    def sortieTraducteur(self,langInt:str,langOut:int):
        fncArreraTrad(self.configNeuron,langInt,langOut)
        text = "J'espere que c'est bien"
        return text