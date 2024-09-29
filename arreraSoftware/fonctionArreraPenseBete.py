from tkinter import *
from librairy.travailJSON import*
from tkinter import filedialog 
from tkinter import messagebox

class fncArreraPostite:
    def __init__(self,fileConf:jsonWork):
        self.__name = fileConf.lectureJSON("name")
        self.__icon = fileConf.lectureJSON("iconAssistant")
        self.__color = fileConf.lectureJSON("interfaceColor")
        self.__textColor = fileConf.lectureJSON("interfaceTextColor")
        self.__nameFile = ""
    
    def __windows(self):
        # Création de la fenêtre Toplevel
        self.__penseBete = Toplevel()
        self.__penseBete.title(self.__name+" : Postite")
        self.__penseBete.iconphoto(False,PhotoImage(file=self.__icon))
        self.__penseBete.configure(bg=self.__color)
        self.__penseBete.geometry("800x600")
        self.__penseBete.grid_rowconfigure(0, weight=1)
        self.__penseBete.grid_columnconfigure(0, weight=1)
        
        # Création d'un cadre pour contenir le post-it et les boutons
        frame = Frame(self.__penseBete, bg=self.__color)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        # Zone de texte pour le post-it avec fond jaune
        self.zoneTexte = Text(frame, bg="lightyellow", font=("Arial", 20))
        self.zoneTexte.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Création du bouton "Enregistrer"
        btnSave = Button(self.__penseBete, text="Enregistrer", font=("Arial", 14),bg=self.__color,fg=self.__textColor,command=self.__saveFile)
        btnSave.grid(row=1, column=0, pady=10)  # Placer le bouton en dessous de la zone de texte

        # Rendre la fenêtre responsive
        self.__responsive(frame)
        self.__responsive(self.zoneTexte)
        
        return True
    
    def __responsive(self, widget):
        widget.grid(sticky="nsew")
    
    def activePenseBete(self,mode:int)->bool:
        """
        Args:
            mode (int): 1 -> Ouverture fichier pense bete 2-> Lancement pense-bete vide

        """
        match mode :
            case 1 :
                emplacementFile = filedialog.askopenfilename(
                            defaultextension='.ab', 
                            filetypes=[("Fichier Pense-bete", "*.ab")])
                if (emplacementFile):
                    self.__windows()
                    with open(emplacementFile, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                        self.zoneTexte.delete(1.0,END)
                        self.zoneTexte.insert(END,file_content) 
                    self.__nameFile = emplacementFile
                    return True      
                else :
                    return False  
            case 2 :
                self.__windows()
                return True
        return False
    
    def getNamefile(self):
        return self.__nameFile
    
    def __saveFile(self):
        penseBete = self.zoneTexte.get(1.0,END)
        if (self.__nameFile!=""):
            sortie = messagebox.askyesno(self.__name+" : Postite","Voulez-vous enregistrer dans le meme fichier")
            if (sortie == True):
                with open(self.__nameFile, "w") as fichier:
                    fichier.write(penseBete)
                self.__penseBete.destroy()
            else :
                file = filedialog.asksaveasfilename(
                            defaultextension='.ab', 
                            filetypes=[("Fichier Pense-bete", "*.ab")])
                if (file):
                    with open(file, "w") as fichier:
                        fichier.write(penseBete)
                    self.__penseBete.destroy()
                else :
                    messagebox.showerror(self.__name+" : Postite","Impossible d'enregistrer")
        else :
            file = filedialog.asksaveasfilename(
                            defaultextension='.ab', 
                            filetypes=[("Fichier Pense-bete", "*.ab")])
            if (file):
                with open(file, "w") as fichier:
                    fichier.write(penseBete)
                self.__penseBete.destroy()
            else :
                messagebox.showerror(self.__name+" : Postite","Impossible d'enregistrer")