from tkinter import filedialog 
from tkinter import*
from tkinter.messagebox import*
from objet.arreradocument import*
from objet.arreratableur import*
from librairy.travailJSON import*
from librairy.dectectionOS import*
import subprocess
import re
import os


class fncArreraWork :
    def __init__(self,neuronfile:jsonWork,dectOs:OS):
        # Objet 
        self.__dectOs = dectOs
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
            if (self.__verifTableurCase(case)== True):
                if (str(valeur).isdigit() == True):
                    self.__objTableur.write(case,int(valeur))
                else :
                    self.__objTableur.write(valeur)
                self.__objTableur.saveFile()
                showinfo("Work","Valeur ecrite")
            else :
                showerror("Work","La case n'est pas valide")
        else :
            showerror("Work","Il n'a pas de tableur ouvert")

    def __verifTableurCase(self,chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False
    
    def guiAddFormule(self,mode:int):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        if ((self.__tableurOpen == True)and (mode < 5)):
            tab = Toplevel()
            tab.iconphoto(False,PhotoImage(file=self.__iconAssistant))
            tab.title(self.__nameAssistant+" Work : Tableur")
            tab.configure(background=self.__guiColor)
            tab.maxsize(300,175)
            tab.minsize(300,175)
            frameCaseDest = Frame(tab,bg=self.__guiColor)
            frameCaseDebut = Frame(tab,bg=self.__guiColor)
            frameCaseFin = Frame(tab,bg=self.__guiColor)
            # Declaration des widget
            # Indication
            labelIndication = Label(tab,font=("arial","20"),
                              bg=self.__guiColor,fg=self.__textColor)
            # Destination
            labelCaseDest = Label(frameCaseDest,text="Destination :",font=("arial","15"),
                              bg=self.__guiColor,fg=self.__textColor)
            entryCaseDest = Entry(frameCaseDest,font=("arial","15"),relief=SOLID)
            # Debut
            labelCaseDebut = Label(frameCaseDebut,text="Debut :",font=("arial","15"),
                                bg=self.__guiColor,fg=self.__textColor)
            entryCaseDebut = Entry(frameCaseDebut,font=("arial","15"),relief=SOLID)
            # Fin
            labelCaseFin = Label(frameCaseFin,text="Fin :",font=("arial","15"),
                                bg=self.__guiColor,fg=self.__textColor)
            entryCaseFin = Entry(frameCaseFin,font=("arial","15"),relief=SOLID)
            # Valider
            btnValider = Button(tab,text="Valider",font=("arial","15"),bg=self.__guiColor,
                                fg=self.__textColor,
                                command= lambda :self.__fncAddFormuleTableurTk(mode,tab,entryCaseDest,entryCaseDebut,entryCaseFin))
            
            # Definition du texte du label indication et de la bonne fnc
            match mode :
                case 1 :
                    labelIndication.configure(text="Somme")
                case 2 :
                    labelIndication.configure(text="Moyenne")
                case 3:
                    labelIndication.configure(text="Comptage")
                case 4 :
                    labelIndication.configure(text="Minimun")
                case 5 :
                    labelIndication.configure(text="Maximun")
            # Affichage 
            # Widget in frame
            labelCaseDest.pack(side="left")
            entryCaseDest.pack(side="right")

            labelCaseDebut.pack(side="left")
            entryCaseDebut.pack(side="right")

            labelCaseFin.pack(side="left")
            entryCaseFin.pack(side="right")

            # Windows
            labelIndication.pack()
            frameCaseDest.pack()
            frameCaseDebut.pack()
            frameCaseFin.pack()
            btnValider.pack()
            return True
        else :
            return False
    
    def __fncAddFormuleTableurTk(self,mode:int,w:Toplevel,edest:Entry,edebut:Entry,eFin:Entry):
        dest = edest.get()
        debut = edebut.get()
        fin = eFin.get()

        if ((self.__verifTableurCase(dest) == True) 
            and (self.__verifTableurCase(debut)== True) 
            and (self.__verifTableurCase(fin) == True)):

            sortie = self.__setFormuleTableur(mode,debut,fin,dest)

            if (sortie == True):
                showinfo("Work","Formule ajouter")
            else :
                showerror("Work","Formule non ajouter")
        else :
            showerror("Work","Les cases ne sont pas valide")
        
        edest.delete(0,END)
        edebut.delete(0,END)
        eFin.delete(0,END)
        w.destroy()

    def openTableurOs(self):
        if (self.__tableurOpen==True):
            if ((self.__dectOs.osLinux() == True) 
                and (self.__dectOs.osWindows() == False)):
                subprocess.call(["xdg-open",self.__fileTableur])
                return True
            else :
                if ((self.__dectOs.osLinux() == False) 
                and (self.__dectOs.osWindows() == True)):
                    os.startfile(self.__fileTableur)
                    return True
                else :
                    return False                    
        else :
            return False
        
    def openWordOs(self):
        if (self.__tableurOpen==True):
            if ((self.__dectOs.osLinux() == True) 
                and (self.__dectOs.osWindows() == False)):
                subprocess.call(["xdg-open",self.__fileWork])
                return True
            else :
                if ((self.__dectOs.osLinux() == False) 
                and (self.__dectOs.osWindows() == True)):
                    os.startfile(self.__fileWork)
                    return True
                else :
                    return False                    
        else :
            return False
