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
        self.operateurChooseComplex = ""
        
        
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
        self.operateurComplex = Frame(self.nbComplex)
        self.complex1 = Frame(self.nbComplex)
        self.complex2 = Frame(self.nbComplex)
        self.pythagore = Frame(self.screen,width=500,height=500,bg=self.color)
        self.chooseCal = Frame(self.pythagore)
        self.nbPythagore = Frame(self.pythagore)
        #widget
        self.ZoneCalcule = Text(self.screen,width=50, height=10,highlightthickness=2, highlightbackground="black",font=("arial","25"))
        self.affichageComplexOut = Entry(self.nbComplex,state="disabled",width=42,highlightthickness=2, highlightbackground="black",font=("arial","15"))
        self.zoneComplex1A = Entry(self.complex1,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.zoneComplex1B = Entry(self.complex1,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.zoneComplex2A = Entry(self.complex2,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.zoneComplex2B = Entry(self.complex2,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.zonePythagore1 = Entry(self.nbPythagore,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.zonePythagore2 = Entry(self.nbPythagore,highlightthickness=1, highlightbackground="black",font=("arial","15"))
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
        self.btnAngle = Button(self.clavier,text="Randian en degres",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.convertiseurDegRad)
        self.btnPythagore = Button(self.clavier,text="Theoreme de pythagore",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.modePythagore)
        self.btnNbComplex = Button(self.clavier,text="Nombre Complex",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.modeComplex)
        #btn nb complex
        self.btnEgalComplex = Button(self.nbComplex,image=self.imgEgal,command= lambda : self.calculeComplex())
        self.btnplusComplex = Button(self.operateurComplex,image=self.imgPlus,command= lambda : self.setOperateurComplex("+"))
        self.btnMoinComplex = Button(self.operateurComplex,image=self.imgMoin,command= lambda : self.setOperateurComplex("-"))
        self.btnFoisComplex = Button(self.operateurComplex,image=self.imgFois,command= lambda : self.setOperateurComplex("*"))
        self.btnDiviserComplex = Button(self.operateurComplex,image=self.imgDiviser,command= lambda : self.setOperateurComplex("/"))
        self.btnCancelComplex = Button(self.nbComplex,text="Annuler",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.cancelOperateurComplex)
        self.btnRetourComplex = Button(self.nbComplex,text="Retour",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.modeCalcule)
        #bouton pythagore
        self.btnReciproque = Button(self.chooseCal,text="Reciproque",bg=self.color,fg=self.textColor,command=lambda : self.calculePythagore(2))
        self.btnTheoreme = Button(self.chooseCal,text="Theoreme",bg=self.color,fg=self.textColor,command=lambda : self.calculePythagore(1))
        self.btnRetourPythagore = Button(self.pythagore,text="Retour",font=("arial","13"),bg=self.color,fg=self.textColor,command=self.modeCalcule)
        #label
        self.labelPlus = Label(self.operateurComplex,image=self.imgPlus)
        self.labelMois = Label(self.operateurComplex,image=self.imgMoin)
        self.labelDiviser = Label(self.operateurComplex,image=self.imgDiviser)
        self.labelFois = Label(self.operateurComplex,image=self.imgFois)
        self.affichageHistorique = Label(self.historique,text="Historique :",width=30,bg=self.color,fg=self.textColor,font=("arial","20"), anchor="w")
        self.affichageComplexOut = Label(self.nbComplex,width=42,font=("arial","15"),bg="grey",fg="white")
        self.complex1L = Label(self.complex1,text="j",font=("arial","15"),bg=self.color)
        self.complex2L = Label(self.complex2,text="j",font=("arial","15"),bg=self.color)
        self.affichagePythagoreOut =  Label(self.pythagore,width=42,font=("arial","15"),bg="grey",fg="white")
        #affichage 
        self.WidgetnbComplex()
        self.widgetPythagore()
        self.affichageClavier()
        self.historique.pack(side="left",fill="both", expand=True) 
        if mode == "0":
            self.modeCalcule()
        else :
            if mode == "1":
                self.modeComplex()
            else :
                if mode == "2":
                    self.modePythagore()
        #affichage historique
        self.affichageHistorique.place(x=0,y=0)
        #verrifaction de carratere taper
        self.ZoneCalcule.bind("<KeyPress-Return>",self.enterPressed)
        self.ZoneCalcule.bind("<KeyPress>",self.carractereInterdit)
    
    def modeCalcule(self):
        self.nbComplex.pack_forget()
        self.pythagore.pack_forget()
        self.updateCalculatrice() 
        self.clavier.pack(side="bottom",anchor="sw")
        self.ZoneCalcule.pack(side="top",anchor="nw") 
        
        
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
        
    def updateCalculatrice(self):
        self.btnNb7.update() 
        self.btnNb8.update() 
        self.btnNb9.update() 
        self.btnParenthese1.update() 
        self.btnParenthese2.update() 
        
        self.btnNb4.update() 
        self.btnNb5.update() 
        self.btnNb6.update() 
        self.btnFois.update() 
        self.btnDiviser.update() 
        
        self.btnNb1.update() 
        self.btnNb2.update() 
        self.btnNb3.update() 
        self.btnplus.update() 
        self.btnMoin.update() 
        
        self.btnNb0.update()
        self.btnVirgule.update()
        self.btnPuissanceDix.update()
        self.btnEgal.update()
        self.btnSuppr.update()
        self.btnClear.update()
        
        self.btnSIN.update()
        self.btnCOS.update()
        self.btnTAN.update()
        self.btnARCSIN.update()
        self.btnARCCOS.update()
        self.btnARCTAN.update()
        
        self.btnPI.update() 
        self.btnRacine.update() 
        self.btnExposant.update() 
        self.btnExpodentiel.update() 
        self.btnLN.update() 
        self.btnLOG.update() 
        
        self.btnAngle.update() 
        self.btnPythagore.update() 
        self.btnNbComplex.update() 
        
        self.ZoneCalcule.update() 
       
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
            self.affichageHistorique.configure(text="Historique :\n" + str(contenu) + " = " + str(resultat))
            self.affichageHistorique.update()
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere(str(resultat))
        except Exception as e:
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
            
    def modeComplex(self):
        self.clavier.pack_forget()
        self.ZoneCalcule.pack_forget()
        self.nbComplex.pack(side="left")  
        self.complex1.place(x=15,y=25)
        self.operateurComplex.place(x=((self.nbComplex.winfo_reqwidth()-self.operateurComplex.winfo_reqwidth())//2),y=75)
        self.complex2.place(x=15,y=125)
        self.btnEgalComplex.place(x=((self.nbComplex.winfo_reqwidth()-self.btnEgalComplex.winfo_reqwidth())//2),y=175)
        self.affichageComplexOut.place(x=15,y=225)
        self.btnCancelComplex.place(x=(500-self.btnCancelComplex.winfo_reqwidth()),y=(500-self.btnCancelComplex.winfo_reqheight()))
        self.btnRetourComplex.place(x=0,y=(500-self.btnCancelComplex.winfo_reqheight()))
        self.affichageComplexOut.configure(text="")
        self.zoneComplex1A.bind("<KeyPress>", self.carractereInterdit)
        self.zoneComplex1B.bind("<KeyPress>", self.carractereInterdit)
        self.zoneComplex2A.bind("<KeyPress>", self.carractereInterdit)
        self.zoneComplex2B.bind("<KeyPress>", self.carractereInterdit)             
    
    def WidgetnbComplex(self):
        self.zoneComplex1A.pack(side="left")
        self.complex1L.pack(side="right")
        self.zoneComplex1B.pack(side="right")
        self.zoneComplex2A.pack(side="left")
        self.complex2L.pack(side="right")
        self.zoneComplex2B.pack(side="right") 
        self.btnplusComplex.pack(side="left")
        self.btnMoinComplex.pack(side="left")
        self.btnFoisComplex.pack(side="left")
        self.btnDiviserComplex.pack(side="left")
    
    def setOperateurComplex(self,operateur:str):
        self.operateurChooseComplex = operateur
        self.btnplusComplex.pack_forget()
        self.btnMoinComplex.pack_forget()
        self.btnFoisComplex.pack_forget()
        self.btnDiviserComplex.pack_forget()
        self.operateurComplex.place_forget()
        if self.operateurChooseComplex == "+":
            self.labelPlus.pack()
        else :
            if self.operateurChooseComplex == "-":
                self.labelMois.pack()
            else :
                if self.operateurChooseComplex == "*":
                    self.labelFois.pack()
                else :
                    if self.operateurChooseComplex== "/":
                        self.labelDiviser.pack()
        self.operateurComplex.update()
        self.operateurComplex.place(x=((self.nbComplex.winfo_reqwidth()-self.operateurComplex.winfo_reqwidth())//2),y=75)
        
    def cancelOperateurComplex(self):
        if self.operateurChooseComplex == "":
            self.operateurChooseComplex = ""
        else :
            self.operateurChooseComplex = ""
            self.labelPlus.pack_forget()
            self.labelMois.pack_forget()
            self.labelFois.pack_forget()
            self.labelDiviser.pack_forget()
            self.operateurComplex.place_forget()
            self.btnplusComplex.pack(side="left")
            self.btnMoinComplex.pack(side="left")
            self.btnFoisComplex.pack(side="left")
            self.btnDiviserComplex.pack(side="left")
            self.operateurComplex.update()
            self.operateurComplex.place(x=((self.nbComplex.winfo_reqwidth()-self.operateurComplex.winfo_reqwidth())//2),y=75)
        
        
    def calculeComplex(self):
        nb1A = self.zoneComplex1A.get()
        nb1B = self.zoneComplex1B.get()
        nb2A = self.zoneComplex2A.get()
        nb2B = self.zoneComplex2B.get()
        if self.operateurChooseComplex == "" or nb1A.strip() == "" or nb1B.strip() == "" or nb2A.strip() == "" or nb2B.strip() == "" :
            self.affichageComplexOut.configure(text="Erreur")
        else :
            calcule = CalculeNbComplexe(int(nb1A),int(nb1B),int(nb2A),int(nb2B))
            if self.operateurChooseComplex == "+":
                nb1 = calcule.recuperationNb1()
                nb2 = calcule.recuperationNb2()
                resultat = calcule.aditionNbComplex()
                self.affichageHistorique.configure(text="Historique :\n" + nb1+"+"+nb2 + " = " + str(resultat))
            else :
                if self.operateurChooseComplex == "-":
                    nb1 = calcule.recuperationNb1()
                    nb2 = calcule.recuperationNb2()
                    resultat = calcule.soustrationNbComplex()
                    self.affichageHistorique.configure(text="Historique :\n" + nb1+"-"+nb2 + " = " + str(resultat))
                else :
                    if self.operateurChooseComplex == "*":
                        nb1 = calcule.recuperationNb1()
                        nb2 = calcule.recuperationNb2()
                        resultat = calcule.multiplicationNbComplex()
                        self.affichageHistorique.configure(text="Historique :\n" + nb1+"*"+nb2 + " = " + str(resultat))
                    else :
                        if self.operateurChooseComplex == "/":
                            nb1 = calcule.recuperationNb1()
                            nb2 = calcule.recuperationNb2()
                            resultat = calcule.divisionNbComplex()
                            self.affichageHistorique.configure(text="Historique :\n" + nb1+"/"+nb2 + " = " + str(resultat))
            self.operateurChooseComplex = ""
            self.affichageComplexOut.configure(text=str(resultat))
    
    def widgetPythagore(self):
        self.btnReciproque.pack(side="left")
        self.btnTheoreme.pack(side="left")
        self.zonePythagore1.pack(side="left")
        self.zonePythagore2.pack(side="left")
    
    def modePythagore(self):
        self.clavier.pack_forget()
        self.ZoneCalcule.pack_forget()
        self.pythagore.pack(side="right")  
        self.nbPythagore.place(x=15,y=25)
        self.chooseCal.place(x=(self.pythagore.winfo_reqwidth() - self.chooseCal.winfo_reqwidth()) // 2,y=125)
        self.affichagePythagoreOut.place(x=15,y=225) 
        self.btnRetourPythagore.place(x=0,y=(500-self.btnRetourPythagore.winfo_reqheight()))
        self.affichagePythagoreOut.configure(text="")
        
    def calculePythagore(self,mode):
        nb1 = self.zonePythagore1.get()
        nb2 = self.zonePythagore2.get()
        if nb1.strip() == "" or nb2.strip() == "":
            self.affichagePythagoreOut.configure(text="Erreur")
        else :
            calcule = Pythagore(int(nb1),int(nb2))
            if mode == 1:
                resultat = str(calcule.theoreme())
                sortieCalcule = calcule.recuperationCalcule()
                self.affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
            else :
                if mode == 2:
                    if int(nb1) <= int(nb2) :
                        self.affichagePythagoreOut.configure(text="Erreur")
                    else :
                        resultat = str(calcule.reciproque())
                        sortieCalcule = calcule.recuperationCalcule()
                        self.affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
    
    def convertiseurDegRad(self):
        contenu = self.ZoneCalcule.get("1.0", END)
        if contenu ==  "":
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        else :
            self.ZoneCalcule.delete("1.0", END)
            self.ecritureCarractere(str(math.degrees(int(contenu))))
                

class CalculeNbComplexe :
    def __init__(self,nb1_1:int,nb1_2:int,nb2_1:int,nb2_2:int):
        self.nb1= complex(nb1_1,nb1_2)
        self.nb2 = complex(nb2_1,nb2_2)
        
    def recuperationNb1(self):
        return str(self.nb1)
    
    def recuperationNb2(self):
        return str(self.nb2)
         
    def aditionNbComplex(self):
        resultat = self.nb1 + self.nb2
        return resultat
    
    def soustrationNbComplex(self):
        resultat = self.nb1 - self.nb2
        return resultat
    
    def multiplicationNbComplex(self):
        resultat = self.nb1 * self.nb2
        return resultat
    
    def divisionNbComplex(self):
        resultat = self.nb1 / self.nb2
        return resultat    
    

class Pythagore :
    def __init__(self,nb1:int,nb2:int):
        self.nb1 = nb1
        self.nb2 = nb2
        self.etatReciproque = bool
       
    def theoreme(self):
        resultat = math.sqrt(self.nb1**2+self.nb2**2)
        self.etatReciproque = False
        return resultat
    
    def reciproque(self):
        resultat = math.sqrt(self.nb1**2-self.nb2**2)
        self.etatReciproque = True
        return resultat 
    
    def recuperationCalcule(self):
        if self.reciproque == False :
            return str("math.sqrt("+str(self.nb1)+"**2"+"+"+str(self.nb2)+"**2"+")") 
        else :
            return str("math.sqrt("+str(self.nb1)+"**2"+"-"+str(self.nb2)+"**2"+")") 