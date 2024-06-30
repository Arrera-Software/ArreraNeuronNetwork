from tkinter import*
from tkinter.messagebox import *
from librairy.travailJSON import*
from ObjetsNetwork.gestion import *
from tkcalendar import DateEntry
from datetime import datetime, timedelta

class fncArreraTache :
    def __init__(self,fichierConfig:jsonWork,gest:gestionNetwork):
        self.__taskFile = jsonWork(gest.getEmplacemntfileTache())
        self.__mainColor = fichierConfig.lectureJSON("interfaceColor")
        self.__textColor = fichierConfig.lectureJSON("interfaceTextColor")
        self.__icon = fichierConfig.lectureJSON("iconAssistant")
        self.__nameAssistant = fichierConfig.lectureJSON("name")

    def __windows(self):
        screen = Toplevel()
        screen.minsize(500,500)
        screen.maxsize(500,500)
        screen.configure(bg=self.__mainColor)
        screen.title(self.__nameAssistant+" : Tache")
        screen.iconphoto(False,PhotoImage(file=self.__icon))
        # Varriable 
        self.__choixSuppr = StringVar(screen)
        tomorrow = datetime.today() + timedelta(days=1)
        # Frame
        self.__frameTask = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameAdd = [Frame(screen,width=500,height=450,bg=self.__mainColor),
                           Frame(screen,width=500,height=450,bg=self.__mainColor),
                           Frame(screen,width=500,height=450,bg=self.__mainColor)]
        self.__frameSuppr = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameCheck = Frame(screen,width=500,height=450,bg=self.__mainColor)
        frameNavigation = Frame(screen,width=500,height=50,bg=self.__mainColor)
        self.__frameShowTache = [Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor)]
        # Widget FrameNavigation
        btnAddNav = Button(frameNavigation,text="Ajouter",font=("arial","15"),
                           fg=self.__textColor,bg=self.__mainColor,command=self.__showAddFrame)
        btnSupprNav = Button(frameNavigation,text="Supprimer",font=("arial","15"),
                             fg=self.__textColor,bg=self.__mainColor,command=self.__showSupprFrame)
        btnCheckNav = Button(frameNavigation,text="Finir un tache",font=("arial","15"),
                             fg=self.__textColor,bg=self.__mainColor,command=self.__showCheckFrame)
        # Widget frameTask
        labelTitreTask = Label(self.__frameTask,text=self.__nameAssistant+" tache",font=("arial","15","bold"),
                               fg=self.__textColor,bg=self.__mainColor)
        
        # Widget framAdd
        labelTitreAdd = [Label(self.__frameAdd[0],text="Ajouter une tache :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                         Label(self.__frameAdd[1],text="Définir la date de fin :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                         Label(self.__frameAdd[2],text="Ajouter une description a la tache :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor)]
        
        self.__nameTaskEntry =  Entry(self.__frameAdd[0],font=("arial",15),highlightthickness=2, highlightbackground="black")
        
        self.__btnValiderAdd = [Button(self.__frameAdd[0],text="Ajouter",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor,command=self.__addEvent),
                         Button(self.__frameAdd[1],text="Valider",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor),
                         Button(self.__frameAdd[2],text="Valider",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor)]
        
        self.__chooseDateTask = DateEntry(self.__frameAdd[1], width=15, background=self.__mainColor, 
                               foreground=self.__textColor, borderwidth=2,year=tomorrow.year, 
                               month=tomorrow.month, day=tomorrow.day)
        
        btnAnnulerAdd = Button(self.__frameAdd[0],text="Annuler",font=("arial","15"),
                               fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        
        self.__descriptionEntryTask =  Entry(self.__frameAdd[2],font=("arial",15),highlightthickness=2, highlightbackground="black")
        # Widget frameSuppr
        labelTitreSuppr = Label(self.__frameSuppr,text="Suprimmer une tache :",font=("arial","15","bold"),
                                fg=self.__textColor,bg=self.__mainColor)
        btnValiderSuppr = Button(self.__frameSuppr,text="Supprimer",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__supprEvent)
        btnAnnulerSuppr = Button(self.__frameSuppr,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Widget frameCheck
        labelTitreCheck = Label(self.__frameCheck,text="Finir une tache :",font=("arial","15","bold"),
                                fg=self.__textColor,bg=self.__mainColor)
        btnValiderCheck = Button(self.__frameCheck,text="Finir",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__checkEvent)
        btnAnnulerCheck = Button(self.__frameCheck,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Affichage Main
        frameNavigation.place(relx=0.5, rely=1.0, anchor="s")
        # Affichage FrameNavigation 
        btnAddNav.place(relx=0.0, rely=0.5, anchor="w")  
        btnSupprNav.place(relx=1.0, rely=0.5, anchor="e") 
        btnCheckNav.place(relx=0.5, rely=0.5, anchor="center")
        # Affichage FrameTask
        labelTitreTask.place(relx=0.5, rely=0.0, anchor="n")
        # Affichage frameAdd 
        for i in range(0,3):
            labelTitreAdd[i].place(x=0,y=0)
        self.__btnValiderAdd[0].place(relx=1, rely=1, anchor='se')
        btnAnnulerAdd.place(relx=0, rely=1, anchor='sw')
        for i in range(1,3):
            self.__btnValiderAdd[i].place(relx=1, rely=1, anchor='se')

        self.__descriptionEntryTask.place(relx=0.5, rely=0.5, anchor="center")
        self.__nameTaskEntry.place(relx=0.5, rely=0.5, anchor="center")
        self.__chooseDateTask.place(relx=0.5, rely=0.5, anchor="center")
        # Affichage frameSuppr
        labelTitreCheck.place(x=0,y=0)
        btnValiderCheck.place(relx=1, rely=1, anchor='se')
        btnAnnulerCheck.place(relx=0, rely=1, anchor='sw')
        # Affichage frameSuppr
        labelTitreSuppr.place(x=0,y=0)
        btnValiderSuppr.place(relx=1, rely=1, anchor='se')
        btnAnnulerSuppr.place(relx=0, rely=1, anchor='sw')
        self.__frameShowTache[0].place(x=0,y=labelTitreTask.winfo_reqheight())
        self.__frameShowTache[1].place(x=self.__frameShowTache[0].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight())
        self.__frameShowTache[2].place(x=self.__frameShowTache[0].winfo_reqwidth()+self.__frameShowTache[1].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight())
        
        self.__frameShowTache[3].place(x=0,y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
        self.__frameShowTache[4].place(x=self.__frameShowTache[3].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
        self.__frameShowTache[5].place(x=self.__frameShowTache[3].winfo_reqwidth()+self.__frameShowTache[4].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
    
    def activeViewTask(self):
        self.__windows()
        self.__showTaskFrame()
    
    def activeViewAdd(self):
        self.__windows()
        self.__showAddFrame()
    
    def activeViewSuppr(self):
        check = self.__checkIsTache()
        if (check == True) :
            self.__windows()
            self.__showSupprFrame()
        return check
    
    def activeViewCheck(self):
        check = self.__checkIsTache()
        if (check == True) :
            self.__windows()
            self.__showCheckFrame()
        return check
        
    def __showAddFrame(self):
        self.__frameTask.place_forget()
        self.__frameCheck.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameAdd[0].place(x=0,y=0)
    
    def __showTaskFrame(self):
        #self.__labelListTask.configure(text="")
        self.__frameTask.place(x=0,y=0)
        self.__frameCheck.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameAdd[0].place_forget()
        self.__frameAdd[1].place_forget()
        self.__frameAdd[2].place_forget()
        dictTache = self.__taskFile.dictJson()
        if(len(dictTache)!=0):
            nbTache = self.__taskFile.compteurFlagJSON()
            """
            self.__labelListTask.configure(text=dictTache["0"]+"\n")
            for i in range(1,nbTache):
                texte = self.__labelListTask.cget('text')
                self.__labelListTask.configure(text=texte+dictTache[str(i)]+"\n")
        #else :
            #self.__labelListTask.configure(text="Aucun tache")
        """

    def __checkIsTache(self):
        if(len(self.__taskFile.dictJson())==0):
            return False
        else :
            return True

    def __showSupprFrame(self):
        if (self.__checkIsTache() == True) :
            dictTache = self.__taskFile.dictJson()
            self.__frameTask.place_forget()
            self.__frameCheck.place_forget()
            self.__frameSuppr.place(x=0,y=0)
            self.__frameAdd[0].place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)]["name"])
            OptionMenu(self.__frameSuppr,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            showwarning("Avertisement","Vous pouvez supprimer une tache avant d'en ajouter")

    
    def __showCheckFrame(self):
        if(self.__checkIsTache()==True):
            dictTache = self.__taskFile.dictJson()
            self.__frameTask.place_forget()
            self.__frameCheck.place(x=0,y=0)
            self.__frameSuppr.place_forget()
            self.__frameAdd[0].place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)]["name"])
            OptionMenu(self.__frameCheck,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            showwarning("Avertisement","Vous pouvez finir une tache avant d'en ajouter")

    
    def __addEvent(self):
        name = self.__nameTaskEntry.get()
        if(name==""):
            showwarning("Avertisement","Vous crée une tache sans nom")
        else :
            nb = self.__taskFile.compteurFlagJSON()
            self.__taskFile.creerFlagDictionnaire(str(nb))
            self.__taskFile.ajouterFlagDict(str(nb),"name",name)
            reponseDate = askyesno("Tache", "Voulez-vous mettre un date de fin ?")
            self.__nameTaskEntry.delete(0,END)
            if (reponseDate) :
                self.__addDate(str(nb))
            else :
                self.__taskFile.ajouterFlagDict(str(nb),"date","none")
                reponseDes = askyesno("Tache", "Voulez-vous mettre une description ?")
                if (reponseDes) :
                    self.__addDescription(str(nb))
                else :
                    self.__taskFile.ajouterFlagDict(str(nb),"description","none")
                    showinfo("Tache","Tache ajouter")
                    self.__showTaskFrame()

                
    
    def __addDate(self,nb:str):
        self.__frameAdd[0].place_forget()
        self.__frameAdd[2].place_forget()
        self.__frameAdd[1].place(x=0,y=0)
        self.__btnValiderAdd[1].configure(command=lambda:self.__addEventDate(nb))

    def __addDescription(self,nb:str):
        self.__frameAdd[0].place_forget()
        self.__frameAdd[1].place_forget()
        self.__frameAdd[2].place(x=0,y=0)
        self.__btnValiderAdd[2].configure(command=lambda:self.__addEventDescription(nb))
    
    def __addEventDate(self,nb:str):
        self.__taskFile.ajouterFlagDict(nb,"date",self.__formatageDateEntry(self.__chooseDateTask))
        reponseDes = askyesno("Tache", "Voulez-vous mettre une description ?")
        if (reponseDes) :
            self.__addDescription(nb)
        else :
            self.__taskFile.ajouterFlagDict(nb,"description","none")
            showinfo("Tache","Tache ajouter")
            self.__showTaskFrame()


    def __addEventDescription(self,nb:str):
        description = self.__descriptionEntryTask.get()
        self.__descriptionEntryTask.delete(0,END)
        if (description != ""):
            self.__taskFile.ajouterFlagDict(nb,"description",description)
            showinfo("Tache","Tache ajouter")
            self.__showTaskFrame()
        else :
            showwarning("Tache","Imposible d'ajouter une description vide")
    
    def __supprEvent(self):
        nameTache = self.__choixSuppr.get()       
        self.__taskFile.supprDictByFlag("name",nameTache)
        showinfo("événement","Tache supprimer")  
        self.__showTaskFrame()

    def __checkEvent(self):
        nameTache = self.__choixSuppr.get()
        self.__taskFile.supprDictByFlag("name",nameTache)
        showinfo("événement","Tache fini et supprimer")
        self.__showTaskFrame() 

    def __formatageDateEntry(self,dateEntry:DateEntry):
        date_obj = dateEntry.get_date()  # Obtenir la date sous forme d'objet datetime.date
        formatted_date = f"{date_obj.year}-{date_obj.month}-{date_obj.day}"  # Formatter la date
        return formatted_date 