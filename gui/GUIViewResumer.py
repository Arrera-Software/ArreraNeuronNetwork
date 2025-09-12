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
        self.__textRead = ""

    def _mainframe(self):
        self._screen.minsize(500, 620)
        self._screen.maxsize(500, 620)

        self._screen.grid_columnconfigure(0, weight=1)
        self._screen.grid_rowconfigure(0, weight=0, minsize=25)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_rowconfigure(2, weight=0, minsize=25)

        # Frame
        topFrame = self._arrtk.createFrame(self._screen)
        labelFrame = self._arrtk.createFrame(self._screen)
        btnFrame = self._arrtk.createFrame(self._screen)

        # Conf frame
        labelFrame.grid_rowconfigure(0, weight=1)
        labelFrame.grid_columnconfigure(0, weight=1)

        # IMG
        imgLogo = self._arrtk.createImage(pathDark=self._gestionnaire.getConfigFile().icon,
                                          pathLight=self._gestionnaire.getConfigFile().icon,
                                          tailleX=50,tailleY=50)
        # Widgets
        logoLabel = self._arrtk.createLabel(topFrame,image=imgLogo)
        self.__titleLabel = self._arrtk.createLabel(topFrame,text="Resumer",ppolice="Arial",
                                                    ptaille=35,pstyle="bold")

        btnRead = self._arrtk.createButton(btnFrame,text="Lire",
                                           bg=self._btnColor,fg=self._btnTexteColor,
                                           ppolice="Arial",ptaille=20,pstyle="bold")
        btnQuit = self._arrtk.createButton(btnFrame,text="Quitter",
                                           bg=self._btnColor,fg=self._btnTexteColor,
                                           ppolice="Arial",ptaille=20,pstyle="bold",
                                           command=self._screen.destroy)
        wTextBox,self.__textBox = self._arrtk.createTextBoxScrolled(labelFrame)
        # Affichage
        logoLabel.pack(side="left", anchor="center", padx=(6, 10), pady=6)
        self.__titleLabel.pack(side="left", anchor="center", pady=6)

        btnRead.pack(side="left", anchor="center", padx=(6, 10), pady=6)
        btnQuit.pack(side="right", anchor="center", pady=6)

        wTextBox.grid(row=0, column=0, sticky="nsew")

        topFrame.grid(row=0, column=0, sticky="nsew")
        labelFrame.grid(row=1, column=0, sticky="nsew")
        btnFrame.grid(row=2, column=0, sticky="nsew")


    def __manageTexte(self, dict:dict=None,list:list=None, intIn:int=0):
        """
        12 : Reussite du resumer actulités
        18 : Resumer tache / agenda
        19 : Resumer all ok
        """
        self.__textBox.configure(state="normal")
        match intIn:
            case 12:
                if dict is not None:
                    actu = dict["actu"]
                    meteo = dict["meteo"]

                    texteMeteo = f"La météo actuelle à {meteo['ville']} est de {meteo['temperature']}°C avec {meteo['weather']}.\n"
                    texteActu = "Voici les dernières actualités :\n\n"

                    for i in actu:
                        texteActu += f"- {i}\n"

                    self.__textBox.delete(1.0, "end")
                    self.__textBox.insert("end", f"{texteActu}\n")
                    self.__textBox.insert("end", texteMeteo)
                    self.__textBox.configure(state="disabled",font=("Arial", 20,"normal"))
                    self.__textRead = f"{texteActu} {texteMeteo}"
                    return True
                else:
                    return False
            case 18:
                if list is not None:
                    task = list
                    texteTask = "Voici les tache qui reste a faire : \n\n"
                    if len(task) == 0:
                        texteTask = "Aucune tache a faire !"
                    else:
                        for i in task:
                            texteTask += f"- {i}\n"

                    self.__textBox.delete(1.0, "end")
                    self.__textBox.insert("end", texteTask)
                    self.__textBox.configure(state="disabled",font=("Arial", 20,"normal"))
                    self.__textRead = texteTask
                    return True
                else:
                    return False
            case 19:
                if dict is not None:
                    actu = dict["actu"]
                    meteo = dict["meteo"]
                    task = dict["task"]

                    texteActu = "Voici les dernières actualités :\n\n"
                    for i in actu:
                        texteActu += f"- {i}\n"
                    texteMeteo = f"La météo actuelle à {meteo['ville']} est de {meteo['temperature']}°C avec {meteo['weather']}.\n"
                    texteTask = "\nVoici les tache qui reste a faire : \n\n"
                    if len(task) == 0:
                        texteTask = "Aucune tache a faire !"
                    else:
                        for i in task:
                            texteTask += f"- {i}\n"

                    self.__textBox.delete(1.0, "end")
                    self.__textBox.insert("end", texteActu+"\n"+texteMeteo+"\n"+texteTask)
                    self.__textBox.configure(state="disabled",font=("Arial", 20,"normal"))
                    self.__textRead = f"{texteActu} {texteMeteo} {texteTask}"
                    return True
                else :
                    self.__textBox.configure(state="disabled",font=("Arial", 20,"normal"))
                    return False
            case _:
                self.__textBox.configure(state="disabled",font=("Arial", 20,"normal"))
                return False

    def activeView(self,dict:dict=None,list:list=None, intIn:int=0):
        self.active()
        self.__manageTexte(dict,list,intIn)