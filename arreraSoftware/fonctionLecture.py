from tkinter import *
from gtts import gTTS
from playsound import playsound
from librairy.travailJSON import *
from librairy.speak import*

class fncLecture :
    def __init__(self,json:jsonWork,name,icon):
        #initilation objet
        self.json = json
        self.name = name
        self.icon = icon
        self.lang = ""
        self.langSet = 0
        self.color = self.json.lectureJSON("interfaceColor")
        self.textColor = self.json.lectureJSON("interfaceTextColor")
        #initilisation et configuration fenetre tkinter 
        self.screen = Tk()
        self.screen.title(self.name+" : lecture ")
        self.screen.minsize(600,500)
        self.screen.maxsize(600,500)
        self.screen.iconphoto(False,PhotoImage(file=self.icon))
        self.screen.config(bg=self.color)
        #varriable
        listeLang = ["en","fr","zh-CN","zh-TW","pt","es"]
        self.varLang = StringVar(self.screen)
        #Creation et configuration d'un menu
        self.menuTop = Menu(self.screen)
        self.menuTop.add_command(label="Langue de lecture",command=self.changementLang)
        #creation widget
        self.entryLect = Text(self.screen,width=70,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.boutonValider  = Button(self.screen,text="Valider",bg="green",fg="white",font=("arial",15),width=70,command=self.lecture)
        self.menuDeroulant = OptionMenu(self.screen,self.varLang,*listeLang)
        #Affichage
        self.entryLect.pack()
        self.boutonValider.pack(side="bottom")
        #fin de la fenetre
        self.screen.config(menu=self.menuTop)
        self.screen.mainloop()
    
    def retourAcceuil(self):
        self.menuTop.entryconfigure("Retour Acceuil",label="Langue de lecture",command=self.changementLang)
        self.menuDeroulant.place_forget()
        self.boutonValider.configure(command=self.lecture)
        self.entryLect.pack()

    def changementLang(self):
        self.menuTop.entryconfigure("Langue de lecture",label="Retour Acceuil",command=self.retourAcceuil)
        self.entryLect.pack_forget()
        self.boutonValider.configure(command=self.setlang)
        self.menuDeroulant.place(relx=0.5,rely=0.5,anchor="center")
    
    def setlang(self):
        self.lang = self.varLang.get()
        self.langSet =  1
        self.retourAcceuil()
    
    def lecture(self):
        texte = self.entryLect.get("1.0",END)
        if self.langSet == 0 :
            Speaking(self.json.lectureJSON("lang")).speak(texte)
        else :
            Speaking(self.lang).speak(texte)
        self.screen.destroy()
            