from gui.guibase import GuiBase,gestionnaire
from tkcalendar import Calendar
from datetime import date

class GUIAgenda(GuiBase):
    def __init__(self, gest: gestionnaire):
        super().__init__(gest, "Agenda")
        self.__fncAgenda = gest.getGestFNC().getFNCTask()
        self.__assetPath = self._gestionnaire.getConfigFile().asset+"calendar/"

    def _mainframe(self):
        # Config de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.columnconfigure(0, weight=1)
        # Creation des frames Maitre
        self.__frameMain = self._arrtk.createFrame(self._screen)
        self.__frameAddEvent = self._arrtk.createFrame(self.__frameMain)
        self.__frameConfirm = self._arrtk.createFrame(self.__frameMain)
        # Frame fille
        frameLogoTitle = self._arrtk.createFrame(self.__frameMain)
        frameBTN = self._arrtk.createFrame(self.__frameMain)
        frameEventDay = self._arrtk.createFrame(self.__frameMain,wightBoder=2)
        frameCalendar = self._arrtk.createFrame(self.__frameMain)

        # Configuration des frames
        self.__frameMain.columnconfigure(0, weight=0)
        self.__frameMain.columnconfigure(1, weight=1)
        self.__frameMain.rowconfigure(0, weight=1)
        self.__frameMain.rowconfigure(1, weight=1)
        self.__frameMain.rowconfigure(2, weight=1)

        frameLogoTitle.grid_columnconfigure(0, weight=0)
        frameLogoTitle.grid_columnconfigure(1, weight=1)
        frameLogoTitle.grid_columnconfigure(2, weight=0)

        frameLogoTitle.grid_rowconfigure(0, weight=1)
        frameLogoTitle.grid_rowconfigure(1, weight=0)
        frameLogoTitle.grid_rowconfigure(2, weight=1)
        frameBTN.grid_columnconfigure(0, weight=1)
        frameBTN.grid_columnconfigure(1, weight=0)
        frameBTN.grid_columnconfigure(2, weight=1)

        frameBTN.grid_rowconfigure(0, weight=0)
        frameBTN.grid_rowconfigure(1, weight=1, minsize=24)
        frameBTN.grid_rowconfigure(2, weight=0)

        frameEventDay.grid_columnconfigure(0, weight=1)
        frameEventDay.grid_rowconfigure(0, weight=0)
        frameEventDay.grid_rowconfigure(1, weight=0)
        frameEventDay.grid_rowconfigure(2, weight=1)

        # Asset
        assetLogo = self._arrtk.createImage(pathLight=self.__assetPath+"calendar.png",
                                       pathDark=self.__assetPath+"calendar.png",
                                       tailleX=64, tailleY=64)

        # Widget
        # Logo et titre
        lLogoApp = self._arrtk.createLabel(frameLogoTitle,image=assetLogo)
        lTitleApp = self._arrtk.createLabel(frameLogoTitle,
                                            text=self._gestionnaire.getName()+" : Agenda",
                                            ppolice="Arial", ptaille=20, pstyle="bold")

        # Boutons
        btnCreateEvent = self._arrtk.createButton(frameBTN,text="Créer\nun événement",
                                                  ppolice="Arial",ptaille=15,pstyle="bold",
                                                  bg=self._btnColor,fg=self._btnTexteColor)
        btnSupprimerEvent = self._arrtk.createButton(frameBTN, text="Supprimer\nun événement",
                                                  ppolice="Arial", ptaille=15, pstyle="bold",
                                                  bg=self._btnColor, fg=self._btnTexteColor)

        # Calendrier
        miniCalendar = Calendar(frameCalendar,selectmode="day",year=date.today().year,
            month=date.today().month,locale="fr_FR",firstweekday="monday",showweeknumbers=False,
            borderwidth=0)

        # Jour
        self.__labelDate = self._arrtk.createLabel(frameEventDay,text="DATE",ppolice="Arial", ptaille=30, pstyle="bold")
        self.__labelEvent = self._arrtk.createLabel(frameEventDay,text="EVENT",ppolice="Arial", ptaille=20, pstyle="bold")
        self.__btnAddEventDay = self._arrtk.createButton(frameEventDay,text="Ajouter un événement",
                                                    ppolice="Arial", ptaille=25, pstyle="bold",
                                                    bg=self._btnColor, fg=self._btnTexteColor)
        # Placement des frames
        frameEventDay.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=0, pady=0)
        frameLogoTitle.grid(row=0, column=0, sticky="nw", padx=0, pady=0)
        frameBTN.grid(row=1, column=0, sticky="w", padx=(40, 0), pady=0)
        frameCalendar.grid(row=2, column=0, sticky="sw", padx=0, pady=0)

        # Placement des widgets
        # Logo et titre
        lLogoApp.grid(row=1, column=0, sticky="w")
        lTitleApp.grid(row=1, column=2, sticky="e")
        # Boutons
        btnCreateEvent.grid(row=0, column=1, sticky="n")
        btnSupprimerEvent.grid(row=2, column=1, sticky="s")
        # Mini calendrier
        miniCalendar.pack(expand=True, fill="both", padx=8, pady=8)
        # Jour
        self.__labelDate.grid(row=0, column=0, sticky="nw")
        self.__labelEvent.grid(row=1, column=0, sticky="w")
        self.__btnAddEventDay.grid(row=2, column=0, sticky="s", padx=10, pady=10)
        # Affichage principal
        self.__frameMain.grid(row=0, column=0, sticky="nsew")