from tkinter import*
from librairy.travailJSON import *
from ObjetsNetwork.gestion import*
from arreraSoftware.fonctionLecture import *

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
        
    def reading(self):
        fncLecture(self.travailJSON,self.name,self.icon)
        if self.etatVous == True :
            text = "J'espere que sa vous etais utile "+self.genre
        else :
            text = "J'espere que sa ta servie "+self.name
        return text
    
