from arrera_tk import *
from gui.guibase import GuiBase,gestionnaire
from fnc.fonctionActu import fncActualiter

class GuiNews(GuiBase):
    def __init__(self,gestionnaire:gestionnaire,name:str):
        super().__init__(gestionnaire,f"Actualités")
        self.__fnc_news = self._gestionnaire.getGestFNC().getFNCActu()

    def __get_actu(self):
        pass

    def _mainframe(self):
        # Configuration de la grille principale
        self._screen.grid_columnconfigure(0, weight=0)  # Frame gauche fixe
        self._screen.grid_columnconfigure(1, weight=1)  # Frame droite extensible
        self._screen.grid_rowconfigure(0, weight=1)  # Les frames prennent toute la hauteur

        left = aFrame(self._screen)
        right = aFrame(self._screen)

        right.grid_rowconfigure(0, weight=0)
        right.grid_rowconfigure(1, weight=1)
        right.grid_columnconfigure(0, weight=1)

        left.grid_rowconfigure(0, weight=0)

        for ligne in range(1, 7):
            left.grid_rowconfigure(ligne, weight=0)

        left.grid_columnconfigure(0, weight=1)

        self.__l_cath = aLabel(right,text="",police_size=25,anchor="w",justify="left")
        self.__fs_view_actu = aScrollableFrame(right)

        l_title = aLabel(left,text="Cathegorie",police_size=30)

        btn_cath_all = aButton(left,text="Tout",command=self.__view_all)
        btn_cath_main = aButton(left,text="Généraliste",command=self.__view_main)
        btn_cath_tech = aButton(left,text="Nouvelle technologie",command=self.__view_tech)
        btn_cath_cul = aButton(left,text="Culture",command=self.__view_culture)
        btn_cath_sci = aButton(left,text="Science",command=self.__view_science)
        btn_cath_sport = aButton(left,text="Sport",command=self.__view_sport)

        btn_cath_all.grid(row=1,column=0,sticky="ew",padx=10,pady=25)
        btn_cath_main.grid(row=2, column=0, sticky="ew", padx=10, pady=15)
        btn_cath_tech.grid(row=3, column=0, sticky="ew", padx=10, pady=15)
        btn_cath_cul.grid(row=4, column=0, sticky="ew", padx=10, pady=15)
        btn_cath_sci.grid(row=5, column=0, sticky="ew", padx=10, pady=15)
        btn_cath_sport.grid(row=6, column=0, sticky="ew", padx=10, pady=15)

        self.__l_cath.grid(row=0,column=0,sticky="ew",padx=10,pady=(5, 2))
        self.__fs_view_actu.grid(row=1,column=0,sticky="nsew",padx=10,pady=(5, 10))

        l_title.grid(row=0,column=0,sticky="ew",padx=10,pady=(5, 10))

        right.grid(row=0,column=1,sticky="nsew",padx=(5, 0),pady=0)
        left.grid(row=0,column=0,sticky="nsew",padx=(0, 5),pady=0)

    def __view_load(self):
        pass

    def __view_main(self):
        self.__l_cath.configure(text="Généraliste")

    def __view_all(self):
        self.__l_cath.configure(text="Tous")

    def __view_tech(self):
        self.__l_cath.configure(text="Nouvel technologie")

    def __view_culture(self):
        self.__l_cath.configure(text="Culture")

    def __view_sport(self):
        self.__l_cath.configure(text="Sport")

    def __view_science(self):
        self.__l_cath.configure(text="Science")

    def active_all(self):
        self.active()
        self.__get_actu()
        self.__view_all()


    def active_main(self):
        self.active()
        self.__get_actu()
        self.__view_main()


    def active_tech(self):
        self.active()
        self.__get_actu()
        self.__view_tech()


    def active_culture(self):
        self.active()
        self.__get_actu()
        self.__view_culture()


    def active_sport(self):
        self.active()
        self.__get_actu()
        self.__view_sport()


    def active_science(self):
        self.active()
        self.__get_actu()
        self.__view_science()