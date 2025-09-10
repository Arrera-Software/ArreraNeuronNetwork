"""
11 : Erreur du resumer actulités
12 : Reussite du resumer actulités
18 : Resumer tache / agenda
19 : Resumer all ok
20 : Resumer all fail
"""
from gui.guibase import GuiBase,gestionnaire

class GUIViewResumer(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Resumer")

    def _mainframe(self):
        self._screen.minsize(500, 620)
        self._screen.maxsize(500, 620)

        self._screen.grid_columnconfigure(0, weight=1)     # 1 seule colonne, qui s’étire
        self._screen.grid_rowconfigure(0, weight=0, minsize=25)  # rangée du haut: petite hauteur (50 px)
        self._screen.grid_rowconfigure(1, weight=1)

        # Frame
        topFrame = self._arrtk.createFrame(self._screen,bg="red")
        labelFrame = self._arrtk.createFrame(self._screen,bg="blue")

        # Affichage
        topFrame.grid(row=0, column=0, sticky="nsew")    # pleine largeur, faible hauteur
        labelFrame.grid(row=1, column=0, sticky="nsew")
