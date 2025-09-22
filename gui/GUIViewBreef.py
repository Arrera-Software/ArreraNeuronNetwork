from tkinter.messagebox import showerror

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

        weatherFrame = self._arrtk.createFrame(mainFrame)
        alertFrame = self._arrtk.createFrame(weatherFrame,bg="purple")

        taskFrame = self._arrtk.createScrollFrame(mainFrame,bg="green")
        taskProjectFrame = self._arrtk.createScrollFrame(mainFrame,bg="yellow")

        # Configuration
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(0, weight=0)
        mainFrame.grid_rowconfigure(1, weight=0)
        mainFrame.grid_rowconfigure(2, weight=1)
        mainFrame.grid_rowconfigure(3, weight=1)
        mainFrame.grid_rowconfigure(4, weight=0)

        weatherFrame.rowconfigure(0, weight=1)
        weatherFrame.rowconfigure(1, weight=1)
        weatherFrame.rowconfigure(2, weight=1)
        weatherFrame.columnconfigure(0, weight=1)
        weatherFrame.columnconfigure(1, weight=1)
        weatherFrame.columnconfigure(2, weight=1)

        alertFrame.columnconfigure(0, weight=1)   # Pour s'étendre en largeur
        alertFrame.rowconfigure(0, weight=1)
        alertFrame.rowconfigure(1, weight=1)
        alertFrame.rowconfigure(2, weight=1)

        # Widgets
        labelTitle = self._arrtk.createLabel(mainFrame,text=self._gestionnaire.getName()+" : Breef",
                                             ppolice="Arial",ptaille=30,pstyle="bold")
        btnRead = self._arrtk.createButton(mainFrame,text="Lire",ppolice="Arial",ptaille=20,
                                           pstyle="normal",bg=self._btnColor,fg=self._btnTexteColor)

        # Meteo
        self.__labelLogoMeteo = self._arrtk.createLabel(weatherFrame,text="Logo")

        self.__lnameTown = self._arrtk.createLabel(weatherFrame,text="Ville",
                                                   ppolice="Arial",ptaille=30,pstyle="bold",justify="left")
        self.__ltemp = self._arrtk.createLabel(weatherFrame,text="Temperature",
                                               ppolice="Arial",ptaille=40,pstyle="bold",justify="left")
        self.__lweather = self._arrtk.createLabel(weatherFrame,text="description",
                                                  ppolice="Arial",ptaille=25,pstyle="bold",justify="left")

        self.__lAlertRed = self._arrtk.createLabel(alertFrame,text="Alerte",bg="red",
                                                   ppolice="Arial",ptaille=20,pstyle="bold",justify="left")
        self.__lAlertOrange = self._arrtk.createLabel(alertFrame,text="Alerte",bg="orange",fg="black",
                                                      ppolice="Arial",ptaille=20,pstyle="bold",justify="left")
        self.__lAlertYellow = self._arrtk.createLabel(alertFrame,text="Alerte",bg="yellow",fg="black",
                                                      ppolice="Arial",ptaille=20,pstyle="bold",justify="left")
        self.__lNoAlert = self._arrtk.createLabel(alertFrame,text="Aucune d'alerte",
                                                  ppolice="Arial",ptaille=20,pstyle="bold",justify="left")

        # Placement
        labelTitle.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        weatherFrame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        taskFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        taskProjectFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        btnRead.grid(row=4, column=0, sticky="ew", padx=10, pady=(5, 10))

        alertFrame.grid(row=0, column=2, sticky="ne", padx=(4, 8), pady=(8, 2))
        self.__labelLogoMeteo.grid(row=0, column=0, sticky="nw", padx=(8, 4), pady=(8, 2))
        self.__lnameTown.grid(row=1, column=0, sticky="w", padx=(8, 4), pady=(2, 8))
        self.__ltemp.grid(row=1, column=1, sticky="", padx=4, pady=4)
        self.__lweather.grid(row=2, column=2, sticky="se", padx=(4, 8), pady=(2, 8))

        mainFrame.grid(row=0, column=0, sticky="nsew")

    def activeBreef(self):
        self.active()
        outBreef = self._gestionnaire.getGestFNC().getFNCBreef().morningBreef()
        if outBreef is None:
            showerror("Erreur","Impossible de charger le breef du jour")
            self._screen.destroy()
        else:
            self.__selectMeteo(outBreef)
            print("parfais")

    def __selectMeteo(self,out:dict):
        meteoDict = out["meteo"]
        self.__lnameTown.configure(text=meteoDict["ville"])
        self.__ltemp.configure(text=str(meteoDict["temperature"])+"°C")
        self.__lweather.configure(text=meteoDict["weather"])
        print(meteoDict["redAlert"])
        print(meteoDict["yellowAlert"])
        print(meteoDict["orangeAlert"])
        print(meteoDict["greenAlert"])

        try :
            print(meteoDict["icon"])
            imgMeteo = self._arrtk.createImage(meteoDict["icon"],tailleX=100,tailleY=100)
            self.__labelLogoMeteo.configure(image=imgMeteo,text="")
        except:
            imgMeteo = self._arrtk.createImage(self._gestionnaire.getConfigFile().asset+"meteo/meteo-error.png",
                                               tailleX=100,tailleY=100)
            self.__labelLogoMeteo.configure(image=imgMeteo,text="")





        self.__lNoAlert.grid(row=1, column=0, sticky="ew", padx=8, pady=4)

        if meteoDict["redAlert"]:
            self.__lNoAlert.grid_forget()
            self.__lAlertRed.grid(row=0, column=0, sticky="new", padx=8, pady=(8, 4))

        if meteoDict["orangeAlert"]:
            self.__lNoAlert.grid_forget()
            self.__lAlertOrange.grid(row=1, column=0, sticky="ew", padx=8, pady=4)

        if meteoDict["yellowAlert"]:
            self.__lNoAlert.grid_forget()
            self.__lAlertYellow.grid(row=2, column=0, sticky="sew", padx=8, pady=(4, 8))


