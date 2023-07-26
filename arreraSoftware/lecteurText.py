from tkinter import*
from librairy.travailJSON import *
from ObjetsNetwork.gestion import*

class Reading:
    def __init__(self,json:jsonWork,gestionNeuron:gestionNetwork):
        #Recuperation des objet
        self.travailJSON = json
        self.gestionNeuron = gestionNeuron
        #Recuperation varriable
        self.color = self.travailJSON.lectureJSON("interfaceColor")
        self.textColor = self.travailJSON.lectureJSON("interfaceTextColor")
        self.name = gestionNeuron.getName()
        #initilisation fenetre tkinter
        self.screen = Tk()
        self.screen.title(self.name+" : lecture ")
        self.screen.minsize(600,500)
        self.screen.maxsize(600,500)
        #self.screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        self.screen.config(bg=self.color)
        self.entryLect = Text(self.screen,width=50)
        boutonValider  = Button(self.screen,text="Valider",bg=self.color,fg=self.textColor,font=("arial",15),command=self.Lecture)
        self.entryLect.pack(side="left")
        boutonValider.pack(side="right")
        self.screen.mainloop()
        
    def Lecture(self):
        texte = self.entryLect.get("1.0",END)
        self.screen.destroy()
        