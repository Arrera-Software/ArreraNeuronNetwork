from tkinter import *
from librairy.travailJSON import*
from tkinter import filedialog 
from tkinter import messagebox
import markdown
from tkhtmlview import HTMLLabel

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
        self.zoneTexte = HTMLLabel(frame)
        self.zoneTexte.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Rendre la fenêtre responsive
        self.__responsive(frame)
        self.__responsive(self.zoneTexte)
        
        return True
    
    def __responsive(self, widget):
        widget.grid(sticky="nsew")
    
    def activePenseBete(self)->bool:
        emplacementFile = filedialog.askopenfilename(
            defaultextension='.ab',
            filetypes=[("Fichier Pense-bete", "*.ab")])
        if (emplacementFile):
            self.__windows()
            with open(emplacementFile, 'r', encoding='utf-8') as file:
                file_content = file.read()
                html_content = markdown.markdown(file_content)
                self.zoneTexte.set_html(html_content)
            self.__nameFile = emplacementFile
            return True
        else:
            self.__nameFile = ""
            return False

    def getNamefile(self):
            return self.__nameFile
