from gestionnaire.gestion import gestionnaire,confNeuron

conf = confNeuron(name="Opale",
                  lang="fr",
                  icon="asset/icon.png",
                  assetHorloge="asset/horloge/",
                  assetCalculatrice="asset/calculatrice/",
                  assetMicro = "",
                  assistant_color="white",
                  assistant_texte_color="black",
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
user = gest.getUserConf()



def main():
    boucle= True
    while boucle :
        print("_____________________________________________________")
        print("1.USER\n2.Genre\n3.Ville Meteo"
              "\n4.Domicile\n5.Travail\n6.Adresse Domicile"
              "\n7.Adresse Travail\n8.LOGICIEL\n9.Site Internet"
              "\n10.Moteur de recherche\n11.Token github\n12.Dossier de travail"
              "\n13.Dossier video\n14.Sound Micro\n15.Tiger Word\n0.Quitter")

        print("_____________________________________________________")
        boucleVerif = True
        while boucleVerif:
            nb = input("Choix : ")
            try:
                nb = int(nb)
                boucleVerif = False
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        match nb :
            case 0 :
                print("Au revoir !")
                boucle = False
            case 1:
                print("1.AJouter\n2.Lire")
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
                        user.setUser(nom)
                    case 2:
                        print(user.getUser())
            case 2:
                print("1.AJouter\n2.Lire")
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
                        genre = input("Genre : ")
                        user.setGenre(genre)
                    case 2:
                        print(user.getGenre())
            case 3:
                print("1.AJouter\n2.Lire\n3.Supprimer")
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
                        ville = input("Ville : ")
                        if user.addTown(ville):
                            print("Ville ajoutée avec succès.")
                        else:
                            print("Erreur lors de l'ajout de la ville ou la ville existe déjà.")
                    case 2:
                        print(user.getListVille())
                    case 3:
                        ville = input("Ville : ")
                        if user.removeTown(ville):
                            print("Ville supprimée avec succès.")
                        else:
                            print("Erreur lors de la suppression de la ville.")
            case 4 :
                print("1.AJouter\n2.Lire")
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
                        adresse = input("Adresse Domicile : ")
                        user.setAdresseDomicile(adresse)
                    case 2:
                        print(user.getAdresseDomicile())
            case 5:
                print("1.AJouter\n2.Lire")
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
                        adresse = input("Adresse Travail : ")
                        user.setAdresseTravail(adresse)
                    case 2:
                        print(user.getAdresseTravail())
            case 6:
                print("1.AJouter\n2.Lire")
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
                        lieu = input("Lieu Domicile : ")
                        user.setLieuDomicile(lieu)
                    case 2:
                        print(user.getLieuDomicile())
            case 7:
                print("1.AJouter\n2.Lire")
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
                        lieu = input("Lieu Travail : ")
                        user.setLieuTravail(lieu)
                    case 2:
                        print(user.getLieuTravail())
            case 9:
                print("1.AJouter\n2.Lire\n3.Supprimer")
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
                        site = input("Nom Site Internet : ")
                        url = input("URL du site : ")
                        if user.setSite(site, url):
                            print("Site ajouté avec succès.")
                        else:
                            print("Erreur lors de l'ajout du site ou le site existe déjà.")
                    case 2:
                        print(user.getSite())
                    case 3:
                        site = input("Site Internet : ")
                        if user.removeSite(site):
                            print("Site supprimé avec succès.")
                        else:
                            print("Erreur lors de la suppression du site.")
            case 10:
                print("1.AJouter\n2.Lire")
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
                        moteur = input("Moteur de recherche : ")
                        user.setMoteurRecherche(moteur)
                    case 2:
                        print(user.getMoteurRecherche())
            case 11:
                print("1.AJouter\n2.Lire")
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
                        token = input("Token Github : ")
                        if user.setTokenGithub(token):
                            print("Token ajouté avec succès.")
                        else:
                            print("Erreur lors de l'ajout du token ou le token existe déjà.")
                    case 2:
                        print(user.getTokenGithub())
            case 12:
                print("1.AJouter\n2.Lire\n3.Supprimer")
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
                        if user.setWorkFolder():
                            print("Dossier ajouté avec succès.")
                        else:
                            print("Erreur lors de l'ajout du dossier ou le dossier existe déjà.")
                    case 2:
                        print(user.getWorkFolder())
                    case 3:
                        if user.removeWorkFolder():
                            print("Dossier supprimé avec succès.")
                        else:
                            print("Erreur lors de la suppression du dossier.")
            case 13:
                print("1.AJouter\n2.Lire\n3.Supprimer")
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
                        if user.setVideoDownloadFolder():
                            print("Dossier ajouté avec succès.")
                        else:
                            print("Erreur lors de l'ajout du dossier ou le dossier existe déjà.")
                    case 2:
                        print(user.getVideoDownloadFolder())
                    case 3:
                        if user.removeVideoDownloadFolder():
                            print("Dossier supprimé avec succès.")
                        else:
                            print("Erreur lors de la suppression du dossier.")
            case 14:
                print("1.Activer\n2.Desactiver\n3.Voir")
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
                        if user.setSoundMicro(True):
                            print("Micro activé avec succès.")
                        else:
                            print("Erreur lors de l'activation du micro.")
                    case 2:
                        if user.setSoundMicro(False):
                            print("Micro désactivé avec succès.")
                        else:
                            print("Erreur lors de la désactivation du micro.")
                    case 3:
                        print(user.getSoundMicro())
            case 15:
                print("1.Ajouter\n2.Lire\n3.Supprimer")
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
                        word = input("Mot à ajouter : ")
                        if user.addWord(word):
                            print("Mot ajouté avec succès.")
                        else:
                            print("Erreur lors de l'ajout du mot ou le mot existe déjà.")
                    case 2:
                        print(user.getListWord())
                    case 3:
                        word = input("Mot à supprimer : ")
                        if user.removeWord(word):
                            print("Mot supprimé avec succès.")
                        else:
                            print("Erreur lors de la suppression du mot ou le mot n'existe pas.")
            case _:
                print("Errureur, veuillez choisir un nombre entre 0 et 13.")

if __name__ == "__main__":
    main()