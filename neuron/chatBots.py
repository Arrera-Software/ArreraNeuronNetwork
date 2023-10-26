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
        
        
    def neurone(self,requette,oldSortie:str,oldRequette:str):
        #Recuperation de l'heure
        hour = datetime.datetime.now().hour
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
        #Reponse chat bot
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
                        listReponse1 =  ["Désoler de ne pas etre drole pour vous "+self.genre,
                                        "Désoler si je ne suis pas drole "+self.genre,
                                        "Je peux vous en racontez une autre"]
                        listReponse2 =  ["Désoler de ne pas etre drole pour toi "+self.user,
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
                    if "Avant de dire sa , laisse t'en raconter une" in self.oldsortie or "Avant de dire sa , laissez-vous en raconter une" in self.oldsortie :
                        if "non" in requette :
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
                                nbRand = random.randint(0,8) 
                                if self.etatVous == True:
                                    text = "Ok "+self.genre+"."+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                                else :
                                    text = "Ok "+self.user+"."+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                            else :
                                if "vasy" in requette or "comme tu veux" in requette or "si vous voulez" in requette :
                                    nbRand = random.randint(0,8) 
                                    if self.etatVous == True:
                                        text = "Ok "+self.genre+" je vous en raconte une . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                                    else :
                                        text = "Ok "+self.user+" je t'en raconte une . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand] 
                                else :
                                    if "pas besoin" in requette :
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
                        if "Je peux vous en racontez une autre" in self.oldsortie or "Je peux t'en raconter une autre" in self.oldsortie or "Si tu veux je peux t'en raconter une autre" in self.oldsortie :
                            if "vasy" in requette or "comme tu veux" in requette or "si vous voulez" in requette :
                                nbRand = random.randint(0,8) 
                                if self.etatVous == True:
                                    text = "Ok "+self.genre+" en voici une autre . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                                else :
                                    text = "Ok "+self.user+" en voici une autre . "+self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                        else :
                            if "Désoler de ne pas etre drole pour vous " in self.oldsortie or "Désoler si je ne suis pas drole" in self.oldsortie or "Désoler de ne pas etre drole pour toi" in self.oldsortie :
                                if "pas grave" in requette :
                                    if self.etatVous == True:
                                        text = "Je veux pas rester sur un echec " + self.genre + ". Je peux vous en racontez une autre si vous voulez bien."
                                    else :
                                        text = "Je ne peux pas rester sur un echec . Si tu veux je peux t'en raconter une autre"
                                else :
                                    if "ne sois pas desoler" in requette or "c'est tres grave" in requette :
                                        if self.etatVous == True :
                                            text = "Veuillez m'excusez "+self.genre+" je peux servir a autre chose."
                                        else :
                                            text =  "Excuse moi .Veux-tu faire autre chose ?"
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
                                            else :
                                                if self.oldrequette == "boot":
                                                    if "oui" in requette :
                                                        if "J'espère que vous avez un peu dormi." in self.oldsortie :
                                                            nbRand = random.randint(0,1)
                                                            listReponse = ["Tant mieux dit moi si vous avez besoin de moi",
                                                                           "Je suis content de savoir sa" ]
                                                            text = listReponse[nbRand]+" "+self.genre
                                                        else:
                                                            if "Êtes-vous prêt à travailler ?" in self.oldsortie :
                                                                nbRand = random.randint(0,1)
                                                                listReponse =["Okay je peux vous aider sur quoi "+self.genre,
                                                                              "Super sur quoi vous voulez travailler sur quoi" ]
                                                                text = listReponse[nbRand]
                                                            else :
                                                                if "J'espère que vous avez passé une bonne nuit." in self.oldsortie :
                                                                    text = "Super sur quoi vous voulez travaille "+self.genre
                                                                else :
                                                                    if "J'espère que vous avez bien dormi." in self.oldsortie :
                                                                        text = "Super sur quoi je peux vous aider "+self.genre
                                                                    else :
                                                                        if "J'espère que vous passez une bonne matinée." in self.oldsortie :
                                                                            text = "Formidable sur quoi vous occupez votre début de matinée"
                                                                        else :
                                                                            if "J'espère que vous passez un bon début de journée." in self.oldsortie :
                                                                                text = "Formidable, vous travaillez sur quoi ?"
                                                                            else :
                                                                                if "J'espère que vous passez une bonne après-midi ?" in self.oldsortie :
                                                                                    text = "Formidable que fais-vous de votre après-midi"
                                                                                else :
                                                                                    if "Comment se passe votre début de soirée ?" in self.oldsortie :
                                                                                        text = "Ceci me réjouit genre vous voulez faire quoi "+self.genre
                                                                                    else :
                                                                                        if "J'espère que votre début de soirée se passe bien." in self.oldsortie :
                                                                                            text = "Formidable vous voulez faire quoi ce soir"
                                                                                        else :
                                                                                            if "Comment se passe votre soirée ?" in self.oldsortie :
                                                                                                text = "Parfais je peux vous aidez ce soir "+self.genre
                                                                                            else :
                                                                                                if "J'espère que votre soirée s'est bien passée." in self.oldsortie :
                                                                                                    text = "Ok vous vouliez faire quoi cette nuit"
                                                                                                else :
                                                                                                    if "As-tu bien dormi ?" in self.oldsortie :
                                                                                                        text = "C'est surper pour toi"
                                                                                                    else :
                                                                                                        if "As-tu passé une bonne nuit ?" in self.oldsortie :
                                                                                                            text = "Tant mieux pour toi tu veux travailler sur quoi aujourd'hui"
                                                                                                        else :
                                                                                                            if "Comment se passe ta matinée ?" in self.oldsortie :
                                                                                                                text = "Parfais sur quoi on travaille aujourd'hui"
                                                                                                            else :
                                                                                                                if "Prêt à travailler ?" in self.oldsortie :
                                                                                                                    text = "Ok on travaille sur quoi aujourd'hui"
                                                                                                                else :
                                                                                                                    if "es-tu prêt à travailler cet après-midi ?" in self.oldsortie :
                                                                                                                        text = "Ok on travaille sur quoi cette aprem"
                                                    else :
                                                       if "non" in requette : 
                                                            if "J'espère que vous avez un peu dormi" in self.oldsortie :
                                                                nbRand = random.randint(0,1)
                                                                listReponse = ["Je suis désolé pour vous je suis la pour vous aidez si vous a besoin "+self.genre,
                                                                                "Vous dormirez mieux ce soir en attendant en quoi je peux vous aider"]    
                                                                text = listReponse[nbRand]  
                                                            else :
                                                                if "Êtes-vous prêt à travailler ?" in self.oldsortie :
                                                                    nbRand = random.randint(0,1)
                                                                    listReponse = ["Okay, vous voulez faire quoi",
                                                                                    "OK je reste disponible pour vous "+self.genre]
                                                                    text = listReponse[nbRand]
                                                                else :
                                                                    if "J'espère que vous avez passé une bonne nuit." in self.oldsortie :
                                                                        text ="Dommage je reste disponible si vous avez besoin de moi "+self.genre
                                                                    else :
                                                                        if "J'espère que vous avez bien dormi." in self.oldsortie :
                                                                            text ="Dommage si vous avez besoin de moi je suis la"
                                                                        else :  
                                                                            if "J'espère que vous passez une bonne matinée." in self.oldsortie :
                                                                                text ="OK je suis à votre service si vous avez besoin de moi"
                                                                            else :   
                                                                                if "J'espère que vous passez un bon début de journée." in self.oldsortie :
                                                                                    text = "Dommage comment je peux vous la rendre meilleure genre"
                                                                                else :    
                                                                                    if "J'espère que vous passez une bonne après-midi ?" in self.oldsortie :
                                                                                        text ="Ha, je reste la si vous avez besoin de moi je suis la "
                                                                                    else :
                                                                                        if "Comment se passe votre début de soirée ?" in self.oldsortie :
                                                                                            text ="Comment je peux la rendre meilleur genre"
                                                                                        else :  
                                                                                            if "J'espère que votre début de soirée se passe bien." in self.oldsortie :
                                                                                                text ="Comment je peux rendre votre soirée exceptionnelle"
                                                                                            else :
                                                                                                if "Comment se passe votre soirée ?" in self.oldsortie :
                                                                                                    text ="Ceci me rend triste"
                                                                                                else :
                                                                                                    if "J'espère que votre soirée s'est bien passée." in self.oldsortie :
                                                                                                        text = "Je vous conseiller d'allez dormir"
                                                                                                    else :
                                                                                                        if "As-tu bien dormi ?" in self.oldsortie :
                                                                                                            text ="Dommage je peux d'aidez sur quoi ?"
                                                                                                        else :  
                                                                                                            if"As-tu passé une bonne nuit ?"in self.oldsortie :
                                                                                                                text ="Dommage comment je peux t'aider aujourd'hui"
                                                                                                            else :   
                                                                                                                if "Prêt à travailler ?" in self.oldsortie :
                                                                                                                    text ="Ok je reste la au besoin"
                                                                                                                else :    
                                                                                                                    if "Prêt à travailler ?" in self.oldsortie :
                                                                                                                        text ="Ok je reste la au besoin"
                                                                                                                    else :
                                                                                                                        if "Es-tu prêt à travailler cet après-midi ?" in self.oldsortie :
                                                                                                                            text ="Ok dit moi quand tu sera prét"                                    
                                                       else :
                                                            if "bien" in requette :
                                                                if "Comment se passe votre début de soirée ?" in self.oldsortie :
                                                                   text = "Ceci me réjouit "+self.genre+" que vous voulez faire ce soir ?"  
                                                                else :
                                                                    if "Comment se passe votre soirée ?" in self.oldsortie:
                                                                        text =  "Parfais en quoi je vous aidez ce soir "+self.genre+" ?"
                                                                    else :
                                                                        if "Comment se passe ta matinée ?" in self.oldsortie:
                                                                            text = "Parfais sur quoi on travaille aujourd'hui ?"
                                                            else : 
                                                                if "je profite du calme du matin pour travailler peu"  in requette and "Que faites-vous si tôt ?" in self.oldsortie or  "juste des choses à faire." in requette and "Que faites-vous si tôt ?" in self.oldsortie  :
                                                                    nbRand = random.randint(0,1)
                                                                    listReponse = ["Ok je suis là si vous avez besoin de "+self.genre,
                                                                                   "Dis-moi si vous avez besoin de moi"]
                                                                    text =  listReponse[nbRand]
                                                                else :
                                                                    if "je suis pret" in requette and "Êtes-vous prêt à travailler ?" in self.oldsortie:
                                                                        nbRand = random.randint(0,1)
                                                                        listReponse = ["Parfait sur quoi on travaille aujourd'hui " +self.genre, 
                                                                                       "Sur quoi l’on travaille aujourd'hui"]
                                                                        text = listReponse[nbRand]
                                                                    else :
                                                                        if "j'ai un truc a faire" in requette :
                                                                            if "Il faudrait peut-être dormir, non ?" in self.oldsortie :
                                                                                text = "Tres bien je vais t'aider "
                                                                            else :
                                                                                if "Comment peux-tu travailler si tard ?" in self.oldsortie :
                                                                                    text = "C'est pas une bonne idée de travailler" 
                                                                                else :
                                                                                    if "Il faudrait peut-être dormir, non ?" in self.oldsortie :
                                                                                        text = "Ok je peux d'aider comment"
                                                                                    else :
                                                                                        if "Que fais-tu si tard ?" in self.oldsortie:
                                                                                            text = "Comment je peux t'aider ?"
                                                                                        else :
                                                                                            if "Pourquoi me réveilles-tu si tard ?" in self.oldsortie:
                                                                                                text = "Comment je peux t'aider ?"
                                                                        else :
                                                                            if "il faut que je fasse un truc"  in requette :
                                                                                if "il faudrait peut-être dormir, non ?" in self.oldsortie :
                                                                                    text = "Ok je vais d'aider pour que tu finisse vite. Quesque je peux faire"
                                                                                else :
                                                                                    if "comment peux-tu travailler si tard ?" in self.oldsortie :
                                                                                        text = "Ok comment je peux t'aider" 
                                                                                    else :
                                                                                        if "il faudrait peut-être dormir, non ?" in self.oldsortie :
                                                                                            text = "Sur quoi tu dois travailler"
                                                                                        else :
                                                                                            if "que fais-tu si tard ?" in self.oldsortie:
                                                                                                text = "Sur quoi tu travaille"
                                                                                            else :
                                                                                                if "pourquoi me réveilles-tu si tard ?" in self.oldsortie:
                                                                                                    text = "Sur quoi tu travaille"
                                                                                                else :
                                                                                                    if "comment peux-tu travailler si tard ?" in self.oldsortie:
                                                                                                        text = "Je peux t'aider comment ?"    
                                                                            else :
                                                                                if "je dois finir un truc" in requette and "Que veux-tu faire ce soir ?" in self.oldsortie :
                                                                                    text = "Je peux t'aider comment ?"
                                                                                else :
                                                                                    if "me divertir" in requette and "Que veux-tu faire ce soir ?" in self.oldsortie :
                                                                                        text = "Sur quoi tu veux te divertir"
                                                                                    else :
                                                                                        if "travailler" in requette and "Veux-tu travailler ou te divertir ce soir ?" in self.oldsortie :
                                                                                            text = "Sur quoi tu travaille"
                                                                                        else :
                                                                                            if "me divertir" in requette and "Veux-tu travailler ou te divertir ce soir ?" in self.oldsortie :
                                                                                                text = "Sur quelle platforme veux-tu te divertir"                            
                                                else :
                                                    if "quesque tu peux faire" in requette or "tu peux faire quoi" in requette or "vous pouvez faire quoi" in requette :
                                                        listFonction = self.gestionNeuron.getListFonction()
                                                        nbFonction = self.gestionNeuron.getNbListFonction()
                                                        nb = nbFonction - 1
                                                        if self.etatVous == True :
                                                            text = "je peux vous aidez a "
                                                            for i in range(0,nbFonction) :
                                                                if i == nb :
                                                                    text = text + " et " + listFonction[i]
                                                                else :
                                                                    if i == 0 :
                                                                        text = text + listFonction[i]
                                                                    else :
                                                                        text = text + ","+listFonction[i]
                                                        else :
                                                            text = "je peux t'aidez a faire "
                                                            for i in range(0,nbFonction) :
                                                                if i == nb :
                                                                    text = text + " et " + listFonction[i]
                                                                else :
                                                                    if i == 0 :
                                                                        text = text + listFonction[i]
                                                                    else :
                                                                        text = text + ","+listFonction[i]   
                                                    else :
                                                        if "non" in requette : 
                                                            if self.etatVous == True :
                                                                text = "OK "+self.genre+" je reste la au besoin"
                                                            else :
                                                                text = "Ok "+self.user+" ,Je reste la si tu a besoin de moi."
                                                        else :
                                                            if "oui" in requette : 
                                                                text = "OK parfais" 
                                                            else :
                                                                if "merci" in requette :
                                                                    if self.etatVous == True :
                                                                        text = "De rien "+self.genre+" je reste a votre servie si vous avez besoin de moi" 
                                                                    else :
                                                                        text = "De rien "+self.user+" je peux encore t'aider"                                         
                                                                                                                                                             
        #Mise a jour de la valeur                                                               
        valeur = self.gestionNeuron.verrifSortie(text)
        #Retour des valeur
        return valeur , text