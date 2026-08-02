import json
from gestionnaire.gestion import gestionnaire
from librairy.ArreraIALoad import ArreraIALoad
from librairy.model_downloader import *

class gestIA :
    def __init__(self,gestionnaire:gestionnaire):

        self.__gestionnaire =  gestionnaire

        self.__ia_mode_enabled = False
        self.__ia_loader : ArreraIALoad = None

        self.__reponse_ia = ""

        self.__model_reponse_ok = False

        self.__downloader_model = model_downloader()

        self.__dir_ia_instruction = "instruction_ia/"

        self.__dict_help_file = {"orthographe":"prompt_orthographe.txt",
                                 "dedoublonnage":"prompt_dedoublonnage.txt"}

    def loadIA(self):
        user_conf = self.__gestionnaire.getUserConf()
        model_name = user_conf.get_ia_model()
        if model_name !="":
            try:
                if model_name in self.get_list_model_download():
                    self.__ia_loader = ArreraIALoad()
                    self.__ia_loader.load_model_gguf(
                        model_path=self.__downloader_model.get_path_model(model_name),
                        n_ctx=4096
                    )

                    prompt_dynamique = self.__generate_main_prompt()
                    if self.__ia_loader.add_system_instruction(prompt_dynamique):
                        self.__ia_mode_enabled = True
                        return True
                    else:
                        return False
                else:
                    self.__ia_mode_enabled = False
                    return False
            except Exception as e:
                #print(f"Erreur fatale dans loadIA : {e}")
                self.__ia_mode_enabled = False
                return False
        else :
            self.__ia_mode_enabled = False
            return False

    def load_help(self,help:str):
        if self.__ia_mode_enabled:
             if help in self.__dict_help_file.keys():
                 return self.__ia_loader.load_help_file(self.__dir_ia_instruction+self.__dict_help_file[help])
             else :
                 return False
        else :
            return False

    def send_request_ia(self, requette: str):
        if self.__ia_mode_enabled:
            try:
                # Attention : On utilise bien le nouveau nom de méthode défini dans ArreraIALoad
                self.__reponse_ia = self.__ia_loader.send_request(requette)

                if self.__reponse_ia is not None:
                    self.__model_reponse_ok = True
                    return True
                else:
                    self.__model_reponse_ok = False
                    return False

            except Exception as e:
                self.__model_reponse_ok = False
                print(f"Erreur lors de l'appel IA : {e}")
                return False
        else:
            self.__model_reponse_ok = False
            return False

    def correted_text(self,text:str):
        if self.__ia_mode_enabled:
            self.__ia_loader.unload_help()

            try:
                with open(self.__dir_ia_instruction+"prompt_orthographe.txt", 'r', encoding='utf-8') as f:
                    content = f.read()
                raw_reponse = self.__ia_loader.send_request(content+"\n"+text, False)
                try:
                    parsed = json.loads(raw_reponse)
                    if "texte_corrige" in parsed:
                        self.__reponse_ia = parsed["texte_corrige"]
                    else:
                        self.__reponse_ia = raw_reponse
                except json.JSONDecodeError:
                    self.__reponse_ia = raw_reponse

                self.__model_reponse_ok = True
                self.__ia_loader.unload_help()
                if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                    self.__ia_mode_enabled = True
                return True

            except Exception as e:
                self.__model_reponse_ok = False
                if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                    self.__ia_mode_enabled = True
                print(e)
                return False
        else:
            self.__model_reponse_ok = False
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
            return False

    def deduplicate_actu(self, articles: list) -> list:
        if not articles or not isinstance(articles, list):
            return articles

        if self.__ia_mode_enabled:
            self.__ia_loader.unload_help()

            try:
                with open(self.__dir_ia_instruction + "prompt_dedoublonnage.txt", 'r', encoding='utf-8') as f:
                    content = f.read()

                # On va tronquer les descriptions pour économiser énormément de tokens
                truncated_articles = []
                for art in articles:
                    new_art = art.copy()
                    if "description" in new_art and isinstance(new_art["description"], str):
                        # On limite la description à 150 caractères
                        if len(new_art["description"]) > 150:
                            new_art["description"] = new_art["description"][:147] + "..."
                    truncated_articles.append(new_art)

                articles_json = json.dumps(truncated_articles, ensure_ascii=False)
                
                # Sécurité ultime : si le JSON est encore trop long (ex: > 10000 caractères), on le coupe brutalement
                if len(articles_json) > 10000:
                    articles_json = articles_json[:10000] + '...}]'
                    
                request_text = f"{content}\n\n{articles_json}"

                raw_reponse = self.__ia_loader.send_request(request_text, False)

                start_idx = raw_reponse.find('[')
                end_idx = raw_reponse.rfind(']')

                if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                    json_str = raw_reponse[start_idx:end_idx + 1]
                    clean_articles = json.loads(json_str)
                    if isinstance(clean_articles, list):
                        self.__reponse_ia = raw_reponse
                        self.__model_reponse_ok = True
                        self.__ia_loader.unload_help()
                        if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                            self.__ia_mode_enabled = True
                        return clean_articles

            except Exception as e:
                print(f"Erreur lors du dédoublonnage par l'IA : {e}")

            self.__model_reponse_ok = False
            self.__ia_loader.unload_help()
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
            return articles
        else:
            self.__model_reponse_ok = False
            return articles

    def __generate_main_prompt(self):
        conf = self.__gestionnaire.getConfigFile()

        prompt = f"""Tu es {conf.name}, un assistant virtuel créé par {conf.createur}. Ton but est : {conf.bute}.
            Tu fonctionnes comme le routeur principal du système.
            Tu DOIS IMPÉRATIVEMENT répondre UNIQUEMENT par un objet JSON valide. Ne génère aucun texte avant ou après le JSON.
        
            Format JSON attendu :
            {{
                "action": "nom_de_la_fonction",
                "args": ["argument_1", "argument_2"],
                "reponse": "À UTILISER UNIQUEMENT SI action='reponse_simple'. Texte de réponse conversationnelle."
            }}
        
            Voici la liste stricte des actions autorisées selon la configuration active :
            """
        prompt += self.__gestionnaire.getGestFNC().get_prompt()
        prompt += self.__gestionnaire.getGestGUI().get_prompt()

        # 3. Clôture avec des règles comportementales strictes
        prompt += """
            Règles strictes :
            1. Choisis l'action la plus pertinente en fonction de la demande de l'utilisateur.
            2. Si une action nécessite des arguments, fournis-les dans le tableau "args". Sinon, laisse le tableau vide [].
            3. NE REMPLIS la clé "reponse" QUE SI l'action choisie est "reponse_simple".
            """
        return prompt

    def classify_intent(self, requete: str) -> str:
        """
        Passe 0 : Classification rapide de l'intention.
        Demande à l'IA de générer une "pseudo-commande" (ex: METEO DEMAIN LOCATE, RADIO NRJ, COMPLEXE)
        pour déclencher les neurones classiques (Fast-Track) avec des arguments simples.
        """
        if not self.__ia_mode_enabled:
            return "COMPLEXE"
            
        self.__ia_loader.unload_help()
        
        prompt_classification = f"""Tu es un classificateur d'intention ultra-rapide.
            Analyse la phrase suivante et réponds STRICTEMENT avec l'un des formats suivants (en majuscules, séparé par des espaces) :
            
            1. Météo : METEO [MOMENT] [LIEU]
               - MOMENT : MAINTENANT ou DEMAIN
               - LIEU : LOCATE, DOMICILE, TRAVAIL, ou le nom d'une ville précise (ex: PARIS)
               - Exemple : METEO MAINTENANT LOCATE
            
            2. Température : TEMPERATURE [MOMENT] [LIEU]
               - MOMENT : MAINTENANT ou DEMAIN
               - LIEU : LOCATE, DOMICILE, TRAVAIL, ou le nom d'une ville (ex: LYON)
               - Exemple : TEMPERATURE DEMAIN DOMICILE
            
            3. Actualité : ACTU [THEME]
               - THEME : TOUT, TECH, GENERALISTE, SCIENCE, SPORT, ou CULTURE
               - Exemple : ACTU TECH
            
            4. Radio : RADIO [ACTION/NOM]
               - Pour arrêter : RADIO STOP
               - Pour écouter, choisis dans cette liste : EUROPE 1, EUROPE 2, FRANCE INFO, FRANCE INTER, FRANCE MUSIQUE, FRANCE CULTURE, FRANCE BLEU, FUN RADIO, NRJ, RFM, NOSTALGIE, SKYROCK, RTL
               - Exemple : RADIO NRJ
            
            5. Heure et Date : HEURE
               - S'il demande l'heure, le jour ou la date.
               - Exemple : HEURE
            
            6. Minuteur : MINUTEUR
               - S'il demande un minuteur ou un chronomètre.
               - Exemple : MINUTEUR
            
            7. Arrêt / Au revoir : ARRET
               - S'il veut éteindre ou dit au revoir.
               - Exemple : ARRET
            
            8. Autre : COMPLEXE
               - Pour toute autre demande (ouvrir un projet, calculer, chercher sur internet, traduire, etc.) ou si tu n'es pas sûr.
            
            Phrase à classer : "{requete}"
            
            Règle absolue : Ne réponds RIEN D'AUTRE que la pseudo-commande choisie. Aucun point, aucune phrase. Juste les mots-clés demandés.
        """

        try:
            reponse = self.__ia_loader.send_request(prompt_classification, False, False)
            mot_cle = reponse.strip().upper()
            
            self.__ia_loader.unload_help()
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
                
            # Validation de base (vérifie juste le premier mot pour s'assurer que c'est une commande valide)
            premier_mot = mot_cle.split(" ")[0]
            mots_autorises = ["METEO", "TEMPERATURE", "ACTU", "RADIO", "HEURE", "ARRET", "MINUTEUR"]
            
            if premier_mot in mots_autorises:
                return mot_cle
            else:
                return "COMPLEXE"
            
        except Exception as e:
            print(f"Erreur lors de la classification IA : {e}")
            self.__ia_loader.unload_help()
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
            return "COMPLEXE"

    def generate_final_response(self, requete: str, donnees_systeme: str) -> str:
        """
        Deuxième passe de l'IA : génère une réponse naturelle en se basant sur les données récoltées.
        """
        if not self.__ia_mode_enabled:
            return ""

        self.__ia_loader.unload_help()

        personnalite = self.__gestionnaire.getLanguageObjet().getPersonnalite()

        if requete.strip():
            contexte_requete = f'L\'utilisateur t\'a demandé : "{requete}"\nLe système a exécuté l\'action et a retourné le résultat suivant : \n"{donnees_systeme}"'
            tache = "Ta tâche : Formule une réponse naturelle et conversationnelle pour l'utilisateur pour lui transmettre ce résultat."
        else:
            contexte_requete = f'Directive système : "{donnees_systeme}"'
            tache = "Ta tâche : Rédige ce que tu vas dire spontanément à l'utilisateur en accomplissant cette directive."

        prompt_passe2 = f"""Tu es {self.__gestionnaire.getConfigFile().name}, l'assistant virtuel. 

=== TA PERSONNALITÉ ===
{personnalite}
=======================

{contexte_requete}
            
{tache}
N'invente pas de fausses informations techniques, mais sois fluide, poli et humain. Ne génère pas de JSON, réponds directement en texte brut.
"""
        
        try:
            reponse = self.__ia_loader.send_request(prompt_passe2, False, False)
            self.__ia_loader.unload_help()
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
            return reponse.strip()
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse finale : {e}")
            self.__ia_loader.unload_help()
            if self.__ia_loader.add_system_instruction(self.__generate_main_prompt()):
                self.__ia_mode_enabled = True
            return "Une erreur est survenue lors de la formulation de la réponse."

    def get_state_ia_reponse(self):
        return self.__model_reponse_ok

    def get_reponse_ia(self):
        return self.__reponse_ia

    def get_ia_is_enable(self):
        return self.__ia_mode_enabled

    def get_list_model_available(self):
        return self.__downloader_model.get_model_list()

    def get_list_model_on_dir(self):
        return self.__downloader_model.get_model_on_dir()

    def gest_data_model(self,model:str):
        if model in self.get_list_model_available():
            return self.__downloader_model.get_data_model(model)
        else :
            return None,None,None

    def get_list_model_download(self):
        return self.__downloader_model.get_model_download()

    def download_model(self,model:str):
        return self.__downloader_model.download_model(model)

    def del_model(self,model:str):
        return self.__downloader_model.del_model(model)