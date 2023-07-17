import datetime
import random
import time

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
        text=self.salutation(hour)
        self.stokage("boot",text)
        self.nbDiscution += 1 
        return str(text)
    
    def salutation(self,hour):      
        if hour>=0 and hour<3 :
            if self.vous == True :
                formule = "Bonjour,"
                cmp = self.genre+" "+self.user
                phrase = ["Que fait vous si tot ?","J'espere que vous avez un peux dormie."]
            else :
                formule = "Zzzz "
                cmp = self.user
                phrase = ["Il faudrais peut etre dormir non ?","Comment peut tu travailler si tart ?"]
        else :
            if hour>= 3 and hour<= 6:
                if self.vous == True :
                    formule = "Bonjour,"
                    cmp = self.genre+" "+self.user
                    phrase = ["Etes-vous prét a travailler .",""]
                else :
                    formule = "Zzzz "
                    cmp = self.user
                    phrase = ["Il faut peut etre dormir non?","Comment peut tu travailler si tart ?"]   
            else :
                if hour>= 6 and hour<= 10 :
                    if self.vous == True :
                        formule = "Bonjour, "
                        cmp = self.genre+" "+self.user
                        phrase = ["J'espére que vous passer une bonne nuit.","J'espére que vous avez bien dormi."]
                    else :
                        formule = "Hey ,"
                        cmp = self.user
                        phrase = ["as-tu bien dormi ?","as-tu passer une bonne nuit ?"]
                else :
                    if hour>= 10 and hour<= 12 : 
                        if self.vous == True :
                            formule = "Bonjour, "
                            cmp = self.genre+" "+self.user
                            phrase = ["J'espére que vous passer une bonne matinée","J'espére que vous passer un bon début de journée"]
                        else :
                            formule = "Salut ,"
                            cmp = self.user
                            phrase = ["comment ce passe ta matinée?","Que fait tu de beau ce matin ?"]
                    else :
                        if hour>= 13 and hour<= 14 :
                            if self.vous == True :
                                formule = "Bonjour ,"
                                cmp = self.genre+" "+self.user
                                phrase = ["J'espére que vous passer une bonne aprem ?","J'espére que vous passer une bonne après-midi ?"]
                            else :
                                formule = "Alors "
                                cmp = self.user
                                phrase = ["pret a travailler ?","Es-tu prét a travailler cette aprem ?"]
                        else :
                            if hour>= 15 and hour<= 18 :
                                if self.vous == True :
                                    formule = "Bonjour ,"
                                    cmp = self.genre+" "+self.user
                                    phrase = ["Sur quoi je peux vous aider cette aprem ?","Comment je peux vous aidez ?"]
                                else :
                                    formule = "Salut"
                                    cmp = self.user
                                    phrase = ["Sur quoi tu travaille ?","En quoi je peux d'aider ?"]
                            else :
                                if hour>= 18 and hour<= 20 : 
                                    if self.vous == True :
                                        formule = "Bonsoir ,"
                                        cmp = self.genre+" "+self.user
                                        phrase = ["comment se passe votre début de soirée ?","j'espére que votre début de soirée se passe bien"]
                                    else :
                                        formule = "Alors"
                                        cmp = self.user
                                        phrase = ["Que veut-tu faire ce soir ?","Veux tu travailler ou te divertire ce soir ?"]
                                else :
                                    if hour>= 20 and hour <= 23 : 
                                        if self.vous == True :
                                            formule = "Bonsoir ,"
                                            cmp = self.genre+" "+self.user
                                            phrase = ["comment se passe votre soirée ?","J'espére que votre soirée c'est bien passer"]
                                        else :
                                            formule = "*baille*"
                                            cmp = self.user
                                            phrase = ["que fais tu si tard ?","pourquoi tu me réveiller si tart ?"]
                                    else : 
                                        if hour >= 00 and hour < 3 : 
                                            if self.vous == True :
                                                formule = "Bonjour,"
                                                cmp = self.genre+" "+self.user
                                                phrase = ["Que fait vous si tot ?","J'espere que vous avez un peux dormie."]
                                            else :
                                                formule = "Zzzz"
                                                cmp = self.user
                                                phrase = ["Il faut peut etre dormir non?","Comment peut tu travailler si tart ?"]
                                        else :
                                            if self.vous == True :
                                                formule = "Bonjour,"
                                                cmp = self.genre+" "+self.user
                                                phrase = ["Quesque vous voulez qu'on fasse",""]
                                            else :
                                                formule = "Salut,"
                                                cmp = self.user
                                                phrase = ["Tu veux que je t'aide a faire quoi ?",""]     
            
            nbrand = random.randrange(0,1)
            return str(formule+" "+cmp+" "+phrase[nbrand])
            
            
            
    
    def neurone(self,var):
        requette = str(str(var).lower())
        requette = self.netoyage(requette)
        text = ""
        hour = datetime.datetime.now().hour
        nbRand = 0
        if  "salut" in requette   or "bonjour" in requette  or "bonsoir" in requette:
            text = self.salutation(hour)
            self.stokage(requette,text)
            self.nbDiscution += 1 
            return 1 , text 
        