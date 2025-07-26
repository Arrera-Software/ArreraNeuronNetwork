import datetime

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

def main():
    while True:
        boucleVerif = True
        print("Teste des fonction d'Arrera Neuron NetworkW\n")
        print("1.Taches\n2.Recherche\n0.Quitter")
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
            case 0:
                print("Fin du programme")
                break
            case _:
                continue

if __name__ == "__main__":
    main()