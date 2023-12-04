from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneAPI :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__etatVilleDomicile = self.__gestionNeuron.getEtatLieuDomicile()
        self.__etatVilleTravail = self.__gestionNeuron.getEtatLieuTravail()
        self.__villeGPS1 = ""
        self.__villeGPS2 = ""
        self.__listeLang = ["anglais","francais","espagnol","allemand", "chinois simplifie","chinois traditionnel",
                        "arabe", "russe","japonais","coreen","italien","portugais","neerlandais",
                        "suedois","danois","norvegien","finnois","grec","hebreu","indonesien"]
        
        self.__dictLang = {"anglais":"en","francais":"fr","espagnol":"es","allemand":"de", "chinois simplifie":"zh-CN",
                        "chinois traditionnel":"zh-TW","arabe":"ar", "russe":"ru","japonais":"ja",
                        "coreen":"ko","italien":"it","portugais":"pt","neerlandais":"nl","suedois":"sv",
                        "danois":"da","norvegien":"no","finnois":"fi","grec":"el","hebreu":"he","indonesien":"id"}
        
    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #Recuperation atribut de l'assistant
        self.__oldrequette = oldRequette
        self.__oldsortie = oldSortie
        self.__nbDiscution = self.__gestionNeuron.getNbDiscution()
        self.__name = self.__gestionNeuron.getName()
        self.__etatVous = self.__gestionNeuron.getVous()
        self.__genre = self.__gestionNeuron.getGenre()
        self.__user = self.__gestionNeuron.getUser()
        self.__bute = self.__gestionNeuron.getBute()
        self.__createur = self.__gestionNeuron.getCreateur()
        #reponse du neuron main
        if "resumer actualites" in requette or "resumer actu" in requette or "resumer" in requette :
            text = self.__fonctionArreraNetwork.ResumerActualite()
        if "actualites" in requette :
            text = self.__fonctionArreraNetwork.sortieActualités()
        else :
            if "meteo" in requette :
                nb = self.__gestionNeuron.getnbVilleMeteo()
                villes = self.__gestionNeuron.getListVilleMeteo()
                resultat = 0
                for i in range(0,nb):
                    ville = chaine.netoyage(villes[i])
                    if ville in requette :
                        text = self.__fonctionArreraNetwork.sortieMeteo(villes[i])
                        resultat = 1
                        break
                    else :
                        resultat = 0
                if resultat == 0 :
                    if self.__etatVilleDomicile == True or self.__etatVilleTravail == True : 
                        if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                            text = self.__fonctionArreraNetwork.sortieMeteo(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                        else :
                            if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                text = self.__fonctionArreraNetwork.sortieMeteo(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                            else :
                                text = self.__fonctionArreraNetwork.sortieMeteo("")
                    else :    
                        text = self.__fonctionArreraNetwork.sortieMeteo("")
            else :
                if "temperature" in requette :
                    text = self.__fonctionArreraNetwork.sortieTemperature()
                else :
                    if "coordonnee gps" in requette or "position gps" in requette :
                        text = self.__fonctionArreraNetwork.sortieGPS()
                    else :
                        if "itineraire" in requette or "comment aller" in requette :
                            sortieFnc = False
                            etatde = False
                            if "de" in requette :
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    self.__villeGPS1 = self.__gestionNeuron.getValeurfichierUtilisateur("adresseDomicile")
                                    etatde = True
                                else :
                                    if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self.__villeGPS1 = self.__gestionNeuron.getValeurfichierUtilisateur("adresseTravail")
                                        etatde = True
                                    else :
                                        loc = requette.replace("comment","")
                                        loc = requette.replace("aller","")
                                        loc = requette.replace("trouve-moi","")
                                        loc = requette.replace("trouve","")
                                        loc = requette.replace("moi","")
                                        self.__villeGPS1 = loc
                                        etatde = True
                            else :
                                if "a" in requette or "au" in requette :
                                    if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                        sortieFnc = self.__fonctionArreraNetwork.sortieItineraires("loc",self.__gestionNeuron.getValeurfichierUtilisateur("adresseDomicile"))
                                    else :
                                        if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                            sortieFnc = self.__fonctionArreraNetwork.sortieItineraires("loc",self.__gestionNeuron.getValeurfichierUtilisateur("adresseTravail"))
                                        else :
                                            loc = requette.replace("comment","")
                                            loc = requette.replace("aller","")
                                            loc = requette.replace("trouve-moi","")
                                            loc = requette.replace("trouve","")
                                            loc = requette.replace("moi","")
                                            sortieFnc= self.__fonctionArreraNetwork.sortieItineraires("loc",loc)
                            if sortieFnc== True :
                                if self.__etatVous == True :
                                    text = "J'espére que sa vous aidera "+self.__genre+" "+self.__user
                                else :
                                    text ="Voila "+self.__user
                            else :
                                if etatde == True :
                                    if self.__etatVous == True :
                                        text = "Quelle est votre destination "+self.__genre
                                    else :
                                        text = "Quelle est ta destination final "+self.__user
                                else :
                                    if self.__etatVous == True :
                                        text = "Je suis desoler "+self.__genre+" "+self.__user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire"
                                    else :
                                        text ="Desoler"+self.__user+" Je ne peux pas te fournir ton itinéraire"
                        if "Quelle est votre destination" in self.__oldsortie or "Quelle est ta destination final" in self.__oldsortie :
                            sortieFnc = False
                            if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                sortieFnc = self.__fonctionArreraNetwork.sortieItineraires(self.__villeGPS1,self.__gestionNeuron.getValeurfichierUtilisateur("adresseDomicile"))
                            else :
                                if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                    sortieFnc = self.__fonctionArreraNetwork.sortieItineraires(self.__villeGPS1,self.__gestionNeuron.getValeurfichierUtilisateur("adresseTravail"))
                                else :
                                    loc = requette.replace("comment","")
                                    loc = requette.replace("aller","")
                                    loc = requette.replace("trouve-moi","")
                                    loc = requette.replace("trouve","")
                                    loc = requette.replace("moi","")
                                    sortieFnc = self.__fonctionArreraNetwork.sortieItineraires(self.__villeGPS1,loc)
                            if sortieFnc== True :
                                if self.__etatVous == True :
                                    text = "J'espére que sa vous aidera "+self.__genre+" "+self.__user
                                else :
                                    text ="Voila "+self.__user
                            else :
                                if self.__etatVous == True :
                                    text = "Je suis desoler "+self.__genre+" "+self.__user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire"
                                else :
                                    text ="Desoler"+self.__user+" Je ne peux pas te fournir ton itinéraire"
                        else :
                            if "traduis" in requette or "traduction" in requette or "traduire" in requette :
                                chaineCarractere = str(requette).lower()
                                presenceLang = False
                                for i in range(0,len(self.__listeLang)-1):
                                    if self.__listeLang[i] in chaineCarractere :
                                        presenceLang = True
                                        break
                                if presenceLang == True :
                                    presenceLang = False
                                    firstLang = chaine.firstMots(chaineCarractere,self.__listeLang)
                                    chaineCarractere = chaineCarractere.replace(firstLang,"")
                                    for i in range(0,len(self.__listeLang)-1):
                                        if self.__listeLang[i] in chaineCarractere :
                                            presenceLang = True
                                            break
                                    if presenceLang == True :
                                        secondLang = chaine.firstMots(chaineCarractere,self.__listeLang)
                                        self.__fonctionArreraNetwork.sortieTraducteur(self.__dictLang[firstLang],self.__dictLang[secondLang])
                                        if self.__etatVous == True :
                                            text="J'espère que cet outil de traduction vous a sera utile "+self.__genre
                                        else :
                                            text= "J'espère que sa te sera utile  "+self.__name
                                    else :
                                        if self.__etatVous == True :
                                            text="Desoler "+self.__genre+". Mais les langues que vous demander ne son pas disponible."
                                        else :
                                            text="Desoler,les langues que tu demande n'est pas disponible"
                                else :
                                    if self.__etatVous == True :
                                        text="Desoler "+self.__genre+". Mais les langue que vous demander ne son pas disponible."
                                    else :
                                        text="Desoler,les langues que tu demande n'est pas disponible"
                                
      
                                
                            
        #Mise a jour de la valeur                                                               
        valeur = self.__gestionNeuron.verrifSortie(text)
        return valeur , text