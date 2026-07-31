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
                - "tache" : Gérer les tâches (ajouter, supprimer, terminer, réactiver, lister).
                    Arguments : ["type_action", "nom_tache", "date_tache", "description_tache"]
                    > Si ajouter une tâche : type_action="ajouter", nom_tache="nom de la tâche", date_tache="YYYY-MM-DD" (optionnel, "" si pas de date), description_tache="description" (optionnel, "" si pas de description).
                    > Si supprimer une tâche : type_action="supprimer", nom_tache="nom de la tâche", date_tache="", description_tache="".
                    > Si marquer une tâche comme terminée : type_action="terminer", nom_tache="nom de la tâche", date_tache="", description_tache="".
                    > Si réactiver une tâche (la remettre non terminée) : type_action="reactiver", nom_tache="nom de la tâche", date_tache="", description_tache="".
                    > Si lister toutes les tâches : type_action="lister_tout", nom_tache="", date_tache="", description_tache="".
                    > Si lister les tâches non terminées : type_action="lister_non_terminees", nom_tache="", date_tache="", description_tache="".
                    > Si lister les tâches terminées : type_action="lister_terminees", nom_tache="", date_tache="", description_tache="".
                    > Si lister les tâches du jour : type_action="lister_aujourdhui", nom_tache="", date_tache="", description_tache="".
                    > Si lister les tâches de demain : type_action="lister_demain", nom_tache="", date_tache="", description_tache="".
                    > Si lister les tâches en retard : type_action="lister_retard", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches (combien de tâches) : type_action="compter", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches non terminées : type_action="compter_non_terminees", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches terminées : type_action="compter_terminees", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches du jour : type_action="compter_aujourdhui", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches de demain : type_action="compter_demain", nom_tache="", date_tache="", description_tache="".
                    > Si compter les tâches en retard : type_action="compter_retard", nom_tache="", date_tache="", description_tache="".
                - "calendrier" : Gérer l'agenda et les événements (ajouter, supprimer, consulter).
                    Arguments : ["type_action", "nom_event", "date_event", "heure_event", "description_event", "lieu_event", "repetition"]
                    > Si ajouter un événement : type_action="ajouter", nom_event="nom de l'événement", date_event="YYYY-MM-DD", heure_event="HH:MM" (optionnel, "" si pas d'heure), description_event="description" (optionnel, ""), lieu_event="lieu" (optionnel, ""), repetition="true" ou "false" (optionnel, "false" par défaut).
                    > Si supprimer un événement : type_action="supprimer", nom_event="nom de l'événement", date_event="", heure_event="", description_event="", lieu_event="", repetition="".
                    > Si lister tous les événements : type_action="lister_tout", nom_event="", date_event="", heure_event="", description_event="", lieu_event="", repetition="".
                    > Si lister les événements du jour : type_action="lister_aujourdhui", nom_event="", date_event="", heure_event="", description_event="", lieu_event="", repetition="".
                    > Si lister les événements d'une date précise : type_action="lister_date", nom_event="", date_event="YYYY-MM-DD", heure_event="", description_event="", lieu_event="", repetition="".
                    > Si obtenir les détails d'un événement : type_action="details", nom_event="nom de l'événement", date_event="", heure_event="", description_event="", lieu_event="", repetition="".
                - "horloge" : Donner l'heure, gérer le chronomètre ou le minuteur.
                    Arguments : ["type_action", "duree_secondes"]
                    > Si donner l'heure actuelle : type_action="heure", duree_secondes="".
                    > Si démarrer le chronomètre : type_action="chrono_start", duree_secondes="".
                    > Si arrêter le chronomètre : type_action="chrono_stop", duree_secondes="".
                    > Si réinitialiser le chronomètre : type_action="chrono_reset", duree_secondes="".
                    > Si lire le temps du chronomètre : type_action="chrono_temps", duree_secondes="".
                    > Si vérifier si le chronomètre tourne : type_action="chrono_etat", duree_secondes="".
                    > Si démarrer un minuteur : type_action="minuteur_start", duree_secondes="nombre de secondes" (ex: "300" pour 5 minutes). L'IA DOIT convertir les minutes/heures en secondes.
                    > Si arrêter le minuteur : type_action="minuteur_stop", duree_secondes="".
                    > Si vérifier si le minuteur tourne : type_action="minuteur_etat", duree_secondes="".
                    > Si lire le temps restant du minuteur : type_action="minuteur_temps", duree_secondes="".
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
                - "gps" : Trouver une localisation, lancer un itinéraire, obtenir le département d'une ville ou trouver une ville par ses coordonnées GPS.
                    Arguments : ["type_action", "param1", "param2"]
                    > Si itinéraire : type_action="itineraire", param1="ville de départ", param2="ville d'arrivée".
                    > Si localisation : type_action="localisation", param1="", param2="".
                    > Si département : type_action="departement", param1="nom de la ville", param2="".
                    > Si trouver une ville par coordonnées : type_action="ville_coordonnees", param1="latitude", param2="longitude".
                - "meteo" : Obtenir les prévisions météorologiques ou les alertes de vigilance.
                    Arguments : ["moment", "emplacement", "ville_custom"]
                    > moment : "actuel", "demain", "matin", "apres-midi", "soir", "nuit" ou "alerte" (vigilances météo en cours).
                    > emplacement : "home" (domicile), "work" (travail), "locate" (position actuelle) ou "custom" (ville précise).
                    > ville_custom : Le nom de la ville uniquement si emplacement est "custom" (sinon "").
                - "actu" : Obtenir les dernières actualités (généraliste, tech, science, sport, culture).
                    Arguments : ["limite"]
                    > limite : nombre d'articles par source (optionnel, "3" par défaut).
                - "radio" : Lancer, arrêter ou vérifier l'état d'une station de radio.
                    Arguments : ["action_radio"]
                    > action_radio : "stop" (pour arrêter), "etat" (pour vérifier si une radio joue) OU le nom exact de la radio parmi : "Europe 1", "Europe 2", "France Info", "France inter", "France Musique", "France Culture", "France bleu", "Fun radio", "NRJ", "RFM", "Nostalgie", "Skyrock", "RTL".
                - "traduction" : Traduire un mot ou une phrase.
                    Arguments : ["texte_a_traduire", "langue_source", "langue_cible"]
                    > langues supportées : "anglais", "francais", "espagnol", "allemand", "chinois simplifie", "chinois traditionnel", "arabe", "russe", "japonais", "coreen", "italien", "portugais", "neerlandais", "suedois", "danois", "norvegien", "finnois", "grec", "hebreu", "indonesien".
                    > Si la langue source n'est pas précisée par l'utilisateur, utiliser "francais".
                - "brief" : Faire un brief global (météo + tâches + actualités) selon le moment de la journée.
                    Arguments : ["moment_journee"]
                    > moment_journee : "morning" (matin), "afternoon" (après-midi) ou "evening" (soir).
                """

        if conf.etatWork == 1 :
              # WORK
            from fnc.fonctionArreraWork import fncArreraWork  # WORK

            self.__work = fncArreraWork(self.__gestionnaire)

            self.__prompt += """
                - "work" : Gérer l'espace de travail : tableur (Excel), document (Word/ODT), et projets.
                    Arguments : ["type_action", "param1", "param2", "param3"]
                    --- TABLEUR (Excel) ---
                    > Ouvrir un tableur (dialogue fichier) : type_action="tableur_ouvrir", param1="", param2="", param3="".
                    > Ouvrir un tableur directement par chemin : type_action="tableur_ouvrir_direct", param1="chemin du fichier .xlsx", param2="", param3="".
                    > Fermer le tableur : type_action="tableur_fermer", param1="", param2="", param3="".
                    > Lire le contenu du tableur : type_action="tableur_lire", param1="", param2="", param3="".
                    > Écrire une valeur dans une cellule : type_action="tableur_ecrire", param1="cellule (ex: A1)", param2="valeur à écrire", param3="".
                    > Supprimer une valeur d'une cellule : type_action="tableur_supprimer", param1="cellule (ex: A1)", param2="", param3="".
                    > Appliquer une formule (somme, moyenne, comptage, minimum, maximum) : type_action="tableur_formule", param1="nom de la formule" (parmi : "somme", "moyenne", "comptage", "minimum", "maximum"), param2="cellule de début:cellule de fin" (ex: "A1:A10"), param3="cellule de destination (ex: B1)".
                    > Ouvrir le tableur dans l'application du système : type_action="tableur_ouvrir_os", param1="", param2="", param3="".
                    > Vérifier si un tableur est ouvert : type_action="tableur_etat", param1="", param2="", param3="".
                    --- DOCUMENT (Word/ODT) ---
                    > Ouvrir un document (dialogue fichier) : type_action="word_ouvrir", param1="", param2="", param3="".
                    > Ouvrir un document directement par chemin : type_action="word_ouvrir_direct", param1="chemin du fichier", param2="", param3="".
                    > Fermer le document : type_action="word_fermer", param1="", param2="", param3="".
                    > Lire le contenu du document : type_action="word_lire", param1="", param2="", param3="".
                    > Écrire du texte dans le document (ajout) : type_action="word_ecrire", param1="texte à écrire", param2="", param3="".
                    > Écrire du texte dans le document (remplace tout le contenu) : type_action="word_ecrire_ecrase", param1="texte à écrire", param2="", param3="".
                    > Ouvrir le document dans l'application du système : type_action="word_ouvrir_os", param1="", param2="", param3="".
                    > Vérifier si un document est ouvert : type_action="word_etat", param1="", param2="", param3="".
                    --- PROJET ---
                    > Lister tous les projets existants : type_action="projet_lister", param1="", param2="", param3="".
                    > Créer un nouveau projet : type_action="projet_creer", param1="nom du projet", param2="", param3="".
                    > Ouvrir un projet existant : type_action="projet_ouvrir", param1="nom du projet", param2="", param3="".
                    > Fermer le projet en cours : type_action="projet_fermer", param1="", param2="", param3="".
                    > Définir le type du projet : type_action="projet_type", param1="type du projet" (parmi : "Développement d'application web", "Développement d'application desktop", "Développement d'application mobile", "Électronique", "Électrique", "Système embarqué", "Développement de jeux vidéo", "Écriture de livre"), param2="", param3="".
                    > Obtenir le nom du projet ouvert : type_action="projet_nom", param1="", param2="", param3="".
                    > Obtenir le type du projet ouvert : type_action="projet_get_type", param1="", param2="", param3="".
                    > Vérifier si un projet est ouvert : type_action="projet_etat", param1="", param2="", param3="".
                    > Créer un fichier dans le projet : type_action="projet_creer_fichier", param1="nom du fichier (sans extension)", param2="type de fichier" (parmi : "excel", "word", "Open Document Texte", "markdown", "Arrera Postite"), param3="".
                    > Lister les fichiers du projet : type_action="projet_lister_fichiers", param1="", param2="", param3="".
                    --- TÂCHES DU PROJET (projet doit être ouvert) ---
                    > Ajouter une tâche au projet : type_action="projet_tache_ajouter", param1="nom de la tâche", param2="YYYY-MM-DD" (optionnel, "" si pas de date), param3="description" (optionnel, "").
                    > Supprimer une tâche du projet : type_action="projet_tache_supprimer", param1="nom de la tâche", param2="", param3="".
                    > Terminer une tâche du projet : type_action="projet_tache_terminer", param1="nom de la tâche", param2="", param3="".
                    > Lister les tâches non terminées du projet : type_action="projet_tache_non_terminees", param1="", param2="", param3="".
                    > Lister les tâches du jour du projet : type_action="projet_tache_aujourdhui", param1="", param2="", param3="".
                    > Lister les tâches de demain du projet : type_action="projet_tache_demain", param1="", param2="", param3="".
                """

        if conf.etatService == 1 :
            from fnc.fonctionCalculatrice import fncCalculatrice
            from fnc.fonctionLecture import fncLecture
            from fnc.fonctionOrthographe import fncOrthographe

            self.__calculatrice = fncCalculatrice(self.__gestionnaire)
            self.__read = fncLecture(self.__gestionnaire)
            self.__orthographe = fncOrthographe(self.__gestionnaire)

            self.__prompt += """
                - "calculatrice" : Effectuer un calcul mathématique (opérations de base, nombres complexes, théorème de Pythagore).
                    Arguments : ["type_calcul", "param1", "param2", "param3", "param4"]
                    --- Opérations de base ---
                    > Addition : type_calcul="addition", param1="nombre1", param2="nombre2", param3="", param4="".
                    > Soustraction : type_calcul="soustraction", param1="nombre1", param2="nombre2", param3="", param4="".
                    > Multiplication : type_calcul="multiplication", param1="nombre1", param2="nombre2", param3="", param4="".
                    > Division : type_calcul="division", param1="nombre1", param2="nombre2", param3="", param4="".
                    > Puissance : type_calcul="puissance", param1="base", param2="exposant", param3="", param4="".
                    > Modulo (reste de la division) : type_calcul="modulo", param1="nombre1", param2="nombre2", param3="", param4="".
                    > Racine : type_calcul="racine", param1="nombre", param2="indice de la racine (ex: 2 pour racine carrée)", param3="", param4="".
                    --- Nombres complexes ---
                    > Opération sur nombres complexes : type_calcul="complexe", param1="partie réelle du 1er nombre", param2="partie imaginaire du 1er nombre", param3="partie réelle du 2ème nombre", param4="partie imaginaire du 2ème nombre".
                      L'opération complexe à effectuer sera déduite de la demande de l'utilisateur. Si addition complexe, ajouter un 5ème argument : "addition", "soustraction", "multiplication" ou "division".
                    --- Théorème de Pythagore ---
                    > Calculer l'hypoténuse (théorème de Pythagore) : type_calcul="pythagore", param1="côté 1", param2="côté 2", param3="", param4="".
                    > Calculer un côté manquant (réciproque de Pythagore) : type_calcul="pythagore_reciproque", param1="hypoténuse", param2="côté connu", param3="", param4="".
                - "lecture" : Lire un texte à voix haute (synthèse vocale).
                    Arguments : ["type_action", "texte"]
                    > Lire un texte : type_action="lire", texte="le texte à lire à voix haute".
                    > Vérifier si une lecture est en cours : type_action="etat", texte="".
                - "orthographe" : Corriger l'orthographe et la grammaire d'un texte.
                    Arguments : ["type_action", "texte"]
                    > Corriger un texte : type_action="corriger", texte="le texte à corriger".
                    > Copier la correction dans le presse-papiers : type_action="copier", texte="".
                    > Vérifier si l'outil est disponible : type_action="etat", texte="".
                """

        if conf.etatSearch == 1 :
            from fnc.fonctionRecherche import fncArreraSearch
            self.__search_assistant = fncArreraSearch(self.__gestionnaire)

            self.__prompt += """
                - "recherche" : Faire une recherche sur internet.
                    Arguments : ["type_recherche", "requete"]
                    > Recherche avec le moteur par défaut de l'utilisateur : type_recherche="recherche", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Google : type_recherche="google", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Brave : type_recherche="brave", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur DuckDuckGo : type_recherche="duckduckgo", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Qwant : type_recherche="qwant", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Ecosia : type_recherche="ecosia", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Bing : type_recherche="bing", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Perplexity : type_recherche="perplexity", requete="ce que l'utilisateur veut chercher".
                    > Recherche sur Amazon : type_recherche="amazon", requete="produit ou objet recherché".
                    > Grande recherche (ouvre Google, Qwant, DuckDuckGo, Bing et Perplexity en même temps) : type_recherche="big_recherche", requete="ce que l'utilisateur veut chercher".
                """

        if conf.etatOpen == 1 :
            from fnc.fonctionOPEN import fonctionOpen
            from fnc.fonctionArreraDownload import fncArreraVideoDownload
            self.__open = fonctionOpen(self.__gestionnaire)
            self.__downloader_youtube = fncArreraVideoDownload(self.__gestionnaire)

            self.__prompt += """
                - "open" : Ouvrir un logiciel, un site web enregistré ou une URL directe.
                    Arguments : ["type_action", "cible"]
                    > Ouvrir un logiciel (essaie en local puis via socket) : type_action="logiciel", cible="nom du logiciel".
                    > Ouvrir un site web enregistré par l'utilisateur (ex: "youtube", "gmail") : type_action="site_enregistre", cible="nom du site".
                    > Ouvrir une URL directe : type_action="url", cible="l'URL complète (ex: https://www.exemple.com)".
                - "download_youtube" : Télécharger une vidéo ou un audio depuis YouTube.
                    Arguments : ["mode", "url"]
                    > Télécharger une vidéo : mode="1", url="URL de la vidéo YouTube".
                    > Télécharger uniquement l'audio (musique) : mode="2", url="URL de la vidéo YouTube".
                """

        if conf.etatCodehelp == 1 :
            from fnc.fonctionCodeHelp import fncCodehelp  # CODE HELP
            self.__codehelp = fncCodehelp(self.__gestionnaire)
            self.__prompt +="""
                - "codehelp" : Outils d'aide au développement (recherche de documentation, outils graphiques, GitHub).
                    Arguments : ["type_action", "param1"]
                
                    --- Recherche de documentation ---
                    > Rechercher dans DevDocs (documentation multi-langages) : type_action="doc_devdoc", param1="terme à rechercher".
                    > Rechercher dans la documentation Microsoft : type_action="doc_microsoft", param1="terme à rechercher".
                    > Rechercher dans la documentation Python : type_action="doc_python", param1="terme à rechercher".
                
                    --- GitHub ---
                    > Rechercher un dépôt sur GitHub : type_action="github_search", param1="terme à rechercher".
                    > Ouvrir le site GitHub dans le navigateur : type_action="github_site", param1="".
                
                    --- Outils graphiques ---
                    > Ouvrir le sélecteur de couleurs : type_action="gui_color", param1="".
                    > Ouvrir le gestionnaire GitHub : type_action="gui_github", param1="".
                    > Ouvrir le gestionnaire de librairies : type_action="gui_librairy", param1="".
                    > Ouvrir l'organisateur de variables : type_action="gui_orgavar", param1="".
                """

        self.__prompt += """
            - "reponse_simple" : Action par défaut. 
            Utilise cette action UNIQUEMENT si aucune autre action ci-dessus ne correspond à la demande de l'utilisateur (ex: salutations, conversation libre, questions générales). Arguments : []
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