from fnc.fncBase import fncBase, gestionnaire
import pyperclip

class fncMail(fncBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        self.__tool_launched = True
        self.__gest_ia = gestionnaire.getGestIA()
        self.__user_conf = gestionnaire.getUserConf()

        # Données sources
        self.__objet_source = ""
        self.__mail_source = ""
        self.__consigne_source = ""

        # Données générées / corrigées
        self.__objet_genere = ""
        self.__corps_genere = ""

    def __ensure_ia_loaded(self) -> bool:
        """S'assure que l'IA est chargée et prête."""
        if not self.__gest_ia.get_ia_is_enable():
            return self.__gest_ia.loadIA()
        return True

    def __get_user_signature(self) -> str:
        """Récupère le prénom et nom de l'utilisateur pour la signature."""
        try:
            firstname = self.__user_conf.getFirstnameUser() or ""
            lastname = self.__user_conf.getLastnameUser() or ""
            signature = f"{firstname} {lastname}".strip()
            return signature
        except Exception:
            return ""

    def __auto_copy_corps(self):
        """Copie automatiquement le corps généré dans le presse-papier."""
        try:
            if self.__corps_genere:
                pyperclip.copy(self.__corps_genere)
        except Exception:
            pass

    def action_mail(self, action: str, objet: str = "", p1: str = "", p2: str = "") -> bool:
        """
        Méthode publique d'action unifiée pour piloter la fonction mail.

        Actions supportées :
          - "creer" / "creation" : Rédige un mail (objet=objet, p1=consigne) et copie le corps dans le presse-papier
          - "corriger" / "correction" : Corrige un mail (objet=objet, p1=corps_du_mail) et copie le corps dans le presse-papier
          - "repondre" / "reponse" : Rédige une réponse (objet=objet, p1=mail_recu, p2=consigne_reponse) et copie le corps dans le presse-papier
          - "copier_objet" : Copie l'objet généré dans le presse-papier
          - "copier_tout" / "copier_mail" : Copie le mail complet dans le presse-papier
          - "etat" : Vérifie si la fonction est active
        """
        action = action.lower().strip()
        if action in ("creer", "creation", "create"):
            return self.create_mail(objet=objet, consigne=p1)
        elif action in ("corriger", "correction", "correct"):
            return self.correct_mail(objet=objet, mail=p1)
        elif action in ("repondre", "reponse", "reply"):
            return self.reply_mail(objet=objet, mail_recu=p1, consigne_reponse=p2)
        elif action in ("copier_objet", "copy_objet"):
            return self.copy_objet()
        elif action in ("copier_tout", "copier_mail", "copy_mail", "copy_all"):
            return self.copy_mail_complet()
        elif action in ("etat", "state"):
            return self.getToolLaunched()
        return False

    def create_mail(self, objet: str, consigne: str = "") -> bool:
        """
        Rédige un mail complet à partir d'un objet et d'éventuelles consignes.
        Copie automatiquement le corps généré dans le presse-papier.
        """
        if not self.__tool_launched or not objet.strip():
            return False

        if not self.__ensure_ia_loaded():
            return False

        self.__objet_source = objet
        self.__consigne_source = consigne
        self.__mail_source = ""

        signature = self.__get_user_signature()
        result = self.__gest_ia.create_mail(objet, consigne, signature)

        if result and isinstance(result, dict):
            self.__objet_genere = result.get("objet", objet)
            self.__corps_genere = result.get("corps", "")
            self.__auto_copy_corps()
            return True
        return False

    def correct_mail(self, objet: str, mail: str) -> bool:
        """
        Corrige l'orthographe, la grammaire et la syntaxe de l'objet et du corps du mail.
        Copie automatiquement le corps corrigé dans le presse-papier.
        """
        if not self.__tool_launched or not mail.strip():
            return False

        if not self.__ensure_ia_loaded():
            return False

        self.__objet_source = objet
        self.__mail_source = mail
        self.__consigne_source = ""

        result = self.__gest_ia.correct_mail(objet, mail)

        if result and isinstance(result, dict):
            self.__objet_genere = result.get("objet", objet)
            self.__corps_genere = result.get("corps", "")
            self.__auto_copy_corps()
            return True
        return False

    def reply_mail(self, objet: str, mail_recu: str, consigne_reponse: str) -> bool:
        """
        Rédige une réponse adaptée à un mail reçu selon les consignes de l'utilisateur.
        Copie automatiquement le corps de la réponse dans le presse-papier.
        """
        if not self.__tool_launched or not mail_recu.strip() or not consigne_reponse.strip():
            return False

        if not self.__ensure_ia_loaded():
            return False

        self.__objet_source = objet
        self.__mail_source = mail_recu
        self.__consigne_source = consigne_reponse

        signature = self.__get_user_signature()
        result = self.__gest_ia.reply_mail(objet, mail_recu, consigne_reponse, signature)

        if result and isinstance(result, dict):
            self.__objet_genere = result.get("objet", f"Re: {objet}" if objet else "")
            self.__corps_genere = result.get("corps", "")
            self.__auto_copy_corps()
            return True
        return False

    # Getters
    def get_objet(self) -> str:
        return self.__objet_genere

    def get_corps(self) -> str:
        return self.__corps_genere

    def get_mail_complet(self) -> str:
        if self.__objet_genere and self.__corps_genere:
            return f"Objet : {self.__objet_genere}\n\n{self.__corps_genere}"
        elif self.__corps_genere:
            return self.__corps_genere
        return ""

    def get_objet_source(self) -> str:
        return self.__objet_source

    def get_mail_source(self) -> str:
        return self.__mail_source

    def get_consigne_source(self) -> str:
        return self.__consigne_source

    def getToolLaunched(self) -> bool:
        return self.__tool_launched

    # Presse-papier
    def copy_objet(self) -> bool:
        if not self.__tool_launched or not self.__objet_genere:
            return False
        try:
            pyperclip.copy(self.__objet_genere)
            return True
        except Exception:
            return False

    def copy_mail_complet(self) -> bool:
        texte_complet = self.get_mail_complet()
        if not self.__tool_launched or not texte_complet:
            return False
        try:
            pyperclip.copy(texte_complet)
            return True
        except Exception:
            return False
