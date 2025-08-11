from tkinter import PhotoImage, END
import customtkinter as ctk
from tkinter.messagebox import showerror
from gui.guibase import GuiBase,gestionnaire
import math

class GUICalculatrice(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Calculatrice")
        self.__operateurChooseComplex = ""

    def _mainframe(self):
        self._screen.minsize(500,500)
        self._screen.grid_rowconfigure(0, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        #cadre
        # Partie calculatrice
        self.__mainView = self._arrtk.createFrame(self._screen)
        fclavier = self._arrtk.createFrame(self.__mainView)
        # Partie historique
        self.__fhistorique = self._arrtk.createFrame(self._screen)

        # Configuration des frame
        fclavier.grid_columnconfigure(0, weight=1, uniform="col")
        fclavier.grid_columnconfigure(1, weight=1, uniform="col")
        fclavier.grid_columnconfigure(2, weight=1, uniform="col")
        fclavier.grid_columnconfigure(3, weight=1, uniform="col")
        fclavier.grid_columnconfigure(4, weight=1, uniform="col")
        fclavier.grid_columnconfigure(5, weight=1, uniform="col")
        fclavier.grid_columnconfigure(6, weight=1, uniform="col")

        fclavier.grid_rowconfigure(0, weight=1)
        fclavier.grid_rowconfigure(1, weight=1)
        fclavier.grid_rowconfigure(2, weight=1)
        fclavier.grid_rowconfigure(3, weight=1)
        fclavier.grid_rowconfigure(4, weight=1)
        fclavier.grid_rowconfigure(5, weight=1)
        fclavier.grid_rowconfigure(6, weight=1)

        self.__mainView.grid_rowconfigure(0, weight=1)  # la zone texte prend de la place en vertical
        self.__mainView.grid_rowconfigure(1, weight=2)  # la zone clavier peut prendre plus
        self.__mainView.grid_columnconfigure(0, weight=1)

        self.__fhistorique.grid_columnconfigure(0, weight=1)
        self.__fhistorique.grid_rowconfigure(0, weight=1)
        self.__fhistorique.grid_rowconfigure(1, weight=3)

        # widget
        self.__zoneCalcule = self._arrtk.createText(self.__mainView, ptaille=30,
                                                    ppolice="Arial", pstyle="bold", center=True)
        #touche clavier
        #chiffre
        btnNb0 = self._arrtk.createButton(fclavier,text="0", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("0"),pstyle="bold",ptaille=20)
        btnNb1 = self._arrtk.createButton(fclavier,text="1", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("1"),pstyle="bold",ptaille=20)
        btnNb2 = self._arrtk.createButton(fclavier,text="2", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("2"),pstyle="bold",ptaille=20)
        btnNb3 = self._arrtk.createButton(fclavier,text="3", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("3"),pstyle="bold",ptaille=20)
        btnNb4 = self._arrtk.createButton(fclavier,text="4", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("4"),pstyle="bold",ptaille=20)
        btnNb5 = self._arrtk.createButton(fclavier,text="5", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("5"),pstyle="bold",ptaille=20)
        btnNb6 = self._arrtk.createButton(fclavier,text="6", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("6"),pstyle="bold",ptaille=20)
        btnNb7 = self._arrtk.createButton(fclavier,text="7", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("7"),pstyle="bold",ptaille=20)
        btnNb8 = self._arrtk.createButton(fclavier,text="8", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("8"),pstyle="bold",ptaille=20)
        btnNb9 = self._arrtk.createButton(fclavier,text="9", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("9"),pstyle="bold",ptaille=20)
        btnPI = self._arrtk.createButton(fclavier,text="PI", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("3.1415926535897932"),pstyle="bold",ptaille=20)
        # operateur
        btnVirgule = self._arrtk.createButton(fclavier,text=".", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("."),pstyle="bold",ptaille=20)
        btnPuissanceDix = self._arrtk.createButton(fclavier,text="10^", bg=self._btnColor, fg=self._btnTexteColor,
                                        command= lambda : self.__ecritureCarractere("*10**"),pstyle="bold",ptaille=20)
        btnEgal = self._arrtk.createButton(fclavier,text="=", bg=self._btnColor, fg=self._btnTexteColor,
                                command=self.__calcule,pstyle="bold",ptaille=30)
        btnplus = self._arrtk.createButton(fclavier,text="+", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("+"),pstyle="bold",ptaille=30)
        btnMoin = self._arrtk.createButton(fclavier,text="-", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("-"),pstyle="bold",ptaille=30)
        btnFois = self._arrtk.createButton(fclavier,text="*", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("*"),pstyle="bold",ptaille=30)
        btnDiviser = self._arrtk.createButton(fclavier,text="/", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("/"),pstyle="bold",ptaille=30)
        btnParenthese1 = self._arrtk.createButton(fclavier,text="(", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("("),pstyle="bold",ptaille=30)
        btnParenthese2 = self._arrtk.createButton(fclavier,text=")", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere(")"),pstyle="bold",ptaille=30)
        btnRacine = self._arrtk.createButton(fclavier,text="sqrt", bg=self._btnColor, fg=self._btnTexteColor,
                                  command= lambda : self.__ecritureCarractere("math.sqrt("),pstyle="bold",ptaille=20)
        btnExposant = self._arrtk.createButton(fclavier,text="^", bg=self._btnColor, fg=self._btnTexteColor,
                                    command= lambda : self.__ecritureCarractere("**"),pstyle="bold",ptaille=30)
        btnExpodentiel = self._arrtk.createButton(fclavier,text="e^", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("math.exp("),pstyle="bold",ptaille=30)
        btnLN = self._arrtk.createButton(fclavier,text="ln", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("math.log(x,math.e)"),pstyle="bold",ptaille=20)
        btnLOG = self._arrtk.createButton(fclavier,text="log", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("math.log(x,10)"),pstyle="bold",ptaille=20)
        #cercle trigo
        btnSIN = self._arrtk.createButton(fclavier,text="SIN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.sin("),pstyle="bold",ptaille=20)
        btnCOS = self._arrtk.createButton(fclavier,text="COS", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=20)
        btnTAN = self._arrtk.createButton(fclavier,text="TAN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda :self.__ecritureCarractere("math.tan("),pstyle="bold",ptaille=20)
        btnARCSIN = self._arrtk.createButton(fclavier,text="SIN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.asin("),pstyle="bold",ptaille=18)
        btnARCCOS = self._arrtk.createButton(fclavier,text="COS-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.acos("),pstyle="bold",ptaille=18)
        btnARCTAN = self._arrtk.createButton(fclavier,text="TAN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=18)
        #autre
        btnClear = self._arrtk.createButton(fclavier,text="C",command=self.__clearAll,
                                                   bg=self._btnColor, fg=self._btnTexteColor,pstyle="bold",ptaille=20)
        btnSuppr = self._arrtk.createButton(fclavier,text="CE",bg=self._btnColor,
                                                   fg=self._btnTexteColor,command=self.__suppr,pstyle="bold",ptaille=20)
        #btn fonction special
        btnAngle = self._arrtk.createButton(fclavier, text="Randian en degres", ppolice="Arial",pstyle="bold",ptaille=14
                                                   , bg=self._btnColor, fg=self._btnTexteColor, command=self.__convertiseurDegRad)
        btnPythagore = self._arrtk.createButton(fclavier, text="Theoreme de pythagore", ppolice="Arial",pstyle="bold",ptaille=16
                                                       , bg=self._btnColor, fg=self._btnTexteColor)
        btnNbComplex = self._arrtk.createButton(fclavier, text="Nombre Complex", ppolice="Arial",pstyle="bold",ptaille=15
                                                     , bg=self._btnColor, fg=self._btnTexteColor)
        btnHist = self._arrtk.createButton(fclavier, text="Historique", ppolice="Arial",pstyle="bold",ptaille=20
                                          , bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewHistorique)

        # Frame Historique
        labelHist = self._arrtk.createLabel(self.__fhistorique, text="Historique",
                                            ppolice="Arial", ptaille=20)
        self.__affichageHistorique = self._arrtk.createText(self.__fhistorique)
        scroll_y = ctk.CTkScrollbar(self.__fhistorique, orientation="vertical", command=self.__affichageHistorique.yview)
        self.__affichageHistorique.configure(state='disabled')
        btnBackHist = self._arrtk.createButton(self.__fhistorique, text="Retour", ppolice="Arial", ptaille=25,
                                               bg=self._btnColor, fg=self._btnTexteColor,
                                               command=self.__viewCalcule)

        # Affichage des widgets
        # Clavier
        btnClear.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        btnSuppr.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        btnParenthese1.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        btnParenthese2.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
        btnDiviser.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)
        btnFois.grid(row=0, column=5, sticky="nsew", padx=2, pady=2)
        btnExposant.grid(row=0, column=6, sticky="nsew", padx=2, pady=2)
        btnRacine.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        btnPuissanceDix.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        btnPI.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        btnVirgule.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
        btnSIN.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
        btnCOS.grid(row=1, column=5, sticky="nsew", padx=2, pady=2)
        btnTAN.grid(row=1, column=6, sticky="nsew", padx=2, pady=2)
        btnNb7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        btnNb8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        btnNb9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        btnMoin.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        btnARCSIN.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
        btnARCCOS.grid(row=2, column=5, sticky="nsew", padx=2, pady=2)
        btnARCTAN.grid(row=2, column=6, sticky="nsew", padx=2, pady=2)
        btnNb4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        btnNb5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        btnNb6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        btnplus.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        btnExpodentiel.grid(row=3, column=4, sticky="nsew", padx=2, pady=2)
        btnLN.grid(row=3, column=5, sticky="nsew", padx=2, pady=2)
        btnLOG.grid(row=3, column=6, sticky="nsew", padx=2, pady=2)
        btnNb1.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        btnNb2.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        btnNb3.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        btnEgal.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=2, pady=2)
        btnHist.grid(row=4, column=4, rowspan=2, columnspan=3, sticky="nsew", padx=2, pady=2)
        btnNb0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        btnAngle.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=2, pady=4)
        btnPythagore.grid(row=6, column=2, columnspan=3, sticky="nsew", padx=2, pady=4)
        btnNbComplex.grid(row=6, column=5, columnspan=2, sticky="nsew", padx=2, pady=4)
        # affichage historique
        labelHist.grid(row=0, column=0)
        self.__affichageHistorique.grid(row=1, column=0, sticky="nsew", padx=(10, 0), pady=10)
        scroll_y.grid(row=1, column=1, sticky="ns", padx=(0, 10), pady=10)
        btnBackHist.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        # Affichage MainView
        self.__zoneCalcule.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        fclavier.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))
        self.__viewCalcule()
        # Configuration de la zone de calcul
        self.__zoneCalcule.bind("<KeyPress-Return>",self.__enterPressed)
        self.__zoneCalcule.bind("<KeyPress>",self.__carractereInterdit)

    
    def __viewCalcule(self):
        self.__fhistorique.grid_forget()
        self.__mainView.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __viewHistorique(self):
        self.__mainView.grid_forget()
        self.__fhistorique.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __addHistorique(self,texte:str):
        """Ajoute un texte à l'historique de la calculatrice."""
        if not texte:
            return
        self.__affichageHistorique.configure(state='normal')
        self.__affichageHistorique.insert(END, texte + "\n")
        self.__affichageHistorique.see(END)
        self.__affichageHistorique.configure(state='disabled')

    
    def __carractereInterdit(self,event):
        carractereSpeciaux = "'_,?;§!ùµ*£$¤¨@ç|~&²¹#`\°"
        carractereSpeciaux2 = '"'
        if event.char.isalpha():
            return "break"
        elif event.char in carractereSpeciaux:
            return "break"
        elif event.char in carractereSpeciaux2:
            return "break"
        self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        
    def __enterPressed(self,event):
        self.__calcule()
        return "break"
        
    def __ecritureCarractere(self,crc:str):
        self.__zoneCalcule.insert("end",crc)
        self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        self._screen.update()
        
    def __clearAll(self):
        self.__zoneCalcule.delete("1.0",END)
        self._screen.update()
        
    def __suppr(self):
        # Récupérer le contenu actuel du widget Text
        contenu = self.__zoneCalcule.get("1.0", "end-1c")

        if contenu:
            # Supprimer le dernier caractère
            contenu = contenu[:-1]

            # Mettre à jour le widget Text avec le nouveau contenu
            self.__zoneCalcule.delete("1.0", "end")
            self.__zoneCalcule.insert("1.0", contenu)
            self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        self._screen.update()
            
    def __calcule(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        contenu = contenu.replace(" ", "")
        try:
            resultat = eval(contenu)
            self.__affichageHistorique.update()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(resultat))
            self.__addHistorique(contenu + " = " + str(resultat))
        except Exception as e:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        self._screen.update()

    def __convertiseurDegRad(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        if contenu == "":
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        else:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(math.degrees(int(contenu))))
        self._screen.update()
    """
    def __modeComplex(self):
        self.__zoneCalcule.pack_forget()
        self.__labelTitreNbComplex.place(relx=0.5, rely=0.0, anchor="n") 
        self.__fnbComplex.pack(side="left")  
        fcomplex1.place(relx=0.5, rely=0.0, anchor="n")
        foperateurComplex.place(relx=0.5, rely=0.5, anchor="center")
        fcomplex2.place(relx=0.5, rely=1.0, anchor="s")
        fCalculeComplex.place(x=0,y=80)
        fResultatComplex.place(x=0,y=220)
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
        foperateurComplex.place_forget()
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
        foperateurComplex.update()
        foperateurComplex.place(x=((self.__fnbComplex.winfo_reqwidth()-foperateurComplex.winfo_reqwidth())//2),y=75)
        
    def __resetOperateurComplex(self):
        if self.__operateurChooseComplex == "":
            self.__operateurChooseComplex = ""
        else :
            self.__operateurChooseComplex = ""
            self.__labelPlus.pack_forget()
            self.__labelMois.pack_forget()
            self.__labelFois.pack_forget()
            self.__labelDiviser.pack_forget()
            foperateurComplex.place_forget()
            self.__btnplusComplex.pack(side="left")
            self.__btnMoinComplex.pack(side="left")
            self.__btnFoisComplex.pack(side="left")
            self.__btnDiviserComplex.pack(side="left")
            foperateurComplex.update()
            foperateurComplex.place(x=((self.__fnbComplex.winfo_reqwidth()-foperateurComplex.winfo_reqwidth())//2),y=75)
        
        
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
    
    """