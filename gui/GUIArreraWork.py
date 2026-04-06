from tkinter.messagebox import showerror

from librairy.arrera_tk import *
from gui.guibase import GuiBase,gestionnaire
from gui.GUITaskProject import GUITaskProject

class GUIWork(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Work")
        # Attributs
        self.__emplacementAsset = self._gestionnaire.getConfigFile().asset + "work/"
        self.__fnc_work = gestionnaire.getGestFNC().getFNCWork()
        self.__guiTaskProject = None
        self.__wordOpen = False
        self.__tableurOpen = False
        self.__projectOpen = False

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

        self.__f_projet = aFrame(self._screen)
        f_projet_header = aFrame(self.__f_projet,height=50)
        self.__f_projet_body = aFrame(self.__f_projet)
        self.__f_projet_footer = aFrame(self.__f_projet,height=50)

        # Configuration des grid
        self.__f_welcome.grid_rowconfigure(0, weight=1)
        self.__f_welcome.grid_columnconfigure(0, weight=1)
        self.__f_welcome.grid_columnconfigure(1, weight=1)

        self.__f_projet.grid_rowconfigure(0, weight=0)
        self.__f_projet.grid_rowconfigure(1, weight=1)
        self.__f_projet.grid_rowconfigure(2, weight=0)
        self.__f_projet.grid_columnconfigure(0, weight=1)

        self.__f_projet_body.grid_rowconfigure(0, weight=1)
        self.__f_projet_body.grid_columnconfigure(0, weight=1)

        for i in range(3):
            f_welcome_btn.grid_rowconfigure(i, weight=1)
        f_welcome_btn.grid_columnconfigure(0, weight=1)

        f_welcome_task_projet.grid_rowconfigure(0, weight=0)
        f_welcome_task_projet.grid_rowconfigure(1, weight=1)
        f_welcome_task_projet.grid_columnconfigure(0, weight=1)

        f_projet_header.grid_rowconfigure(0, weight=1)
        f_projet_header.grid_columnconfigure(0, weight=1)

        self.__f_projet_footer.grid_rowconfigure(0, weight=1)
        self.__f_projet_footer.grid_columnconfigure(0, weight=1)

        f_projet_header.grid_propagate(False)
        self.__f_projet_footer.grid_propagate(False)
        # header
        l_title = aLabel(f_header,police_size=30,text=f"{self._gestionnaire.getConfigFile().name} : Work")
        # Welcome
        btn_w_tableur = aButton(f_welcome_btn,text="Tableur",
                                image=img_w_tableur)
        btn_w_word = aButton(f_welcome_btn,text="Traitement\nde texte",image=img_w_texte)
        btn_w_projet = aButton(f_welcome_btn,text="Projet",
                               image=img_w_project,command=self.__view_projet)

        # Projet
        l_title_projet = aLabel(f_projet_header,text="Projet",police_size=25)
        btn_p_exit = aButton(self.__f_projet_footer,text="Retour",command=self.__view_acceuil)

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

        f_projet_header.grid(row=0, column=0, sticky="ew",padx=10,pady=10)
        self.__f_projet_body.grid(row=1, column=0, sticky="nsew",padx=10,pady=10)
        self.__f_projet_footer.grid(row=2, column=0, sticky="ew",padx=10,pady=10)

        l_title_projet.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)
        btn_p_exit.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

        self.__f_welcome.grid(row=1, column=0, sticky="nsew")

        self.__load_view_task_projet()

    def __update_etat(self):
        self.__wordOpen = self.__fnc_work.getEtatWord()
        self.__tableurOpen = self.__fnc_work.getEtatTableur()
        self.__projectOpen = self.__fnc_work.getEtatProject()
        if self.__projectOpen:
            self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                   self.__fnc_work.getNameProjet(),
                                                   self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())
        else:
            self.__guiTaskProject = None

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
                    # Récupération des tâches non terminées
                    if self.__fnc_work.setListTacheNoFinishProjet():
                        for i in self.__fnc_work.getListTacheNoFinishProjet():
                            list_tache.append(f"{projet} : {i}")
                    self.__fnc_work.closeProjet()

        self.__text_view_task.enableTextBox()
        self.__text_view_task.getTextBox().delete(1.0, END)

        if list_projet is None:
            self.__text_view_task.getTextBox().insert(END, "Aucun projet enregistré")
        elif len(list_tache) > 0:
            for task in list_tache:
                self.__text_view_task.getTextBox().insert(END, f"{task}\n\n")
        else:
            self.__text_view_task.getTextBox().insert(END, "Aucune tâche enregistrée dans les projets")

        self.__text_view_task.disableTextBox()

        if name_project is not None:
            self.__fnc_work.openProjet(name_project)

    def activeProjet(self):
        self.active()
        self._mainframe()
        self.__view_projet()

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
        self.__view_acceuil()

    def __view_acceuil(self):
        self.__f_projet.grid_forget()
        self.__f_welcome.grid(row=1, column=0, sticky="nsew")

    def __view_projet(self):
        self.__f_welcome.grid_forget()
        self.__f_projet.grid(row=1, column=0, sticky="nsew")

        self.__f_projet_footer.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        for widget in self.__f_projet_body.winfo_children():
            widget.destroy()
 
        list_projet = self.__fnc_work.getListProjet()
        f_view_projet = aScrollableFrame(self.__f_projet_body,fg_color=self.__f_projet_body.cget("fg_color"))
        f_view_projet.grid_columnconfigure(0, weight=1)

        for i, p in enumerate(list_projet):
            b = aButton(f_view_projet, text=p,size=17,command= lambda p=p: self.__open_projet(p))
            b.grid(row=i, column=0, sticky="ew", padx=15, pady=15)

        f_view_projet.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def __windows_action_projet(self, title:str, texte:str):
        screen = aTopLevel(width=300, height=125,resizable=False,title=title)
        aLabel(screen, text=texte,police_size=25).placeTopCenter()
        entry = aEntry(screen,width=150)
        entry.placeCenter()
        return screen,entry

    def __win_add_type(self):
        screen,entry = self.__windows_action_projet("Type du projet","Entrez le type du projet")
        aButton(screen,text="Enregistrer le type",
                command=lambda: self.__fnc_work.addTypeProjet(entry.get())).placeBottomCenter()

    def __create_file_projet(self, screen: ctk.CTkToplevel,menu:aOptionMenu):
        name_file = self.__entryNameFile.get()
        if not name_file:
            showerror("Erreur", "Imposible de créer un fichier sans nom.")
            return

        type_file = menu.getValue()

        self.__fnc_work.createFileProject(name_file, type_file)
        screen.destroy()

    def __win_create_file(self):
        """
        Ouvre une fenêtre pour créer un fichier de projet.
        """
        listType = ["excel","xlsx",
                    "word","docx",
                    "Open Document Texte","odt",
                    "markdown","md",
                    "Arrera Postite",".ab"]
        screen = aTopLevel(title="Création d'un fichier de projet",
                           width=300, height=200, resizable=False)


        aLabel(screen, text="Creation d'un\nfichier dans le projet",
               police_size=25).placeTopCenter()
        self.__entryNameFile = aEntry(screen,width=150)
        self.__entryNameFile.placeLeftCenter()
        menuType = aOptionMenu(screen, value=listType).placeRightCenter()
        aButton(screen, text="Valider", command=lambda: self.__create_file_projet(screen,menuType)
                ).placeBottomCenter()

    def __open_task_projet(self):
        self.__update_etat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.active()
            return True
        else :
            return False

    def __view_projet_open(self):
        for widget in self.__f_projet_body.winfo_children():
            widget.destroy()

        f_projet = aFrame(self.__f_projet_body,fg_color=self.__f_projet_body.cget("fg_color"))
        frame_center = aFrame(f_projet,fg_color=self.__f_projet_body.cget("fg_color"))

        f_projet.grid_rowconfigure(0, weight=0)
        f_projet.grid_rowconfigure(1, weight=1)
        f_projet.grid_rowconfigure(2, weight=0)
        f_projet.grid_columnconfigure(0, weight=1)

        label_title = aLabel(f_projet, text="",anchor="w")
        btn_bottom = aButton(f_projet, text="Ferme le projet",size=25,
                             command=self.__close_projet)

        label_title.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        frame_center.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        f_projet.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        btn_bottom.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

        self.__f_projet_footer.grid_forget()

        name = self.__fnc_work.getNameProjet()

        label_title.configure(text=f"Projet : {name}", font=("Roboto", 25, "normal"),
                              justify="left")

        for i in range(2):
            frame_center.grid_columnconfigure(i, weight=1)

        for i in range(3):
            frame_center.grid_rowconfigure(i, weight=1)

        buttons = []
        list_image = [aImage(path_light="asset/work/project/setType-project.png", width=80, height=80),
                      aImage(path_light="asset/work/project/create-file-project.png", width=80, height=80),
                      aImage(path_light="asset/work/project/view-task-project.png", width=80, height=80)]

        for i in range(3):
            btn = aButton(frame_center, text="", image=list_image[i])
            buttons.append(btn)

        buttons[0].configure(command=self.__win_add_type)
        buttons[1].configure(command=self.__win_create_file)
        buttons[2].configure(command=self.__open_task_projet)

        buttons[0].grid(row=0, column=0, padx=5, pady=5)
        buttons[1].grid(row=0, column=1, padx=5, pady=5)
        buttons[2].grid(row=1, column=0, padx=5, pady=5)

    def __open_projet(self,name:str):
        if self.__fnc_work.openProjet(name):
            self.__update_etat()
            self.__view_projet_open()


    def __close_projet(self):
        self.__fnc_work.closeProjet()
        self.__guiTaskProject = None
        self.__view_projet()