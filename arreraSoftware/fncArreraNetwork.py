from tkinter import*
import random
from librairy.travailJSON import *
from ObjetsNetwork.gestion import*
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *
from arreraSoftware.fonctionGPS import*

class fncArreraNetwork:
    def __init__(self,json:jsonWork,gestionNeuron:gestionNetwork,iconAssistant:str):
        #Recuperation des objet
        self.travailJSON = json
        self.gestionNeuron = gestionNeuron
        self.icon = iconAssistant
        #Recuperation varriable
        self.color = self.travailJSON.lectureJSON("interfaceColor")
        self.textColor = self.travailJSON.lectureJSON("interfaceTextColor")
        self.etatVous = self.gestionNeuron.getVous()
        self.name = self.gestionNeuron.getName()
        self.user = self.gestionNeuron.getUser()
        self.genre = self.gestionNeuron.getGenre()
        #initialisation objet 
        self.actu = Actu("3b43e18afcf945888748071d177b8513","6","fr","fr")
        self.gps = GPS("19bfbee6112be5b3d9a64d4ccec72602")
        self.meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        
    def reading(self):
        fncLecture(self.travailJSON,self.name,self.icon)
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