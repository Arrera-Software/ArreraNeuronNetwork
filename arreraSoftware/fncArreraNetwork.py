from tkinter import*
import random
from librairy.travailJSON import *
from ObjetsNetwork.gestion import*
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *

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