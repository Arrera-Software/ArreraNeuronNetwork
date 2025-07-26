from gestionnaire.gestion import gestionnaire

class gestFNC:
    def __init__(self, gestionnaire: gestionnaire):
        # Import
        # Fichier de fonction
        from fnc.fonctionTache import fncArreraTache, CArreraDate
        from fnc.fonctionRecherche import fncArreraSearch
        # Fichier de GUI

        # ______________ Initialisation des fonctions ______________
        self.__gestionnaire = gestionnaire

        # Librairy
        self.__libDate = CArreraDate()
        # Fonction de tache
        self.__taskAssistant = fncArreraTache(self.__gestionnaire,
                                              self.__libDate,
                                              self.__gestionnaire.getEmplacemntfileTache())
        # Fonction de recherche
        self.__searchAssistant = fncArreraSearch(self.__gestionnaire)

    def __initTaskProject(self, fileTask: str):
        # Initialisation des fonctions
        from fnc.fonctionTache import fncArreraTache
        return fncArreraTache(self.__gestionnaire,self.__libDate,fileTask)

    def getFNCTask(self):
        return self.__taskAssistant

    def getFNCSearch(self):
        return self.__searchAssistant
