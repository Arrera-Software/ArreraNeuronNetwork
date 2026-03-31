from librairy.arrera_tk import *
from gui.codehelp.CCHguiBase import*
from tkinter import colorchooser

class CCHcolorSelector(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Selecteur de couleur")

    def _mainframe(self):
        self._screen.maxsize(800, 500)
        self._screen.minsize(800, 500)
        self._screen.resizable(False, False)
        #fonction
        #cadre
        cadreNoir = aFrame(self._screen, fg_color="black", width=325, height=325)
        self.__cadreColor = aFrame(cadreNoir,fg_color="#ffffff",width=310,height=310)
        #label
        self.__labelIndicationCode = aLabel(self._screen, text="Code HTML : #ffffff \nCode RGB : (255,255,255)", justify="left")
        #declaration des bouton
        buttonSelection = aButton(self._screen, text="Selectionner la couleur",command=self.__selecteur)
        self.__buttonCopiHTLM = aButton(self._screen, text="Copier le code HTML")
        self.__buttonCopiRGB = aButton(self._screen, text="Copier le code RGB")
        #affichage
        self._arrtk.placeCenter(self.__cadreColor)
        cadreNoir.pack(side="right")
        self.__labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        self.__buttonCopiHTLM.place(x=15,y=235)
        self.__buttonCopiRGB.place(x=15,y=335)
        
    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur")
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__cadreColor.configure(fg_color=self.__colorHTLM)
        self.__buttonCopiHTLM.configure(command=self.__copieHTLM)
        self.__buttonCopiRGB.configure(command=self.__copieRGB)
        self.__labelIndicationCode.configure(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self._screen.clipboard_clear()
        self._screen.clipboard_append(self.__colorRGB)