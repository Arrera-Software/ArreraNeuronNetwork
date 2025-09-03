from gui.guibase import GuiBase,gestionnaire
import customtkinter as ctk
import tkinter as tk

class GUITache(GuiBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire,"Tache")

    def _mainframe(self):

        frameTitle = self._arrtk.createFrame(self._screen,bg="red")
        self.__frameTask = self._arrtk.createFrame(self._screen,bg="green")

        # Widgets
        labelLogo = self._arrtk.createLabel(frameTitle,text="LOGO")
        labelTitle = self._arrtk.createLabel(frameTitle,text=self._gestionnaire.getName()+" : Tâches",
                                             ppolice="Arial",ptaille=20,pstyle="bold")
        btnAddTask = self._arrtk.createButton(frameTitle,text="Ajouter une tâche")
        btnDelTask = self._arrtk.createButton(frameTitle,text="Supprimer une tâche")

        # Placement
        # Widget
        labelLogo.pack(side="left", padx=(10, 5))
        labelTitle.pack(side="left", padx=(5, 10))
        btnDelTask.pack(side="right", padx=(5, 10))
        btnAddTask.pack(side="right", padx=(10, 5))
        # Frame
        frameTitle.pack(side="top", fill="x", pady=(0, 2))
        self.__frameTask.pack(side="top", fill="both", expand=True, pady=(2, 2))
        self.__viewTask()

    def __viewTask(self):
        # ta liste de tâches
        tasks = [
            "Préparer le rapport",
            "Envoyer l'email client",
            "Nettoyer les logs",
            "Backup de la DB",
            "Planifier la réunion",
            "Revue de code",
            "Mettre à jour la doc",
            "Tester la feature X",
            "Analyser les métriques",
            "Corriger le bug Y",
            "Rédiger le changelog",
            "Déployer en staging",
            "Préparer le rapport",
            "Envoyer l'email client",
            "Nettoyer les logs",
            "Backup de la DB",
            "Planifier la réunion",
            "Revue de code",
            "Mettre à jour la doc",
            "Tester la feature X",
            "Analyser les métriques",
            "Corriger le bug Y",
            "Rédiger le changelog",
            "Déployer en staging",
        ]

        # 1) nettoyer le frame si déjà utilisé
        for w in self.__frameTask.winfo_children():
            w.destroy()

        # 2) faire en sorte que le frame parent grandisse correctement
        self.__frameTask.grid_rowconfigure(0, weight=1)
        self.__frameTask.grid_columnconfigure(0, weight=1)

        # 3) un unique conteneur scrollable, toujours
        container = ctk.CTkScrollableFrame(
            master=self.__frameTask,
            fg_color="transparent",  # ton frame parent est vert, on garde le fond
        )
        container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # 4) les colonnes du conteneur prennent la largeur
        container.grid_columnconfigure(0, weight=1)

        # 5) créer les checkboxes
        self._task_vars = []  # pour relire l'état plus tard
        for i, label in enumerate(tasks):
            var = tk.BooleanVar(value=False)
            cb = ctk.CTkCheckBox(container, text=label, variable=var)
            cb.grid(row=i, column=0, sticky="w", padx=8, pady=(0, 4))
            self._task_vars.append(var)