from translate import Translator
from librairy.speak import*
from librairy.travailJSON import*
from tkinter import messagebox
from tkinter import*

class fncArreraTrad :
    def __init__(self,ConfigNeuron:jsonWork):
        #objet
        
        self.configNeuron = ConfigNeuron
        #varriable fenetre Tkinter
        self.name = self.configNeuron.lectureJSON("name")
        self.icon = self.configNeuron.lectureJSON("iconAssistant")
        self.color = self.configNeuron.lectureJSON("interfaceColor")
        self.textColor = self.configNeuron.lectureJSON("interfaceTextColor")
    
    def fenetreTrad(self,langInt:str,langOut:str):
        #objet
        self.traducteur = Translator(to_lang=langInt,from_lang=langOut)
        self.paroleInt = Speaking(langInt)
        self.paroleOut = Speaking(langOut)
        #Creation fenetre Tkinter
        self.fenetreTK = Tk()
        self.fenetreTK.title(self.name+" : Outil de traduction")
        self.fenetreTK.maxsize(1050,550)
        self.fenetreTK.minsize(1050,550)
        self.fenetreTK.iconphoto(False,PhotoImage(file=self.icon))
        self.fenetreTK.config(bg=self.color)
        #cadre
        self.frameBTN = Frame(self.fenetreTK,bg=self.color)
        #widget
        self.textInt = Text(self.fenetreTK,width=50,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.textOut = Text(self.fenetreTK,width=50,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.btnTrad = Button(self.frameBTN,text="Traduire",bg="green",fg="white",font=("arial",15),width=450,command=self.traduire)
        self.btnQuitter = Button(self.frameBTN,text="Quitter",bg="red",fg="white",font=("arial",15),width=450,command=self.quitter)
        self.btnClear = Button(self.frameBTN,text="Supprimer",bg=self.color,fg=self.textColor,font=("arial",15),width=450,command=self.clearText)
        #affichage
        self.textInt.pack(side="left")
        self.textOut.pack(side="right")
        self.frameBTN.place(relx=0.5,rely=0.5,anchor="center")
        self.btnTrad.pack()
        self.btnQuitter.pack()
        self.btnClear.pack()

    def traduire(self):
        texte = self.textInt.get("1.0",END).strip()
        if len(texte) == 0 :
            messagebox.showwarning("Attention", "Veuillez entrer une phase dans la la zone de texte de gauche")
        else :
            sortieTraducteur = self.traducteur.translate(texte)
            self.textOut.delete("1.0",END)
            self.textOut.insert("1.0",sortieTraducteur)
    
    def clearText(self):
        self.textOut.delete("1.0",END)
        self.textInt.delete("1.0",END)
        
    def quitter(self):
        self.fenetreTK.destroy()      
    
            
            
