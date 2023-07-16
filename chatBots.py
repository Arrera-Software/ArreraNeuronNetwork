import datetime
import random
import time

class neuroneDiscution :
    def __init__(self,name:str,user:str,genre:str,createur:str,bute:str) :
        self.name = name
        self.user = user
        self.genre = genre
        self.createur = createur
        self.bute = bute
        self.nbDiscution = 0
        self.oldrequette =  ""
        self.oldSortie = ""
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
    
    def neurone(self,var):
        requette = str(str(var).lower())
        requette = self.netoyage(requette)
        text = ""
        hour = datetime.datetime.now().hour
        nbRand = 0
        if  "salut" in requette   or "bonjour" in requette  or "bonsoir" in requette:
            if "salut" in requette :
                nbRand = random.randint(1,2)
                if nbRand == 1 :
                    formule = "Salut"
                else : 
                    if hour>=0 and hour<3:
                        formule = "Salutation"
                    else :
                        if hour>=3 and hour<18:
                            formule ="Bonjours"
                        else :
                            formule = "Bonsoir"
            else :
                if "bonsoir" in requette :
                    formule = "Bonsoir"
                else :
                    formule = "Bonjour"
            if hour>=0 and hour<3 :
                text= str(formule+","+self.genre+" "+self.user+".Quesque vous faites si tart "+self.genre+" ?")
            else :
                if hour>= 3 and hour<= 6:
                    text= str(formule+","+self.genre+" "+self.user+".Quesque vous faite si tot ce matin "+self.genre+" ?")
                else :
                    if hour>= 6 and hour<= 10 :
                       text= str(formule+","+self.genre+" "+self.user+".Comment avez-vous dormie cette nuit  "+self.genre+" ?")
                    else :
                        if hour>= 10 and hour<= 12 : 
                           text= str(formule+","+self.genre+" "+self.user+".Comment c'est passer votre matinnée  "+self.genre+" ?")
                        else :
                            if hour>= 13 and hour<= 14 :
                                text= str(formule+","+self.genre+" "+self.user+". Comment ce passe votre debut d'aprés-midi "+self.genre+" ?") 
                            else :
                                if hour>= 15 and hour<= 18 :
                                    text= str(formule+","+self.genre+" "+self.user+". Comment ce passe votre aprés-midi "+self.genre+" ?")
                                else :
                                    if hour>= 18 and hour<= 20 : 
                                      text= str(formule+","+self.genre+" "+self.user+". Comment c'est passée votre journée "+self.genre+" ?") 
                                    else :
                                        if hour>= 20 and hour <= 23 : 
                                            text= str(formule+","+self.genre+" "+self.user+". Comment c'est passée votre journée "+self.genre+" ?") 
                                        else : 
                                            if hour >= 00 and hour < 3 : 
                                                text = str(formule+","+self.genre+" "+self.user+". Il faudrait allez-vous couché "+self.genre+" ?") 
                                            else :
                                                text =  str(formule)
            self.stokage(requette,text)
            self.nbDiscution += 1 
            return 1 , text
        else :
            if "bien" in requette or "oui" in requette:
                phrase = ""
                if "comment" in self.oldSortie and "c'est passer" in self.oldSortie or "ce passe" in self.oldSortie :
                    if "c'est passer" in self.oldSortie :
                        phrase = "Quesque vous avez fait de votre journée."
                    else :
                        if "ce passe" in self.oldSortie :
                            if "aprés-midi" in self.oldSortie :
                                if "debut" in self.oldSortie :
                                    phrase = "Quesque vous avez prévu de faire de votre aprés-midi "+ self.genre + ". Es que je peux vous etre utile ?"
                                else :
                                    phrase = "Quesque vous faite de votre apres-midi " + self.genre + ". En quoi je peux vous aidez ?"
                        else : 
                            if "avez vous dormie" in self.oldSortie and "nuit" in self.oldSortie :
                                phrase = "C'est super sa " + self.genre + ". Quesque vous avez prévu de faire aujourd'hui "+self.genre+ "?"
                            else :
                                if "Il faudrait allez-vous couché" in self.oldSortie or "Quesque vous faites si tart" in self.oldSortie :
                                    phrase = "Mais je pense "+self.genre+", qu'il faudrait allez vous coucher."
                                else : 
                                    phrase = ""
                nbRand = random.randint(0,2)
                listReponse = ["Je suis heureux de savoir que vous allez bien","Sa me rejouit que vous allez bein","Tant mieux "+self.genre]
                debut = listReponse[nbRand]
                listReponse2 = ["Je suis un programme informatique je resent pas de sentiment.","Je ne peut pas resentir de sentiment, je suis qu'un programmme informatique."]
                if "et vous" in requette or "vous" in requette or "et toi" in requette or "toi" in requette :
                    finPhrase = listReponse2[nbRand]
                else :
                    if "comment ça va " in requette or "ca va" in requette or "ça va" in requette or "comment vas tu" in requette or "comment allez vous" in requette or "tu vas bien" in requette or "vous allez bien" in requette or "est ce que tout va bien" in requette or "tout va bien pour toi" in requette or "tout va bien pour vous" in requette: 
                        finPhrase = listReponse2[nbRand]
                    else :
                        finPhrase = ""
                text = debut +" "+ phrase+" "+finPhrase 
                self.stokage(requette,text)
                self.nbDiscution += 1 
                return 1 , text                 
            else :
                if "toujours là"  in requette  or "es tu là" in requette or self.name in requette or "tu es là" in requette or "vous étes là" in requette or "vous etes là" in requette :
                    nbRand = random.randint(0,2)
                    listReponse3 = ["Je ne peut pas partir de tout façon","Je ne pas partir tant que je peux servir","A moin de m'arréter qui serait un acte horible je suis toujour la"]
                    text =str("Oui, je suis toujours la "+self.genre+" "+self.user+"." + listReponse3[nbRand])
                    self.stokage(requette,text)
                    self.nbDiscution += 1 
                    return 1 , text
                else :
                    if "tu es qui" in requette or "présente toi" in requette or "présentation" in requette or "qui es tu" in requette or "qui es tu" in requette:
                        if self.nbDiscution >= 5 :
                            finPhrase = str("Vous me parler depuis un moment sans savoir qui je suis ?")
                        else :
                            finPhrase = str("")
                        if self.name == "SIX" :
                            debutPhrase = str("Je suis Six , l'assistant personnelle Vocal de "+self.genre+" "+self.user+" "+". Crée par Baptiste Pauchet pour simplifier et automatiser l'uttilisation de son ordinateur et pour le divertire.")
                        else :
                            if self.name == "Ryley" :
                                debutPhrase = str("Je suis Ryley un assistant textuel crée a l'origine par Baptiste Pauchet et Wiruto2 .Pour les assister dans leurs etude et par la suite les aider dans le developement informatique")
                            else : 
                                debutPhrase = str("Je suis "+self.name+" crée par "+ self.createur + ". Qui a pour bute "+ self.bute+ ". Et qui utilise un algorythme d'assistant personnelle developper par Arrera Software")
                        text = debutPhrase+finPhrase
                        self.stokage(requette,text)
                        self.nbDiscution += 1 
                        return 1 , text
                    else :
                        if "comment ça va " in requette or "ca va" in requette or "ça va" in requette or "comment vas tu" in requette or "comment allez vous" in requette or "tu vas bien" in requette or "vous allez bien" in requette or "est ce que tout va bien" in requette or "tout va bien pour toi" in requette or "tout va bien pour vous" in requette: 
                            nbRand = random.randint(0,1)
                            listReponse = ["Je suis un programme informatique je resent pas de sentiment.","Je ne peut pas resentir de sentiment, je suis qu'un programmme informatique"]
                            text = listReponse[nbRand]
                            self.stokage(requette,text)
                            self.nbDiscution += 1 
                            return 1 , text
                        else :
                            if "tu peux me parler de toi" in requette or "tu peux te presenter" in requette:
                                if "tu es qui" in self.oldrequette or "présente toi" in self.oldrequette or "présentation" in self.oldrequette or "qui es tu" in self.oldrequette or "qui es tu" in self.oldrequette:
                                    phrase = "Je vous l'ai deja dit monsieur je peux pas trop vous dire plus je n'est pas de passion ni de hobbie je ne suis qu'un programme informatique"
                                else :
                                    phrase ="Je suis un assistant personnelle nommer "+self.name+" qui a été crée par Baptiste Pauchet. Je n'ai pas pas de passion ni de hobbie du a ma conditions de programme informatique."
                                text = "Ok ," + phrase
                                self.nbDiscution += 1 
                                self.stokage(requette,text)
                                return 1, text
                            else :
                                if "vous pouvez faire quoi" in requette or "tu peux faire quoi" in requette or "en quoi je peux vous étes utile" in requette or "que peut tu faire" in requette or "que pouvez-vous faire" in requette:
                                    text = ""
                                    return 2 , text
                                else :
                                    if "raconter une blague" in requette or "raconte-moi une blague" in requette :
                                        if "vous etes pas drole" in self.oldrequette or "tu es pas drole" in self.oldrequette :
                                            text ="Je peux pas raconter un blague si je suis pas drole"
                                            return 1, text
                                        else :
                                            nb = random.randint(0,8)
                                            text = self.blague[nb]+" "+self.reponseBlague[nb]
                                            self.nbDiscution += 1 
                                            self.stokage(requette,text)
                                            return 1, text
                                    if "vous etes pas drole" in requette  or "tu es pas drole" in requette :
                                        if "raconter une blague" in self.oldrequette or "raconte-moi une blague" in self.oldrequette :
                                            nb = random.randint(0,2)
                                            listReponse4 =  ["Je suis désoler de ne pas etre drole pour vous "+self.genre,"Désoler si je ne suis pas drole "+self.genre,"Je peux m'en raconter une autre"]
                                            text = listReponse4[nb]
                                            self.nbDiscution += 1 
                                            self.stokage(requette,text)
                                            return 1, text
                                    else :
                                        if self.oldSortie == "Je peux m'en raconter une autre" :
                                           if "vasy" in requette or "si tu veux" in requette or "comme tu veux" in requette or "comme vous voulez" in requette or "si vous voulez" in requette :
                                                nb = random.randint(0,8)
                                                text ="Ok, "+ self.blague[nb]+" "+self.reponseBlague[nb]
                                                self.nbDiscution += 1 
                                                self.stokage(requette,text)
                                                return 1, text
                                           else :
                                               if "non" in requette or "pas besoin" in requette :
                                                   text = "Comme vous voulez "+self.genre+", je voulez juste etre sympa"
                                        else :
                                            text = ""
                                            return 0 , text