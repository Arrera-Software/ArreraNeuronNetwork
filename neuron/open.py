from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneOpen :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__listSortie = ["",""]
        self.__valeurOut = int

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getOpen() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            #Recuperation atribut de l'assistant
            listeLogiciel = self.__gestionNeuron.getListLogiciel()
            nbLogiciel = len(listeLogiciel)
            listeSite = self.__gestionNeuron.getListWeb()
            nbSite = len(listeSite)
            #varriable
            logOuverture = 0
            #fonction neuron Open
            if (("ouvre" in requette) or ("ouvrir" in requette)):
                if (("traitement de texte" in requette) or ("microsoft word" in requette) 
                    or ("word" in requette) or ("libreOffice writer" in requette) 
                    or ("writer" in requette) or ("openOffice writer" in requette) 
                    or  ("wps office writer" in requette) or ("abiword" in requette) 
                    or ("zoho writer" in requette) or ("calligra words" in requette) 
                    or ("scrivener" in requette)) :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTraitementTexte(),""]
                else :
                    if (("tableur" in requette) or ("microsoft excel" in requette) 
                        or ("excel"in requette) or ("google sheets" in requette) 
                        or ("sheets" in requette) or ("libreOffice calc" in requette) 
                        or ("calc" in requette) or ("openOffice calc" in requette) 
                        or ("wps office spreadsheets" in requette) or ("zoho sheet" in requette) 
                        or  ("gnumeric" in requette) or ("onlyoffice spreadsheet editor" in requette) 
                        or ("calligra sheets" in requette)) :
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTableur(),""]
                    else :
                        if (("logiciel de présentation" in requette) or ("logiciel de diaporama" in requette) 
                            or ("diaporama" in requette) or ("microsoft powerpoint" in requette) 
                            or ("powerpoint" in requette) or ("google slides" in requette) 
                            or ("slides" in requette) or ("libreoffice impress" in requette) 
                            or ("impress" in requette) or ("prezi" in requette) 
                            or ("canva" in requette) or ("slideshare" in requette) 
                            or ("visme" in requette) or ("haiku deck" in requette) 
                            or ("powtoon" in requette)) :
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenDiapo(),""]
                        else :
                            if (("navigateur internet" in requette) or ("browser" in requette) 
                                or ("logiciel de navigation" in requette) or ("client web" in requette) 
                                or ("explorateur web" in requette) or ("navigateur web" in requette) 
                                or ("fureteur web" in requette) or ("visualiseur web" in requette) 
                                or ("programme de navigation en ligne" in requette) or ("nagivateur de pages web" in requette) 
                                or ("visionneuse web" in requette) or ("google chrome" in requette) 
                                or ("chrome" in requette) or ("mozilla firefox" in requette) 
                                or ("mozilla" in requette) or ("firefox" in requette) 
                                or ("microsoft edge" in requette) or ("edge" in requette) 
                                or ("opera" in requette) or ("brave" in requette) 
                                or ("vivaldi" in requette) or ("tor browser" in requette) 
                                or ("tor browser" in requette) or ("arc" in requette)) :
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenBrowser(),""]
                            else :
                                if (("note" in requette) or ("bloc-notes" in requette) 
                                    or ("bloc-note" in requette) or ("journal electronique" in requette) 
                                    or ("microsoft onenote" in requette) or ("onenote" in requette) 
                                    or ("simplenote" in requette) or ("bear" in requette)) :
                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenNote(),""]
                                else :
                                    if (("musique" in requette) or ("music" in requette) 
                                        or ("windows media player" in requette) or ("vlc" in requette) 
                                        or ("clementine" in requette) or ("groove music" in requette) 
                                        or ("spotify" in requette) or ("deezer" in requette) 
                                        or ("youTube music" in requette)) :
                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenMusic(),""]
                                    else :
                                        for i in range(0,nbLogiciel):
                                            if listeLogiciel[i-1] in requette:
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSoftware(listeLogiciel[i-1]),""]
                                                logOuverture = 1
                                                break
                                        if (logOuverture == 0) :
                                            if ("youtube" in requette ):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenYoutube(),""]
                                            else :
                                                if (("stockage en ligne" in requette) or ("stockage sur le cloud" in requette) 
                                                    or ("drive" in requette) or ("stokage cloud" in requette) 
                                                    or ("stockage distant" in requette) or ("google drive" in requette) 
                                                    or ("dropbox" in requette) or ("onedrive" in requette) 
                                                    or ("amazon drive" in requette) or ("box" in requette) 
                                                    or ("nextcloud" in requette)) :
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenCloud(),""]
                                                else :
                                                    for i in range(0,nbSite):
                                                        if (listeSite[i] in requette):
                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSite(listeSite[i]),""]
                                                            break
                                                    if (self.__gestionNeuron.verrifSortie(self.__listSortie) == 0) :
                                                        if (self.__gestionNeuron.getVous() == True) :
                                                            self.__listSortie = ["Desoler "+self.__gestionNeuron.getGenre()+" mais je ne peux pas ouvrir ce que vous me demandez",""]
                                                        else :
                                                            self.__listSortie = ["Desoler "+self.__gestionNeuron.getGenre()+" mais je ne peux pas ouvrir ce que tu me demande",""]
            else :
                if (("liste les logiciels" in requette)or("quelles sont les logiciels enregister" in requette) 
                    or ("fais une liste de logiciels"in requette) or ("liste les logiciel" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieListLogiciel(nbLogiciel,listeLogiciel),""]                                     
                                            
                                                
            #Mise a jour de la valeur                                                               
            self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])