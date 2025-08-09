from librairy.travailJSON import *
from gestionnaire.gestion import gestionnaire
from pathlib import Path

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
    "videoDownloadFolder":""
}

class gestUserSetting:
    def __init__(self,gestionnaire:gestionnaire):
        self.__osDect = gestionnaire.getOSObjet()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux(): # Linux
            home = Path.home()
            self.__userSettingPath = str(home)+"/.config/arrera-assistant/user-config.json"
            self.__userTaskPath = str(home)+"/.config/arrera-assistant/user-task.json"
            self.__userHistoriquePath = str(home)+"/.config/arrera-assistant/user-hist.json"
            self.__userEventPath = str(home)+"/.config/arrera-assistant/user-event.json"
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