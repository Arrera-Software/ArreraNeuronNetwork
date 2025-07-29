from gestionnaire.gestion import gestionnaire

class gestFNC:
    def __init__(self, gestionnaire: gestionnaire):
        # Import
        # Fichier de fonction
        from fnc.fonctionTache import fncArreraTache, CArreraDate
        from fnc.fonctionRecherche import fncArreraSearch
        from fnc.fonctionArreraDownload import fncArreraVideoDownload
        from fnc.fonctionCalendar import fncCalendar
        from fnc.fonctionGPS import fncGPS
        from fnc.fonctionMeteo import fncMeteo
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
        # Fonction de telechargement de video youtube
        self.__downloaderYoutube = fncArreraVideoDownload(self.__gestionnaire)
        # Fonction Agenda
        self.__calendar = fncCalendar(self.__gestionnaire)
        # Fonction GPS
        self.__gps = fncGPS(self.__gestionnaire)
        # Fonction Meteo
        self.__meteo = fncMeteo(self.__gestionnaire,self.__gps)

    def __initTaskProject(self, fileTask: str):
        # Initialisation des fonctions
        from fnc.fonctionTache import fncArreraTache
        return fncArreraTache(self.__gestionnaire,self.__libDate,fileTask)

    def getFNCTask(self):
        return self.__taskAssistant

    def getFNCSearch(self):
        return self.__searchAssistant

    def getFNCDownload(self):
        return self.__downloaderYoutube

    def getFNCCalendar(self):
        return self.__calendar

    def getFNCGPS(self):
        return self.__gps

    def getFNCMeteo(self):
        return self.__meteo
