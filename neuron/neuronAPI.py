from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *

class neuroneAPI :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork) :
        #Init objet
        self.gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork
        self.etatVilleDomicile = self.gestionNeuron.getEtatLieuDomicile()
        self.etatVilleTravail = self.gestionNeuron.getEtatLieuTravail()
        self.villeGPS1 = ""
        self.villeGPS2 = ""
        
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
        #reponse du neuron main
        if "resumer actualites" in requette or "resumer actu" in requette or "resumer" in requette :
            text = self.fonctionArreraNetwork.ResumerActualite()
        if "actualites" in requette :
            text = self.fonctionArreraNetwork.sortieActualités()
        else :
            if "meteo" in requette :
                nb = self.gestionNeuron.getnbVilleMeteo()
                villes = self.gestionNeuron.getListVilleMeteo()
                resultat = 0
                for i in range(0,nb):
                    ville = chaine.netoyage(villes[i])
                    if ville in requette :
                        text = self.fonctionArreraNetwork.sortieMeteo(villes[i])
                        resultat = 1
                        break
                    else :
                        resultat = 0
                if resultat == 0 :
                    if self.etatVilleDomicile == True or self.etatVilleTravail == True : 
                        if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                            text = self.fonctionArreraNetwork.sortieMeteo(self.gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                        else :
                            if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                text = self.fonctionArreraNetwork.sortieMeteo(self.gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                            else :
                                text = self.fonctionArreraNetwork.sortieMeteo("")
                    else :    
                        text = self.fonctionArreraNetwork.sortieMeteo("")
            else :
                if "temperature" in requette :
                    text = self.fonctionArreraNetwork.sortieTemperature()
                else :
                    if "coordonnee gps" in requette or "position gps" in requette :
                        text = self.fonctionArreraNetwork.sortieGPS()
                    else :
                        if "itineraire" in requette or "comment aller" in requette :
                            sortieFnc = False
                            etatde = False
                            if "de" in requette :
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    self.villeGPS1 = self.gestionNeuron.getValeurfichierUtilisateur("adresseDomicile")
                                    etatde = True
                                else :
                                    if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self.villeGPS1 = self.gestionNeuron.getValeurfichierUtilisateur("adresseTravail")
                                        etatde = True
                                    else :
                                        loc = requette.replace("comment","")
                                        loc = requette.replace("aller","")
                                        loc = requette.replace("trouve-moi","")
                                        loc = requette.replace("trouve","")
                                        loc = requette.replace("moi","")
                                        self.villeGPS1 = loc
                                        etatde = True
                            else :
                                if "a" in requette or "au" in requette :
                                    if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                        sortieFnc = self.fonctionArreraNetwork.sortieItineraires("loc",self.gestionNeuron.getValeurfichierUtilisateur("adresseDomicile"))
                                    else :
                                        if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                            sortieFnc = self.fonctionArreraNetwork.sortieItineraires("loc",self.gestionNeuron.getValeurfichierUtilisateur("adresseTravail"))
                                        else :
                                            loc = requette.replace("comment","")
                                            loc = requette.replace("aller","")
                                            loc = requette.replace("trouve-moi","")
                                            loc = requette.replace("trouve","")
                                            loc = requette.replace("moi","")
                                            sortieFnc= self.fonctionArreraNetwork.sortieItineraires("loc",loc)
                            if sortieFnc== True :
                                if self.etatVous == True :
                                    text = "J'espére que sa vous aidera "+self.genre+" "+self.user
                                else :
                                    text ="Voila "+self.user
                            else :
                                if etatde == True :
                                    if self.etatVous == True :
                                        text = "Quelle est votre destination "+self.genre
                                    else :
                                        text = "Quelle est ta destination final "+self.user
                                else :
                                    if self.etatVous == True :
                                        text = "Je suis desoler "+self.genre+" "+self.user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire"
                                    else :
                                        text ="Desoler"+self.user+" Je ne peux pas te fournir ton itinéraire"
                        if "Quelle est votre destination" in self.oldsortie or "Quelle est ta destination final" in self.oldsortie :
                            sortieFnc = False
                            if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                sortieFnc = self.fonctionArreraNetwork.sortieItineraires(self.villeGPS1,self.gestionNeuron.getValeurfichierUtilisateur("adresseDomicile"))
                            else :
                                if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                    sortieFnc = self.fonctionArreraNetwork.sortieItineraires(self.villeGPS1,self.gestionNeuron.getValeurfichierUtilisateur("adresseTravail"))
                                else :
                                    loc = requette.replace("comment","")
                                    loc = requette.replace("aller","")
                                    loc = requette.replace("trouve-moi","")
                                    loc = requette.replace("trouve","")
                                    loc = requette.replace("moi","")
                                    sortieFnc = self.fonctionArreraNetwork.sortieItineraires(self.villeGPS1,loc)
                            if sortieFnc== True :
                                if self.etatVous == True :
                                    text = "J'espére que sa vous aidera "+self.genre+" "+self.user
                                else :
                                    text ="Voila "+self.user
                            else :
                                if self.etatVous == True :
                                    text = "Je suis desoler "+self.genre+" "+self.user+" mais je subis un probleme qui m'empeche de vous montrer l'itinéraire"
                                else :
                                    text ="Desoler"+self.user+" Je ne peux pas te fournir ton itinéraire"
                            
                            
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        return valeur , text