from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuroneOpen :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron,objHist:CHistorique) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__objHistorique = objHist
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
            if (("ouvre" in requette) or ("ouvrir" in requette) or ("lance" in requette)):
                if (("logiciel de présentation" in requette) or ("logiciel de diaporama" in requette) 
                    or ("diaporama" in requette) or ("microsoft powerpoint" in requette) 
                    or ("powerpoint" in requette) or ("google slides" in requette) 
                    or ("slides" in requette) or ("libreoffice impress" in requette) 
                    or ("impress" in requette) or ("prezi" in requette) 
                    or ("canva" in requette) or ("slideshare" in requette) 
                    or ("visme" in requette) or ("haiku deck" in requette) 
                    or ("powtoon" in requette)) :
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenDiapo(),""]
                    self.__objHistorique.setAction("Ouverture du logciel de présentation")
                else :
                    if (("navigateur internet" in requette) or ("browser" in requette) 
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
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenBrowser(),""]
                        self.__objHistorique.setAction("Ouverture du navigateur internet")
                    else :
                        if (("note" in requette) or ("bloc-notes" in requette) 
                            or ("bloc-note" in requette) or ("journal electronique" in requette) 
                            or ("microsoft onenote" in requette) or ("onenote" in requette) 
                            or ("simplenote" in requette) or ("bear" in requette)) :
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenNote(),""]
                            self.__objHistorique.setAction("Ouverture du logiciel de note")
                        else :
                            if ((("musique" in requette) or ("music" in requette) 
                                or ("windows media player" in requette) or ("vlc" in requette) 
                                or ("clementine" in requette) or ("groove music" in requette) 
                                or ("spotify" in requette) or ("deezer" in requette) 
                                or ("youTube music" in requette)) and ("france musique" not in requette)) :
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenMusic(),""]
                                self.__objHistorique.setAction("Ouverture du logiciel d'ecoute du musique")
                            else :
                                if ("europe 1" in requette):
                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(1),""]
                                    self.__objHistorique.setAction("Lancement de la radio europe 1")
                                else :
                                    if ("europe 2" in requette):
                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(2),""]
                                        self.__objHistorique.setAction("Lancement de la radio europe 2")
                                    else :
                                        if ("france info" in requette):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(3),""]
                                            self.__objHistorique.setAction("Lancement de la radio france info")
                                        else :
                                            if ("france inter" in requette):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(4),""]
                                                self.__objHistorique.setAction("Lancement de la radio france inter")
                                            else :
                                                if ("france musique" in requette):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(5),""]
                                                    self.__objHistorique.setAction("Lancement de la radio france musique")
                                                else :
                                                    if ("france culture" in requette):
                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(6),""]
                                                        self.__objHistorique.setAction("Lancement de la radio france culture")
                                                    else :
                                                        if ("france bleu" in requette):
                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(7),""]
                                                            self.__objHistorique.setAction("Lancement de la radio france bleu")
                                                        else :
                                                            if ("fun radio" in requette):
                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(8),""]
                                                                self.__objHistorique.setAction("Lancement de la radio fun radio")
                                                            else :
                                                                if ("nrj" in requette):
                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(9),""]
                                                                    self.__objHistorique.setAction("Lancement de la radio nrj")
                                                                else :
                                                                    if ("rfm" in requette):
                                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(10),""]
                                                                        self.__objHistorique.setAction("Lancement de la radio rfm")
                                                                    else :
                                                                        if ("nostalgi" in requette):
                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(11),""]
                                                                            self.__objHistorique.setAction("Lancement de la radio nostalgi")
                                                                        else :
                                                                            if ("skyrock" in requette):
                                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(12),""]
                                                                                self.__objHistorique.setAction("Lancement de la radio skyrock")
                                                                            else :
                                                                                if ("rtl" in requette):
                                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieStartRadio(13),""]
                                                                                    self.__objHistorique.setAction("Lancement de la radio rtl")
                                                                                else :
                                                                                    for i in range(0,nbLogiciel):
                                                                                        if listeLogiciel[i-1] in requette:
                                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSoftware(listeLogiciel[i-1]),""]
                                                                                            self.__objHistorique.setAction("Ouverture du logiciel "+listeLogiciel[i-1])
                                                                                            logOuverture = 1
                                                                                            break
                                                                                    if (logOuverture == 0) :
                                                                                        if ("youtube" in requette ):
                                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenYoutube(),""]
                                                                                            self.__objHistorique.setAction("Ouverture de youtube")
                                                                                        else :
                                                                                            if (("stockage en ligne" in requette) or ("stockage sur le cloud" in requette) 
                                                                                                or ("drive" in requette) or ("stokage cloud" in requette) 
                                                                                                or ("stockage distant" in requette) or ("google drive" in requette) 
                                                                                                or ("dropbox" in requette) or ("onedrive" in requette) 
                                                                                                or ("amazon drive" in requette) or ("box" in requette) 
                                                                                                or ("nextcloud" in requette)) :
                                                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenCloud(),""]
                                                                                                self.__objHistorique.setAction("Ouverture du site de stokage cloud")
                                                                                            else :
                                                                                                for i in range(0,nbSite):
                                                                                                    if (listeSite[i] in requette):
                                                                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSite(listeSite[i]),""]
                                                                                                        self.__objHistorique.setAction("Ouverture du site "+listeSite)
                                                                                                        break
                                                                                                if (self.__gestionNeuron.verrifSortie(self.__listSortie) == 0) :
                                                                                                    if (self.__gestionNeuron.getVous() == True) :
                                                                                                        self.__listSortie = ["Desoler "+self.__gestionNeuron.getGenre()+" mais je ne peux pas ouvrir ce que vous me demandez",""]
                                                                                                    else :
                                                                                                        self.__listSortie = ["Desoler "+self.__gestionNeuron.getGenre()+" mais je ne peux pas ouvrir ce que tu me demande",""]
            else :
                if (("liste les logiciels" in requette)or("quelles sont les logiciels enregister" in requette) 
                    or("quelles sont les logiciel enregister" in requette) or("quelles sont les logiciels enregiste" in requette) 
                    or("quelles sont les logiciels enregiste" in requette) or ("fais une liste des logiciel"in requette)
                    or ("fais une liste des logiciels"in requette) or ("liste les logiciel" in requette)):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieListLogiciel(nbLogiciel,listeLogiciel),""] 
                else :
                    if (("liste les sites" in requette)or("quelles sont les sites enregister" in requette) 
                    or("quelles sont les site enregister" in requette) or("quelles sont les sites enregiste" in requette) 
                    or("quelles sont les sites enregiste" in requette) or ("fais une liste des site"in requette)
                    or ("fais une liste des sites"in requette) or ("liste les site" in requette)): 
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieListSite(nbSite,listeSite),""]     
                    else :
                        if (("liste" in requette) and ("radio" in requette)):
                            self.__listSortie = ["Les radio qui peuvent etre lancer par l'assistant sont :"
                                                 +"\n- Europe 1"
                                                 +"\n- Europe 2"
                                                 +"\n- France Info"
                                                 +"\n- France Inter"
                                                 +"\n- France Musique"
                                                 +"\n- France Culture"
                                                 +"\n- France Bleu"
                                                 +"\n- Fun Radio"
                                                 +"\n- NRJ"
                                                 +"\n- RFM"
                                                 +"\n- Nostalgi"
                                                 +"\n- Skyrock"
                                                 +"\n- RTL"
                                                 ,""]
                            self.__valeurOut = 17                         
                                            
                                                
            #Mise a jour de la valeur 
            if (self.__valeurOut == 0):                                                              
                self.__valeurOut = self.__gestionNeuron.verrifSortie(self.__listSortie[0])