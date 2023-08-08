from tkinter import *
from librairy.travailJSON import *
import math

class fncCalculatrice :
    def __init__(self,ConfigNeuron:jsonWork):
        self.configNeuron = ConfigNeuron
        self.name = self.configNeuron.lectureJSON("name")
        self.icon = self.configNeuron.lectureJSON("iconAssistant")
        self.color = self.configNeuron.lectureJSON("interfaceColor")
        self.textColor = self.configNeuron.lectureJSON("interfaceTextColor")
        self.emplacementTouche = self.configNeuron.lectureJSON("toucheCalculatrice")+"/"
        
        
    def calculatrice(self,mode):
        self.screen = Tk()
        self.imageTouche()
        self.screen.title(self.name+" : Calculatrice")
        self.screen.iconphoto(False,PhotoImage(file=self.icon))
        self.screen.maxsize(1000,500)
        self.screen.minsize(1000,500)
        #cadre
        self.clavier = Frame(self.screen,width=500,height=250,bg=self.color)
        self.historique = Frame(self.screen,width=500,height=500,bg=self.color)
        self.nbComplex = Frame(self.screen,width=500,height=500,bg=self.color)
        #widget
        self.ZoneCalcule = Text(self.screen,width=50, height=10,highlightthickness=2, highlightbackground="black",font=("arial","25"))
        #touche clavier
        #chiffre
        self.btnNb0 = Button(self.clavier,image=self.imgNb0,command= lambda : self.ecritureCarractere("0"))
        self.btnNb1 = Button(self.clavier,image=self.imgNb1,command= lambda : self.ecritureCarractere("1"))
        self.btnNb2 = Button(self.clavier,image=self.imgNb2,command= lambda : self.ecritureCarractere("2"))
        self.btnNb3 = Button(self.clavier,image=self.imgNb3,command= lambda : self.ecritureCarractere("3"))
        self.btnNb4 = Button(self.clavier,image=self.imgNb4,command= lambda : self.ecritureCarractere("4"))
        self.btnNb5 = Button(self.clavier,image=self.imgNb5,command= lambda : self.ecritureCarractere("5"))
        self.btnNb6 = Button(self.clavier,image=self.imgNb6,command= lambda : self.ecritureCarractere("6"))
        self.btnNb7 = Button(self.clavier,image=self.imgNb7,command= lambda : self.ecritureCarractere("7"))
        self.btnNb8 = Button(self.clavier,image=self.imgNb8,command= lambda : self.ecritureCarractere("8"))
        self.btnNb9 = Button(self.clavier,image=self.imgNb9,command= lambda : self.ecritureCarractere("9"))
        self.btnPI = Button(self.clavier,image=self.imgPI,command= lambda : self.ecritureCarractere("3.1415926535897932"))
        #operateur
        self.btnVirgule = Button(self.clavier,image=self.imgVirgule,command= lambda : self.ecritureCarractere("."))
        self.btnPuissanceDix = Button(self.clavier,image=self.imgPuissanceDix,command= lambda : self.ecritureCarractere("*10**"))
        self.btnEgal = Button(self.clavier,image=self.imgEgal,command=self.calcule)
        self.btnplus = Button(self.clavier,image=self.imgPlus,command= lambda : self.ecritureCarractere("+"))
        self.btnMoin = Button(self.clavier,image=self.imgMoin,command= lambda : self.ecritureCarractere("-"))
        self.btnFois = Button(self.clavier,image=self.imgFois,command= lambda : self.ecritureCarractere("*"))
        self.btnDiviser = Button(self.clavier,image=self.imgDiviser,command= lambda : self.ecritureCarractere("/"))
        self.btnParenthese1 = Button(self.clavier,image=self.imgParenthese1,command= lambda : self.ecritureCarractere("("))
        self.btnParenthese2 = Button(self.clavier,image=self.imgParenthese2,command= lambda : self.ecritureCarractere(")"))
        self.btnRacine = Button(self.clavier,image=self.imgRacine,command= lambda : self.ecritureCarractere("math.sqrt("))
        self.btnExposant = Button(self.clavier,image=self.imgExposant,command= lambda : self.ecritureCarractere("**"))
        self.btnExpodentiel = Button(self.clavier,image=self.imgExpodentiel,command= lambda : self.ecritureCarractere("math.exp("))
        self.btnLN = Button(self.clavier,image=self.imgLN,command= lambda : self.ecritureCarractere("math.log(x,math.e)"))
        self.btnLOG = Button(self.clavier,image=self.imgLOG,command= lambda : self.ecritureCarractere("math.log(x,10)"))
        #cercle trigo
        self.btnSIN = Button(self.clavier,image=self.imgSIN,command=lambda : self.ecritureCarractere("math.sin("))
        self.btnCOS = Button(self.clavier,image=self.imgCOS,command=lambda : self.ecritureCarractere("math.cos("))
        self.btnTAN = Button(self.clavier,image=self.imgTAN,command=lambda :self.ecritureCarractere("math.tan("))
        self.btnARCSIN = Button(self.clavier,image=self.imgARCSIN,command=lambda : self.ecritureCarractere("math.asin("))
        self.btnARCCOS = Button(self.clavier,image=self.imgARCCOS,command=lambda : self.ecritureCarractere("math.acos("))
        self.btnARCTAN = Button(self.clavier,image=self.imgARCTAN,command=lambda : self.ecritureCarractere("math.cos("))
        #autre
        self.btnClear = Button(self.clavier,image=self.imgClear,command=self.clearAll)
        self.btnSuppr = Button(self.clavier,image=self.imgSuppr,command=self.suppr)
        #btn fonction special
        self.btnAngle = Button(self.clavier,text="Randian en degres",font=("arial","13"),bg=self.color,fg=self.textColor)
        self.btnPythagore = Button(self.clavier,text="Theoreme de pythagore",font=("arial","13"),bg=self.color,fg=self.textColor)
        self.btnNbComplex = Button(self.clavier,text="Nombre Complex",font=("arial","13"),bg=self.color,fg=self.textColor)
        #label
        self.affichageHistorique = Label(self.historique,text="Historique :",width=30,bg=self.color,fg=self.textColor,font=("arial","20"), anchor="w")
        #affichage 
        self.affichageClavier()
        self.historique.pack(side="left",fill="both", expand=True) 
        self.clavier.pack(side="bottom",anchor="sw")
        self.ZoneCalcule.pack(side="top",anchor="nw")
        #affichage historique
        self.affichageHistorique.place(x=0,y=0)
        #verrifaction de carratere taper
        self.ZoneCalcule.bind("<KeyPress-Return>",self.enterPressed)
        self.ZoneCalcule.bind("<KeyPress>",self.carractereInterdit)
    
    def modeComplex(self):
        self.clavier.place_forget()
        
    def affichageClavier(self):
        self.btnNb7.place(x=0,y=0)
        self.btnNb8.place(x=35,y=0)
        self.btnNb9.place(x=70,y=0)
        self.btnParenthese1.place(x=105,y=0)
        self.btnParenthese2.place(x=140,y=0)
        
        self.btnNb4.place(x=0,y=35)
        self.btnNb5.place(x=35,y=35)
        self.btnNb6.place(x=70,y=35)
        self.btnFois.place(x=105,y=35)
        self.btnDiviser.place(x=140,y=35)
        
        self.btnNb1.place(x=0,y=70)
        self.btnNb2.place(x=35,y=70)
        self.btnNb3.place(x=70,y=70)
        self.btnplus.place(x=105,y=70)
        self.btnMoin.place(x=140,y=70)
        
        self.btnNb0.place(x=0,y=105)
        self.btnVirgule.place(x=35,y=105)
        self.btnPuissanceDix.place(x=70,y=105)
        self.btnEgal.place(x=105,y=105)
        self.btnSuppr.place(x=140,y=105)
        self.btnClear.place(x=175,y=105)
        
        self.btnSIN.place(x=0,y=140)
        self.btnCOS.place(x=35,y=140)
        self.btnTAN.place(x=70,y=140)
        self.btnARCSIN.place(x=105,y=140)
        self.btnARCCOS.place(x=140,y=140)
        self.btnARCTAN.place(x=175,y=140)
        
        self.btnPI.place(x=0,y=175)
        self.btnRacine.place(x=35,y=175)
        self.btnExposant.place(x=70,y=175)
        self.btnExpodentiel.place(x=105,y=175)
        self.btnLN.place(x=140,y=175)
        self.btnLOG.place(x=175,y=175)
        
        self.btnAngle.place(x=250,y=35)
        self.btnPythagore.place(x=250,y=105)
        self.btnNbComplex.place(x=250,y=175)
       
    def imageTouche(self):
        self.imgNb0 = PhotoImage(file=self.emplacementTouche+"tchNB0.png")
        self.imgNb1 = PhotoImage(file=self.emplacementTouche+"tchNB1.png")
        self.imgNb2 = PhotoImage(file=self.emplacementTouche+"tchNB2.png")
        self.imgNb3 = PhotoImage(file=self.emplacementTouche+"tchNB3.png")
        self.imgNb4 = PhotoImage(file=self.emplacementTouche+"tchNB4.png")
        self.imgNb5 = PhotoImage(file=self.emplacementTouche+"tchNB5.png")
        self.imgNb6 = PhotoImage(file=self.emplacementTouche+"tchNB6.png")
        self.imgNb7 = PhotoImage(file=self.emplacementTouche+"tchNB7.png")
        self.imgNb8 = PhotoImage(file=self.emplacementTouche+"tchNB8.png")
        self.imgNb9 = PhotoImage(file=self.emplacementTouche+"tchNB9.png")
        self.imgPI = PhotoImage(file=self.emplacementTouche+"tchPI.png")
        
        self.imgVirgule = PhotoImage(file=self.emplacementTouche+"tchVirgule.png")
        self.imgPuissanceDix = PhotoImage(file=self.emplacementTouche+"tchDixPuissance.png")
        self.imgEgal = PhotoImage(file=self.emplacementTouche+"tchEgal.png")
        self.imgPlus = PhotoImage(file=self.emplacementTouche+"tchPlus.png")
        self.imgMoin = PhotoImage(file=self.emplacementTouche+"tchMoin.png")
        self.imgFois = PhotoImage(file=self.emplacementTouche+"tchFois.png")
        self.imgDiviser = PhotoImage(file=self.emplacementTouche+"tchDiviser.png")
        self.imgParenthese1 = PhotoImage(file=self.emplacementTouche+"tchParenthese1.png")
        self.imgParenthese2 = PhotoImage(file=self.emplacementTouche+"tchParenthese2.png")
        self.imgRacine = PhotoImage(file=self.emplacementTouche+"tchRacine.png")
        self.imgExposant = PhotoImage(file=self.emplacementTouche+"tchExposant.png")
        self.imgExpodentiel = PhotoImage(file=self.emplacementTouche+"tchExpodentiel.png")
        self.imgLN = PhotoImage(file=self.emplacementTouche+"tchLN.png")
        self.imgLOG = PhotoImage(file=self.emplacementTouche+"tchLOG.png")
        
        self.imgClear = PhotoImage(file=self.emplacementTouche+"tchClear.png")
        self.imgSuppr = PhotoImage(file=self.emplacementTouche+"tchSuppr.png")
        
        self.imgSIN = PhotoImage(file=self.emplacementTouche+"tchSIN.png")
        self.imgCOS = PhotoImage(file=self.emplacementTouche+"tchCOS.png")
        self.imgTAN = PhotoImage(file=self.emplacementTouche+"tchTAN.png")
        self.imgARCSIN = PhotoImage(file=self.emplacementTouche+"tchARCSIN.png")
        self.imgARCCOS = PhotoImage(file=self.emplacementTouche+"tchARCCOS.png")
        self.imgARCTAN = PhotoImage(file=self.emplacementTouche+"tchARCTAN.png")
    
    def carractereInterdit(self,event):
        carractereSpeciaux = "',?;§!ùµ*£$¤¨@ç|~&²¹#`\_°"
        carractereSpeciaux2 = '"'
        if event.char.isalpha():
            return "break"
        elif event.char in carractereSpeciaux:
            return "break"
        elif event.char in carractereSpeciaux2:
            return "break"
        
    def enterPressed(self,event):
        self.calcule()
        return "break"
        
    def ecritureCarractere(self,crc:str):
        self.ZoneCalcule.insert("end",crc)
        
    def clearAll(self):
        self.ZoneCalcule.delete("1.0",END)
        
    def suppr(self):
        # Récupérer le contenu actuel du widget Text
        contenu = self.ZoneCalcule.get("1.0", "end-1c")

        if contenu:
            # Supprimer le dernier caractère
            contenu = contenu[:-1]

            # Mettre à jour le widget Text avec le nouveau contenu
            self.ZoneCalcule.delete("1.0", "end")
            self.ZoneCalcule.insert("1.0", contenu)
            
    def calcule(self):
        contenu = self.ZoneCalcule.get("1.0", END)
        contenu = contenu.replace(" ", "")
        try:
            resultat = eval(contenu)
            self.affichageHistorique.configure(text="Historique :\n" + contenu + " = " + str(resultat))
            self.affichageHistorique.update()
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere(str(resultat))
        except Exception as e:
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")

        