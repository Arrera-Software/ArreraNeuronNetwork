from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneSoftware :
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
        #reponse neuron software
        if "telecharge" in requette :
            if "video" in requette :
                text = self.fonctionArreraNetwork.sortieDownload("video")
            else :
                if "musique" in requette :
                    text = self.fonctionArreraNetwork.sortieDownload("music")
                else :
                    if self.etatVous == True :
                        text = "Je suis désoler "+self.genre+" mais je ne peux télécharger que des vidéo ou de musique"
                    else :
                        text = self.user+" je ne peux télécharger que de video ou de musique. "
        if "calculatrice" in requette or "calculette" in requette :
            if "nombre complex" in requette or "nb complex" in requette :
                text = self.fonctionArreraNetwork.sortieCalculatrice("1")
            else :
                text = self.fonctionArreraNetwork.sortieCalculatrice("0")
        else :
            if "pythagore" in requette :
                text = self.fonctionArreraNetwork.sortieCalculatrice("2")
        if "ouvre" in requette :
            listeLogiciel = self.gestionNeuron.getListLogiciel()
            nbLogiciel = int(self.gestionNeuron.getValeurfichierUtilisateur("nbSoft"))
            logOuvrerture = 0
            i = 0 
            for i in range(0,nbLogiciel):
                if listeLogiciel[i-1] in requette:
                    text = self.fonctionArreraNetwork.sortieOpenSoftware(listeLogiciel[i-1])
                    logOuvrerture = 1
                    break
                else :
                    logOuvrerture = 0
            if logOuvrerture == 0 :
                if "traitement de texte" in requette or "microsoft word" in requette or "word" in requette or "libreOffice writer" in requette or "writer" in requette or "openOffice writer" in requette or  "wps office writer" in requette or "abiword" in requette or "zoho writer" in requette or "calligra words" in requette or "scrivener" in requette :
                    text = self.fonctionArreraNetwork.sortieOpenTraitementTexte()
                else :
                    if "tableur" in requette or "microsoft excel" in requette or "excel"in requette or "google sheets" in requette or "sheets" in requette or "libreOffice calc" in requette or "calc" in requette or "openOffice calc" in requette or "wps office spreadsheets" in requette or "zoho sheet" in requette or  "gnumeric" in requette or "onlyoffice spreadsheet editor" in requette or "calligra sheets" in requette :
                        text = self.fonctionArreraNetwork.sortieOpenTableur()    
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text