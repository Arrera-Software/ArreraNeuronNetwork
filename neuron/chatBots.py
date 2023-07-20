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
        valeur = 0
        if  "salut" in requette   or "bonjour" in requette  or "bonsoir" in requette:
            text = self.objetFormule.salutation(hour)
            self.gestionNeuron.setHistory(text,requette)
            self.gestionNeuron.addDiscution()
            valeur = 1
        else :
            if "raconter une blague" in requette or "raconte moi une blague" in requette or "raconte une blague" in requette :
                if "vous etes pas drole" in self.oldrequette or "tu es pas drole" in self.oldrequette:
                    text ="Je peux pas raconter un blague si je suis pas drole"
                    valeur = 1
                else :
                    nbRand = random.randint(0,8)
                    text = self.blague[nbRand]+" "+self.reponseBlague[nbRand]
                    self.gestionNeuron.setHistory(text,requette)
                    self.gestionNeuron.addDiscution()
                    valeur = 1
            else :
                if "vous etes pas drole" in requette  or "tu es pas drole" in requette :
                    if "raconter une blague" in self.oldrequette or "raconte moi une blague" in self.oldrequette or "raconte une blague" in self.oldrequette :
                        nbRand = random.randint(0,2)
                        listReponse1 =  ["Je suis désoler de ne pas etre drole pour vous "+self.genre,
                                        "Désoler si je ne suis pas drole "+self.genre,
                                        "Je peux vous en racontez une autre"]
                        listReponse2 =  ["Je suis désoler de ne pas etre drole pour toi "+self.user,
                                        "Désoler si je ne suis pas drole "+self.name,
                                        "Je peux t'en raconter une autre"]
                        if self.vous == True:
                            text = listReponse1[nbRand]
                        else :
                            text = listReponse2[nbRand]
                        self.gestionNeuron.setHistory(text,requette)
                        self.gestionNeuron.addDiscution()
                        valeur = 1
                    else :
                        nbRand = random.randint(0,2)
                        listReponse1 = ["Pourquoi vous dites sa je ne vous es meme pas racompter une blague",
                                        "Avant de dire sa , laissez-vous en raconter une"]
                        listReponse2 = ["Pourquoi tu dit sa je ne t'en ai meme pas raconter une",
                                        "Avant de dire sa , laisse t'en raconter une"]
                        if self.vous == True:
                            text = listReponse1[nbRand]
                        else :
                            text = listReponse2[nbRand]
                        valeur =  0            
        return valeur , text