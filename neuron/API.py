from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneAPI :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__gestNeuron = neuronGest
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__etatVilleDomicile = self.__gestionNeuron.getEtatLieuDomicile()
        self.__etatVilleTravail = self.__gestionNeuron.getEtatLieuTravail()
        self.__villeGPS1 = ""
        self.__listeLang = ["anglais","francais","espagnol","allemand", "chinois simplifie","chinois traditionnel",
                        "arabe", "russe","japonais","coreen","italien","portugais","neerlandais",
                        "suedois","danois","norvegien","finnois","grec","hebreu","indonesien"]
        
        self.__dictLang = {"anglais":"en","francais":"fr","espagnol":"es","allemand":"de", "chinois simplifie":"zh-CN",
                        "chinois traditionnel":"zh-TW","arabe":"ar", "russe":"ru","japonais":"ja",
                        "coreen":"ko","italien":"it","portugais":"pt","neerlandais":"nl","suedois":"sv",
                        "danois":"da","norvegien":"no","finnois":"fi","grec":"el","hebreu":"he","indonesien":"id"}

    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if self.__gestNeuron.getAPI() == True :
            #Initilisation des variable nbRand et text et valeur
            self.__listSortie = []
            self.__valeurOut = 0
            #Recuperation atribut de l'assistant
            oldsortie = self.__gestionNeuron.getOld()
            name = self.__gestionNeuron.getName()
            etatVous = self.__gestionNeuron.getVous()
            genre = self.__gestionNeuron.getGenre()
            user = self.__gestionNeuron.getUser()
            #reponse du neuron main
            if "resumer actualites" in requette or "resumer actu" in requette or "resumer" in requette or "resume" in requette :
                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.ResumerActualite()
            if "actualites" in requette :
                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieActualités()
            else :
                if "meteo" in requette :
                    nb = self.__gestionNeuron.getnbVilleMeteo()
                    villes = self.__gestionNeuron.getListVilleMeteo()
                    resultat = 0
                    if ("demain matin" in requette):
                        for i in range(0,nb):
                            ville = chaine.netoyage(villes[i])
                            if ville in requette :
                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmoroMorning(villes[i])
                                resultat = 1
                                break
                            else :
                                resultat = 0
                        if resultat == 0 :
                            if self.__etatVilleDomicile == True or self.__etatVilleTravail == True : 
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmoroMorning(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                else :
                                    if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmoroMorning(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                    else :
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmoroMorning("")
                            else :    
                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmoroMorning("")
                    else :
                        for i in range(0,nb):
                            ville = chaine.netoyage(villes[i])
                            if ville in requette :
                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(villes[i])
                                resultat = 1
                                break
                            else :
                                resultat = 0
                        if resultat == 0 :
                            if self.__etatVilleDomicile == True or self.__etatVilleTravail == True : 
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                else :
                                    if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                    else :
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday("")
                            else :    
                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday("")
                else :
                    if "temperature" in requette :
                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieTemperature()
                    else :
                        if "coordonnee gps" in requette or "position gps" in requette :
                            self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieGPS()
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
                                    if etatVous == True :
                                        self.__listSortie = ["J'espére que sa vous aidera "+genre+" "+user,""]
                                    else :
                                        self.__listSortie =["Voila "+user,""]
                                    self.__valeurOut = 4 
                                else :
                                    if etatde == True :
                                        if etatVous == True :
                                            self.__listSortie = ["Quelle est votre destination "+genre,""]
                                            self.__valeurOut = 4
                                        else :
                                            self.__listSortie = ["Quelle est ta destination final "+user,""]
                                            self.__valeurOut = 4
                                    else :
                                        if etatVous == True :
                                            self.__listSortie = ["Je suis desoler "+genre+" "+user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire",""]
                                            self.__valeurOut = 4
                                        else :
                                            self.__listSortie =["Desoler"+user+" Je ne peux pas te fournir ton itinéraire",""]
                                            self.__valeurOut = 4
                            if "Quelle est votre destination" in oldsortie or "Quelle est ta destination final" in oldsortie :
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
                                    if etatVous == True :
                                        self.__listSortie = ["J'espére que sa vous aidera "+genre+" "+user,""]
                                        self.__valeurOut = 4
                                    else :
                                        self.__listSortie =["Voila "+user,""]
                                        self.__valeurOut = 4
                                else :
                                    if etatVous == True :
                                        self.__listSortie = ["Je suis desoler "+genre+" "+user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire",""]
                                        self.__valeurOut = 4
                                    else :
                                        self.__listSortie =["Desoler"+user+" Je ne peux pas te fournir ton itinéraire",""]
                                        self.__valeurOut = 4
                            
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
                                            if etatVous == True :
                                                self.__listSortie=["J'espère que cet outil de traduction vous a sera utile "+genre,""]
                                                self.__valeurOut = 3
                                            else :
                                                self.__listSortie= ["J'espère que sa te sera utile  "+name,""]
                                                self.__valeurOut = 3
                                        else :
                                            if etatVous == True :
                                                self.__listSortie=["Desoler "+genre+". Mais les langues que vous demander ne son pas disponible.",""]
                                                self.__valeurOut = 1
                                            else :
                                                self.__listSortie=["Desoler,les langues que tu demande n'est pas disponible",""]
                                                self.__valeurOut = 1
                                    else :
                                        if etatVous == True :
                                            self.__listSortie=["Desoler "+genre+". Mais les langue que vous demander ne son pas disponible.",""]
                                            self.__valeurOut = 1
                                        else :
                                            self.__listSortie=["Desoler,les langues que tu demande n'est pas disponible",""]
                                            self.__valeurOut = 1