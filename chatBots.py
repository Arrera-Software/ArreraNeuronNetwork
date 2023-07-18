import datetime
import random
import time
#fichier
from formule import*
class neuroneDiscution :
    def __init__(self,name:str,user:str,genre:str,createur:str,bute:str,vous:bool) :
        self.name = name
        self.user = user
        self.genre = genre
        self.createur = createur
        self.bute = bute
        self.nbDiscution = 0
        self.oldrequette =  ""
        self.oldSortie = ""
        self.vous = vous
        self.objetFormule = formule(self.vous)
        self.blague = ["Que dit une noisette quand elle tombe dans l’eau ?"
                        ,"Comment est-ce que les abeilles communiquent entre elles ?"
                        ,"Quel est l’arbre préféré du chômeur ?","Qu’est-ce qu’une frite enceinte ?"
                        ,"Que dit une mère à son fils geek quand le dîner est servi ?"
                        ,"Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?"
                        ,"Pourquoi les Ch’tis aiment les fins de vacances au camping ?"
                        ,"Quelle est la partie de la voiture la plus dangereuse ?"
                        ,"Pourquoi dit-on que les poissons travaillent illégalement ?"
                        ,"Mettre du sirop dans son gel douche"] 
        self.reponseBlague=["Je me noix."
                            ,"Par-miel."
                            ,"Le bouleau."
                            ,"Une patate sautée."
                            ,"Alt Tab !"
                            ,"Marcher"
                            ,"Parce que c’est le moment où ils peuvent démonter leur tente."
                            ,"La conductrice."
                            ,"Parce qu'ils n'ont pas de FISH de paie"
                            ,"En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible."]
        
    
    def stokage(self,requette,text):
        self.oldrequette = requette.lower()
        self.oldSortie = text.lower()
    
    def netoyage(self,chaine):
        chaine = str(chaine)
        chaine.replace("-"," ")
        chaine.replace('"'," ")
        chaine.replace("_"," ")
        chaine.replace('/'," ")
        return chaine
    
    def boot(self):
        hour = datetime.datetime.now().hour
        text= self.objetFormule.salutation(hour)
        self.stokage("boot",text)
        self.nbDiscution += 1 
        return str(text)
    
    def shutdown(self):
        hour = datetime.datetime.now().hour
        text = self.objetFormule.aurevoir(hour)
        return str(text)
        
    def neurone(self,var):
        requette = str(str(var).lower())
        requette = self.netoyage(requette)
        text = ""
        hour = datetime.datetime.now().hour
        nbRand = 0
        if  "salut" in requette   or "bonjour" in requette  or "bonsoir" in requette:
            text = self.objetFormule.aurevoir(hour)
            self.stokage(requette,text)
            self.nbDiscution += 1 
            return 1 , text 
        else :
            if "stop"in requette or "au revoir" in requette or "quitter" in requette or "bonne nuit" in requette or "adieu" in requette or "bonne soirée" in requette :
                text = self.objetFormule.aurevoir(hour)
                return 15 , text
        