from tkinter import filedialog 
from tkinter import*
from tkinter.messagebox import*
from objet.arreradocument import*
from objet.arreratableur import*
from librairy.travailJSON import*
import re


class fncArreraWork :
    def __init__(self,neuronfile:jsonWork):
        # Variable etat ouverture fichier
        self.__tableurOpen = False
        self.__wordOpen = False 
        # Varriable des objet 
        self.__objTableur = None
        self.__objWord = None
        # Varriable de nom du fichier
        self.__fileTableur = ""
        self.__fileWork = ""
        # Chargement des variable
        self.__nameAssistant = neuronfile.lectureJSON("name")
        self.__iconAssistant = neuronfile.lectureJSON("iconAssistant")
        self.__guiColor = neuronfile.lectureJSON("interfaceColor")
        self.__textColor =  neuronfile.lectureJSON("interfaceTextColor")


    def openTableur(self) : 
        if (self.__tableurOpen==False):
            # Demande de l'emplacement du fichier
            showinfo("Work","Choisissez votre fichier exel")
            emplacementFile = filedialog.askopenfilename(
                    defaultextension='.xlsx', 
                    filetypes=[("Fichiers Excel", "*.xlsx")])
            self.__fileTableur = emplacementFile
            if (emplacementFile == ""):
                showwarning("Work","Aucun fichier selectionner")
                return False
            else :
                self.__objTableur = CArreraTableur(emplacementFile)
                showinfo("Work","Exel ouvert")
                self.__tableurOpen = True
                return True
        else :
            return False   

    def openWord(self):
        if (self.__wordOpen == False):
            # Demande de l'emplacement du fichier
            showinfo("Work","Choisissez votre fichier exel")
            emplacementFile = filedialog.askopenfilename(
                    defaultextension='.xlsx', 
                    filetypes=[('Fichiers Word', '*.docx'),
                               ("Texte OpenDocument","*.odt")])
            self.__fileWork = emplacementFile
            if (emplacementFile == ""):
                showwarning("Work","Aucun fichier selectionner")
                return False
            else :
                self.__objWord = CArreraDocx(emplacementFile)
                showinfo("Work","Word ouvert")
                self.__wordOpen = True
                return True
        else :
            return False       

    def __setFormuleTableur(self,mode:int,case1:str,case2:str,caseDest:str):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        if (self.__tableurOpen==True):
            match mode :
                case 1 :
                    self.__objTableur.somme(caseDest,case1,case1)
                    self.__objTableur.saveFile()
                    return True
                case 2 :
                    self.__objTableur.moyenne(caseDest,case1,case2)
                    self.__objTableur.saveFile()
                    return True
                case 3 : 
                    self.__objTableur.comptage(caseDest,case1,case2)
                    self.__objTableur.saveFile()
                    return True
                case 4 :
                    self.__objTableur.minimun(caseDest,case1,case2)
                    self.__objTableur.saveFile()
                    return True
                case 5 :
                    self.__objTableur.maximun(caseDest,case1,case2)
                    self.__objTableur.saveFile()
                    return True
                case other :
                    return False
        else :
            return False
    
    def readTableur(self):
        if (self.__tableurOpen==True):
            listSorti = []
            contenu = self.__objTableur.read()
            for cell_position, cell_value in contenu.items():
                listSorti.append("Cellule "+str(cell_position)+" : "+str(cell_value))
            return listSorti
        else :
            return ["error",""]
        
    def setValeurTableur(self,case:str,valeur):
        if ((self.__tableurOpen==True) and (case != "")):
            self.__objTableur.write(case,valeur)
            self.__objTableur.saveFile()
            return True
        else :
            return False
    
    def closeTableur(self):
        if (self.__tableurOpen==True):
            self.__objTableur.saveFile()
            self.__objTableur.closeFile()
            del self.__objTableur
            self.__objTableur = None
            self.__fileTableur = ""
            return True
        else :
            return False

    def writeDocxFile(self,text:str):
        if (self.__wordOpen == True):
            return self.__objWord.write(text)
        else :
            return False
    
    def readDocxFile(self):
        if (self.__wordOpen == True):
            return self.__objWord.read()
        else :
            return "error"

    def closeDocx(self):
        if (self.__wordOpen == True) :
            del self.__objWord
            self.__objWord = None
            self.__fileWork = ""
            self.__wordOpen = False
            return True
        else :
            return False
    
    def getEtatTableur(self):
        return self.__tableurOpen
    
    def getEtatWord(self):
        return self.__wordOpen
    
    def getNameFileTableur(self):
        return self.__fileTableur
    
    def getNameFileWord(self):
        return self.__fileWork
    
    def guiAddValeur(self):
        if (self.__tableurOpen == True):
            tab = Toplevel()
            tab.iconphoto(False,PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant+" Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300,100)
            tab.minsize(300,100)
            frameCase = Frame(tab,bg=self.__guiColor)
            frameValeur = Frame(tab,bg=self.__guiColor)
            # Declaration des widget
            labelCase = Label(frameCase,text="Case :",font=("arial","15"),
                              bg=self.__guiColor,fg=self.__textColor)
            entryCase = Entry(frameCase,font=("arial","15"),relief=SOLID)
            labelValeur = Label(frameValeur,text="Valeur :",font=("arial","15"),
                                bg=self.__guiColor,fg=self.__textColor)
            entryValeur = Entry(frameValeur,font=("arial","15"),relief=SOLID)
            btnValider = Button(tab,text="Valider",font=("arial","15"),bg=self.__guiColor,
                                fg=self.__textColor,command= lambda : self.__fncAddValeurTk(tab,entryValeur,entryCase))
            # Affichage de widget
            labelCase.pack(side="left")
            labelValeur.pack(side="left")
            entryCase.pack(side="right")
            entryValeur.pack(side="right")
            
            frameCase.pack()
            frameValeur.pack()

            btnValider.pack(side="bottom")

            return True
        else :
            showerror("Work","Il n'a pas de tableur ouvert")
            return False
    
    def __fncAddValeurTk(self,w:Toplevel,evaleur:Entry,ecase:Entry):
        valeur = evaleur.get()
        case = ecase.get()
        if (case == ""):
            showerror("Work","Vous avez pas définie de case.")
        else :
            self.__addValeur(case,valeur)
        
        evaleur.delete(0,END)
        ecase.delete(0,END)
        w.destroy()

    def __addValeur(self,case:str,valeur):
        if (self.__tableurOpen == True):
            if (self.__verifChaine(case)== True):
                self.__objTableur.write(case,valeur)
                self.__objTableur.saveFile()
                showinfo("Work","Valeur ecrite")
            else :
                showerror("Work","La case n'est pas valide")
        else :
            showerror("Work","Il n'a pas de tableur ouvert")

    def __verifChaine(self,chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False