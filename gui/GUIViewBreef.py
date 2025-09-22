from gui.guibase import GuiBase,gestionnaire

class GUIViewBreef(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Breef")

    def _mainframe(self):
        # Configuration de la fenetre
        self._screen.grid_rowconfigure(0, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # Frame
        mainFrame = self._arrtk.createFrame(self._screen,bg="red")

        weatherFrame = self._arrtk.createFrame(mainFrame,bg="blue")
        taskFrame = self._arrtk.createScrollFrame(mainFrame,bg="green")
        taskProjectFrame = self._arrtk.createScrollFrame(mainFrame,bg="yellow")

        # Configuration
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(0, weight=0)
        mainFrame.grid_rowconfigure(1, weight=0)
        mainFrame.grid_rowconfigure(2, weight=1)
        mainFrame.grid_rowconfigure(3, weight=1)
        mainFrame.grid_rowconfigure(4, weight=0)

        # Widgets
        labelTitle = self._arrtk.createLabel(mainFrame,text=self._gestionnaire.getName()+" : Breef",
                                             ppolice="Arial",ptaille=30,pstyle="bold")
        btnRead = self._arrtk.createButton(mainFrame,text="Lire",ppolice="Arial",ptaille=20,
                                           pstyle="normal",bg=self._btnColor,fg=self._btnTexteColor)
        # Placement
        labelTitle.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        weatherFrame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        taskFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        taskProjectFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        btnRead.grid(row=4, column=0, sticky="ew", padx=10, pady=(5, 10))

        mainFrame.grid(row=0, column=0, sticky="nsew")

        self._gestionnaire.getGestFNC().getFNCBreef().morningBreef()