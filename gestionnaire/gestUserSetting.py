from librairy.travailJSON import *
from gestionnaire.gestion import gestionnaire
from pathlib import Path
from tkinter import filedialog

DICTUSER = {
    "user":"",
    "genre":"",
    "listVille":[""],
    "lieuDomicile":"",
    "lieuTravail":"",
    "adresseDomicile" : "",
    "adresseTravail":"",
    "dictSoft":{},
    "dictSite":{},
    "moteurRecherche":"",
    "tokenGithub":"",
    "wordFolder":"",
    "videoDownloadFolder":"",
    "soundMicro":"0",
    "listWord":[]
}

class gestUserSetting:
    def __init__(self,gestionnaire:gestionnaire):
        self.__osDect = gestionnaire.getOSObjet()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = Path.home()
            self.__userSettingPath = str(home)+"/.config/arrera-assistant/user-config.json"
            self.__userTaskPath = str(home)+"/.config/arrera-assistant/user-task.json"
            self.__userHistoriquePath = str(home)+"/.config/arrera-assistant/user-hist.json"
            self.__userEventPath = str(home)+"/.config/arrera-assistant/user-event.json"
        elif self.__osDect.osWindows():
            home = Path.home() / "AppData" / "Roaming"
            self.__userSettingPath = str(home)+"/arrera-assistant/user-config.json"
            self.__userTaskPath = str(home)+"/arrera-assistant/user-task.json"
            self.__userHistoriquePath = str(home)+"/arrera-assistant/user-hist.json"
            self.__userEventPath = str(home)+"/arrera-assistant/user-event.json"
        else :
            self.__userSettingPath = None


        # Teste si le fichier de configuration utilisateur existe
        if not Path(self.__userSettingPath).is_file():
            path = Path(self.__userSettingPath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as f:
                json.dump(DICTUSER, f, ensure_ascii=False, indent=2)

            path = Path(self.__userTaskPath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            path = Path(self.__userHistoriquePath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            path = Path(self.__userEventPath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            self.__firstRun = True

        # Chargement du fichier de configuration utilisateur
        self.__fileUser = jsonWork(self.__userSettingPath)

    def getFirstRun(self):
        return self.__firstRun

    def getTaskPath(self):
        return self.__userTaskPath

    def getEventPath(self):
        return self.__userEventPath

    def getHistoriquePath(self):
        return self.__userHistoriquePath

    # Partie USER

    def setUser(self, user:str):
        if user == "":
            return False
        return self.__fileUser.setValeurJson("user", user)

    def getUser(self):
        return self.__fileUser.getContentJsonFlag("user")

    # Partie Genre

    def setGenre(self, genre:str):
        if genre == "":
            return False
        return self.__fileUser.setValeurJson("genre", genre)

    def getGenre(self):
        return self.__fileUser.getContentJsonFlag("genre")

    # Partie Ville

    def addTown(self,ville:str):
        if ville == "":
            return False

        listVille = self.__fileUser.getFlagListJson("listVille")

        if listVille is None:
            listVille = []

        if ville not in listVille:
            listVille.append(ville)
            return self.__fileUser.setValeurJson("listVille", listVille)
        else:
            return False

    def removeTown(self, ville:str):
        if ville == "":
            return False

        listVille = self.__fileUser.getFlagListJson("listVille")

        if listVille is None:
            return False

        if ville in listVille:
            listVille.remove(ville)
            return self.__fileUser.setValeurJson("listVille", listVille)
        else:
            return False

    def getListVille(self):
        listVille = self.__fileUser.getFlagListJson("listVille")
        if listVille is None:
            return None
        return listVille

    # Lieu Domicile

    def setLieuDomicile(self, lieu:str):
        if lieu == "":
            return False
        return self.__fileUser.setValeurJson("lieuDomicile", lieu)

    def getLieuDomicile(self):
        lieuDomicile = self.__fileUser.getContentJsonFlag("lieuDomicile")
        if lieuDomicile is None:
            return ""
        return lieuDomicile

    # Lieu Travail
    def setLieuTravail(self, lieu:str):
        if lieu == "":
            return False
        return self.__fileUser.setValeurJson("lieuTravail", lieu)

    def getLieuTravail(self):
        lieuTravail = self.__fileUser.getContentJsonFlag("lieuTravail")
        if lieuTravail is None:
            return ""
        return lieuTravail

    # Adresse Domicile
    def setAdresseDomicile(self, adresse:str):
        if adresse == "":
            return False
        return self.__fileUser.setValeurJson("adresseDomicile", adresse)

    def getAdresseDomicile(self):
        adresseDomicile = self.__fileUser.getContentJsonFlag("adresseDomicile")
        if adresseDomicile is None:
            return ""
        return adresseDomicile

    # Adresse Travail

    def setAdresseTravail(self, adresse:str):
        if adresse == "":
            return False
        return self.__fileUser.setValeurJson("adresseTravail", adresse)

    def getAdresseTravail(self):
        adresseTravail = self.__fileUser.getContentJsonFlag("adresseTravail")
        if adresseTravail is None:
            return ""
        return adresseTravail

    # SOFT

    # Site

    def setSite(self, site:str, url:str):
        if site == "" or url == "":
            return False
        return  self.__fileUser.setDictJson("dictSite", site, url)

    def getSite(self):
        return  self.__fileUser.getFlagDictJson("dictSite")

    def removeSite(self, site:str):
        if site == "":
            return False

        return self.__fileUser.unsetDictJson("dictSite", site)

    # Moteur de recherche
    def setMoteurRecherche(self, moteur:str):
        if moteur == "":
            return False
        return self.__fileUser.setValeurJson("moteurRecherche", moteur)

    def getMoteurRecherche(self):
        return  self.__fileUser.getContentJsonFlag("moteurRecherche")

    # Token Github
    def setTokenGithub(self, token:str):
        if token == "":
            return False
        return self.__fileUser.setValeurJson("tokenGithub", token)

    def getTokenGithub(self):
        return self.__fileUser.getContentJsonFlag("tokenGithub")

    # Work Folder

    def setWorkFolder(self):
        folder = filedialog.askdirectory(title="Dossier de travail")
        if folder == "":
            return False
        return self.__fileUser.setValeurJson("wordFolder", folder)

    def removeWorkFolder(self):
        return self.__fileUser.setValeurJson("wordFolder","")

    def getWorkFolder(self):
        return self.__fileUser.getContentJsonFlag("wordFolder")

    # Video Download Folder
    def setVideoDownloadFolder(self):
        folder = filedialog.askdirectory(title="Dossier de téléchargement de vidéo")
        if folder == "":
            return False
        return self.__fileUser.setValeurJson("videoDownloadFolder", folder)

    def removeVideoDownloadFolder(self):
        return self.__fileUser.setValeurJson("videoDownloadFolder", "")

    def getVideoDownloadFolder(self):
        return self.__fileUser.getContentJsonFlag("videoDownloadFolder")

    # Sound Micro
    def setSoundMicro(self, value:bool):
        if value:
            return self.__fileUser.setValeurJson("soundMicro", "1")
        else:
            return self.__fileUser.setValeurJson("soundMicro", "0")

    def getSoundMicro(self):
        soundMicro = self.__fileUser.getContentJsonFlag("soundMicro")
        if soundMicro is None:
            return "0"
        return soundMicro

    # List Word
    def addWord(self, word:str):
        if word == "":
            return False

        listWord = self.__fileUser.getFlagListJson("listWord")

        if listWord is None:
            listWord = []

        if word not in listWord:
            listWord.append(word)
            return self.__fileUser.setValeurJson("listWord", listWord)
        else:
            return False

    def removeWord(self, word:str):
        if word == "":
            return False

        listWord = self.__fileUser.getFlagListJson("listWord")

        if listWord is None:
            return False

        if word in listWord:
            listWord.remove(word)
            return self.__fileUser.setValeurJson("listWord", listWord)
        else:
            return False

    def getListWord(self):
        listWord = self.__fileUser.getFlagListJson("listWord")
        if listWord is None:
            return []
        return listWord