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
        self.__fclavier = self._arrtk.createFrame(self._screen,bg="red")
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

        # Configuration des frame
        self.__fclavier.grid_columnconfigure(0, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(1, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(2, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(3, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(4, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(5, weight=1, uniform="col")
        self.__fclavier.grid_columnconfigure(6, weight=1, uniform="col")

        self.__fclavier.grid_rowconfigure(0, weight=1)
        self.__fclavier.grid_rowconfigure(1, weight=1)
        self.__fclavier.grid_rowconfigure(2, weight=1)
        self.__fclavier.grid_rowconfigure(3, weight=1)
        self.__fclavier.grid_rowconfigure(4, weight=1)
        self.__fclavier.grid_rowconfigure(5, weight=1)
        self.__fclavier.grid_rowconfigure(6, weight=1)
        #touche clavier
        #chiffre
        btnNb0 = self._arrtk.createButton(self.__fclavier,text="0", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("0"),pstyle="bold",ptaille=20)
        btnNb1 = self._arrtk.createButton(self.__fclavier,text="1", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("1"),pstyle="bold",ptaille=20)
        btnNb2 = self._arrtk.createButton(self.__fclavier,text="2", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("2"),pstyle="bold",ptaille=20)
        btnNb3 = self._arrtk.createButton(self.__fclavier,text="3", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("3"),pstyle="bold",ptaille=20)
        btnNb4 = self._arrtk.createButton(self.__fclavier,text="4", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("4"),pstyle="bold",ptaille=20)
        btnNb5 = self._arrtk.createButton(self.__fclavier,text="5", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("5"),pstyle="bold",ptaille=20)
        btnNb6 = self._arrtk.createButton(self.__fclavier,text="6", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("6"),pstyle="bold",ptaille=20)
        btnNb7 = self._arrtk.createButton(self.__fclavier,text="7", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("7"),pstyle="bold",ptaille=20)
        btnNb8 = self._arrtk.createButton(self.__fclavier,text="8", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("8"),pstyle="bold",ptaille=20)
        btnNb9 = self._arrtk.createButton(self.__fclavier,text="9", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("9"),pstyle="bold",ptaille=20)
        btnPI = self._arrtk.createButton(self.__fclavier,text="PI", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("3.1415926535897932"),pstyle="bold",ptaille=20)
        # operateur
        btnVirgule = self._arrtk.createButton(self.__fclavier,text=".", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("."),pstyle="bold",ptaille=20)
        btnPuissanceDix = self._arrtk.createButton(self.__fclavier,text="10^", bg=self._btnColor, fg=self._btnTexteColor,
                                        command= lambda : self.__ecritureCarractere("*10**"),pstyle="bold",ptaille=20)
        btnEgal = self._arrtk.createButton(self.__fclavier,text="=", bg=self._btnColor, fg=self._btnTexteColor,
                                command=self.__calcule,pstyle="bold",ptaille=30)
        btnplus = self._arrtk.createButton(self.__fclavier,text="+", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("+"),pstyle="bold",ptaille=30)
        btnMoin = self._arrtk.createButton(self.__fclavier,text="-", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("-"),pstyle="bold",ptaille=30)
        btnFois = self._arrtk.createButton(self.__fclavier,text="*", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("*"),pstyle="bold",ptaille=30)
        btnDiviser = self._arrtk.createButton(self.__fclavier,text="/", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("/"),pstyle="bold",ptaille=30)
        btnParenthese1 = self._arrtk.createButton(self.__fclavier,text="(", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("("),pstyle="bold",ptaille=30)
        btnParenthese2 = self._arrtk.createButton(self.__fclavier,text=")", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere(")"),pstyle="bold",ptaille=30)
        btnRacine = self._arrtk.createButton(self.__fclavier,text="sqrt", bg=self._btnColor, fg=self._btnTexteColor,
                                  command= lambda : self.__ecritureCarractere("math.sqrt("),pstyle="bold",ptaille=20)
        btnExposant = self._arrtk.createButton(self.__fclavier,text="^", bg=self._btnColor, fg=self._btnTexteColor,
                                    command= lambda : self.__ecritureCarractere("**"),pstyle="bold",ptaille=30)
        btnExpodentiel = self._arrtk.createButton(self.__fclavier,text="e^", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("math.exp("),pstyle="bold",ptaille=30)
        btnLN = self._arrtk.createButton(self.__fclavier,text="ln", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("math.log(x,math.e)"),pstyle="bold",ptaille=20)
        btnLOG = self._arrtk.createButton(self.__fclavier,text="log", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("math.log(x,10)"),pstyle="bold",ptaille=20)
        #cercle trigo
        btnSIN = self._arrtk.createButton(self.__fclavier,text="SIN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.sin("),pstyle="bold",ptaille=20)
        btnCOS = self._arrtk.createButton(self.__fclavier,text="COS", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=20)
        btnTAN = self._arrtk.createButton(self.__fclavier,text="TAN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda :self.__ecritureCarractere("math.tan("),pstyle="bold",ptaille=20)
        btnARCSIN = self._arrtk.createButton(self.__fclavier,text="SIN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.asin("),pstyle="bold",ptaille=18)
        btnARCCOS = self._arrtk.createButton(self.__fclavier,text="COS-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.acos("),pstyle="bold",ptaille=18)
        btnARCTAN = self._arrtk.createButton(self.__fclavier,text="TAN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=18)
        #autre
        btnClear = self._arrtk.createButton(self.__fclavier,text="C",command=self.__clearAll,
                                                   bg=self._btnColor, fg=self._btnTexteColor,pstyle="bold",ptaille=20)
        btnSuppr = self._arrtk.createButton(self.__fclavier,text="CE",bg=self._btnColor,
                                                   fg=self._btnTexteColor,command=self.__suppr,pstyle="bold",ptaille=20)
        #btn fonction special
        btnAngle = self._arrtk.createButton(self.__fclavier, text="Randian en degres", ppolice="Arial",pstyle="bold",ptaille=14
                                                   , bg=self._btnColor, fg=self._btnTexteColor, command=self.__convertiseurDegRad)
        btnPythagore = self._arrtk.createButton(self.__fclavier, text="Theoreme de pythagore", ppolice="Arial",pstyle="bold",ptaille=16
                                                       , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modePythagore)
        btnNbComplex = self._arrtk.createButton(self.__fclavier, text="Nombre Complex", ppolice="Arial",pstyle="bold",ptaille=15
                                                     , bg=self._btnColor, fg=self._btnTexteColor, command=self.__modeComplex)
        btnHist = self._arrtk.createButton(self.__fclavier, text="Historique", ppolice="Arial",pstyle="bold",ptaille=20
                                          , bg=self._btnColor, fg=self._btnTexteColor)
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
        # --- Ligne 0 : édition / parenthèses / opérateurs rapides ---
        btnClear.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        btnSuppr.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        btnParenthese1.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)   # (
        btnParenthese2.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)   # )
        btnDiviser.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)   # /
        btnFois.grid(row=0, column=5, sticky="nsew", padx=2, pady=2)   # *
        btnExposant.grid(row=0, column=6, sticky="nsew", padx=2, pady=2)   # ^ -> **

        # --- Ligne 1 : racine / puissances / PI ---
        btnRacine.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)  # sqrt(
        btnPuissanceDix.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)  # 10^
        btnPI.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)  # PI
        btnVirgule.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)  # .
        btnSIN.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
        btnCOS.grid(row=1, column=5, sticky="nsew", padx=2, pady=2)
        btnTAN.grid(row=1, column=6, sticky="nsew", padx=2, pady=2)

        # --- Ligne 2 : 7 8 9 / trig inverse 1 ---
        btnNb7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        btnNb8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        btnNb9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        btnMoin.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)  # -
        btnARCSIN.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
        btnARCCOS.grid(row=2, column=5, sticky="nsew", padx=2, pady=2)
        btnARCTAN.grid(row=2, column=6, sticky="nsew", padx=2, pady=2)

        # --- Ligne 3 : 4 5 6 / logs ---
        btnNb4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        btnNb5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        btnNb6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        btnplus.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)  # +
        btnExpodentiel.grid(row=3, column=4, sticky="nsew", padx=2, pady=2)  # e^ -> math.exp(
        btnLN.grid(row=3, column=5, sticky="nsew", padx=2, pady=2)  # ln()
        btnLOG.grid(row=3, column=6, sticky="nsew", padx=2, pady=2)  # log()

        # --- Ligne 4 : 1 2 3 / opérateur = placé plus bas pour le style calculatrice ---
        btnNb1.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        btnNb2.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        btnNb3.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        btnEgal.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=2, pady=2)
        btnHist.grid(row=4, column=4, rowspan=2, columnspan=3, sticky="nsew", padx=2, pady=2)

        # Colonne fonctions (ligne 4 libre ici) -> rien à placer si tu veux laisser aéré
        btnNb0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)  # 0 plus large


        # --- Ligne 6 : boutons spéciaux (pieds de page) ---
        btnAngle.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=2, pady=4)
        btnPythagore.grid(row=6, column=2, columnspan=3, sticky="nsew", padx=2, pady=4)
        btnNbComplex.grid(row=6, column=5, columnspan=2, sticky="nsew", padx=2, pady=4)
        
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