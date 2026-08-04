from neuron.CNeuronBase import neuronBase,gestionnaire

class core_neuron(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fnc_meteo = self._gestFNC.getFNCMeteo()
        self.__fnc_radio = self._gestFNC.getFNCRadio()
        self.__gestIA = self._gestionnaire.getGestIA()

    def neuron(self, intent:str, requette_raw:str):
        mots = intent.split(" ")
        #print(intent)
        
        if mots[0] != "COMPLEXE" and mots[0] != "ARRET":
            
            if mots[0] == "METEO":
                if self.__part_meteo(mots):
                    town = self.__fnc_meteo.getNameTown()
                    temperature = self.__fnc_meteo.getTemperature()
                    description = self.__fnc_meteo.getDescription()
                    donnees = f"OK {town} : {description} avec {temperature}°C"
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._valeurOut = 1
                    self._listSortie = [reponse, ""]
                else :
                    donnees = "PAS OK : Impossible de récupérer la météo."
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._valeurOut = 1
                    self._listSortie = [reponse, ""]
                
            elif mots[0] == "TEMPERATURE":
                if self.__part_meteo(mots):
                    temperature = self.__fnc_meteo.getTemperature()
                    donnees = f"OK {temperature}°C"
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._valeurOut = 1
                    self._listSortie = [reponse, ""]
                else :
                    donnees = "PAS OK : Impossible de récupérer la température."
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._valeurOut = 1
                    self._listSortie = [reponse, ""]
                
            elif mots[0] == "ACTU":
                theme = mots[1] if len(mots) > 1 else ""
                print(f"[Neuron Core] Action: ACTUALITÉ")
                # Parse theme
                if theme == "TOUT":
                    print("  -> Thème : Tout (Général)")
                elif theme == "TECH":
                    print("  -> Thème : Technologie")
                elif theme == "GENERALISTE":
                    print("  -> Thème : Généraliste")
                elif theme == "SCIENCE":
                    print("  -> Thème : Science")
                elif theme == "SPORT":
                    print("  -> Thème : Sport")
                elif theme == "CULTURE":
                    print("  -> Thème : Culture")
                else:
                    print(f"  -> Thème : Inconnu ({theme})")
                
            elif mots[0] == "RADIO":
                nom_radio = " ".join(mots[1:]) if len(mots) > 1 else ""
                if self.__part_radio(mots):
                    if nom_radio == "STOP":
                        donnees = "OK Radio arrêtée"
                        self._valeurOut = 1
                    else:
                        donnees = f"OK Radio lancée : {nom_radio}"
                        self._valeurOut = 22
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._listSortie = [reponse, ""]
                else:
                    donnees = "PAS OK pour la radio"
                    reponse = self.__gestIA.generate_final_response(requette_raw, donnees)
                    self._valeurOut = 1
                    self._listSortie = [reponse, ""]
                    
            elif mots[0] == "HEURE":
                print("[Neuron Core] Je dois donner l'HEURE ou la DATE.")
                
            elif mots[0] == "MINUTEUR":
                print("[Neuron Core] Je dois lancer un MINUTEUR.")

        elif mots[0] == "ARRET":
            self._valeurOut = 15
            self._listSortie = ["stop",""]

    def __part_meteo(self,mots:list):
        valid_moments = ["MAINTENANT", "NOW", "DEMAIN", "MATIN", "APREM"]
        
        # Si le 2ème mot est un moment valide, on parse normalement
        if len(mots) > 1 and mots[1] in valid_moments:
            moment = mots[1]
            lieu = " ".join(mots[2:]) if len(mots) > 2 else ""
        else:
            # Sinon, ça veut dire que l'IA a omis le moment, et mots[1] est déjà le début du lieu !
            moment = "MAINTENANT" # Moment par défaut
            lieu = " ".join(mots[1:]) if len(mots) > 1 else ""

        if lieu == "DOMICILE" or lieu == "HOME":
            location = "home"
        elif lieu == "TRAVAIL" or lieu == "WORK":
            location = "work"
        elif lieu == "LOCATE" or lieu == "":
            location = "locate"
        else:
            location = "custom"

        if moment == "DEMAIN":
            return self.__fnc_meteo.weather_tomorrow(location, town=lieu)
        elif moment == "MATIN":
            return self.__fnc_meteo.weather_matin(location, town=lieu)
        elif moment == "APREM":
            return self.__fnc_meteo.weather_afternoon(location, town=lieu)
        else :
            return self.__fnc_meteo.weather_current(location, town=lieu)

    def __part_radio(self, mots: list):
        nom_radio = " ".join(mots[1:]) if len(mots) > 1 else ""
        if nom_radio == "STOP":
            return self.__fnc_radio.stop()
        elif nom_radio == "EUROPE 1":
            return self.__fnc_radio.startEurope1()
        elif nom_radio == "EUROPE 2":
            return self.__fnc_radio.startEurope2()
        elif nom_radio == "FRANCE INFO":
            return self.__fnc_radio.startFranceInfo()
        elif nom_radio == "FRANCE INTER":
            return self.__fnc_radio.startFranceInter()
        elif nom_radio == "FRANCE MUSIQUE":
            return self.__fnc_radio.startFranceMusique()
        elif nom_radio == "FRANCE CULTURE":
            return self.__fnc_radio.startFranceCulture()
        elif nom_radio == "FRANCE BLEU":
            return self.__fnc_radio.startFranceBleu()
        elif nom_radio == "FUN RADIO":
            return self.__fnc_radio.startFunRadio()
        elif nom_radio == "NRJ":
            return self.__fnc_radio.startNRJ()
        elif nom_radio == "RFM":
            return self.__fnc_radio.startRFM()
        elif nom_radio == "NOSTALGIE":
            return self.__fnc_radio.startNostalgi()
        elif nom_radio == "SKYROCK":
            return self.__fnc_radio.startSkyrock()
        elif nom_radio == "RTL":
            return self.__fnc_radio.startRTL()
        else:
            return False
