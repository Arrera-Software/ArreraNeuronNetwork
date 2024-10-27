from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuroneAPI :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__objHistorique = objHist
        self.__etatVilleDomicile = self.__gestionNeuron.getEtatLieuDomicile()
        self.__etatVilleTravail = self.__gestionNeuron.getEtatLieuTravail()
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
            #reponse du neuron main
            if (("resumer actualites" in requette) or ("resumer actu" in requette)) :
                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieResumerActualite()
                self.__objHistorique.setAction("Resumer actualiter")
            else :
                if (("resumer" in requette) and (("jour" in requette) or ("aujourd'hui" in requette))) :
                    nb,listout = self.__fonctionArreraNetwork.sortieResumerAll()
                    self.__listSortie = listout
                    self.__valeurOut = nb
                    self.__objHistorique.setAction("Resumer complete de la journee")
                else :
                    if "actualites" in requette or "actu" in requette:
                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieActualités()
                        self.__objHistorique.setAction("Actualités")
                    else :
                        if "meteo" in requette :
                            nb = self.__gestionNeuron.getnbVilleMeteo()
                            villes = self.__gestionNeuron.getListVilleMeteo()
                            resultat = 0
                            if ("demain midi" in requette):
                                for i in range(0,nb):
                                    ville = chaine.netoyage(villes[i])
                                    if ville in requette :
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmorNoon(villes[i])
                                        resultat = 1
                                        break
                                    else :
                                        resultat = 0
                                if resultat == 0 :
                                    if self.__etatVilleDomicile == True or self.__etatVilleTravail == True : 
                                        if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                            self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmorNoon(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                        else :
                                            if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmorNoon(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                            else :
                                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmorNoon("")
                                    else :    
                                        self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoTowmorNoon("")
                                self.__objHistorique.setAction("Meteo demain midi")
                            else :
                                if (("demain matin" in requette) or ("demain" in requette)):
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
                                        self.__objHistorique.setAction("Meteo demain matin")
                                else :
                                    for i in range(0,nb):
                                        ville = chaine.netoyage(villes[i])
                                        if ville in requette :
                                            self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(villes[i])
                                            self.__objHistorique.setAction("Meteo aujourd'hui dans "+ville[i])
                                            resultat = 1
                                            break
                                        else :
                                            resultat = 0
                                    if resultat == 0 :
                                        if self.__etatVilleDomicile == True or self.__etatVilleTravail == True : 
                                            if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                                self.__objHistorique.setAction("Meteo aujourd'hui au domicile")
                                            else :
                                                if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                                    self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                                    self.__objHistorique.setAction("Meteo aujourd'hui au lieu de travail")
                                                else :
                                                    self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday("")
                                                    self.__objHistorique.setAction("Meteo aujourd'hui a la localisation")
                                        else :    
                                            self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieMeteoToday("")
                                            self.__objHistorique.setAction("Meteo aujourd'hui a la localisation")

                        else :
                            if "temperature" in requette :
                                self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieTemperature()
                                self.__objHistorique.setAction("Temperature")
                            else :
                                if "coordonnee gps" in requette or "position gps" in requette :
                                    self.__valeurOut,self.__listSortie = self.__fonctionArreraNetwork.sortieGPS()
                                    self.__objHistorique.setAction("Possition gps")
                                else :
                                    if ((("indique moi l'itineraire de" in requette)and("sur le gps" in requette))
                                        or(("lance le gps pour un trajet de" in requette )and("a" in requette))):
                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieItineraire(requette),""]
                                        self.__valeurOut = 1
                                        self.__objHistorique.setAction("Ouverture d'un itineraire sur google map")
                                    else :
                                        if ("gps aide" in requette):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieHelpItineraire(),""]
                                            self.__valeurOut = 1
                                        else :
                                            if "traduis" in requette or "traduction" in requette or "traduire" in requette :
                                                chaineCarractere = str(requette).lower()
                                                presenceLang = False
                                                self.__objHistorique.setAction("Outil de traduction")
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
                                                        self.__listSortie= [
                                                            self.__fonctionArreraNetwork.sortieTraducteur(self.__dictLang[firstLang],self.__dictLang[secondLang])
                                                            ,""]
                                                        self.__valeurOut = 3
                                                    else :
                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieErrorLangue(),""]
                                                        self.__valeurOut = 1
                                                else :
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieErrorLangue(), ""]
                                                    self.__valeurOut = 1