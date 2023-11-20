import holidays
from tkinter import *
from tkinter.messagebox import showinfo 
from tkcalendar import DateEntry
from ObjetsNetwork.gestion import *
from arreraSoftware.fonctionDate import *

class fncArreraCalendar :
    def __init__(self,fichierConfig:jsonWork,gestionnaire:gestionNetwork):
        self.configNeuron = fichierConfig
        self.gestionnaire = gestionnaire
        self.objetDate = fncDate()
        self.fichierEvenement = jsonWork(self.gestionnaire.getValeurfichierUtilisateur("emplacementEvenenement"))
        name = self.configNeuron.lectureJSON("name")
        icon = self.configNeuron.lectureJSON("iconAssistant")
        color = self.configNeuron.lectureJSON("interfaceColor")
        textColor = self.configNeuron.lectureJSON("interfaceTextColor")
        self.interfaceCalendar = ArreraCalendarAddSuppr(color,icon,textColor,name,self.fichierEvenement,self.objetDate)
        dictEvenement =  self.fichierEvenement.dictJson()
        nbEvent = self.fichierEvenement.compteurFlagJSON()
        dateHier = self.objetDate.dateTowmoro()
        
            
    
    
    def addEvenemnt(self):
        self.interfaceCalendar.interfaceAdd()
    
    def supprEvenement(self):
        self.interfaceCalendar.interfaceSuppr()

    def checkEvenement(self):
        self.objetDate.rafraichisement()
        listEvent = []
        dictionnaireEvenement = self.fichierEvenement.dictJson()
        dateJour = str(self.objetDate.annes() + "-" +  self.objetDate.nbMois() + "-" + self.objetDate.jour())
        nbEvent = 0
        nb = self.fichierEvenement.compteurFlagJSON()
        if nb == 0 :
           return nbEvent , listEvent  
        for i in range(0,nb) :
            if dictionnaireEvenement[str(i)][0] == dateJour :
                nbEvent += 1 
                listEvent.append(dictionnaireEvenement[str(i)][1])
        
        return nbEvent , listEvent
            
            
       
          

class ArreraCalendarAddSuppr :
    def __init__(self,color:str,icon:str,textColor:str,name:str,fileEvenement:jsonWork,date:fncDate) :
        self.color = color
        self.icon = icon
        self.textColor = textColor
        self.name = name 
        self.fileEvenement = fileEvenement
        self.objetDate = date
        
    
    def _fenetreTk(self):
        #fenetre tkinter
        self.screen = Toplevel()
        self.screen.title(self.name+" : Calendrier")
        self.screen.iconphoto(False,PhotoImage(file=self.icon))
        self.screen.maxsize(500,200)
        self.screen.minsize(500,200)
        self.screen.config(bg=self.color)
        #varriable
        self.event = StringVar(self.screen)
        #carde
        self.cadreAdd = Frame(self.screen,bg=self.color,height=200,width=500)
        self.cadreSuppr = Frame(self.screen,bg=self.color,height=200,width=500)
        #diferent widget
        #cadreAdd
        self.labelAdd = Label(self.cadreAdd,text="Ajout d'un événement",font=("arial",20),bg=self.color,fg=self.textColor)
        self.labelDate = Label(self.cadreAdd,text="Choisir date : ",font=("arial",20),bg=self.color,fg=self.textColor)
        self.labelName = Label(self.cadreAdd,text="Nom du rappel : ",font=("arial",20),bg=self.color,fg=self.textColor)
        self.chooseDate = DateEntry(self.cadreAdd, width=15, background='darkblue', foreground='white', borderwidth=2)
        self.entryName = Entry(self.cadreAdd,font=("arial",12),highlightthickness=2, highlightbackground="black")
        self.btnValiderAdd = Button(self.cadreAdd,text="Ajouter",font=("arial",20),bg=self.color,fg=self.textColor,command=self._addEvent)
        #cadreSuppr
        self.btnValiderSuppr = Button(self.cadreSuppr,text="Supprimer",font=("arial",20),bg=self.color,fg=self.textColor,command=self._supprEvent)
        #affichage
        #cadre add
        self.labelAdd.place(x=0,y=0)
        self.labelDate.place(x=0,y=55)
        self.chooseDate.place(x=190,y=60)
        self.labelName.place(x=0,y=105)
        self.entryName.place(x=200,y=110)
        self.btnValiderAdd.place(x=200,y=150)
        #cadreSuppr
        self.btnValiderSuppr.place(x=200,y=150)
        

    def interfaceAdd(self):
        self._fenetreTk()
        self.cadreAdd.pack()
        
    def interfaceSuppr(self):
        self._fenetreTk()
        self.cadreSuppr.pack()
        dictEvenement = self.fileEvenement.dictJson()
        if len(dictEvenement) == 0 :
            showinfo("Avertisement","Vous pouvez supprimer d'evenement avant d'en ajouter")
        else :
            nbEvent = self.fileEvenement.compteurFlagJSON()
            listEvent = []
            for i in range(0,nbEvent) :
                listEvent.append(dictEvenement[str(i)][1])
            listMenu = OptionMenu(self.cadreSuppr,self.event,*listEvent)
            listMenu.place(relx=0.5,rely=0.5,anchor=CENTER)
            self.event.set(listEvent[0])
        
    def _addEvent(self):
        self.objetDate.rafraichisement()
        dateJour = str(self.objetDate.annes() + "-" +  self.objetDate.nbMois() + "-" + self.objetDate.jour())
        dateIn = str(self.chooseDate.get_date())
        if dateIn ==  dateJour :
            showinfo("Avertisement","Vous pouvez pas crée un événement a la date du jours")
        else :
            nom = self.entryName.get()
            if nom == "" :
                showinfo("Avertisement","Vous crée un événement sans nom")
            else :
                nb = self.fileEvenement.compteurFlagJSON()
                self.fileEvenement.EcritureJSON(str(nb),[dateIn,nom])
                self.entryName.delete(0,END)
                self.chooseDate.set_date(datetime.date.today())
                showinfo("événement","Evénement enregistrer avec succes")
                
    def _supprEvent(self):
        nameEvent = self.event.get()
        dictEvenement = self.fileEvenement.dictJson()
        for flag, valeurs in dictEvenement.items():
            deuxieme_valeur = valeurs[1]  # Deuxième valeur de la liste
            if deuxieme_valeur == nameEvent:
                break  
        self.fileEvenement.supprDictReorg(flag)
        showinfo("événement","Evénement supprimer")
        self.screen.destroy()   