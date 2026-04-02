from librairy.arrera_tk import *
from gui.guibase import GuiBase,gestionnaire

class GUIWork(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Work")
        # Attributs
        self.__emplacementAsset = self._gestionnaire.getConfigFile().asset + "work/"
        self.__fnc_work = gestionnaire.getGestFNC().getFNCWork()

    def _mainframe(self):
        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)

        # Image
        img_w_tableur= aImage(path_light=self.__emplacementAsset + "acceuil/tableur.png",
                              width=50, height=50)
        img_w_texte = aImage(path_light=self.__emplacementAsset + "acceuil/word.png",
                                width=50, height=50)
        img_w_project = aImage(path_light=self.__emplacementAsset + "acceuil/project.png",
                                   width=50, height=50)

        # Frame
        f_header = aFrame(self._screen,height=50)
        self.__f_welcome = aFrame(self._screen)
        f_welcome_btn = aFrame(self.__f_welcome)
        f_welcome_task_projet = aFrame(self.__f_welcome)

        # Configuration des grid
        self.__f_welcome.grid_rowconfigure(0, weight=1)
        self.__f_welcome.grid_columnconfigure(0, weight=1)
        self.__f_welcome.grid_columnconfigure(1, weight=1)

        for i in range(3):
            f_welcome_btn.grid_rowconfigure(i, weight=1)
        f_welcome_btn.grid_columnconfigure(0, weight=1)

        f_welcome_task_projet.grid_rowconfigure(0, weight=0)
        f_welcome_task_projet.grid_rowconfigure(1, weight=1)
        f_welcome_task_projet.grid_columnconfigure(0, weight=1)

        # header
        l_title = aLabel(f_header,police_size=30,text=f"{self._gestionnaire.getConfigFile().name} : Work")
        # Welcome
        btn_w_tableur = aButton(f_welcome_btn,text="Tableur",image=img_w_tableur)
        btn_w_word = aButton(f_welcome_btn,text="Traitement\nde texte",image=img_w_texte)
        btn_w_projet = aButton(f_welcome_btn,text="Projet",image=img_w_project)

        # Welcome Task Projet
        l_title_task = aLabel(f_welcome_task_projet,text="Tache des projets",police_size=25)
        self.__text_view_task = aTextScrollable(f_welcome_task_projet)

        # Placement
        l_title.pack(pady=10)

        btn_w_tableur.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        btn_w_word.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        btn_w_projet.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        l_title_task.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        self.__text_view_task.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

        f_header.grid(row=0, column=0, sticky="ew")
        f_header.grid_propagate(False)

        f_welcome_btn.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)
        f_welcome_task_projet.grid(row=0, column=1, sticky="nsew",padx=10,pady=10)

        self.__f_welcome.grid(row=1, column=0, sticky="nsew")

        self.__load_view_task_projet()

    def __load_view_task_projet(self):
        name_project = None
        list_tache = []
        if self.__fnc_work.getEtatProject():
            name_project = self.__fnc_work.getNameProjet()
            self.__fnc_work.closeProjet()

        list_projet = self.__fnc_work.getListProjet()

        if list_projet is not None:
            for projet in list_projet:
                if self.__fnc_work.openProjet(projet):
                    if self.__fnc_work.setListTacheNoFinishProjet():
                        for i in self.__fnc_work.getListTacheNoFinishProjet():
                            list_tache.append(f"{projet} : {i}")
            self.__text_view_task.enableTextBox()
            self.__text_view_task.getTextBox().delete(1.0, END)
            if len(list_tache) > 0:
                for task in list_tache:
                    self.__text_view_task.getTextBox().insert(END, f"{task}\n\n")
            else :
                self.__text_view_task.getTextBox().insert(END, "Aucune tache enregistrer dans les projet")
            self.__text_view_task.disableTextBox()
        else :
            self.__text_view_task.enableTextBox()
            self.__text_view_task.getTextBox().delete(1.0, END)
            self.__text_view_task.getTextBox().insert(END, "Aucun projet enregistrer")
            self.__text_view_task.disableTextBox()

        if name_project is not None:
            self.__fnc_work.openProjet(name_project)



    def activeProjet(self):
        self.active()
        self._mainframe()
        #self.__activeProjet()

    def activeTableur(self):
        self.active()
        self._mainframe()
        #self.__activeTableur()

    def activeWord(self):
        self.active()
        self._mainframe()
        #self.__activeWord()

    def activeAcceuil(self):
        self.active()
        self._mainframe()
        #self.__activeAcceuil()