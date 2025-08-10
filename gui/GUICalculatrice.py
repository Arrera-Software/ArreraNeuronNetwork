from tkinter import PhotoImage, END
from tkinter.messagebox import showerror
from gui.guibase import GuiBase,gestionnaire
import math

class GUICalculatrice(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Calculatrice")
        self.__operateurChooseComplex = ""
        
        
    def _mainframe(self):
        self._screen.minsize(1000,500)
        #cadre
        self.__fclavier = self._arrtk.createFrame(self._screen, width=500, height=250)
        self.__fhistorique = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__fnbComplex = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__fCalculeComplex = self._arrtk.createFrame(self.__fnbComplex, width=500, height=120)
        self.__fResultatComplex = self._arrtk.createFrame(self.__fnbComplex, width=500, height=80)
        self.__foperateurComplex = self._arrtk.createFrame(self.__fCalculeComplex)
        self.__fcomplex1 = self._arrtk.createFrame(self.__fCalculeComplex)
        self.__fcomplex2 = self._arrtk.createFrame(self.__fCalculeComplex)
        self.__fpythagore = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__fchooseCal = self._arrtk.createFrame(self.__fpythagore, width=400, height=50)
        self.__fnbPythagore = self._arrtk.createFrame(self.__fpythagore, width=500, height=100)
        #widget
        self.__zoneCalcule = self._arrtk.createText(self._screen, width=500, height=250)
        
        self.__zoneComplex1A = self._arrtk.createEntry(self.__fcomplex1,ppolice="Arial",ptaille=15)
        self.__zoneComplex1B = self._arrtk.createEntry(self.__fcomplex1,ppolice="Arial",ptaille=15)
        self.__zoneComplex2A = self._arrtk.createEntry(self.__fcomplex2,ppolice="Arial",ptaille=15)
        self.__zoneComplex2B = self._arrtk.createEntry(self.__fcomplex2,ppolice="Arial",ptaille=15)
        
        self.__zonePythagore1 = self._arrtk.createEntry(self.__fnbPythagore,ppolice="Arial",ptaille=15)
        self.__zonePythagore2 = self._arrtk.createEntry(self.__fnbPythagore,ppolice="Arial",ptaille=15)
        # Label
        self.__labelTitrePythagore = self._arrtk.createLabel(self.__fnbPythagore, text="Calcule du théoréme de pythagore"
                                                             ,ppolice="Arial",ptaille=25)
        self.__labelTitreNbComplex = self._arrtk.createLabel(self.__fnbComplex, text="Calcule de nombre complex"
                                                             ,ppolice="Arial",ptaille=25)
        #touche clavier
        #chiffre
        btnNb0 = self._arrtk.createButton(self.__fclavier,text="0", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("0"),width=36,height=36,conerRadus=18)
        btnNb1 = self._arrtk.createButton(self.__fclavier,text="1", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("1"),width=36,height=36,conerRadus=18)
        btnNb2 = self._arrtk.createButton(self.__fclavier,text="2", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("2"),width=36,height=36,conerRadus=18)
        btnNb3 = self._arrtk.createButton(self.__fclavier,text="3", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("3"),width=36,height=36,conerRadus=18)
        btnNb4 = self._arrtk.createButton(self.__fclavier,text="4", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("4"),width=36,height=36,conerRadus=18)
        btnNb5 = self._arrtk.createButton(self.__fclavier,text="5", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("5"),width=36,height=36,conerRadus=18)
        btnNb6 = self._arrtk.createButton(self.__fclavier,text="6", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("6"),width=36,height=36,conerRadus=18)
        btnNb7 = self._arrtk.createButton(self.__fclavier,text="7", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("7"),width=36,height=36,conerRadus=18)
        btnNb8 = self._arrtk.createButton(self.__fclavier,text="8", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("8"),width=36,height=36,conerRadus=18)
        btnNb9 = self._arrtk.createButton(self.__fclavier,text="9", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("9"),width=36,height=36,conerRadus=18)
        btnPI = self._arrtk.createButton(self.__fclavier,text="PI", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("3.1415926535897932"))
        # operateur
        btnVirgule = self._arrtk.createButton(self.__fclavier,text=".", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("."),width=36,height=36,conerRadus=18)
        btnPuissanceDix = self._arrtk.createButton(self.__fclavier,text="10^", bg=self._btnColor, fg=self._btnTexteColor,
                                        command= lambda : self.__ecritureCarractere("*10**"),width=36,height=36,conerRadus=18)
        btnEgal = self._arrtk.createButton(self.__fclavier,text="=", bg=self._btnColor, fg=self._btnTexteColor,
                                command=self.__calcule)
        btnplus = self._arrtk.createButton(self.__fclavier,text="+", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("+"),width=36,height=36,conerRadus=18)
        btnMoin = self._arrtk.createButton(self.__fclavier,text="-", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("-"),width=36,height=36,conerRadus=18)
        btnFois = self._arrtk.createButton(self.__fclavier,text="*", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("*"),width=36,height=36,conerRadus=18)
        btnDiviser = self._arrtk.createButton(self.__fclavier,text="/", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("/"),width=36,height=36,conerRadus=18)
        btnParenthese1 = self._arrtk.createButton(self.__fclavier,text="(", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("("),width=36,height=36,conerRadus=18)
        btnParenthese2 = self._arrtk.createButton(self.__fclavier,text=")", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere(")"),width=36,height=36,conerRadus=18)
        btnRacine = self._arrtk.createButton(self.__fclavier,text="sqrt", bg=self._btnColor, fg=self._btnTexteColor,
                                  command= lambda : self.__ecritureCarractere("math.sqrt("),width=36,height=36,conerRadus=18)
        btnExposant = self._arrtk.createButton(self.__fclavier,text="^", bg=self._btnColor, fg=self._btnTexteColor,
                                    command= lambda : self.__ecritureCarractere("**"),width=36,height=36,conerRadus=18)
        btnExpodentiel = self._arrtk.createButton(self.__fclavier,text="e^", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("math.exp("),width=36,height=36,conerRadus=18)
        btnLN = self._arrtk.createButton(self.__fclavier,text="ln()", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("math.log(x,math.e)"),width=36,height=36,conerRadus=18)
        btnLOG = self._arrtk.createButton(self.__fclavier,text="log()", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("math.log(x,10)"),width=36,height=36,conerRadus=18)
        #cercle trigo
        btnSIN = self._arrtk.createButton(self.__fclavier,text="SIN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.sin("),width=50,height=36,conerRadus=18)
        btnCOS = self._arrtk.createButton(self.__fclavier,text="COS", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.cos("),width=50,height=36,conerRadus=18)
        btnTAN = self._arrtk.createButton(self.__fclavier,text="TAN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda :self.__ecritureCarractere("math.tan("),width=50,height=36,conerRadus=18)
        btnARCSIN = self._arrtk.createButton(self.__fclavier,text="ARCSIN", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.asin("),width=50,height=36,conerRadus=18)
        btnARCCOS = self._arrtk.createButton(self.__fclavier,text="ARCCOS", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.acos("),width=50,height=36,conerRadus=18)
        btnARCTAN = self._arrtk.createButton(self.__fclavier,text="ARCTAN", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.cos("),width=50,height=36,conerRadus=18)
        #autre
        btnClear = self._arrtk.createButton(self.__fclavier,text="C",command=self.__clearAll,
                                                   bg=self._btnColor, fg=self._btnTexteColor,
                                                   width=50,height=36,conerRadus=18)
        btnSuppr = self._arrtk.createButton(self.__fclavier,text="SUPPR",bg=self._btnColor,
                                                   fg=self._btnTexteColor,command=self.__suppr,width=50,
                                                   height=36,conerRadus=18)
        #btn fonction special
        btnAngle = self._arrtk.createButton(self.__fclavier, text="Randian en degres", ppolice="Arial", ptaille=15
                                                   , bg=self._btnColor, fg=self._btnTexteColor, command=self.__convertiseurDegRad)
        btnPythagore = self._arrtk.createButton(self.__fclavier, text="Theoreme de pythagore", ppolice="Arial", ptaille=15
                                                       , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modePythagore)
        btnNbComplex = self._arrtk.createButton(self.__fclavier, text="Nombre Complex", ppolice="Arial", ptaille=15
                                                       , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modeComplex)
        #btn nb complex
        self.__btnEgalComplex = self._arrtk.createButton(self.__fResultatComplex,text="="
                                       ,command= lambda : self.__calculeComplex())
        self.__btnplusComplex = self._arrtk.createButton(self.__foperateurComplex,text="+"
                                       ,command= lambda : self.__setOperateurComplex("+"))
        self.__btnMoinComplex = self._arrtk.createButton(self.__foperateurComplex,text="-"
                                       ,command= lambda : self.__setOperateurComplex("-"))
        self.__btnFoisComplex = self._arrtk.createButton(self.__foperateurComplex,text="*"
                                       ,command= lambda : self.__setOperateurComplex("*"))
        self.__btnDiviserComplex = self._arrtk.createButton(self.__foperateurComplex,text="/"
                                          ,command= lambda : self.__setOperateurComplex("/"))
        self.__btnCancelComplex = self._arrtk.createButton(self.__fnbComplex, text="Annuler", ppolice="Arial", ptaille=15
                                                           , bg=self._btnColor, fg=self._btnTexteColor, command=self.__resetOperateurComplex)
        self.__btnRetourComplex = self._arrtk.createButton(self.__fnbComplex, text="Retour", ppolice="Arial", ptaille=15
                                                           , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modeCalcule)
        #bouton pythagore
        self.__btnReciproque = self._arrtk.createButton(self.__fchooseCal, text="Reciproque", bg=self._btnColor
                                                        , fg=self._btnTexteColor, command=lambda : self.__calculePythagore(2), ppolice="Arial", ptaille=15)
        self.__btnTheoreme = self._arrtk.createButton(self.__fchooseCal, text="Theoreme"
                                                      , bg=self._btnColor, fg=self._btnTexteColor, command=lambda : self.__calculePythagore(1), ppolice="Arial", ptaille=15)
        self.__btnRetourPythagore = self._arrtk.createButton(self.__fpythagore, text="Retour", ppolice="Arial", ptaille=15
                                                             , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modeCalcule)
        #label
        self.__labelPlus = self._arrtk.createLabel(self.__foperateurComplex,text="+")
        self.__labelMois = self._arrtk.createLabel(self.__foperateurComplex,text="-")
        self.__labelDiviser = self._arrtk.createLabel(self.__foperateurComplex,text="/")
        self.__labelFois = self._arrtk.createLabel(self.__foperateurComplex,text="*")
        self.__affichageHistorique = self._arrtk.createLabel(self.__fhistorique, text="Historique :"
                                                             ,width=30, ppolice="Arial", ptaille=20)
        self.__affichageComplexOut = self._arrtk.createLabel(self.__fResultatComplex,width=42,ppolice="Arial", ptaille=15,bg="grey",fg="white")
        self.__complex1L = self._arrtk.createLabel(self.__fcomplex1, text="j", ppolice="Arial", ptaille=15, bg=self._btnColor)
        self.__complex2L = self._arrtk.createLabel(self.__fcomplex2, text="j", ppolice="Arial", ptaille=15, bg=self._btnColor)
        self.__affichagePythagoreOut =  self._arrtk.createLabel(self.__fpythagore,width=42,ppolice="Arial", ptaille=15,bg="grey",fg="white")
        #affichage 
        # Nombre complex
        self.__zoneComplex1A.pack(side="left")
        self.__complex1L.pack(side="right")
        self.__zoneComplex1B.pack(side="right")
        self.__zoneComplex2A.pack(side="left")
        self.__complex2L.pack(side="right")
        self.__zoneComplex2B.pack(side="right") 
        self.__btnplusComplex.pack(side="left")
        self.__btnMoinComplex.pack(side="left")
        self.__btnFoisComplex.pack(side="left")
        self.__btnDiviserComplex.pack(side="left")
        # Nombre Pythagore
        self.__btnReciproque.place(relx=1, rely=1, anchor='se')
        self.__btnTheoreme.place(relx=0, rely=1, anchor='sw')
        self.__zonePythagore1.place(relx=0, rely=1, anchor='sw')  
        self.__zonePythagore2.place(relx=1, rely=1, anchor='se') 
        # Clavier
        btnNb0

        
        self.__fhistorique.pack(side="left",fill="both", expand=True)
        self.__modeCalcule()
        # Affichage 
        self.__labelTitrePythagore.place(relx=0.5, rely=0.0, anchor="n") 
        #affichage historique
        self.__affichageHistorique.place(x=0,y=0)
        #verrifaction de carratere taper
        self.__zoneCalcule.bind("<KeyPress-Return>",self.__enterPressed)
        self.__zoneCalcule.bind("<KeyPress>",self.__carractereInterdit)
    
    def __modeCalcule(self):
        self.__fnbComplex.pack_forget()
        self.__fpythagore.pack_forget()
        self.__updateCalculatrice() 
        self.__fclavier.pack(side="bottom",anchor="sw")
        self.__zoneCalcule.pack(side="top",anchor="nw") 

        
    def __updateCalculatrice(self):
        self._screen.update()
    
    def __carractereInterdit(self,event):
        carractereSpeciaux = "'_,?;§!ùµ*£$¤¨@ç|~&²¹#`\°"
        carractereSpeciaux2 = '"'
        if event.char.isalpha():
            return "break"
        elif event.char in carractereSpeciaux:
            return "break"
        elif event.char in carractereSpeciaux2:
            return "break"
        
    def __enterPressed(self,event):
        self.__calcule()
        return "break"
        
    def __ecritureCarractere(self,crc:str):
        self.__zoneCalcule.insert("end",crc)
        
    def __clearAll(self):
        self.__zoneCalcule.delete("1.0",END)
        
    def __suppr(self):
        # Récupérer le contenu actuel du widget Text
        contenu = self.__zoneCalcule.get("1.0", "end-1c")

        if contenu:
            # Supprimer le dernier caractère
            contenu = contenu[:-1]

            # Mettre à jour le widget Text avec le nouveau contenu
            self.__zoneCalcule.delete("1.0", "end")
            self.__zoneCalcule.insert("1.0", contenu)
            
    def __calcule(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        contenu = contenu.replace(" ", "")
        try:
            resultat = eval(contenu)
            self.__affichageHistorique.configure(text="Historique :\n" + str(contenu) + " = " + str(resultat))
            self.__affichageHistorique.update()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(resultat))
        except Exception as e:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
            
    def __modeComplex(self):
        self.__fclavier.pack_forget()
        self.__zoneCalcule.pack_forget()
        self.__labelTitreNbComplex.place(relx=0.5, rely=0.0, anchor="n") 
        self.__fnbComplex.pack(side="left")  
        self.__fcomplex1.place(relx=0.5, rely=0.0, anchor="n")
        self.__foperateurComplex.place(relx=0.5, rely=0.5, anchor="center")
        self.__fcomplex2.place(relx=0.5, rely=1.0, anchor="s")
        self.__fCalculeComplex.place(x=0,y=80)
        self.__fResultatComplex.place(x=0,y=220)
        self.__btnEgalComplex.place(relx=0.5, rely=0.0, anchor="n")
        self.__affichageComplexOut.place(relx=0.5, rely=1.0, anchor="s")
        self.__btnCancelComplex.place(x=(500-self.__btnCancelComplex.winfo_reqwidth()),y=(500-self.__btnCancelComplex.winfo_reqheight()))
        self.__btnRetourComplex.place(x=0,y=(500-self.__btnCancelComplex.winfo_reqheight()))
        self.__affichageComplexOut.configure(text="")
        self.__zoneComplex1A.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex1B.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex2A.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex2B.bind("<KeyPress>", self.__carractereInterdit)             
    
    
    def __setOperateurComplex(self,operateur:str):
        self.__operateurChooseComplex = operateur
        self.__btnplusComplex.pack_forget()
        self.__btnMoinComplex.pack_forget()
        self.__btnFoisComplex.pack_forget()
        self.__btnDiviserComplex.pack_forget()
        self.__foperateurComplex.place_forget()
        if self.__operateurChooseComplex == "+":
            self.__labelPlus.pack()
        else :
            if self.__operateurChooseComplex == "-":
                self.__labelMois.pack()
            else :
                if self.__operateurChooseComplex == "*":
                    self.__labelFois.pack()
                else :
                    if self.__operateurChooseComplex== "/":
                        self.__labelDiviser.pack()
        self.__foperateurComplex.update()
        self.__foperateurComplex.place(x=((self.__fnbComplex.winfo_reqwidth()-self.__foperateurComplex.winfo_reqwidth())//2),y=75)
        
    def __resetOperateurComplex(self):
        if self.__operateurChooseComplex == "":
            self.__operateurChooseComplex = ""
        else :
            self.__operateurChooseComplex = ""
            self.__labelPlus.pack_forget()
            self.__labelMois.pack_forget()
            self.__labelFois.pack_forget()
            self.__labelDiviser.pack_forget()
            self.__foperateurComplex.place_forget()
            self.__btnplusComplex.pack(side="left")
            self.__btnMoinComplex.pack(side="left")
            self.__btnFoisComplex.pack(side="left")
            self.__btnDiviserComplex.pack(side="left")
            self.__foperateurComplex.update()
            self.__foperateurComplex.place(x=((self.__fnbComplex.winfo_reqwidth()-self.__foperateurComplex.winfo_reqwidth())//2),y=75)
        
        
    def __calculeComplex(self):
        nb1A = self.__zoneComplex1A.get()
        nb1B = self.__zoneComplex1B.get()
        nb2A = self.__zoneComplex2A.get()
        nb2B = self.__zoneComplex2B.get()
        self.__zoneComplex1A.delete(0,END)
        self.__zoneComplex1B.delete(0,END)
        self.__zoneComplex2A.delete(0,END)
        self.__zoneComplex2B.delete(0,END)
        if self.__operateurChooseComplex == "" or nb1A.strip() == "" or nb1B.strip() == "" or nb2A.strip() == "" or nb2B.strip() == "" :
            showerror("Assistant","Il a une erreur qui empéche de faire le calcule")
            self.__affichageComplexOut.configure(text="Erreur")
        else :
            calcule = CalculeNbComplexe(int(nb1A),int(nb1B),int(nb2A),int(nb2B))
            if self.__operateurChooseComplex == "+":
                nb1 = calcule.recuperationNb1()
                nb2 = calcule.recuperationNb2()
                resultat = calcule.aditionNbComplex()
                self.__affichageHistorique.configure(text="Historique :\n" + nb1+"+"+nb2 + " = " + str(resultat))
            else :
                if self.__operateurChooseComplex == "-":
                    nb1 = calcule.recuperationNb1()
                    nb2 = calcule.recuperationNb2()
                    resultat = calcule.soustrationNbComplex()
                    self.__affichageHistorique.configure(text="Historique :\n" + nb1+"-"+nb2 + " = " + str(resultat))
                else :
                    if self.__operateurChooseComplex == "*":
                        nb1 = calcule.recuperationNb1()
                        nb2 = calcule.recuperationNb2()
                        resultat = calcule.multiplicationNbComplex()
                        self.__affichageHistorique.configure(text="Historique :\n" + nb1+"*"+nb2 + " = " + str(resultat))
                    else :
                        if self.__operateurChooseComplex == "/":
                            nb1 = calcule.recuperationNb1()
                            nb2 = calcule.recuperationNb2()
                            resultat = calcule.divisionNbComplex()
                            self.__affichageHistorique.configure(text="Historique :\n" + nb1+"/"+nb2 + " = " + str(resultat))
            self.__resetOperateurComplex()
            self.__affichageComplexOut.configure(text=str(resultat))
    

    def __modePythagore(self):
        self.__fclavier.pack_forget()
        self.__zoneCalcule.pack_forget()
        self.__fpythagore.pack(side="right")  
        self.__fnbPythagore.place(relx=0.5, rely=0.0, anchor="n") 
        self.__fchooseCal.place(x=(self.__fpythagore.winfo_reqwidth() - self.__fchooseCal.winfo_reqwidth()) // 2,y=125)
        self.__affichagePythagoreOut.place(x=15,y=225) 
        self.__btnRetourPythagore.place(x=0,y=(500-self.__btnRetourPythagore.winfo_reqheight()))
        self.__affichagePythagoreOut.configure(text="")
        
    def __calculePythagore(self,mode):
        nb1 = self.__zonePythagore1.get()
        nb2 = self.__zonePythagore2.get()
        if nb1.strip() == "" or nb2.strip() == "":
            self.__affichagePythagoreOut.configure(text="Erreur")
        else :
            calcule = Pythagore(int(nb1),int(nb2))
            if mode == 1:
                resultat = str(calcule.theoreme())
                sortieCalcule = calcule.recuperationCalcule()
                self.__affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
            else :
                if mode == 2:
                    if int(nb1) <= int(nb2) :
                        self.__affichagePythagoreOut.configure(text="Erreur")
                    else :
                        resultat = str(calcule.reciproque())
                        sortieCalcule = calcule.recuperationCalcule()
                        self.__affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
    
    def __convertiseurDegRad(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        if contenu ==  "":
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        else :
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(math.degrees(int(contenu))))
                

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