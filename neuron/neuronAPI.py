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
        
    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        nbRand = 0
        text = ""
        valeur = 0
        #Recuperation atribut de l'assistant
        self.oldrequette = self.gestionNeuron.getOldrequette()
        self.oldsortie = self.gestionNeuron.getOldSortie()
        self.nbDiscution = self.gestionNeuron.getNbDiscution()
        self.name = self.gestionNeuron.getName()
        self.etatVous = self.gestionNeuron.getVous()
        self.genre = self.gestionNeuron.getGenre()
        self.user = self.gestionNeuron.getUser()
        self.bute = self.gestionNeuron.getBute()
        self.createur = self.gestionNeuron.getCreateur()
        #reponse du neuron main
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
                            if "a" in requette or "au" in requette :
                                loc2 = requette.replace("comment","")
                                loc2 = requette.replace("aller","")
                                loc2 = requette.replace("trouve-moi","")
                                loc2 = requette.replace("trouve","")
                                loc2 = requette.replace("moi","")
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    sortieFnc = self.fonctionArreraNetwork.sortieItineraires("loc",self.gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                else :
                                    if "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        sortieFnc = self.fonctionArreraNetwork.sortieItineraires("loc",self.gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                    else :
                                        sortieFnc= self.fonctionArreraNetwork.sortieItineraires("loc",loc2)
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
        #Sauvegarde des sortie                         
        self.gestionNeuron.setHistory(text,requette)
        #Ajout d'une discution
        self.gestionNeuron.addDiscution()
        #Retour des valeur
        return valeur , text