from gestionnaire.gestion import gestionnaire
from fnc.fonctionCalendar import CArreraDate

class gestFNC:
    def __init__(self, gestionnaire: gestionnaire):
        conf = gestionnaire.getConfigFile()
        self.__gestionnaire = gestionnaire

        self.__prompt = ""

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

            self.__prompt += """
                - "tache": Args ["action", "nom", "date(YYYY-MM-DD)", "desc"]. actions: ajouter, supprimer, terminer, reactiver, lister_tout, lister_non_terminees, lister_terminees, lister_aujourdhui, lister_demain, lister_retard, compter, compter_non_terminees, compter_terminees, compter_aujourdhui, compter_demain, compter_retard.
                - "calendrier": Args ["action", "nom", "date(YYYY-MM-DD)", "heure(HH:MM)", "desc", "lieu", "repetition(true/false)"]. actions: ajouter, supprimer, lister_tout, lister_aujourdhui, lister_date, details.
                - "horloge": Args ["action", "duree_sec"]. actions: heure, chrono_start, chrono_stop, chrono_reset, chrono_temps, chrono_etat, minuteur_start, minuteur_stop, minuteur_etat, minuteur_temps.
                """

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

            self.__prompt += """
                - "gps": Args ["action", "p1", "p2"]. actions: itineraire(p1=depart,p2=arrivee), localisation, departement(p1=ville), ville_coordonnees(p1=lat,p2=lon).
                - "meteo": Args ["moment", "emplacement", "ville_custom"]. moments: actuel, demain, matin, apres-midi, soir, nuit, alerte. emplacements: home, work, locate, custom.
                - "actu": Args ["limite"]. limite: nb articles.
                - "radio": Args ["action"]. action: stop, etat, ou nom (Europe 1, etc.).
                - "traduction": Args ["texte", "lang_source", "lang_cible"].
                - "brief": Args ["moment"]. moment: morning, afternoon, evening.
                """

        if conf.etatWork == 1 :
              # WORK
            from fnc.fonctionArreraWork import fncArreraWork  # WORK

            self.__work = fncArreraWork(self.__gestionnaire)

            self.__prompt += """
                - "work": Args ["action", "p1", "p2", "p3"]
                  > Tableur: tableur_ouvrir, tableur_ouvrir_direct(p1=chemin), tableur_fermer, tableur_lire, tableur_ecrire(p1=cell,p2=val), tableur_supprimer(p1=cell), tableur_formule(p1=op,p2=plage,p3=dest), tableur_ouvrir_os, tableur_etat.
                  > Word: word_ouvrir, word_ouvrir_direct(p1=chemin), word_fermer, word_lire, word_ecrire(p1=texte), word_ecrire_ecrase(p1=texte), word_ouvrir_os, word_etat.
                  > Projet: projet_lister, projet_creer(p1=nom), projet_ouvrir(p1=nom), projet_fermer, projet_type(p1=type), projet_nom, projet_get_type, projet_etat, projet_creer_fichier(p1=nom,p2=type), projet_lister_fichiers.
                  > Tâches proj: projet_tache_ajouter(p1=nom,p2=date,p3=desc), projet_tache_supprimer(p1=nom), projet_tache_terminer(p1=nom), projet_tache_non_terminees, projet_tache_aujourdhui, projet_tache_demain.
                """

        if conf.etatService == 1 :
            from fnc.fonctionCalculatrice import fncCalculatrice
            from fnc.fonctionLecture import fncLecture
            from fnc.fonctionOrthographe import fncOrthographe

            self.__calculatrice = fncCalculatrice(self.__gestionnaire)
            self.__read = fncLecture(self.__gestionnaire)
            self.__orthographe = fncOrthographe(self.__gestionnaire)

            self.__prompt += """
                - "calculatrice": Args ["action", "p1", "p2", "p3", "p4"]. actions: addition, soustraction, multiplication, division, puissance, modulo, racine, complexe, pythagore, pythagore_reciproque.
                - "lecture": Args ["action", "texte"]. actions: lire, etat.
                - "orthographe": Args ["action", "texte"]. actions: corriger, copier, etat.
                """

        if conf.etatSearch == 1 :
            from fnc.fonctionRecherche import fncArreraSearch
            self.__search_assistant = fncArreraSearch(self.__gestionnaire)

            self.__prompt += """
                - "recherche": Args ["moteur", "requete"]. moteurs: recherche, google, brave, duckduckgo, qwant, ecosia, bing, perplexity, amazon, big_recherche.
                """

        if conf.etatOpen == 1 :
            from fnc.fonctionOPEN import fonctionOpen
            from fnc.fonctionArreraDownload import fncArreraVideoDownload
            self.__open = fonctionOpen(self.__gestionnaire)
            self.__downloader_youtube = fncArreraVideoDownload(self.__gestionnaire)

            self.__prompt += """
                - "open": Args ["action", "cible"]. actions: logiciel, site_enregistre, url.
                - "download_youtube": Args ["mode", "url"]. modes: "1"(video), "2"(audio).
                """

        if conf.etatCodehelp == 1 :
            from fnc.fonctionCodeHelp import fncCodehelp  # CODE HELP
            self.__codehelp = fncCodehelp(self.__gestionnaire)
            self.__prompt +="""
                - "codehelp": Args ["action", "p1"]. actions: doc_devdoc, doc_microsoft, doc_python, github_search, github_site, gui_color, gui_github, gui_librairy, gui_orgavar.
                """

        self.__prompt += """
            - "reponse_simple": Par defaut. Args: []
        """

    def get_prompt(self):
        return self.__prompt

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