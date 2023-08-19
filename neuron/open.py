from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneOpen :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #Recuperation atribut de l'assistant
        self.oldrequette = oldRequette
        self.oldsortie = oldSortie
        self.nbDiscution = self.gestionNeuron.getNbDiscution()
        self.name = self.gestionNeuron.getName()
        self.etatVous = self.gestionNeuron.getVous()
        self.genre = self.gestionNeuron.getGenre()
        self.user = self.gestionNeuron.getUser()
        self.bute = self.gestionNeuron.getBute()
        self.createur = self.gestionNeuron.getCreateur()
        listeLogiciel = self.gestionNeuron.getListLogiciel()
        nbLogiciel = int(self.gestionNeuron.getValeurfichierUtilisateur("nbSoft"))
        listeSite = self.gestionNeuron.getListWeb()
        nbSite = int(self.gestionNeuron.getValeurfichierUtilisateur("nbSite"))
        #varriable
        logOuverture = 0
        #fonction neuron Open
        if "ouvre" in requette or "ouvrir" in requette:
            if "traitement de texte" in requette or "microsoft word" in requette or "word" in requette or "libreOffice writer" in requette or "writer" in requette or "openOffice writer" in requette or  "wps office writer" in requette or "abiword" in requette or "zoho writer" in requette or "calligra words" in requette or "scrivener" in requette :
                text = self.fonctionArreraNetwork.sortieOpenTraitementTexte()
            else :
                if "tableur" in requette or "microsoft excel" in requette or "excel"in requette or "google sheets" in requette or "sheets" in requette or "libreOffice calc" in requette or "calc" in requette or "openOffice calc" in requette or "wps office spreadsheets" in requette or "zoho sheet" in requette or  "gnumeric" in requette or "onlyoffice spreadsheet editor" in requette or "calligra sheets" in requette :
                    text = self.fonctionArreraNetwork.sortieOpenTableur() 
                else :
                    if "logiciel de présentation" in requette or "logiciel de diaporama" in requette or "diaporama" in requette or "microsoft powerpoint" in requette or "powerpoint" in requette or "google slides" in requette or "slides" in requette or "libreoffice impress" in requette or "impress" in requette or "prezi" in requette or "canva" in requette or "slideshare" in requette or "visme" in requette or "haiku deck" in requette or "powtoon" in requette :
                        text = self.fonctionArreraNetwork.sortieOpenDiapo()
                    else :
                        if "navigateur internet" in requette or"browser" in requette or "logiciel de navigation" in requette or "client web" in requette or "explorateur web" in requette or "navigateur web" in requette or "fureteur web" in requette or "visualiseur web" in requette or "programme de navigation en ligne" in requette or "nagivateur de pages web" in requette or "visionneuse web" in requette or "google chrome" in requette or "chrome" in requette or "mozilla firefox" in requette or "mozilla" in requette or "firefox" in requette or "microsoft edge" in requette or "edge" in requette or "opera" in requette or "brave" in requette or "vivaldi" in requette or "tor browser" in requette or "tor browser" in requette :
                            text = self.fonctionArreraNetwork.sortieOpenBrowser()
                        else :
                            if "note" in requette or "bloc-notes" in requette or "bloc-note" in requette or "journal electronique" in requette or "microsoft onenote" in requette or "onenote" in requette or "simplenote" in requette or "bear" in requette :
                                text = self.fonctionArreraNetwork.sortieOpenNote()
                            else :
                                if "musique" in requette or "music" in requette or "Windows Media Player" in requette or "vlc" in requette or "clementine" in requette or "groove music" in requette or "spotify" in requette or "deezer" in requette or "youTube music" in requette :
                                    text = self.fonctionArreraNetwork.sortieOpenMusic()
                                else :
                                    for i in range(0,nbLogiciel):
                                        if listeLogiciel[i-1] in requette:
                                            text = self.fonctionArreraNetwork.sortieOpenSoftware(listeLogiciel[i-1])
                                            logOuverture = 1
                                            break
                                    if logOuverture == 0 :
                                        if "youtube" in requette :
                                            text = self.fonctionArreraNetwork.sortieOpenYoutube()
                                        else :
                                            if "stockage en ligne" in requette or "stockage sur le cloud" in requette or "drive" in requette or "stokage cloud" in requette or "stockage distant" in requette or "google drive" in requette or "dropbox" in requette or "onedrive" in requette or "amazon drive" in requette or "box" in requette or "nextcloud" in requette :
                                                text = self.fonctionArreraNetwork.sortieOpenCloud()
                                            else :
                                                for i in range(0,nbSite):
                                                    if listeSite[i-1] in requette:
                                                        text = self.fonctionArreraNetwork.sortieOpenSite(listeLogiciel[i-1])
                                                        break
                                        
                                            
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text