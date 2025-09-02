from gui.guibase import GuiBase,gestionnaire

class GUIHorloge(GuiBase):
    def __init__(self, gest: gestionnaire):
        super().__init__(gest, "Horloge")
        self.__fncHorloge = self._gestionnaire.getGestFNC().getFNCHorloge()

    def _mainframe(self):
        # Conf de la fenetre
        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # Frame principal
        self.__frameNav = self._arrtk.createFrame(self._screen,bg="green")
        self.__frameHorloge = self._arrtk.createFrame(self._screen,bg="blue")
        self.__frameChrono = self._arrtk.createFrame(self._screen,bg="red")
        self.__frameMinuteur = self._arrtk.createFrame(self._screen,bg="yellow")

        # Conf frame
        self.__frameNav.grid_columnconfigure(0, weight=1)  # espace à gauche
        self.__frameNav.grid_columnconfigure(1, uniform="btns")
        self.__frameNav.grid_columnconfigure(2, uniform="btns")
        self.__frameNav.grid_columnconfigure(3, uniform="btns")
        self.__frameNav.grid_columnconfigure(4, weight=1)
        self.__frameNav.grid_rowconfigure(0, weight=0)

        self.__frameHorloge.grid_rowconfigure(0, weight=1)
        self.__frameHorloge.grid_columnconfigure(0, weight=1)

        # Widget
        # Nav
        btnHorloge = self._arrtk.createButton(self.__frameNav,text="Horloge",command=self.__viewHorloge)
        btnMinuteur = self._arrtk.createButton(self.__frameNav,text="Minuteur",command=self.__viewMinuteur)
        btnChrono = self._arrtk.createButton(self.__frameNav,text="Chronometre",command=self.__viewChrono)
        # Horloge
        self.__labelViewClock = self._arrtk.createLabel(self.__frameHorloge,text="00:00:00",
                                                        ppolice="Arial",ptaille=60,pstyle="bold")

        # Placement des widget
        btnHorloge.grid( row=0, column=1, padx=(8, 8), pady=10)
        btnMinuteur.grid(row=0, column=2, padx=(8, 8), pady=10)
        btnChrono.grid( row=0, column=3, padx=(8, 8), pady=10)

        self.__labelViewClock.grid(row=0, column=0, padx=10, pady=10)

        self.__frameNav.grid(row=0, column=0, sticky="ew")
        self.__frameHorloge.grid(row=1, column=0, sticky="nsew")

    def __disableAllFrame(self):
        self.__frameHorloge.grid_forget()
        self.__frameChrono.grid_forget()
        self.__frameMinuteur.grid_forget()

    def __viewHorloge(self):
        self.__disableAllFrame()
        self.__frameHorloge.grid(row=1, column=0, sticky="nsew")

    def __viewMinuteur(self):
        self.__disableAllFrame()
        self.__frameMinuteur.grid(row=1, column=0, sticky="nsew")

    def activeMinuteur(self):
        self.active()
        self.__viewMinuteur()

    def __viewChrono(self):
        self.__disableAllFrame()
        self.__frameChrono.grid(row=1, column=0, sticky="nsew")

    def activeChrono(self):
        self.active()
        self.__viewChrono()

