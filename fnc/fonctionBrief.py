from librairy.arrera_date import *
from fnc.fncBase import fncBase,gestionnaire
import threading as th
import random
class fncBrief(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__data_meteo = {}
        self.__data_task = {}

    def __meteo_fnc(self):
        return self._gestionnaire.getGestFNC().getFNCMeteo()

    def __work_fnc(self):
        return self._gestionnaire.getGestFNC().getFNCWork()

    def __task_fnc(self):
        return self._gestionnaire.getGestFNC().getFNCTask()

    def __actuality_fnc(self):
        return self._gestionnaire.getGestFNC().getFNCActu()

    def __brief_meteo(self,time:str):
        time_valide = ["morning","afternoon","evening"]
        self.__data_meteo = {}
        if time not in time_valide:
            return False

        fnc_meteo = self.__meteo_fnc()

        if time == "morning":
            # Home
            if fnc_meteo.weather_current("home"):
                w_home = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_home = {"ok":False}
            # Locate
            if fnc_meteo.weather_current("locate"):
                w_locate = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_locate = {"ok":False}
            # work
            if fnc_meteo.weather_current("work"):
                w_work = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_work = {"ok":False}

            self.__data_meteo = {"w_home":w_home,"w_locate":w_locate,"w_work":w_work}
            return True
        elif time == "afternoon":
            if fnc_meteo.weather_current("locate"):
                w_current = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else:
                w_current = {"ok":False}
            if fnc_meteo.weather_afternoon("locate"):
                w_afternoon = {"ok": True,
                             "town": fnc_meteo.getNameTown(),
                             "temp": fnc_meteo.getTemperature(),
                             "humidity": fnc_meteo.getHumidity(),
                             "description": fnc_meteo.getDescription(),
                             "icon": fnc_meteo.getIcon()}
            else :
                w_afternoon = {"ok":False}

            self.__data_meteo = {"w_current":w_current,"w_afternoon":w_afternoon}
            return True
        elif time == "evening":
            # Home
            if fnc_meteo.weather_tomorrow("home"):
                w_home = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_home = {"ok":False}
            # Locate
            if fnc_meteo.weather_tomorrow("locate"):
                w_locate = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_locate = {"ok":False}
            # work
            if fnc_meteo.weather_tomorrow("work"):
                w_work = {"ok":True,
                          "town":fnc_meteo.getNameTown(),
                          "temp":fnc_meteo.getTemperature(),
                          "humidity":fnc_meteo.getHumidity(),
                          "description":fnc_meteo.getDescription(),
                          "icon":fnc_meteo.getIcon()}
            else :
                w_work = {"ok":False}

            self.__data_meteo = {"w_home":w_home,"w_locate":w_locate,"w_work":w_work}
            return True

    def __task_brief(self):
        self.__data_task = {}

        fnc_task = self.__task_fnc()
        fnc_work = self.__work_fnc()

        all_task = fnc_task.getNoFinishTask()
        if all_task is None:
            all_task = []
            
        today_task = fnc_task.getListTaskToday()
        if today_task is None:
            today_task = []
            
        today_task = [element for element in today_task if element in all_task]
        all_task = [element for element in all_task if element not in today_task]

        projet_task = []

        listProjet = fnc_work.getListProjet()

        if listProjet is not None:
            for projet in listProjet:
                if fnc_work.openProjet(projet):
                    l = []
                    if fnc_work.setListTacheNoFinishProjet():
                        l = fnc_work.getListTacheNoFinishProjet()
                    fnc_work.closeProjet()

                    for d in l:
                        projet_task.append(d+f" du Projet : {projet}")


        self.__data_task = {"all":all_task,"today":today_task,"projet":projet_task}

    def __actu_brief(self):
        self.__data_actu = {}

        fnc_actu = self.__actuality_fnc()

        fnc_actu.setActu()
        fnc_actu.clear_articles()
        article = fnc_actu.getActu()

        if article:
            dict_cat = {}
            for a in article:
                cat = a.get("cathegorie", "Autre")
                if cat not in dict_cat:
                    dict_cat[cat] = []
                
                dict_cat[cat].append({
                    "titre": f"{a["titre"]} de {a["source"]}",
                    "lien": a.get("lien", "")
                })

            for cat, liste_art in dict_cat.items():
                if len(liste_art) > 3:
                    self.__data_actu[cat] = random.sample(liste_art, 3)
                else:
                    self.__data_actu[cat] = liste_art

    def morning_brief(self):
        th_meteo = th.Thread(target=self.__brief_meteo,args=("morning",))
        th_task = th.Thread(target=self.__task_brief)
        th_actuality = th.Thread(target=self.__actu_brief)

        th_meteo.start()
        th_task.start()
        th_actuality.start()

        return th_meteo,th_task,th_actuality

    def evening_brief(self):
        th_meteo = th.Thread(target=self.__brief_meteo,args=("evening",))
        th_actuality = th.Thread(target=self.__actu_brief)

        th_meteo.start()
        th_actuality.start()

        return th_meteo, th_actuality


    def afternoon_brief(self):
        th_meteo = th.Thread(target=self.__brief_meteo, args=("afternoon",))
        th_task = th.Thread(target=self.__task_brief)
        th_actuality = th.Thread(target=self.__actu_brief)

        th_meteo.start()
        th_task.start()
        th_actuality.start()

        return th_meteo, th_task, th_actuality

    def get_data_meteo(self):
        return self.__data_meteo

    def get_data_task(self):
        return self.__data_task

    def get_data_actu(self):
        return self.__data_actu