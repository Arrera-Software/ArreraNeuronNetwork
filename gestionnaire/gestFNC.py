from gestionnaire.gestion import gestionnaire
from fnc.fonctionCalendar import CArreraDate

class gestFNC:
    def __init__(self, gestionnaire: gestionnaire):
        conf = gestionnaire.getConfigFile()
        self.__gestionnaire = gestionnaire

        self.__lib_date = CArreraDate()

        self.__task = None
        self.__calendar = None
        self.__horloge = None
        self.__gps = None
        self.__meteo = None
        self.__actu = None
        self.__radio = None
        self.__traduction = None
        self.__brief = None
        self.__work = None
        self.__calculatrice = None
        self.__read = None
        self.__orthographe = None
        self.__search_assistant = None
        self.__open = None
        self.__downloader_youtube = None
        self.__codehelp = None

        if conf.etatTime == 1 :
            from fnc.fonctionTache import fncArreraTache  # TIME
            from fnc.fonctionCalendar import fncCalendar  # TIME
            from fnc.fonctionHorloge import fncHorloge  # TIME


            self.__task = fncArreraTache(self.__gestionnaire,
                                         self.__lib_date,
                                         self.__gestionnaire.getEmplacemntfileTache())
            self.__calendar = fncCalendar(self.__gestionnaire)
            self.__horloge = fncHorloge(self.__gestionnaire)

        if conf.etatApi == 1 :
            from fnc.fonctionGPS import fncGPS  # API
            from fnc.fonctionMeteo import fncMeteo  # API
            from fnc.fonctionActu import fncActualiter  # API
            from fnc.fonctionRadio import fncRadio  # API
            from fnc.fonctionTraduction import fncTraduction  # API
            from fnc.fonctionBrief import fncBrief  # API

            self.__gps = fncGPS(self.__gestionnaire)
            # Fonction Meteo
            self.__meteo = fncMeteo(self.__gestionnaire, self.__gps)
            # Fonction Actualité
            self.__actu = fncActualiter(self.__gestionnaire)
            # Fonction de radio
            self.__radio = fncRadio(self.__gestionnaire)
            # Fonction de traduction
            self.__traduction = fncTraduction(self.__gestionnaire)
            # Fonction brief
            self.__brief = fncBrief(self.__gestionnaire)

        if conf.etatWork == 1 :
              # WORK
            from fnc.fonctionArreraWork import fncArreraWork  # WORK

            self.__work = fncArreraWork(self.__gestionnaire)

        if conf.etatService == 1 :
            from fnc.fonctionCalculatrice import fncCalculatrice
            from fnc.fonctionLecture import fncLecture
            from fnc.fonctionOrthographe import fncOrthographe

            self.__calculatrice = fncCalculatrice(self.__gestionnaire)
            self.__read = fncLecture(self.__gestionnaire)
            self.__orthographe = fncOrthographe(self.__gestionnaire)

        if conf.etatSearch == 1 :
            from fnc.fonctionRecherche import fncArreraSearch
            self.__search_assistant = fncArreraSearch(self.__gestionnaire)

        if conf.etatOpen == 1 :
            from fnc.fonctionOPEN import fonctionOpen
            from fnc.fonctionArreraDownload import fncArreraVideoDownload
            self.__open = fonctionOpen(self.__gestionnaire)
            self.__downloader_youtube = fncArreraVideoDownload(self.__gestionnaire)

        if conf.etatCodehelp == 1 :
            from fnc.fonctionCodeHelp import fncCodehelp  # CODE HELP
            self.__codehelp = fncCodehelp(self.__gestionnaire)

    def initTaskProject(self, fileTask: str):
        # Initialisation des fonctions
        from fnc.fonctionTache import fncArreraTache
        return fncArreraTache(self.__gestionnaire, self.__lib_date, fileTask)

    def getFNCTask(self):
        return self.__task

    def getFNCSearch(self):
        return self.__search_assistant

    def getFNCDownload(self):
        return self.__downloader_youtube

    def getFNCCalendar(self):
        return self.__calendar

    def getFNCGPS(self):
        return self.__gps

    def getFNCMeteo(self):
        return self.__meteo

    def getFNCActu(self):
        return self.__actu

    def getFNCHorloge(self):
        return self.__horloge

    def getFNCRead(self):
        return self.__read

    def getFNCRadio(self):
        return self.__radio

    def getFNCTraduction(self):
        return self.__traduction

    def getFNCOrthographe(self):
        return self.__orthographe

    def getFNCCalculatrice(self):
        return self.__calculatrice

    def getFNCCodeHelp(self):
        return self.__codehelp

    def getFNCWork(self):
        return self.__work

    def getFNCOpen(self):
        return self.__open

    def getFNCBrief(self):
        return self.__brief