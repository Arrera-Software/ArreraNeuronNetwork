from librairy.arrera_tk import *
from gui.codehelp.CCHguiBase import*
from tkinter import colorchooser

class CCHcolorSelector(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Selecteur de couleur")

    def _mainframe(self):

        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_rowconfigure(2, weight=0)
        self._screen.grid_columnconfigure(0, weight=1)

        #fonction
        #cadre
        f_main = aFrame(self._screen)

        # Cadre de couleur
        f_black = aFrame(f_main, fg_color="black", width=325, height=325)
        self.__f_color = aFrame(f_black, fg_color="#ffffff", width=310, height=310)

        # Autre carde
        f_header = aFrame(self._screen, height=50)
        f_btn = aFrame(f_main)
        f_footer = aFrame(self._screen, height=80)

        # Configuration des frame
        f_btn.grid_columnconfigure(0, weight=1)
        for i in range(7):
            if i % 2 == 0:
                f_btn.grid_rowconfigure(i, weight=1)
            else:  # lignes des boutons
                f_btn.grid_rowconfigure(i, weight=0)

        f_main.grid_columnconfigure(0, weight=0)
        f_main.grid_columnconfigure(1, weight=1)
        f_main.grid_rowconfigure(0, weight=1)

        #label
        #self.__labelIndicationCode = aLabel(self._screen, text="Code HTML : #ffffff \nCode RGB : (255,255,255)", justify="left")
        label_title = aLabel(f_header, text="Codehelp : Selecteur de couleur", anchor="center",font=("Roboto",30,"bold"))
        #declaration des bouton
        buttonSelection = aButton(f_btn, text="Selectionner la couleur",command=self.__selecteur)
        self.__buttonCopiHTLM = aButton(f_btn, text="Copier le code HTML")
        self.__buttonCopiRGB = aButton(f_btn, text="Copier le code RGB")

        #affichage
        f_header.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        f_main.grid(row=1, column=0, sticky="nsew")
        label_title.pack(expand=True)

        self.__f_color.placeCenter()

        f_black.grid(row=0, column=1, sticky="e", padx=20)

        f_btn.grid(row=0, column=0, sticky="nsw", padx=20)
        buttonSelection.grid(row=1, column=0, pady=10)
        self.__buttonCopiHTLM.grid(row=3, column=0, pady=10)
        self.__buttonCopiRGB.grid(row=5, column=0, pady=10)

        f_footer.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur")
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__f_color.configure(fg_color=self.__colorHTLM)
        self.__buttonCopiHTLM.configure(command=self.__copieHTLM)
        self.__buttonCopiRGB.configure(command=self.__copieRGB)
        #self.__labelIndicationCode.configure(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorRGB)