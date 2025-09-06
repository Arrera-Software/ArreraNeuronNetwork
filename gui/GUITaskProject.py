from gui.GUITache import GUITache,gestionnaire
from fnc.fonctionTache import fncArreraTache

class GUITaskProject(GUITache):
    def __init__(self, gestionnaire:gestionnaire,nameProject:str,fncTask:fncArreraTache):
        super().__init__(gestionnaire)
        self._fncTask = fncTask
        self._title = f"{self._gestionnaire.getName()} : {nameProject} tâches"