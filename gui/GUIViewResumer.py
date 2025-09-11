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

        self._screen.grid_columnconfigure(0, weight=1)
        self._screen.grid_rowconfigure(0, weight=0, minsize=25)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_rowconfigure(2, weight=0, minsize=25)

        # Frame
        topFrame = self._arrtk.createFrame(self._screen,bg="red")
        labelFrame = self._arrtk.createFrame(self._screen,bg="blue")
        btnFrame = self._arrtk.createFrame(self._screen,bg="green")

        # IMG
        imgLogo = self._arrtk.createImage(pathDark=self._gestionnaire.getConfigFile().icon,
                                          pathLight=self._gestionnaire.getConfigFile().icon,
                                          tailleX=50,tailleY=50)
        # Widgets
        logoLabel = self._arrtk.createLabel(topFrame,image=imgLogo)
        self.__titleLabel = self._arrtk.createLabel(topFrame,text="Resumer",ppolice="Arial",
                                                    ptaille=35,pstyle="bold")

        # Affichage
        logoLabel.pack(side="left", anchor="center", padx=(6, 10), pady=6)
        self.__titleLabel.pack(side="left", anchor="center", pady=6)

        topFrame.grid(row=0, column=0, sticky="nsew")
        labelFrame.grid(row=1, column=0, sticky="nsew")
        btnFrame.grid(row=2, column=0, sticky="nsew")
