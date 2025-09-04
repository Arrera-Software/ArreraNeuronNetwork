from gui.guibase import GuiBase,gestionnaire
import customtkinter as ctk
import tkinter as tk

class GUITache(GuiBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire,"Tache")
        self._fnctask = self._gestionnaire.getGestFNC().getFNCTask()

    def _mainframe(self):

        frameTitle = self._arrtk.createFrame(self._screen,bg="red")
        self.__frameTask = self._arrtk.createFrame(self._screen,bg="green")

        # Widgets
        labelLogo = self._arrtk.createLabel(frameTitle,text="LOGO")
        labelTitle = self._arrtk.createLabel(frameTitle,text=self._gestionnaire.getName()+" : Tâches",
                                             ppolice="Arial",ptaille=20,pstyle="bold")
        btnAddTask = self._arrtk.createButton(frameTitle,text="Ajouter une tâche")
        btnDelTask = self._arrtk.createButton(frameTitle,text="Supprimer une tâche")
        self.__btnFinishTask = self._arrtk.createButton(frameTitle,text="Voir les tâches finies")

        # Placement
        # Widget
        labelLogo.pack(side="left", padx=(10, 5))
        labelTitle.pack(side="left", padx=(5, 10))
        self.__btnFinishTask.pack(side="right", padx=(5, 10))
        btnDelTask.pack(side="right", padx=(5, 10))
        btnAddTask.pack(side="right", padx=(10, 5))
        # Frame
        frameTitle.pack(side="top", fill="x", pady=(0, 2))
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__viewTaskNoFinish()

    def __viewTaskNoFinish(self):
        # ta liste de tâches
        tasks = self._fnctask.getNoFinishTask()

        self.__btnFinishTask.configure(text="Voir les tâches finies",
                                       command=self.__viewTaskFinish)

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameTask.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameTask.grid_rowconfigure(0, weight=1)
        self.__frameTask.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        if len(tasks) != 0:
            container = self._arrtk.createScrollFrame(self.__frameTask,bg="transparent")
            container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            # 4) les colonnes du conteneur prennent la largeur
            container.grid_columnconfigure(0, weight=1)

            # 5) créer les checkboxes
            self._task_vars = []  # pour relire l'état plus tard
            for i, label in enumerate(tasks):
                var = tk.BooleanVar(value=False)
                cb = self._arrtk.createCheckbox(container, text=label,
                                                var_chk=var,
                                                command=lambda :self.__finishTask(var, label))
                cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
                self._task_vars.append(var)
        else:
            labelNoTask = self._arrtk.createLabel(self.__frameTask,text="Aucune tâche pour le moment",
                                                  ppolice="Arial",ptaille=40,pstyle="bold")
            labelNoTask.pack(pady=20)

    def __finishTask(self, var:tk.BooleanVar, name:str):
        if var.get():
            self._fnctask.finishTask(name)
            self.__viewTaskNoFinish()

    def __viewTaskFinish(self):
        # ta liste de tâches
        tasks = self._fnctask.getFinishTask()

        self.__btnFinishTask.configure(text="Voir les tâches non finies",
                                       command=self.__viewTaskNoFinish)

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameTask.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameTask.grid_rowconfigure(0, weight=1)
        self.__frameTask.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        if len(tasks) != 0:
            container = self._arrtk.createScrollFrame(self.__frameTask,bg="transparent")
            container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            # 4) les colonnes du conteneur prennent la largeur
            container.grid_columnconfigure(0, weight=1)

            # 5) créer les checkboxes
            self._task_vars = []  # pour relire l'état plus tard
            for i, label in enumerate(tasks):
                var = tk.BooleanVar(value=True)
                cb = self._arrtk.createCheckbox(container, text=label,
                                                var_chk=var,
                                                command=lambda :self.__unfinishTask(var, label))
                cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
                self._task_vars.append(var)
        else:
            labelNoTask = self._arrtk.createLabel(self.__frameTask,text="Aucune tâche fini pour le moment",
                                                  ppolice="Arial",ptaille=40,pstyle="bold")
            labelNoTask.pack(pady=20)

    def __unfinishTask(self, var:tk.BooleanVar, name:str):
        if not var.get():
            self._fnctask.unfinishTask(name)
            self.__viewTaskFinish()