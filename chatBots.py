import datetime
import random

class neuroneDiscution :
    def __init__(self,name,UserCourt,GenreCourt) :
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt
        self.oldrequette =  ""
        self.oldSortie = "" 
    
    def stokage(self,requette,text):
        self.oldrequette = requette
        self.oldSortie = text
        
    def neurone(self,var):
        requette = str(str(var).lower())
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
                if hour>= 3 and hour< 6:
                    text= str(formule+","+self.genre+" "+self.user+".Quesque vous faite si tot ce matin "+self.genre+" ?")
                else :
                    if hour>= 6 and hour< 10 :
                       text= str(formule+","+self.genre+" "+self.user+".Comment avez-vous dormie cette nuit  "+self.genre+" ?")
                    else :
                        if hour>= 10 and hour< 12 : 
                           text= str(formule+","+self.genre+" "+self.user+".Comment c'est passer votre matinnée  "+self.genre+" ?")
                        else :
                            if hour>= 13 and hour< 14 :
                                text= str(formule+","+self.genre+" "+self.user+". Comment ce passe votre debut d'aprés-midi "+self.genre+" ?") 
                            else :
                                if hour>= 15 and hour< 18 :
                                    text= str(formule+","+self.genre+" "+self.user+". Comment ce passe votre aprés-midi "+self.genre+" ?")
                                else :
                                    if hour>= 18 and hour< 20 : 
                                      text= str(formule+","+self.genre+" "+self.user+". Comment c'est passée votre journée "+self.genre+" ?") 
                                    else :
                                        if hour>= 20 and hour <= 23 : 
                                            text= str(formule+","+self.genre+" "+self.user+". Comment c'est passée votre journée "+self.genre+" ?") 
                                        else : 
                                            if hour >= 00 and hour < 3 : 
                                                text = str(formule+","+self.genre+" "+self.user+". Il faudrait allez-vous couché "+self.genre+" ?") 
            self.stokage(requette,text)
            return 1 , text
        else :
            if "bien" in requette or "oui" in requette:
                if "comment" in self.oldrequette and "c'est passer" in self.oldrequette or "ce passe" in self.oldrequette :
                    if "c'est passer" in self.oldrequette and "journée" in self.oldrequette :
                        phrase = "Quesque vous avez fait de votre journée"
                    else :
                        if "ce passe" in self.oldrequette and "aprés-midi" in self.oldrequette :
                            if "debut" in self.oldrequette :
                                phrase = "Quesque vous avez prévu de faire de votre aprés-midi "+ self.genre + ". Es que je peux vous etre utile ?"
                            else :
                                phrase = "Quesque vous faite de votre apres-midi " + self.genre + ". En quoi je peux vous aidez ?"
                        else : 
                            if "avez-vous dormie" in self.oldrequette and "nuit" :
                                phrase = "C'est super sa " + self.genre + ". Quesque vous avez prévu de faire aujourd'hui "+self.genre+ "?"
                            else :
                                if "Il faudrait allez-vous couché" in self.oldrequette or "Quesque vous faites si tart" in self.oldrequette and "oui" in requette :
                                    phrase = "Mais je pense "+self.genre+", qu'il faudrait allez vous coucher"
                self.stokage(requette,text)
                return 1 , text                
                
            else :
                if "toujours là"  in requette  or "es-tu là" in requette or self.name in requette :
                    text =str("Oui, je suis toujours la "+self.genre+" "+self.user+".")
                    self.stokage(requette,text)
                    return 1 , text
                else :
                    if "tu es qui" in requette or "présente-toi" in requette or "présentation" in requette or "qui es tu" in requette or "qui es-tu" in requette:
                        if self.name != "SIX" :
                            text = str("Je suis " + self.name  + ", l'assistant personnelle de "+self.genre+" "+self.user+" "+". Crée par Baptiste Pauchet sous le nom SIX. Si vous voulez savoir tout ce que je peux faire ouvrez ma page d'aide. ")
                        else :
                            text = str("Je suis SIX, l'assistant personnelle de "+self.genre+" "+self.user+" "+". Crée par Baptiste Pauchet, si vous voulez savoir tout ce que je peux faire ouvrez ma page d'aide. ") 
                        self.stokage(requette,text)
                        return 1 , text
                    else :
                        text = ""
                        self.stokage(requette,text)
                        return 0 , text