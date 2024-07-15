from tkinter import filedialog 
from tkinter.messagebox import*
from objet.arreradocument import*
from objet.arreratableur import*

class CArreraWork :
    def __init__(self):
        # Variable etat ouverture fichier
        self.__tableurOpen = False
        self.__wordOpen = False 
        # Varriable des objet 
        self.__objTableur = None
        self.__objWord = None

    def openTableur(self) : 
        if (self.__tableurOpen==False):
            # Demande de l'emplacement du fichier
            showinfo("Work","Choisissez votre fichier exel")
            emplacementFile = filedialog.asksaveasfilename(
                    defaultextension='.xlsx', 
                    filetypes=[("Fichiers Excel", "*.xlsx")])
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
            emplacementFile = filedialog.asksaveasfilename(
                    defaultextension='.xlsx', 
                    filetypes=[('Fichiers Word', '*.docx'),
                               ("Texte OpenDocument","*.odt")])
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

    def setFormuleTableur(self,mode:int,case1:str,case2:str,caseDest:str):
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
            self.__wordOpen = False
            return True
        else :
            return False