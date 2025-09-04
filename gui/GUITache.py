from gui.guibase import GuiBase,gestionnaire
import customtkinter as ctk
import tkinter as tk

from tkcalendar import Calendar
from datetime import date

class GUITache(GuiBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire,"Tache")
        self._fnctask = self._gestionnaire.getGestFNC().getFNCTask()

    def _mainframe(self):
        # Var 
        self.__varAddDescription = tk.BooleanVar(value=False)
        self.__varAddDate = tk.BooleanVar(value=False)
        # Frame
        frameTitle = self._arrtk.createFrame(self._screen,bg="red")
        self.__frameTask = self._arrtk.createFrame(self._screen,bg="green")

        self.__frameAdd = self._arrtk.createFrame(self._screen, bg="blue")
        self.__frameAddTask = self._arrtk.createFrame(self.__frameAdd, bg="orange")
        self.__frameAddTaskDescription = self._arrtk.createFrame(self.__frameAdd, bg="orange")
        self.__frameAddTaskDate = self._arrtk.createFrame(self.__frameAdd, bg="purple")
        frameBTNAdd = self._arrtk.createFrame(self.__frameAddTask, bg="yellow")
        frameBTNAddDescription = self._arrtk.createFrame(self.__frameAddTaskDescription,bg="yellow")
        frameBTNAddDate = self._arrtk.createFrame(self.__frameAddTaskDate,bg="yellow")

        # Config

        self.__frameAdd.rowconfigure(0, weight=1)
        self.__frameAdd.columnconfigure(0, weight=1)

        self.__frameAddTask.columnconfigure(0, weight=1)
        self.__frameAddTask.rowconfigure(4, weight=1)

        frameBTNAdd.columnconfigure(0, weight=1)
        frameBTNAdd.columnconfigure(1, weight=1)

        self.__frameAddTaskDescription.columnconfigure(0, weight=1)
        self.__frameAddTaskDescription.rowconfigure(1, weight=1)
        self.__frameAddTaskDescription.rowconfigure(3, weight=1)

        frameBTNAddDescription.columnconfigure(0, weight=1)
        frameBTNAddDescription.columnconfigure(1, weight=1)

        self.__frameAddTaskDate.columnconfigure(0, weight=1)
        self.__frameAddTaskDate.rowconfigure(1, weight=1)
        self.__frameAddTaskDate.rowconfigure(3, weight=1)

        frameBTNAddDate.columnconfigure(0, weight=1)
        frameBTNAddDate.columnconfigure(1, weight=1)

        # Widgets
        labelLogo = self._arrtk.createLabel(frameTitle,text="LOGO")
        labelTitle = self._arrtk.createLabel(frameTitle,text=self._gestionnaire.getName()+" : Tâches",
                                             ppolice="Arial",ptaille=20,pstyle="bold")
        btnAddTask = self._arrtk.createButton(frameTitle,text="Ajouter une tâche",command=self.__viewAddTask)
        btnDelTask = self._arrtk.createButton(frameTitle,text="Supprimer une tâche")
        self.__btnFinishTask = self._arrtk.createButton(frameTitle,text="Voir les tâches finies")

        # Add task frame
        # Add
        labelTitleAddTask = self._arrtk.createLabel(self.__frameAddTask, text="Ajouter une tâche",
                                                    ppolice="Arial", ptaille=35, pstyle="bold")
        widgetName,self.__entryNameTask = self._arrtk.createEntryLegend(self.__frameAddTask, text="Nom de la tache : ", ppolice="Arial",
                                                                        ptaille=20, gridUsed=True)
        btnAddDate = self._arrtk.createCheckbox(self.__frameAddTask, text="Ajouter une date",
                                                var_chk=self.__varAddDate)
        btnAddDescription = self._arrtk.createCheckbox(self.__frameAddTask, text="Ajouter une description",
                                                       var_chk=self.__varAddDescription)
        btnCancelAddTask = self._arrtk.createButton(frameBTNAdd,text="Annuler",command=self.__addNewTask)
        btnConfirmAddTask = self._arrtk.createButton(frameBTNAdd,text="Confirmer",command=self.__backMAinAddTask)

        # Description
        labelAddTaskDescription = self._arrtk.createLabel(self.__frameAddTaskDescription,text="Ajouter un description a la tache",
                                                          ppolice="Arial",ptaille=35,pstyle="bold")
        wDescription,self.__entryDescription = self._arrtk.createEntryLegend(self.__frameAddTaskDescription,text="Description de la tache :",
                                                                ppolice="Arial",ptaille=25)
        self.__btnConfirmAddDescription = self._arrtk.createButton(frameBTNAddDescription,text="Confirmer")
        btnCancelAddDescription = self._arrtk.createButton(frameBTNAddDescription,text="Annuler")

        # Date
        labelAddTaskDate = self._arrtk.createLabel(self.__frameAddTaskDate,text="Ajouter une date a la tache",
                                                          ppolice="Arial",ptaille=35,pstyle="bold")
        wDate = Calendar(self.__frameAddTaskDate,selectmode="day",year=date.today().year,
                         month=date.today().month,locale="fr_FR",firstweekday="monday",showweeknumbers=False,
                         borderwidth=0)
        self.__btnConfirmAddDate = self._arrtk.createButton(frameBTNAddDate,text="Confirmer")
        btnCancelAddDate = self._arrtk.createButton(frameBTNAddDate,text="Annuler")

        # Placement
        # Widget
        labelLogo.pack(side="left", padx=(10, 5))
        labelTitle.pack(side="left", padx=(5, 10))
        self.__btnFinishTask.pack(side="right", padx=(5, 10))
        btnDelTask.pack(side="right", padx=(5, 10))
        btnAddTask.pack(side="right", padx=(10, 5))

        labelTitleAddTask.grid(row=0, column=0, sticky="n", pady=(10, 8))
        widgetName.grid(row=1, column=0, sticky="ew", padx=10, pady=(2, 8))
        btnAddDate.grid(row=2, column=0, sticky="w", padx=10, pady=(0, 8))
        btnAddDescription.grid(row=3, column=0, sticky="w", padx=10, pady=(0, 8))

        frameBTNAdd.grid(row=5, column=0, sticky="ew", padx=10, pady=(8, 10))

        btnCancelAddTask.grid(row=0, column=0, sticky="w", padx=(0, 5))
        btnConfirmAddTask.grid(row=0, column=1, sticky="e", padx=(5, 0))

        labelAddTaskDescription.grid(row=0, column=0, sticky="n", pady=(10, 8))
        wDescription.grid(row=2, column=0, sticky="w", padx=10)

        frameBTNAddDescription.grid(row=4, column=0, sticky="ew", padx=10, pady=(8, 10))

        btnCancelAddDescription.grid(row=0, column=0, sticky="w", padx=(0, 5))
        self.__btnConfirmAddDescription.grid(row=0, column=1, sticky="e", padx=(5, 0))

        labelAddTaskDate.grid(row=0, column=0, sticky="n", pady=(10, 8))
        wDate.grid_configure(row=2, column=0, sticky="", padx=10)

        frameBTNAddDate.grid(row=4, column=0, sticky="ew", padx=10, pady=(8, 10))

        self.__btnConfirmAddDate.grid(row=0, column=0, sticky="w", padx=(0, 5))
        btnCancelAddDate.grid(row=0, column=1, sticky="e", padx=(5, 0))
        # Frame
        frameTitle.pack(side="top", fill="x", pady=(0, 2))
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__viewTaskNoFinish()

    def __disableAllFrame(self):
        self.__frameTask.pack_forget()
        self.__frameAdd.pack_forget()

    def __viewTaskNoFinish(self):
        self.__disableAllFrame()
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
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
        self.__disableAllFrame()
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
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

    def __viewAddTask(self):
        self.__disableAllFrame()
        self.__varAddDate.set(False)
        self.__varAddDescription.set(False)
        self.__entryNameTask.delete(0, tk.END)
        self.__frameAddTaskDate.grid_forget()
        self.__frameAddTaskDescription.grid_forget()
        self.__frameAdd.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__frameAddTask.grid(row=0, column=0, sticky="nsew")

    def __addNewTask(self):
        pass

    def __backMAinAddTask(self):
        pass