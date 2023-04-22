from unidecode import unidecode
import datetime
import random

class neuroneDiscution :
    def __init__(self,name,UserCourt,GenreCourt) :
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt
        self.nbDiscution = 0
        self.oldrequette =  ""
        self.oldSortie = "" 
    
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
                if "toujours là"  in requette  or "es tu là" in requette or self.name in requette or "tu es là" in requette or "vous étes là" in requette or "vous etes là" :
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
                        if self.name != "SIX" :
                            debutPhrase = str("Je suis " + self.name  + ", l'assistant personnelle de "+self.genre+" "+self.user+" "+". Crée par Baptiste Pauchet sous le nom SIX. Si vous voulez savoir tout ce que je peux faire ouvrez ma page d'aide. ")
                        else :
                            debutPhrase = str("Je suis SIX, l'assistant personnelle de "+self.genre+" "+self.user+" "+". Crée par Baptiste Pauchet, si vous voulez savoir tout ce que je peux faire ouvrez ma page d'aide. ") 
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
                            text = ""
                            return 0 , text