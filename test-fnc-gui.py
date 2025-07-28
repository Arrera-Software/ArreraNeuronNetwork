import datetime

from gestionnaire.gestFNC import gestFNC
from gestionnaire.gestion import gestionnaire
from config.confNeuron import confNeuron

conf = confNeuron(name="Opale",
            lang="fr",
            icon="assets/icon.png",
            assetHorloge="asset/horloge/",
            assetCalculatrice="asset/calculatrice/",
            guiColor="white",
            textColor="black",
            bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
            createur="Pauchet Baptiste",
            listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                          "faire un résumer des actualités"],
            moteurderecherche="google",
            etatService=1,
            etatSoftware=1,
            etatTime=1,
            etatOpen=1,
            etatSearch=1,
            etatChatbot=1,
            etatApi=1,
            etatCodehelp=1,
            etatWork=1,
            etatSocket=1,
            lienDoc="www.google.com",
            fichierLangue="language/vouvoiment/")

gest = gestionnaire(conf)
fnc = gest.getGestFNC()

def partTask():
    taskBoucle = True
    while taskBoucle:
        print("Test des fonctions de tache")
        print(
            "1.Ajouter une tache\n2.Lister les taches\n3.Supprimer une tache\n4.Compter le nombre de taches\n5.finir une tache\n6.Check date today\n7.Tache a faire aujourd'hui\n8.Check date towmorow\n9.Tache a faire demain\n10.Check task late\n11.Tache en retard\n0.Quitter")
        print("__________________________\n")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                title = input("Titre de la tache : ")
                date = input("Date de la tache (YYYY-MM-DD) : ")
                try:
                    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                    description = input("Description de la tache : ")
                    print(fnc.getFNCTask().addTask(title, date, description))
                except ValueError:
                    print("Format de date invalide. Utilisez YYYY-MM-DD.")
            case 2:
                print(fnc.getFNCTask().getTask())
            case 3:
                taskId = input("Name : ")
                sortie = fnc.getFNCTask().delTask(taskId)
                if sortie:
                    print("Tache supprimer")
                else:
                    print("Erreur")
            case 4:
                print(f"Nombre de taches : {fnc.getFNCTask().getNbTask()}")
            case 5:
                taskId = input("Name : ")
                sortie = fnc.getFNCTask().finishTask(taskId)
                if sortie:
                    print("Tache terminer")
                else:
                    print("Erreur")
            case 6:
                taskId = input("Name : ")
                print(fnc.getFNCTask().checkDateTask(taskId))
            case 7:
                print(fnc.getFNCTask().getNbTaskToday())
                print(fnc.getFNCTask().getListTaskToday())
            case 8:
                taskId = input("Name : ")
                print(fnc.getFNCTask().checkDateTaskTowmorow(taskId))
            case 9:
                print(fnc.getFNCTask().getNbTaskTowmorow())
                print(fnc.getFNCTask().getListTaskTowmorow())
            case 10:
                taskId = input("Name : ")
                print(fnc.getFNCTask().checkTaskLate(taskId))
            case 11:
                print(fnc.getFNCTask().getNbTaskLate())
                print(fnc.getFNCTask().getListTaskLate())

            case 0:
                taskBoucle = False
            case _:
                print("Choix invalide, veuillez réessayer.")

def partSearch():
    searchBoucle = True
    while searchBoucle:
        print("Test des fonctions de recherche")
        print("1.Recherche Ecosia\n2.Recherche Bing\n3.Recherche Perplexity\n4.Recherche Google\n5.Recherche Qwant\n6.Recherche DuckDuckGo\n7.Recherche Big\n8.Recherche assistant\n0.Quitter")
        print("__________________________\n")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                query = input("Rechercher : ")
                fnc.getFNCSearch().ecosiaSearch(query)
            case 2:
                query = input("Rechercher : ")
                fnc.getFNCSearch().bingSearch(query)
            case 3:
                query = input("Rechercher : ")
                fnc.getFNCSearch().perplexitySearch(query)
            case 4:
                query = input("Rechercher : ")
                fnc.getFNCSearch().googleSearch(query)
            case 5:
                query = input("Rechercher : ")
                fnc.getFNCSearch().qwantSearch(query)
            case 6:
                query = input("Rechercher : ")
                fnc.getFNCSearch().duckduckgoSearch(query)
            case 7:
                query = input("Rechercher : ")
                fnc.getFNCSearch().bigRecherche(query)
            case 8:
                query = input("Rechercher : ")
                fnc.getFNCSearch().search(query)
            case 0:
                searchBoucle = False
            case _:
                print("Choix invalide, veuillez réessayer.")

def partDownload():
    downloadBoucle = True
    while downloadBoucle:
        print("Test des fonctions de telechargement")
        print("1.Voir les modes possible\n2.Telechargement en etapes\n3.Telechargement direct\n0.Quitter")
        print("__________________________\n")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                print(fnc.getFNCDownload().getAllMode())
            case 2:
                print("Telechargement en etapes")
                url = input("URL de la video : ")
                if fnc.getFNCDownload().setUrl(url):
                    print("URL enregistrée")
                    boucleVerif = True
                    while boucleVerif:
                        mode = input("Mode (1-2-3) : ")
                        try:
                            nb = int(mode)
                            if nb == 1 or nb == 2 or nb == 3:
                                boucleVerif = False
                        except ValueError:
                            print("Veuillez entrer un nombre valide.")
                    if fnc.getFNCDownload().refreshDirectory():
                        print("Dossier de telechargement enregistré")
                        if fnc.getFNCDownload().setMode(nb):
                            if fnc.getFNCDownload().download() :
                                print("Telechargement OK")
                            else :
                                print("Erreur lors du telechargement")
                        else :
                            print("Erreur lors de l'enregistrement du mode")
                    else :
                        print("Impossible d'enregistrer le dossier de telechargement")
                else :
                    print("Erreur lors de l'enregistrement de l'URL")
            case 3:
                print("Telechargement en direct")
                url = input("URL de la video : ")
                boucleVerif = True
                while boucleVerif:
                    mode = input("Mode (1-2-3) : ")
                    try:
                        nb = int(mode)
                        if nb == 1 or nb == 2 or nb == 3:
                            boucleVerif = False
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")
                if fnc.getFNCDownload().downloadDirectely(nb,url):
                    print("Telechargement OK")
            case 0:
                downloadBoucle = False
            case _:
                print("Choix invalide, veuillez réessayer.")

def partCalendar():
    calendarBoucle = True
    while calendarBoucle:
        print("Test des fonctions de calendrier")
        print("1.Ajouter un evenement\n2.Evenement enregister\n3.Voir les information d'un evenement\n4.Check event jour\n0.Quitter")
        print("__________________________\n")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                nom = input("Nom : ")
                date = input("Date (YYYY-MM-DD) : ")
                heure = input("Heure (00:00) : ")
                description = input("Description : ")
                lieu = input("Lieu : ")
                try :
                    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                except ValueError :
                    print("La date n'est pas valide")
                if fnc.getFNCCalendar().addEventToCalendar(nom,date,heure,description,lieu):
                    print("Evenement cree")
                else :
                    print("Impossible de cree l'evenement")
            case 2 :
                print(fnc.getFNCCalendar().getAllEvents())
            case 3 :
                name = input("Entrer le nom de l'evenement :")
                print(fnc.getFNCCalendar().getInformationEvent(name))
            case 4:
                print("Check des evenements du jour")
                print(fnc.getFNCCalendar().checkDateHourEvent())
            case 5 :
                print("Suppression d'un evenement")
                name = input("Entrer le nom de l'evenement :")
                if fnc.getFNCCalendar().delEvent(name):
                    print("Evenement supprimer")
                else :
                    print("Impossible de suppression d'un evenement")
            case 0 :
                calendarBoucle = False
            case _:
                print("Choix invalide, veuillez réessayer.")

def partGPS():
    gpsBoucle = True
    while gpsBoucle:
        print("Test des fonctions de GPS")
        print("1.Get Latitude longitude\n2.Get Ville\n3.Lancer un itineraire sur g map\n0.Quitter")
        print("__________________________\n")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                if fnc.getFNCGPS().locate():
                    print("Localisation reussie")
                    latitude = fnc.getFNCGPS().getLatitude()
                    longitude = fnc.getFNCGPS().getLongitude()
                    print(f"Latidude : {latitude} \n logitude : {longitude}")
                else:
                    print("Erreur de localisation")
            case 2:
                if fnc.getFNCGPS().locate():
                    print("Localisation reussie")
                    print(f"Ville : {fnc.getFNCGPS().getTown()}")
                else:
                    print("Erreur de localisation")
            case 3:
                depart = input("Ville : ")
                arrivee = input("Arrivée : ")
                if fnc.getFNCGPS().launchGoogleMapItinerary(depart, arrivee):
                    print("Itinéraire lancé dans le navigateur")
                else :
                    print("Erreur lors du lancement de l'itinéraire")
            case 0 :
                gpsBoucle = False
            case _:
                print("Choix invalide, veuillez réessayer.")

def main():
    while True:
        boucleVerif = True
        print("Teste des fonction d'Arrera Neuron NetworkW\n")
        print("1.Taches\n2.Recherche\n3.Download\n4.Calendrier\n5.GPS\n0.Quitter")
        print("__________________________\n")


        while boucleVerif:
            nb = input("Choix : ")
            try :
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb:
            case 1:
                partTask()
                break
            case 2 :
                partSearch()
                break
            case 3 :
                partDownload()
            case 4 :
                partCalendar()
            case 5 :
                partGPS()
            case 0:
                print("Fin du programme")
                break
            case _:
                continue

if __name__ == "__main__":
    main()