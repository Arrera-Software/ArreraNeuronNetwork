import datetime
import random
#fichier
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import*
class neuroneDiscution :
    def __init__(self,gestionnaireNeuron:gestionNetwork,gestionnaireFormule:formule) :
        #Init objet
        self.gestionNeuron = gestionnaireNeuron
        self.formule = gestionnaireFormule
        #liste
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
        
        
    def neurone(self,requette):
        hour = datetime.datetime.now().hour
        nbRand = 0
        text = ""
        self.oldrequette = self.gestionNeuron.getOldrequette()
        self.oldsortie = self.gestionNeuron.getOldSortie()
        self.nbDiscution = self.gestionNeuron.getNbDiscution()
        self.name = self.gestionNeuron.getName()
        self.etatVous = self.gestionNeuron.getVous()
        self.genre = self.gestionNeuron.getGenre()
        self.user = self.gestionNeuron.getUser()
        self.bute = self.gestionNeuron.getBute()
        self.createur = self.gestionNeuron.getCreateur()
        valeur = 0
        if  "salut" in requette   or "bonjour" in requette  or "bonsoir" in requette:
            text = self.formule.salutation(hour)
        else :
            if "raconter une blague" in requette or "raconte moi une blague" in requette or "raconte une blague" in requette :
                if "vous etes pas drole" in self.oldrequette or "tu es pas drole" in self.oldrequette or "c'est pas drole" in self.oldrequette or "pas drole" in self.oldrequette :
                    text ="Je peux pas raconter un blague si je suis pas drole"
                else :
                    nbRand = random.randint(0,8)
                    text = self.blague[nbRand]+" "+self.reponseBlague[nbRand]
            else :
                if "vous etes pas drole" in requette  or "tu es pas drole" in requette or "c'est pas drole" in requette or "pas drole" in requette :
                    if "raconter une blague" in self.oldrequette or "raconte moi une blague" in self.oldrequette or "raconte une blague" in self.oldrequette or "je vous en raconte une" in self.oldsortie or "je t'en raconte une" in self.oldsortie:
                        nbRand = random.randint(0,2)
                        listReponse1 =  ["Je suis désoler de ne pas etre drole pour vous "+self.genre,
                                        "Désoler si je ne suis pas drole "+self.genre,
                                        "Je peux vous en racontez une autre"]
                        listReponse2 =  ["Je suis désoler de ne pas etre drole pour toi "+self.user,
                                        "Désoler si je ne suis pas drole "+self.user,
                                        "Je peux t'en raconter une autre"]
                        if self.etatVous == True:
                            text = listReponse1[nbRand]
                        else :
                            text = listReponse2[nbRand]
                    else :
                        nbRand = random.randint(0,1)
                        listReponse1 = ["Pourquoi vous dites sa je ne vous es meme pas racompter une blague",
                                        "Avant de dire sa , laissez-vous en raconter une"]
                        listReponse2 = ["Pourquoi tu dit sa je ne t'en ai meme pas raconter une",
                                        "Avant de dire sa , laisse t'en raconter une"]
                        if self.etatVous == True:
                            text = listReponse1[nbRand]
                        else :
                            text = listReponse2[nbRand]
                else :
                    if "non" in requette :
                        if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                            nbRand = random.randint(0,1)
                            listReponse1 = ["Ok commme vous voulez "+self.genre,
                                            "Etes-vous vraiment sur "+self.genre]
                            listReponse2 = ["Ok comme tu veux "+self.user,
                                            "Es-tu vraiment sure de toi "+self.user]
                            if self.etatVous == True:
                                text = listReponse1[nbRand]
                            else :
                                text = listReponse2[nbRand]  
                    else :
                        if "oui" in requette :
                            if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                                nbRand = random.randint(0,8) 
                                if self.etatVous == True:
                                    text = "Ok "+self.genre+"."+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                                else :
                                    text = "Ok "+self.user+"."+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                        else :
                            if "vasy" in requette or "comme tu veux" in requette or "si vous voulez" in requette :
                                if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                                    nbRand = random.randint(0,8) 
                                    if self.etatVous == True:
                                        text = "Ok "+self.genre+" je vous en raconte une . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                                    else :
                                        text = "Ok "+self.user+" je t'en raconte une . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand] 
                            else :
                                if "pas besoin" in requette :
                                    if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                                        if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                                            nbRand = random.randint(0,1)
                                            listReponse1 = ["Ok commme vous voulez "+self.genre,
                                                            "Etes-vous vraiment sur "+self.genre]
                                            listReponse2 = ["Ok comme tu veux "+self.user,
                                                            "Es-tu vraiment sure de toi "+self.user]
                                            if self.etatVous == True:
                                                text = listReponse1[nbRand]
                                            else :
                                                text = listReponse2[nbRand]    
                                else :
                                    if "comment ça va " in requette or "ca va" in requette or "ça va" in requette or "comment vas tu" in requette or "comment allez vous" in requette or "tu vas bien" in requette or "vous allez bien" in requette or "est ce que tout va bien" in requette or "tout va bien pour toi" in requette or "tout va bien pour vous" in requette: 
                                        nbRand = random.randint(0,1)
                                        listReponse = ["Je suis un programme informatique je resent pas de sentiment.",
                                                       "Je ne peut pas resentir de sentiment, je suis qu'un programmme informatique"]
                                        text = listReponse[nbRand]
                                    else :
                                        if "tu peux me parler de toi" in requette or "tu peux te presenter" in requette or "presente toi" in requette :
                                            if "tu es qui" in self.oldrequette or "présente toi" in self.oldrequette or "présentation" in self.oldrequette or "qui es tu" in self.oldrequette or "qui es tu" in self.oldrequette:
                                                if self.etatVous == True:
                                                    phrase = "Je vous l'ai deja dit "+self.genre+" je peux pas trop vous dire plus je n'est pas de passion ni de hobbie je ne suis qu'un programme informatique qui a pour bute "+self.bute+"."
                                                else : 
                                                   phrase = "Je te l'ai deja dit "+self.user+" je peux pas trop t'en dire plus je n'est pas de passion ni de hobbie je ne suis qu'un programme informatique qui a pour bute "+self.bute+"." 
                                            else :
                                                phrase ="Je suis un assistant personnelle nommer "+self.name+" qui a été crée par "+self.createur+". Je n'ai pas pas de passion ni de hobbie du a ma conditions de programme informatique."
                                            text = "Ok ," + phrase
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
                                            else :
                                                if "toujours la"  in requette  or "es tu la" in requette or self.name in requette or "tu es la" in requette or "vous étes la" in requette or "vous etes la" in requette :
                                                    nbRand = random.randint(0,2)
                                                    listReponse = ["Je ne peut pas partir de tout façon",
                                                                    "Je ne pas partir tant que je peux servir",
                                                                    "A moin de m'arréter qui serait un acte horible je suis toujour la"]
                                                    if self.etatVous == True :
                                                        text ="Oui, je suis toujours la "+self.genre+" "+self.user+"." + listReponse[nbRand]
                                                    else :
                                                        text = "Oui, je suis toujours la "+self.user+ listReponse[nbRand]
        
        valeur = self.gestionNeuron.verrifSortie(text)                           
        self.gestionNeuron.setHistory(text,requette)
        self.gestionNeuron.addDiscution()
        return valeur , text