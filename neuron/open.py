from neuron.CNeuronBase import *

class neuroneOpen(neuronBase) :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork, objHist:CHistorique) :
        #Init objet
        self._gestionNeuron = gestionnaire
        self._fonctionArreraNetwork = fncArreraNetwork
        self._gestNeuron = self._gestionNeuron.getEtatNeuronObjet()
        self._objHistorique = objHist
        self._listSortie = ["", ""]
        self._valeurOut = 0

    def getListSortie(self)->list:
        return self._listSortie

    def getValeurSortie(self)->int :
        return self._valeurOut

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getOpen() == True :
            #Recuperation atribut de l'assistant
            listeLogiciel = self._gestionNeuron.getListLogiciel()
            nbLogiciel = len(listeLogiciel)
            listeSite = self._gestionNeuron.getListWeb()
            nbSite = len(listeSite)
            #varriable
            logOuverture = 0
            #fonction neuron Open
            if (("ouvre" in requette) or ("ouvrir" in requette) or ("lance" in requette)):
                if (("logiciel de présentation" in requette) or ("logiciel de diaporama" in requette)
                    or ("diaporama" in requette) or ("microsoft powerpoint" in requette)
                    or ("powerpoint" in requette) or ("google slides" in requette)
                    or ("slides" in requette) or ("libreoffice impress" in requette)
                    or ("impress" in requette) or ("prezi" in requette)
                    or ("canva" in requette) or ("slideshare" in requette)
                    or ("visme" in requette) or ("haiku deck" in requette)
                    or ("powtoon" in requette)) :
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenDiapo(), ""]
                    self._objHistorique.setAction("Ouverture du logciel de présentation")
                elif (("navigateur internet" in requette) or ("browser" in requette)
                        or ("logiciel de navigation" in requette) or ("client web" in requette)
                        or ("explorateur web" in requette) or ("navigateur web" in requette)
                        or ("fureteur web" in requette) or ("visualiseur web" in requette)
                        or ("programme de navigation en ligne" in requette) or ("navigateur de pages web" in requette)
                        or ("visionneuse web" in requette) or ("google chrome" in requette)
                        or ("chrome" in requette) or ("mozilla firefox" in requette)
                        or ("mozilla" in requette) or ("firefox" in requette)
                        or ("microsoft edge" in requette) or ("edge" in requette)
                        or ("opera" in requette) or ("brave" in requette)
                        or ("vivaldi" in requette) or ("tor browser" in requette)
                        or ("tor browser" in requette) or ("arc" in requette)) :
                        self._listSortie = [self._fonctionArreraNetwork.sortieOpenBrowser(), ""]
                        self._objHistorique.setAction("Ouverture du navigateur internet")
                elif (("note" in requette) or ("bloc-notes" in requette)
                        or ("bloc-note" in requette) or ("journal electronique" in requette)
                        or ("microsoft onenote" in requette) or ("onenote" in requette)
                        or ("simplenote" in requette) or ("bear" in requette)) :
                        self._listSortie = [self._fonctionArreraNetwork.sortieOpenNote(), ""]
                        self._objHistorique.setAction("Ouverture du logiciel de note")
                elif ((("musique" in requette) or ("music" in requette)
                        or ("windows media player" in requette) or ("vlc" in requette)
                        or ("clementine" in requette) or ("groove music" in requette)
                        or ("spotify" in requette) or ("deezer" in requette)
                        or ("youTube music" in requette)) and ("france musique" not in requette)) :
                        self._listSortie = [self._fonctionArreraNetwork.sortieOpenMusic(), ""]
                        self._objHistorique.setAction("Ouverture du logiciel d'ecoute du musique")
                elif ("europe 1" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(1), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 1")
                elif ("europe 2" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(2), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 2")
                elif ("france info" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(3), ""]
                        self._objHistorique.setAction("Lancement de la radio france info")
                elif ("france inter" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(4), ""]
                        self._objHistorique.setAction("Lancement de la radio france inter")
                elif ("france musique" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(5), ""]
                        self._objHistorique.setAction("Lancement de la radio france musique")
                elif ("france culture" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(6), ""]
                        self._objHistorique.setAction("Lancement de la radio france culture")
                elif ("france bleu" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(7), ""]
                        self._objHistorique.setAction("Lancement de la radio france bleu")
                elif ("fun radio" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(8), ""]
                        self._objHistorique.setAction("Lancement de la radio fun radio")
                elif ("nrj" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(9), ""]
                        self._objHistorique.setAction("Lancement de la radio nrj")
                elif ("rfm" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(10), ""]
                        self._objHistorique.setAction("Lancement de la radio rfm")
                elif ("nostalgi" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(11), ""]
                        self._objHistorique.setAction("Lancement de la radio nostalgi")
                elif ("skyrock" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(12), ""]
                        self._objHistorique.setAction("Lancement de la radio skyrock")
                elif ("rtl" in requette):
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(13), ""]
                        self._objHistorique.setAction("Lancement de la radio rtl")
                else :
                    for i in range(0,nbLogiciel):
                        if listeLogiciel[i-1] in requette:
                            self._listSortie = [self._fonctionArreraNetwork.sortieOpenSoftware(listeLogiciel[i - 1]), ""]
                            self._objHistorique.setAction("Ouverture du logiciel " + listeLogiciel[i - 1])
                            logOuverture = 1
                            break
                        if (logOuverture == 0) :
                            if ("youtube" in requette ):
                                self._listSortie = [self._fonctionArreraNetwork.sortieOpenYoutube(), ""]
                                self._objHistorique.setAction("Ouverture de youtube")
                            else :
                                if (("stockage en ligne" in requette) or ("stockage sur le cloud" in requette)
                                    or ("drive" in requette) or ("stokage cloud" in requette)
                                    or ("stockage distant" in requette) or ("google drive" in requette)
                                    or ("dropbox" in requette) or ("onedrive" in requette)
                                    or ("amazon drive" in requette) or ("box" in requette)
                                    or ("nextcloud" in requette)) :
                                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenCloud(), ""]
                                    self._objHistorique.setAction("Ouverture du site de stokage cloud")
                                else :
                                    for i in range(0,nbSite):
                                        if (listeSite[i] in requette):
                                            self._listSortie = [self._fonctionArreraNetwork.sortieOpenSite(listeSite[i]), ""]
                                            self._objHistorique.setAction("Ouverture du site " + listeSite[i])
                                            break
                                    if (self._gestionNeuron.verrifSortie(self._listSortie) == 0) :
                                        self._listSortie = [self._fonctionArreraNetwork.sortieNoOpen(), ""]
            else :
                if (("liste les logiciels" in requette)or("quelles sont les logiciels enregister" in requette)
                    or("quelles sont les logiciel enregister" in requette) or("quelles sont les logiciels enregiste" in requette)
                    or("quelles sont les logiciels enregiste" in requette) or ("fais une liste des logiciel"in requette)
                    or ("fais une liste des logiciels"in requette) or ("liste les logiciel" in requette)):
                        self._listSortie = [self._fonctionArreraNetwork.sortieListLogiciel(nbLogiciel, listeLogiciel), ""]
                else :
                    if (("liste les sites" in requette)or("quelles sont les sites enregister" in requette)
                    or("quelles sont les site enregister" in requette) or("quelles sont les sites enregiste" in requette)
                    or("quelles sont les sites enregiste" in requette) or ("fais une liste des site"in requette)
                    or ("fais une liste des sites"in requette) or ("liste les site" in requette)):
                        self._listSortie = [self._fonctionArreraNetwork.sortieListSite(nbSite, listeSite), ""]
                    elif (("liste" in requette) and ("radio" in requette)):
                        self._listSortie = [self._fonctionArreraNetwork.sortieListRadio()
                                             ,"radio"]
                        self._valeurOut = 17


            #Mise a jour de la valeur
            if (self._valeurOut == 0):
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])