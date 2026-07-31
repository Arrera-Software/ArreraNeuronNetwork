import json
from datetime import datetime
from gestionnaire.gestion import gestionnaire


class IARouter:
    """
    Routeur principal basé sur l'IA.
    Reçoit la requête utilisateur, l'envoie à l'IA qui retourne un JSON
    {action, args, reponse}, puis dispatch vers la bonne fonction dans gestFNC ou gestGUI.
    """

    def __init__(self, gestionnaire: gestionnaire):
        self.__gestionnaire = gestionnaire
        self.__gestIA = gestionnaire.getGestIA()
        self.__gestFNC = gestionnaire.getGestFNC()
        self.__gestGUI = gestionnaire.getGestGUI()
        self.__listSortie = ["", ""]
        self.__valeurOut = 0

        # Table de dispatch : action -> handler
        self.__dispatch = {
            # Actions FNC
            "tache": self.__handle_tache,
            "calendrier": self.__handle_calendrier,
            "horloge": self.__handle_horloge,
            "gps": self.__handle_gps,
            "meteo": self.__handle_meteo,
            "actu": self.__handle_actu,
            "radio": self.__handle_radio,
            "traduction": self.__handle_traduction,
            "brief": self.__handle_brief,
            "work": self.__handle_work,
            "calculatrice": self.__handle_calculatrice,
            "lecture": self.__handle_lecture,
            "orthographe": self.__handle_orthographe,
            "recherche": self.__handle_recherche,
            "open": self.__handle_open,
            "download_youtube": self.__handle_download,
            "codehelp": self.__handle_codehelp,
            # Actions GUI
            "gui": self.__handle_gui,
            # Fallback
            "reponse_simple": self.__handle_reponse_simple,
        }

        # Mapping radio : nom -> méthode
        self.__radio_map = {
            "Europe 1": "startEurope1",
            "Europe 2": "startEurope2",
            "France Info": "startFranceInfo",
            "France inter": "startFranceInter",
            "France Musique": "startFranceMusique",
            "France Culture": "startFranceCulture",
            "France bleu": "startFranceBleu",
            "Fun radio": "startFunRadio",
            "NRJ": "startNRJ",
            "RFM": "startRFM",
            "Nostalgie": "startNostalgi",
            "Skyrock": "startSkyrock",
            "RTL": "startRTL",
        }

        # Mapping recherche : type -> méthode
        self.__search_map = {
            "recherche": "search",
            "google": "googleSearch",
            "brave": "braveSearch",
            "duckduckgo": "duckduckgoSearch",
            "qwant": "qwantSearch",
            "ecosia": "ecosiaSearch",
            "bing": "bingSearch",
            "perplexity": "perplexitySearch",
            "amazon": "amazonSearch",
            "big_recherche": "bigRecherche",
        }

        # Mapping météo : moment -> méthode
        self.__meteo_map = {
            "actuel": "weather_current",
            "demain": "weather_tomorrow",
            "matin": "weather_morning",
            "apres-midi": "weather_afternoon",
            "soir": "weather_evening",
            "nuit": "weather_night",
        }

        # Mapping formules tableur : nom -> méthode
        self.__formule_map = {
            "somme": "addSommeOnTableur",
            "moyenne": "addMoyenneOnTableur",
            "comptage": "addComptageOnTableur",
            "minimum": "addMinimumOnTableur",
            "maximum": "addMaximumOnTableur",
        }

    # ==========================================
    # MÉTHODES UTILITAIRES
    # ==========================================

    def __arg(self, args, index, default=""):
        """Accès sécurisé aux arguments avec valeur par défaut."""
        if index < len(args):
            return str(args[index]) if args[index] is not None else default
        return default

    def __set_output(self, texte, valeur=1, extra=""):
        """Définit la sortie texte et le code valeurOut."""
        self.__listSortie = [texte, extra]
        self.__valeurOut = valeur

    def __parse_date(self, date_str):
        """Parse une date YYYY-MM-DD en datetime. Retourne None si vide ou invalide."""
        if not date_str or date_str.strip() == "":
            return None
        try:
            return datetime.strptime(date_str.strip(), "%Y-%m-%d")
        except ValueError:
            return None

    def __format_list(self, data):
        """Formate une liste en string lisible."""
        if not data:
            return ""
        if isinstance(data, list):
            return "\n".join(f"- {item}" for item in data)
        return str(data)

    # ==========================================
    # MÉTHODE PRINCIPALE DE ROUTAGE
    # ==========================================

    def route(self, requette: str) -> bool:
        """
        Envoie la requête à l'IA, parse le JSON retourné,
        et dispatch vers le bon handler.
        Retourne True si l'action a été traitée, False sinon.
        """
        self.__listSortie = ["", ""]
        self.__valeurOut = 0

        # 1. Vérifier que l'IA est activée
        if not self.__gestIA.get_ia_is_enable():
            return False

        # 2. Envoyer la requête à l'IA
        if not self.__gestIA.send_request_ia(requette):
            return False

        if not self.__gestIA.get_state_ia_reponse():
            return False

        # 3. Parser la réponse JSON
        reponse_brute = self.__gestIA.get_reponse_ia()
        try:
            parsed = json.loads(reponse_brute)
        except (json.JSONDecodeError, TypeError):
            # L'IA n'a pas retourné du JSON valide → traiter comme texte brut
            self.__set_output(str(reponse_brute))
            return True

        action = parsed.get("action", "")
        args = parsed.get("args", [])
        reponse = parsed.get("reponse", "")

        # 4. Dispatcher vers le bon handler
        if action in self.__dispatch:
            try:
                self.__dispatch[action](args, reponse)
            except Exception as e:
                print(f"Erreur IARouter [{action}]: {e}")
                self.__set_output(reponse)
        else:
            self.__set_output(reponse)

        return self.__valeurOut != 0

    def getListSortie(self) -> list:
        return self.__listSortie

    def getValeurSortie(self) -> int:
        return self.__valeurOut

    # ==========================================
    # HANDLERS - TÂCHES
    # ==========================================

    def __handle_tache(self, args, reponse):
        fnc = self.__gestFNC.getFNCTask()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "ajouter":
            nom = self.__arg(args, 1)
            date = self.__parse_date(self.__arg(args, 2))
            description = self.__arg(args, 3) or None
            fnc.addTask(nom, date, description)
            self.__set_output(reponse)

        elif type_action == "supprimer":
            fnc.delTask(self.__arg(args, 1))
            self.__set_output(reponse)

        elif type_action == "terminer":
            fnc.finishTask(self.__arg(args, 1))
            self.__set_output(reponse)

        elif type_action == "reactiver":
            fnc.unfinishTask(self.__arg(args, 1))
            self.__set_output(reponse)

        elif type_action == "lister_tout":
            data = fnc.getAllTask()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_non_terminees":
            data = fnc.getNoFinishTask()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_terminees":
            data = fnc.getFinishTask()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_aujourdhui":
            data = fnc.getListTaskToday()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_demain":
            data = fnc.getListTaskTowmorow()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_retard":
            data = fnc.getListTaskLate()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action in ("compter", "compter_non_terminees", "compter_terminees",
                             "compter_aujourdhui", "compter_demain", "compter_retard"):
            # L'IA a déjà le compte dans sa réponse
            self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - CALENDRIER
    # ==========================================

    def __handle_calendrier(self, args, reponse):
        fnc = self.__gestFNC.getFNCCalendar()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "ajouter":
            nom = self.__arg(args, 1)
            date = self.__parse_date(self.__arg(args, 2))
            heure = self.__arg(args, 3)
            description = self.__arg(args, 4)
            lieu = self.__arg(args, 5)
            repetition = self.__arg(args, 6, "false").lower() == "true"
            if date:
                fnc.addEventToCalendar(nom, date, heure, description, lieu, repetition)
            self.__set_output(reponse)

        elif type_action == "supprimer":
            fnc.delEvent(self.__arg(args, 1))
            self.__set_output(reponse)

        elif type_action == "lister_tout":
            data = fnc.getAllEvents()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_aujourdhui":
            data = fnc.checkDateDayEvent()
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "lister_date":
            date_str = self.__arg(args, 2)
            data = fnc.checkEventWithDate(date_str)
            self.__set_output(reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "details":
            nom = self.__arg(args, 1)
            data = fnc.getInformationEvent(nom)
            if data and isinstance(data, dict):
                details = "\n".join(f"{k}: {v}" for k, v in data.items())
                self.__set_output(reponse + "\n" + details)
            else:
                self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - HORLOGE
    # ==========================================

    def __handle_horloge(self, args, reponse):
        fnc = self.__gestFNC.getFNCHorloge()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "heure":
            fnc.getHorloge()
            self.__set_output(reponse)

        elif type_action == "chrono_start":
            fnc.startChrono()
            self.__set_output(reponse)

        elif type_action == "chrono_stop":
            fnc.stopChrono()
            self.__set_output(reponse)

        elif type_action == "chrono_reset":
            fnc.resetChrono()
            self.__set_output(reponse)

        elif type_action == "chrono_temps":
            temps = fnc.getTimeChrono()
            formatted = fnc.formatTemps(temps)
            self.__set_output(reponse + " " + formatted if formatted else reponse)

        elif type_action == "chrono_etat":
            fnc.getStatChrono()
            self.__set_output(reponse)

        elif type_action == "minuteur_start":
            duree = self.__arg(args, 1)
            try:
                fnc.startMinuteur(int(duree))
            except (ValueError, TypeError):
                pass
            self.__set_output(reponse)

        elif type_action == "minuteur_stop":
            fnc.stopMinuteur()
            self.__set_output(reponse)

        elif type_action == "minuteur_etat":
            fnc.getStatMinuteur()
            self.__set_output(reponse)

        elif type_action == "minuteur_temps":
            temps = fnc.getTimeMinuteur()
            self.__set_output(reponse + " " + str(temps) if temps else reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - GPS
    # ==========================================

    def __handle_gps(self, args, reponse):
        fnc = self.__gestFNC.getFNCGPS()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "itineraire":
            depart = self.__arg(args, 1)
            arrivee = self.__arg(args, 2)
            fnc.launchGoogleMapItinerary(depart, arrivee)
            self.__set_output(reponse)

        elif type_action == "localisation":
            fnc.locate()
            self.__set_output(reponse)

        elif type_action == "departement":
            ville = self.__arg(args, 1)
            dept = fnc.getFrenchDepartementWithTown(ville)
            if dept:
                self.__set_output(reponse + " " + dept)
            else:
                self.__set_output(reponse)

        elif type_action == "ville_coordonnees":
            lat = self.__arg(args, 1)
            lon = self.__arg(args, 2)
            ville = fnc.getTownWithLatitudeAndLongitude(lat, lon)
            if ville:
                self.__set_output(reponse + " " + ville)
            else:
                self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - MÉTÉO
    # ==========================================

    def __handle_meteo(self, args, reponse):
        fnc = self.__gestFNC.getFNCMeteo()
        if fnc is None:
            self.__set_output(reponse)
            return

        moment = self.__arg(args, 0)
        emplacement = self.__arg(args, 1)
        ville_custom = self.__arg(args, 2)

        if moment == "alerte":
            fnc.set_alerte()
            self.__set_output(reponse, 4)
            return

        method_name = self.__meteo_map.get(moment)
        if method_name:
            method = getattr(fnc, method_name, None)
            if method:
                if emplacement == "custom" and ville_custom:
                    result = method(emplacement, ville_custom)
                else:
                    result = method(emplacement)
                self.__set_output(reponse, 4 if result else 1)
            else:
                self.__set_output(reponse)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - ACTUALITÉS
    # ==========================================

    def __handle_actu(self, args, reponse):
        fnc = self.__gestFNC.getFNCActu()
        if fnc is None:
            self.__set_output(reponse)
            return

        limite = self.__arg(args, 0, "3")
        try:
            limit_int = int(limite)
        except (ValueError, TypeError):
            limit_int = 3

        if fnc.setActu(limit_int):
            self.__set_output(reponse, 3)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - RADIO
    # ==========================================

    def __handle_radio(self, args, reponse):
        fnc = self.__gestFNC.getFNCRadio()
        if fnc is None:
            self.__set_output(reponse)
            return

        action_radio = self.__arg(args, 0)

        if action_radio == "stop":
            fnc.stop()
            self.__set_output(reponse)

        elif action_radio == "etat":
            fnc.getRadioRunning()
            self.__set_output(reponse)

        elif action_radio in self.__radio_map:
            method = getattr(fnc, self.__radio_map[action_radio], None)
            if method and method():
                self.__set_output(reponse, 22)
            else:
                self.__set_output(reponse)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - TRADUCTION
    # ==========================================

    def __handle_traduction(self, args, reponse):
        fnc = self.__gestFNC.getFNCTraduction()
        if fnc is None:
            self.__set_output(reponse)
            return

        texte = self.__arg(args, 0)
        lang_source = self.__arg(args, 1, "francais")
        lang_cible = self.__arg(args, 2)

        if fnc.setTranlator(lang_source, lang_cible):
            result = fnc.tranlate(texte)
            if result:
                self.__set_output(reponse + "\n" + result)
            else:
                self.__set_output(reponse)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - BRIEF
    # ==========================================

    def __handle_brief(self, args, reponse):
        moment = self.__arg(args, 0)

        brief_gui_map = {
            "morning": "morning_brief",
            "afternoon": "afternoon_brief",
            "evening": "evening_brief",
        }

        gui_name = brief_gui_map.get(moment)
        if gui_name and self.__gestGUI.setGUIActive(gui_name):
            self.__set_output(reponse, 5)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - WORK (Tableur / Word / Projet)
    # ==========================================

    def __handle_work(self, args, reponse):
        fnc = self.__gestFNC.getFNCWork()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)
        param1 = self.__arg(args, 1)
        param2 = self.__arg(args, 2)
        param3 = self.__arg(args, 3)

        # --- TABLEUR ---
        if type_action == "tableur_ouvrir":
            fnc.openTableur()
            self.__set_output(reponse, 7)

        elif type_action == "tableur_ouvrir_direct":
            fnc.openTableurDirectly(param1)
            self.__set_output(reponse, 7)

        elif type_action == "tableur_fermer":
            fnc.closeTableur()
            self.__set_output(reponse, 8)

        elif type_action == "tableur_lire":
            if fnc.readTableur():
                data = fnc.getReadTableur()
                self.__set_output(
                    reponse + "\n" + self.__format_list(data) if data else reponse, 13)
            else:
                self.__set_output(reponse)

        elif type_action == "tableur_ecrire":
            fnc.addValeurOnTableur(param1, param2)
            self.__set_output(reponse)

        elif type_action == "tableur_supprimer":
            fnc.delValeur(param1)
            self.__set_output(reponse)

        elif type_action == "tableur_formule":
            formule = param1
            # param2 = "A1:A10" → séparer en case_start et case_stop
            range_parts = param2.split(":") if ":" in param2 else [param2, param2]
            case_start = range_parts[0] if len(range_parts) > 0 else ""
            case_stop = range_parts[1] if len(range_parts) > 1 else ""
            case_dest = param3

            if formule in self.__formule_map:
                method = getattr(fnc, self.__formule_map[formule], None)
                if method:
                    method(case_start, case_stop, case_dest)
            self.__set_output(reponse)

        elif type_action == "tableur_ouvrir_os":
            fnc.openTableurOs()
            self.__set_output(reponse)

        elif type_action == "tableur_etat":
            fnc.getEtatTableur()
            self.__set_output(reponse)

        # --- WORD ---
        elif type_action == "word_ouvrir":
            fnc.openWord()
            self.__set_output(reponse, 7)

        elif type_action == "word_ouvrir_direct":
            fnc.openWordDirectly(param1)
            self.__set_output(reponse, 7)

        elif type_action == "word_fermer":
            fnc.closeWord()
            self.__set_output(reponse, 8)

        elif type_action == "word_lire":
            if fnc.readWord():
                data = fnc.getReadWord()
                self.__set_output(
                    reponse + "\n" + str(data) if data else reponse, 9)
            else:
                self.__set_output(reponse)

        elif type_action == "word_ecrire":
            fnc.writeWord(param1)
            self.__set_output(reponse)

        elif type_action == "word_ecrire_ecrase":
            fnc.writeWordEcrase(param1)
            self.__set_output(reponse)

        elif type_action == "word_ouvrir_os":
            fnc.openWordOs()
            self.__set_output(reponse)

        elif type_action == "word_etat":
            fnc.getEtatWord()
            self.__set_output(reponse)

        # --- PROJET ---
        elif type_action == "projet_lister":
            data = fnc.getListProjet()
            self.__set_output(
                reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "projet_creer":
            fnc.createProjet(param1)
            self.__set_output(reponse, 10)

        elif type_action == "projet_ouvrir":
            fnc.openProjet(param1)
            self.__set_output(reponse, 14)

        elif type_action == "projet_fermer":
            fnc.closeProjet()
            self.__set_output(reponse, 21)

        elif type_action == "projet_type":
            fnc.addTypeProjet(param1)
            self.__set_output(reponse)

        elif type_action == "projet_nom":
            fnc.getNameProjet()
            self.__set_output(reponse)

        elif type_action == "projet_get_type":
            fnc.getTypeProjet()
            self.__set_output(reponse)

        elif type_action == "projet_etat":
            fnc.getEtatProject()
            self.__set_output(reponse)

        elif type_action == "projet_creer_fichier":
            fnc.createFileProject(param1, param2)
            self.__set_output(reponse, 16)

        elif type_action == "projet_lister_fichiers":
            fnc.setlistFileProject()
            data = fnc.getListFileProjet()
            self.__set_output(
                reponse + "\n" + self.__format_list(data) if data else reponse)

        # --- TÂCHES DU PROJET ---
        elif type_action == "projet_tache_ajouter":
            date = self.__parse_date(param2)
            desc = param3 or None
            fnc.addTacheProjet(param1, date, desc)
            self.__set_output(reponse)

        elif type_action == "projet_tache_supprimer":
            fnc.supprTacheProjet(param1)
            self.__set_output(reponse)

        elif type_action == "projet_tache_terminer":
            fnc.finishTacheProjet(param1)
            self.__set_output(reponse)

        elif type_action == "projet_tache_non_terminees":
            fnc.setListTacheNoFinishProjet()
            data = fnc.getListTacheNoFinishProjet()
            self.__set_output(
                reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "projet_tache_aujourdhui":
            fnc.setListTacheTodayProjet()
            data = fnc.getListTacheTodayProjet()
            self.__set_output(
                reponse + "\n" + self.__format_list(data) if data else reponse)

        elif type_action == "projet_tache_demain":
            fnc.setListTacheTowmorowProjet()
            data = fnc.getListTacheTowmorowProjet()
            self.__set_output(
                reponse + "\n" + self.__format_list(data) if data else reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - CALCULATRICE
    # ==========================================

    def __handle_calculatrice(self, args, reponse):
        fnc = self.__gestFNC.getFNCCalculatrice()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_calcul = self.__arg(args, 0)
        param1 = self.__arg(args, 1)
        param2 = self.__arg(args, 2)
        param3 = self.__arg(args, 3)
        param4 = self.__arg(args, 4)

        try:
            if type_calcul == "addition":
                result = fnc.adition(float(param1), float(param2))
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "soustraction":
                result = fnc.soustraction(float(param1), float(param2))
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "multiplication":
                result = fnc.multiplication(float(param1), float(param2))
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "division":
                result = fnc.divsion(float(param1), float(param2))
                if result is not None:
                    self.__set_output(f"{reponse}\nRésultat : {result}")
                else:
                    self.__set_output(reponse)

            elif type_calcul == "puissance":
                result = fnc.puissance(float(param1), float(param2))
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "modulo":
                result = fnc.modulo(float(param1), float(param2))
                if result is not None:
                    self.__set_output(f"{reponse}\nRésultat : {result}")
                else:
                    self.__set_output(reponse)

            elif type_calcul == "racine":
                result = fnc.racine(float(param1), float(param2))
                if result is not None:
                    self.__set_output(f"{reponse}\nRésultat : {result}")
                else:
                    self.__set_output(reponse)

            elif type_calcul == "complexe":
                fnc.setComplexNb(float(param1), float(param2),
                                float(param3), float(param4))
                operation = self.__arg(args, 5, "addition")

                complex_ops = {
                    "addition": fnc.aditionNbComplex,
                    "soustraction": fnc.soustrationNbComplex,
                    "multiplication": fnc.multiplicationNbComplex,
                    "division": fnc.divisionNbComplex,
                }
                op_method = complex_ops.get(operation, fnc.aditionNbComplex)
                result = op_method()
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "pythagore":
                fnc.setNbPythagore(float(param1), float(param2))
                result = fnc.theoremePythagore()
                self.__set_output(f"{reponse}\nRésultat : {result}")

            elif type_calcul == "pythagore_reciproque":
                fnc.setNbPythagore(float(param1), float(param2))
                result = fnc.reciproquePythagore()
                self.__set_output(f"{reponse}\nRésultat : {result}")

            else:
                self.__set_output(reponse)

        except (ValueError, TypeError, ZeroDivisionError):
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - LECTURE
    # ==========================================

    def __handle_lecture(self, args, reponse):
        fnc = self.__gestFNC.getFNCRead()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "lire":
            texte = self.__arg(args, 1)
            fnc.read(texte)
            self.__set_output(reponse)

        elif type_action == "etat":
            fnc.getStatTheard()
            self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - ORTHOGRAPHE
    # ==========================================

    def __handle_orthographe(self, args, reponse):
        fnc = self.__gestFNC.getFNCOrthographe()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)

        if type_action == "corriger":
            texte = self.__arg(args, 1)
            if fnc.corrected_text(texte):
                correction = fnc.getCorrections()
                if correction:
                    self.__set_output(reponse + "\n" + correction)
                else:
                    self.__set_output(reponse)
            else:
                self.__set_output(reponse)

        elif type_action == "copier":
            fnc.copyCorrections()
            self.__set_output(reponse)

        elif type_action == "etat":
            fnc.getToolLaunched()
            self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - RECHERCHE
    # ==========================================

    def __handle_recherche(self, args, reponse):
        fnc = self.__gestFNC.getFNCSearch()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_recherche = self.__arg(args, 0, "recherche")
        requete = self.__arg(args, 1)

        method_name = self.__search_map.get(type_recherche)
        if method_name:
            method = getattr(fnc, method_name, None)
            if method:
                method(requete)
                self.__set_output(reponse)
            else:
                self.__set_output(reponse)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - OPEN
    # ==========================================

    def __handle_open(self, args, reponse):
        fnc = self.__gestFNC.getFNCOpen()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)
        cible = self.__arg(args, 1)

        if type_action == "logiciel":
            fnc.openSoft(cible)
            self.__set_output(reponse)

        elif type_action == "site_enregistre":
            fnc.openSaveWebSite(cible)
            self.__set_output(reponse)

        elif type_action == "url":
            fnc.openWebSite(cible)
            self.__set_output(reponse)

        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - DOWNLOAD YOUTUBE
    # ==========================================

    def __handle_download(self, args, reponse):
        fnc = self.__gestFNC.getFNCDownload()
        if fnc is None:
            self.__set_output(reponse)
            return

        mode = self.__arg(args, 0, "1")
        url = self.__arg(args, 1)

        try:
            mode_int = int(mode)
        except (ValueError, TypeError):
            mode_int = 1

        fnc.downloadDirectely(mode_int, url)
        self.__set_output(reponse)

    # ==========================================
    # HANDLERS - CODEHELP
    # ==========================================

    def __handle_codehelp(self, args, reponse):
        fnc = self.__gestFNC.getFNCCodeHelp()
        if fnc is None:
            self.__set_output(reponse)
            return

        type_action = self.__arg(args, 0)
        param1 = self.__arg(args, 1)

        codehelp_actions = {
            "doc_devdoc": lambda: fnc.searchDocInDevDoc(param1),
            "doc_microsoft": lambda: fnc.searchDocInMicrosoft(param1),
            "doc_python": lambda: fnc.searchDocInPython(param1),
            "github_search": lambda: fnc.searchGithub(param1),
            "github_site": lambda: fnc.openSiteGithub(),
            "gui_color": lambda: fnc.openGUIColorSelector(),
            "gui_github": lambda: fnc.openGUIGithubGestion(),
            "gui_librairy": lambda: fnc.openGUILibrairy(),
            "gui_orgavar": lambda: fnc.openGUIOrgaVar(),
        }

        action = codehelp_actions.get(type_action)
        if action:
            action()
        self.__set_output(reponse)

    # ==========================================
    # HANDLERS - GUI
    # ==========================================

    def __handle_gui(self, args, reponse):
        nom_gui = self.__arg(args, 0)
        parametre = self.__arg(args, 1)

        parms = parametre if parametre else None
        if self.__gestGUI.setGUIActive(nom_gui, parms):
            self.__set_output(reponse, 5)
        else:
            self.__set_output(reponse)

    # ==========================================
    # HANDLERS - RÉPONSE SIMPLE (fallback)
    # ==========================================

    def __handle_reponse_simple(self, args, reponse):
        self.__set_output(reponse)
