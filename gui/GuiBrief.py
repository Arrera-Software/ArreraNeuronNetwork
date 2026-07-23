from gui.guibase import *
import threading as th

# Design de la page

"""
# Morning Brief et Afternoon Brief
+-----------------------------------------------------------------------------+
| HH:MM - DATE                                    NAME_ASSISTANT : TYPE BRIEF |
+-------------------------+---------------------------------------------------+
| BLOC 1                  | BLOC 2                                            |
|                         |                                                   |
|                         |                                                   |
|                         |                                                   |
|                         |                                                   |
| ----------------------- |                                                   |
| BLOC 3                  |                                                   |
|                         |                                                   |
|                         |                                                   |
|                         |                                                   |
|                         |                                                   |
|                         |                                                   |
+-------------------------+---------------------------------------------------+

## Morning Brief 

- BLOC 1: Meteo prevu dans le journer
- BLOC 2: Tache du jour 
- BLOC 3: Actu 

## Afternoon Brief

- BLOC 1: Meteo actuel et prevu dans l'apres midi
- BLOC 2: Tache 
- BLOC 3: Actu  

# Evening brief

+-----------------------------------------------------------------------------+
| HH:MM - DATE                                    NAME_ASSISTANT : TYPE BRIEF |
+------------------------------------+----------------------------------------+
| Bloc 1                             | bloc 2                                 |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
|                                    |                                        |
+------------------------------------+----------------------------------------+

- BLOC 1 : Meteo
- BLOC 2 : Actu

"""

class guiBrief(GuiBase):
    def __init__(self,gestionnaire:gestionnaire,name:str):
        super().__init__(gestionnaire,f"{gestionnaire.getName()} : {name}")
        self.__readVar = ""
        self.__out_breef = None
        self.__thRead = th.Thread()
        self.__thLoad = th.Thread()

    def _mainframe(self):
        # Configuration de la fenetre
        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # Frame
        top_frame = aFrame(self._screen)

        # Configuration des colonnes de top_frame
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_columnconfigure(2, weight=1)

        # Widget Topframe
        self.__label_date = aLabel(top_frame, text="HH:MM - JEUDI XX JUILLET XXXX")
        self.__label_title = aLabel(top_frame, text="NAME_ASSISTANT : TYPE BRIEF")
        self.__btn_read = aButton(top_frame, text="Lire")
        
        # Le widget au centre prendra la ligne 1
        # Exemple de placement au centre :
        # widget_centre.grid(row=1, column=0, sticky="nsew")
        
        self.__main_frame = aFrame(self._screen)
        self.__load_frame = aFrame(self._screen)

        # Placement
        top_frame.grid(row=0, column=0, sticky="ew")

        self.__label_date.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.__label_title.grid(row=0, column=1, pady=10)
        self.__btn_read.grid(row=0, column=2, sticky="e", padx=10, pady=10)