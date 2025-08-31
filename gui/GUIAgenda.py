from tkinter import StringVar, BooleanVar
from tkinter.messagebox import showerror

from gui.guibase import GuiBase,gestionnaire
from tkcalendar import Calendar
from datetime import date,datetime

class GUIAgenda(GuiBase):
    def __init__(self, gest: gestionnaire):
        super().__init__(gest, "Agenda")
        self.__fncAgenda = gest.getGestFNC().getFNCCalendar()
        self.__assetPath = self._gestionnaire.getConfigFile().asset+"calendar/"
        self.__dateSelected = None

    def _mainframe(self):
        self.__varHour = StringVar(self._screen)
        self.__varMinute = StringVar(self._screen)
        self.__varCheckHour = BooleanVar(value=False)
        self.__listHour = ["00","01","02","03",
                           "04","05","06","07",
                           "08","09","10","11",
                           "12","13","14","15",
                           "16","17","18","19",
                           "20","21","22","23"]
        # Config de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.columnconfigure(0, weight=1)
        # Creation des frames Maitre
        self.__frameMain = self._arrtk.createFrame(self._screen)
        self.__frameAddEvent = self._arrtk.createFrame(self._screen)
        self.__frameConfirm = self._arrtk.createFrame(self.__frameMain)
        # Frame fille
        frameLogoTitle = self._arrtk.createFrame(self.__frameMain)
        frameBTN = self._arrtk.createFrame(self.__frameMain)
        frameEventDay = self._arrtk.createFrame(self.__frameMain,wightBoder=2)
        frameCalendar = self._arrtk.createFrame(self.__frameMain)

        self.__frameAdd = self._arrtk.createFrame(self.__frameAddEvent)
        frameBTNFAdd = self._arrtk.createFrame(self.__frameAdd)
        self.__frameHeure = self._arrtk.createFrame(self.__frameAddEvent)

        # Configuration des frames
        # Frame Main
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

        self.__frameAddEvent.rowconfigure(0, weight=1)
        self.__frameAddEvent.columnconfigure(0, weight=1)

        self.__frameAdd.grid_columnconfigure(0, weight=1)
        self.__frameAdd.grid_rowconfigure(0, weight=0)
        self.__frameAdd.grid_rowconfigure(1, weight=0)
        self.__frameAdd.grid_rowconfigure(2, weight=0)
        self.__frameAdd.grid_rowconfigure(3, weight=0)
        self.__frameAdd.grid_rowconfigure(4, weight=0)
        self.__frameAdd.grid_rowconfigure(5, weight=0)
        self.__frameAdd.grid_rowconfigure(6, weight=1)
        self.__frameAdd.grid_rowconfigure(7, weight=0)

        frameBTNFAdd.grid_columnconfigure(0, weight=0)
        frameBTNFAdd.grid_columnconfigure(1, weight=1)
        frameBTNFAdd.grid_columnconfigure(2, weight=0)
        frameBTNFAdd.grid_rowconfigure(0, weight=0)

        # Frame Add Event


        # Asset
        assetLogo = self._arrtk.createImage(pathLight=self.__assetPath+"calendar.png",
                                       pathDark=self.__assetPath+"calendar.png",
                                       tailleX=64, tailleY=64)

        # Widget
        # Frame Main
        # Logo et titre
        lLogoApp = self._arrtk.createLabel(frameLogoTitle,image=assetLogo)
        lTitleApp = self._arrtk.createLabel(frameLogoTitle,
                                            text=self._gestionnaire.getName()+" : Agenda",
                                            ppolice="Arial", ptaille=20, pstyle="bold")

        # Boutons
        btnCreateEvent = self._arrtk.createButton(frameBTN,text="Créer\nun événement",
                                                  ppolice="Arial",ptaille=15,pstyle="bold",
                                                  bg=self._btnColor,fg=self._btnTexteColor,
                                                  command=lambda : self.__viewAddEvent(0))
        btnSupprimerEvent = self._arrtk.createButton(frameBTN, text="Supprimer\nun événement",
                                                  ppolice="Arial", ptaille=15, pstyle="bold",
                                                  bg=self._btnColor, fg=self._btnTexteColor)

        # Calendrier
        self.__miniCalendar = Calendar(frameCalendar,selectmode="day",year=date.today().year,
            month=date.today().month,locale="fr_FR",firstweekday="monday",showweeknumbers=False,
            borderwidth=0)

        # Jour
        self.__labelDate = self._arrtk.createLabel(frameEventDay,text="DATE",ppolice="Arial", ptaille=30, pstyle="bold")
        self.__labelEvent = self._arrtk.createLabel(frameEventDay,text="EVENT",ppolice="Arial", ptaille=20, pstyle="bold")
        self.__btnAddEventDay = self._arrtk.createButton(frameEventDay,text="Ajouter un événement",
                                                    ppolice="Arial", ptaille=25,bg=self._btnColor,
                                                         fg=self._btnTexteColor,command=lambda : self.__viewAddEvent(1))


        # Frame Add Event

        self.__labelTitleAddEvent = self._arrtk.createLabel(self.__frameAdd,
                                                            text="Ajouter un événement",
                                                            ppolice="Arial", ptaille=30, pstyle="bold")
        self.__calendarAddEvent = Calendar(self.__frameAdd,selectmode="day",year=date.today().year,
                                           month=date.today().month,locale="fr_FR",firstweekday="monday",
                                           showweeknumbers=False,borderwidth=0,date_pattern="yyyy-mm-dd")
        self.__labelDateSelected = self._arrtk.createLabel(self.__frameAdd,ppolice="Arial", ptaille=15)
        wEntryName,self.__entryNameEvent = self._arrtk.createEntryLegend(self.__frameAdd,text="Titre : ",ppolice="Arial", ptaille=20,gridUsed=True)
        wEntryDescription,self.__entryDescriptionEvent = self._arrtk.createEntryLegend(self.__frameAdd,ppolice="Arial", ptaille=20,text="Description : ",gridUsed=True)
        wEntryLieu,self.__entryLieuEvent = self._arrtk.createEntryLegend(self.__frameAdd,ppolice="Arial", ptaille=20,text="Lieu :",gridUsed=True)
        self.__checkHour = self._arrtk.createCheckbox(self.__frameAdd,text="Définir une heure",var_chk=self.__varCheckHour)

        btnAddEvent = self._arrtk.createButton(frameBTNFAdd,text="Ajouter",
                                              ppolice="Arial", ptaille=20,command=self.__addNewEvent,
                                              bg=self._btnColor, fg=self._btnTexteColor)

        btnCancelEvent = self._arrtk.createButton(frameBTNFAdd,text="Annuler",
                                               ppolice="Arial", ptaille=20,command=self.__backToMain,
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
        self.__miniCalendar.pack(expand=True, fill="both", padx=8, pady=8)
        # Jour
        self.__labelDate.grid(row=0, column=0, sticky="nw", padx=10, pady=(10, 5))
        self.__labelEvent.grid(row=1, column=0, sticky="w",  padx=10, pady=(0, 10))
        self.__btnAddEventDay.grid(row=2, column=0, sticky="s", padx=10, pady=10)

        # Ajout Event
        self.__labelTitleAddEvent.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 6))
        wEntryName.grid(row=2, column=0, sticky="ew", padx=12, pady=6)
        wEntryDescription.grid(row=3, column=0, sticky="ew", padx=12, pady=6)
        wEntryLieu.grid(row=4, column=0, sticky="ew", padx=12, pady=6)
        self.__checkHour.grid(row=5, column=0, sticky="ew", padx=12, pady=6)
        btnCancelEvent.grid(row=0, column=0, sticky="w", padx=(10, 6), pady=8)
        btnAddEvent.grid(   row=0, column=2, sticky="e", padx=(6, 10), pady=8)
        frameBTNFAdd.grid(row=7, column=0, sticky="sew", padx=12, pady=12)

        # Affichage principal
        self.__frameMain.grid(row=0, column=0, sticky="nsew")

        # Ajout de l'affichage des event du jour
        self.__viewEventDay(datetime.today().strftime("%Y-%m-%d"))
        
        # Check du mini calendar 
        self.__miniCalendar.bind("<<CalendarSelected>>", self.__dateSelectedOnCalendar)
        self._screen.update()

    def __backToMain(self):
        self.__frameAddEvent.grid_forget()
        self.__frameMain.grid(row=0, column=0, sticky="nsew")
        self._screen.update()

    def __viewEventDay(self, date):
        """date (YYYY-MM-DD)"""
        self.__labelDate.configure(text=date)
        try :
            listEvent = self.__fncAgenda.checkEventWithDate(date)
            if not listEvent:
                self.__labelEvent.configure(text="Aucun événement")
                return True
            else :
                texte = ""
                for event in listEvent:
                    texte += "- " + event + "\n"
                self.__labelEvent.configure(text=texte)
            self.__dateSelected = date
            self._screen.update()
            return True
        except Exception as e:
            return False
    
    def __dateSelectedOnCalendar(self,event):
        date = self.__miniCalendar.get_date()
        self.__viewEventDay(datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d"))

    def __viewAddEvent(self,mode:int):

        self.__calendarAddEvent.grid_forget()
        self.__labelDateSelected.grid_forget()

        match mode :
            case 0:
                self.__calendarAddEvent.grid(row=1, column=0, sticky="n",  padx=12, pady=6)
            case 1 :
                self.__labelDateSelected.configure(text="Date sélectionnée : "+self.__dateSelected)
                self.__labelDateSelected.grid(row=1, column=0, sticky="n",  padx=12, pady=6)

        self.__frameMain.grid_forget()
        self.__frameAddEvent.grid(row=0, column=0, sticky="nsew")
        self.__frameAdd.grid(row=0, column=0, sticky="nsew")
        self._screen.update()

    def __addNewEvent(self):
        name = self.__entryNameEvent.get()
        if name == "" :
            showerror("Erreur",
                      "Le nom de l'événement ne peut pas être vide")
            return False
        description = self.__entryDescriptionEvent.get()
        lieu = self.__entryLieuEvent.get()
        if self.__varCheckHour.get():
            print("hour")

        if self.__dateSelected is not None:
            date = datetime.strptime(self.__dateSelected, "%Y-%m-%d").date()
        else :
            date = datetime.strptime(self.__calendarAddEvent.get_date(), "%Y-%m-%d").date()

        if self.__fncAgenda.addEventToCalendar(name=name, date=date, descrption=description, lieu=lieu):
            self.__backToMain()
            self.__viewEventDay(date)
            return True
        else :
            showerror("Erreur",
                      "Une erreur est survenue lors de l'ajout de l'événement")
            return False
        