from tkinter import*
from librairy.travailJSON import *

class fncRoutine :
    def __init__(self,configFile:jsonWork):
        # Varriable
        self.__icon = configFile.lectureJSON("iconAssistant")
        self.__name = configFile.lectureJSON("name")
        self.__guiColor = configFile.lectureJSON("interfaceColor")
        self.__textColor = configFile.lectureJSON("interfaceTextColor")
        # Objet
        self.__jsonRoutine = jsonWork(configFile.lectureJSON("emplacementFileRoutine"))
        
        
    def __windowsRoutine(self):
        # Fenetre
        self.__screen = Toplevel()
        self.__screen.minsize(500,700)
        self.__screen.maxsize(500,700)
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        self.__screen.title(self.__name+" : Routine")
        self.__screen.configure(bg=self.__guiColor)
        
        # Frame 
        self.__frameAcceuil = Frame(self.__screen,width=500,height=600,bg=self.__guiColor)
        self.__frameAdd = Frame(self.__screen,width=500,height=600,bg=self.__guiColor)
        self.__frameGestion = Frame(self.__screen,width=500,height=600,bg=self.__guiColor)
        self.__frameSuppr = Frame(self.__screen,width=500,height=600,bg=self.__guiColor)
        
        # Widget
        
        # Acceuil
        labelIndicationAcceuil= Label(self.__frameAcceuil,text="Routine "+self.__name,bg=self.__guiColor,fg=self.__textColor,font=("Arial","20"))
        btnValiderAcceuil = Button(self.__frameAcceuil,text="Crée une routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnCancelAcceuil = Button(self.__frameAcceuil,text="Gestion des routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        
        # Add
        labelIndicationAdd = Label(self.__frameAdd,text="Crée un nouvelle routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","20"))
        btnValiderAdd = Button(self.__frameAdd,text="Crée",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnCancelAdd = Button(self.__frameAdd,text="Annuler",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        
        # Gestion
        labelIndicationGestion = Label(self.__frameGestion,text="Gérer vos routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","20"))
        btnAddAction = Button(self.__frameGestion,text="Ajouter une action",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnSupprAction = Button(self.__frameGestion,text="Supprimer une action",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnSupprRoutine = Button(self.__frameGestion,text="Supprimer une routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnCancelGestion = Button(self.__frameGestion,text="Annuler",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        
        # Suppr
        labelIndicationSuppr = Label(self.__frameSuppr,text="Supprimer une routine",bg=self.__guiColor,fg=self.__textColor,font=("Arial","20"))
        btnSuppr = Button(self.__frameSuppr,text="Supprimer",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        btnAnnuler = Button(self.__frameSuppr,text="Annuler",bg=self.__guiColor,fg=self.__textColor,font=("Arial","15"))
        
        # Affichage 
        # Acceuil
        labelIndicationAcceuil.place(relx=0.5, rely=0.0, anchor="n") 
        btnValiderAcceuil.place(relx=0.0, rely=0.5, anchor="w")  
        btnCancelAcceuil.place(relx=1.0, rely=0.5, anchor="e") 
        
        # Add
        labelIndicationAdd.place(relx=0.5, rely=0.0, anchor="n") 
        btnValiderAdd.place(relx=0.0, rely=0.5, anchor="w")  
        btnCancelAdd.place(relx=1.0, rely=0.5, anchor="e") 
        
        # Gestion
        labelIndicationGestion.place(relx=0.5, rely=0.0, anchor="n") 
        btnAddAction
        btnSupprAction
        btnSupprRoutine
        btnCancelGestion
        
        # Suppr
        labelIndicationSuppr.place(relx=0.5, rely=0.0, anchor="n") 
        btnSuppr.place(relx=1, rely=1, anchor='se')
        btnAnnuler.place(relx=0, rely=1, anchor='sw')
        
        
    
    def add(self):
        self.__windowsRoutine()