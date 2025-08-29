from gui.guibase import GuiBase,gestionnaire

class GUIAgenda(GuiBase):
    def __init__(self, gest: gestionnaire):
        super().__init__(gest, "Agenda")
        self.__fncAgenda = gest.getGestFNC().getFNCTask()

    def _mainframe(self):
        # Config de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.columnconfigure(0, weight=1)
        # Creation des frames Maitre
        self.__frameMain = self._arrtk.createFrame(self._screen)
        self.__frameAddEvent = self._arrtk.createFrame(self.__frameMain)
        self.__frameConfirm = self._arrtk.createFrame(self.__frameMain)
        # Frame fille
        frameLogoTitle = self._arrtk.createFrame(self.__frameMain,bg="red")
        frameBTN = self._arrtk.createFrame(self.__frameMain,bg="blue")
        frameEventDay = self._arrtk.createFrame(self.__frameMain,bg="yellow")
        frameCalendar = self._arrtk.createFrame(self.__frameMain,bg="green")

        # Configuration des frames
        self.__frameMain.columnconfigure(0, weight=0)
        self.__frameMain.columnconfigure(1, weight=1)
        self.__frameMain.rowconfigure(0, weight=1)
        self.__frameMain.rowconfigure(1, weight=1)
        self.__frameMain.rowconfigure(2, weight=1)

        frameLogoTitle.grid_columnconfigure(0, weight=0)  # colonne gauche (label)
        frameLogoTitle.grid_columnconfigure(1, weight=1)  # espace flexible
        frameLogoTitle.grid_columnconfigure(2, weight=0)  # colonne droite (label)

        frameLogoTitle.grid_rowconfigure(0, weight=1)  # espace haut
        frameLogoTitle.grid_rowconfigure(1, weight=0)  # rangée centrale (labels)
        frameLogoTitle.grid_rowconfigure(2, weight=1)  # espace bas

        frameBTN.grid_columnconfigure(0, weight=1)
        frameBTN.grid_columnconfigure(1, weight=0)
        frameBTN.grid_columnconfigure(2, weight=1)

        frameBTN.grid_rowconfigure(0, weight=0)
        frameBTN.grid_rowconfigure(1, weight=1, minsize=24)  # écart vertical entre les deux boutons
        frameBTN.grid_rowconfigure(2, weight=0)

        # Widget
        lLogoApp = self._arrtk.createLabel(frameLogoTitle,
                                           text="Logo",bg="red") # A remplacer par le logo de l'application
        lTitleApp = self._arrtk.createLabel(frameLogoTitle,
                                            text=self._gestionnaire.getName()+" : Agenda",
                                            ppolice="Arial", ptaille=20, pstyle="bold")

        btnCreateEvent = self._arrtk.createButton(frameBTN,text="Créer\nun événement",
                                                  ppolice="Arial",ptaille=15,pstyle="bold",
                                                  bg=self._btnColor,fg=self._btnTexteColor)
        btnSupprimerEvent = self._arrtk.createButton(frameBTN, text="Supprimer\nun événement",
                                                  ppolice="Arial", ptaille=15, pstyle="bold",
                                                  bg=self._btnColor, fg=self._btnTexteColor)



        # Placement des frames
        frameEventDay.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=0, pady=0)
        frameLogoTitle.grid(row=0, column=0, sticky="nw", padx=0, pady=0)
        frameBTN.grid(row=1, column=0, sticky="w", padx=0, pady=0)
        frameCalendar.grid(row=2, column=0, sticky="sw", padx=0, pady=0)

        # Placement des widgets
        # Logo et titre
        lLogoApp.grid(row=1, column=0, sticky="w")
        lTitleApp.grid(row=1, column=2, sticky="e")
        # Boutons
        btnCreateEvent.grid(row=0, column=1, sticky="n")
        btnSupprimerEvent.grid(row=2, column=1, sticky="s")

        # Affichage principal
        self.__frameMain.grid(row=0, column=0, sticky="nsew")