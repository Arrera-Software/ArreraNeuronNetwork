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
        self.__frameMain.columnconfigure(0, weight=0)  # colonne gauche: taille fixe (pas d'étirement)
        self.__frameMain.columnconfigure(1, weight=1)  # colonne droite: prend tout l'espace restant
        self.__frameMain.rowconfigure(0, weight=1)
        self.__frameMain.rowconfigure(1, weight=1)
        self.__frameMain.rowconfigure(2, weight=1)

        # Placement des frames
        frameEventDay.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=0, pady=0)
        frameLogoTitle.grid(row=0, column=0, sticky="nw", padx=0, pady=0)
        frameBTN.grid(row=1, column=0, sticky="w", padx=0, pady=0)
        frameCalendar.grid(row=2, column=0, sticky="sw", padx=0, pady=0)

        # Affichage principal
        self.__frameMain.grid(row=0, column=0, sticky="nsew")