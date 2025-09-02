from gui.guibase import GuiBase,gestionnaire

class GUILecture(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Lecture")
        self.__fncLecture = self._gestionnaire.getGestFNC().getFNCRead()

    def _mainframe(self):
        self._screen.grid_rowconfigure(0, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # frame
        self.__frameSetText = self._arrtk.createFrame(self._screen)
        self.__frameReadText = self._arrtk.createFrame(self._screen)

        # Configuration
        self.__frameSetText.grid_columnconfigure(0, weight=1)
        self.__frameSetText.grid_rowconfigure(0, weight=0)
        self.__frameSetText.grid_rowconfigure(1, weight=1)
        self.__frameSetText.grid_rowconfigure(2, weight=0)

        self.__frameReadText.grid_rowconfigure(0, weight=1)
        self.__frameReadText.grid_columnconfigure(0, weight=1)

        # Widgets
        labelTitle = self._arrtk.createLabel(self.__frameSetText, text="Lecture de texte",
                                             ppolice="Arial", ptaille=35, pstyle="bold")
        self.__textToRead = self._arrtk.createText(self.__frameSetText)
        buttonRead = self._arrtk.createButton(self.__frameSetText, text="Lire le texte",
                                              ppolice="Arial", ptaille=25, pstyle="bold",
                                              bg=self._btnColor,fg=self._btnTexteColor)

        labelViewRead = self._arrtk.createLabel(self.__frameReadText, text="Lecture en cours...",
                                               ppolice="Arial", ptaille=35, pstyle="bold")

        # Placement
        labelTitle.grid(row=0, column=0, padx=12, pady=(12, 8))
        self.__textToRead.grid(row=1, column=0, sticky="nsew", padx=12, pady=8)
        buttonRead.grid(row=2, column=0, padx=12, pady=(8, 12))

        labelViewRead.grid(row=0, column=0, padx=12, pady=12)

        self.__frameSetText.grid(row=0, column=0, sticky="nsew")