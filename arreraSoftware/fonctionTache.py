from tkinter import*
from tkinter import messagebox
from librairy.travailJSON import*
from ObjetsNetwork.gestion import *

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
        # Frame
        self.__frameTask = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameAdd = Frame(screen,width=500,height=450,bg=self.__mainColor)
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
        labelTitreAdd = Label(self.__frameAdd,text="Ajouter une tache :",font=("arial","15"),
                              fg=self.__textColor,bg=self.__mainColor)
        nameTaskEntry =  Entry(self.__frameAdd,font=("arial",15),highlightthickness=2, highlightbackground="black")
        btnValiderAdd = Button(self.__frameAdd,text="Ajouter",font=("arial","15"),fg=self.__textColor,
                               bg=self.__mainColor,command=lambda:self.__addEvent(nameTaskEntry))
        btnAnnulerAdd = Button(self.__frameAdd,text="Annuler",font=("arial","15"),
                               fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Widget frameSuppr
        labelTitreSuppr = Label(self.__frameSuppr,text="Suprimmer une tache :",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor)
        btnValiderSuppr = Button(self.__frameSuppr,text="Supprimer",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__supprEvent)
        btnAnnulerSuppr = Button(self.__frameSuppr,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Widget frameCheck
        labelTitreCheck = Label(self.__frameCheck,text="Finir une tache :",font=("arial","15"),
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
        labelTitreAdd.place(x=0,y=0)
        nameTaskEntry.place(relx=0.5, rely=0.5, anchor="center")
        btnValiderAdd.place(relx=1, rely=1, anchor='se')
        btnAnnulerAdd.place(relx=0, rely=1, anchor='sw')
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
        self.__frameAdd.place(x=0,y=0)
    
    def __showTaskFrame(self):
        #self.__labelListTask.configure(text="")
        self.__frameTask.place(x=0,y=0)
        self.__frameCheck.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameAdd.place_forget()
        dictTache = self.__taskFile.dictJson()
        if(len(dictTache)!=0):
            nbTache = self.__taskFile.compteurFlagJSON()
            #self.__labelListTask.configure(text=dictTache["0"]+"\n")
            for i in range(1,nbTache):
                texte = self.__labelListTask.cget('text')
                self.__labelListTask.configure(text=texte+dictTache[str(i)]+"\n")
        #else :
            #self.__labelListTask.configure(text="Aucun tache")

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
            self.__frameAdd.place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)])
            OptionMenu(self.__frameSuppr,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            messagebox.showwarning("Avertisement","Vous pouvez supprimer une tache avant d'en ajouter")

    
    def __showCheckFrame(self):
        dictTache = self.__taskFile.dictJson()
        if(self.__checkIsTache==True):
            self.__frameTask.place_forget()
            self.__frameCheck.place(x=0,y=0)
            self.__frameSuppr.place_forget()
            self.__frameAdd.place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)])
            OptionMenu(self.__frameCheck,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            messagebox.showwarning("Avertisement","Vous pouvez finir une tache avant d'en ajouter")

    
    def __addEvent(self,entry:Entry):
        name = entry.get()
        if(name==""):
            messagebox.showwarning("Avertisement",
                                       "Vous crée une tache sans nom")
        else :
            nb = self.__taskFile.compteurFlagJSON()
            self.__taskFile.EcritureJSON(str(nb),name)
            self.__showTaskFrame()
            entry.delete(0,END)
    
    def __supprEvent(self):
        nameTache = self.__choixSuppr.get()
        dictTache = self.__taskFile.dictJson()
        nbTache = self.__taskFile.compteurFlagJSON()
        for i in range(0,nbTache):
            if (dictTache[str(i)]==nameTache):
                break
        self.__taskFile.supprDictReorg(str(i))
        messagebox.showinfo("événement","Tache supprimer")
        self.__showTaskFrame()

    def __checkEvent(self):
        nameTache = self.__choixSuppr.get()
        dictTache = self.__taskFile.dictJson()
        nbTache = self.__taskFile.compteurFlagJSON()
        for i in range(0,nbTache):
            if (dictTache[str(i)]==nameTache):
                break
        self.__taskFile.supprDictReorg(str(i))
        messagebox.showinfo("événement","Tache fini et supprimer")
        self.__showTaskFrame()  