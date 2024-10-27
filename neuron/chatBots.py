import datetime
#fichier
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import*
from ObjetsNetwork.enabledNeuron import*

class neuroneDiscution :
    def __init__(self, gestionnaireNeuron:gestionNetwork, gestionnaireFormule:formule):
        #Init objet
        self.__gestionNeuron = gestionnaireNeuron
        self.__formule = gestionnaireFormule
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
        self.__language = self.__gestionNeuron.getLanguageObjet()
        self.__listSortie = ["",""]
    
    def getListSortie(self)->list :
        return self.__listSortie  

    def getValeurSortie(self)->int :
        return self.__valeurOut
        
    def neurone(self,requette:str):
        if self.__gestNeuron.getChatbot() == True : 
            #Recuperation de l'heure
            hour = datetime.now().hour
            #Initilisation des variable nbRand et text et valeur
            text = ""
            self.__listSortie = ["",""]
            self.__valeurOut = 0
            #Recuperation atribut de l'assistant
            listOldSortie = self.__gestionNeuron.getOld()
            oldrequette = listOldSortie[0]
            oldsortie = listOldSortie[1]
            name = self.__gestionNeuron.getName()
            #Reponse chat bot
            if  (("salut" in requette)   or ("bonjour" in requette)  or( "bonsoir" in requette)):
                text = self.__formule.bootNoHist(hour)
            else :
                if (("raconter une blague" in requette) or ("raconte moi une blague" in requette) or ("raconte une blague" in requette)) :
                    if (("vous etes pas drole" in oldrequette) or( "tu es pas drole" in oldrequette) 
                        or ("c'est pas drole" in oldrequette) or ("pas drole" in oldrequette)) :
                        text = self.__language.getPhraseChatBotNormal("ph1Blague")
                    else :
                        nbRand = random.randint(0,8)
                        text = self.__language.getBlague(nbRand)+" "+self.__language.getReponseBlague(nbRand)
                else :
                    if (("vous etes pas drole" in requette)  or ("tu es pas drole" in requette) 
                        or ("c'est pas drole" in requette) or ("pas drole" in requette)) :
                        if (("raconter une blague" in oldrequette) or ("raconte moi une blague" in oldrequette) 
                            or ("raconte une blague" in oldrequette) or ("je vous en raconte une" in oldsortie) 
                            or ("je t'en raconte une" in oldsortie)):
                            nbRand = random.randint(0,2)
                            text = self.__language.getPhraseChatBotList("ph2Blague")[nbRand]
                        else :
                            nbRand = random.randint(0,1)
                            text = self.__language.getPhraseChatBotList("ph3Blague")[nbRand]
                    else :
                        if (("Avant de dire sa , laisse t'en raconter une" in oldsortie) 
                            or ("Avant de dire sa , laissez-vous en raconter une" in oldsortie)) :
                            if ("non" in requette) :
                                nbRand = random.randint(0,1)
                                text = self.__language.getPhraseChatBotList("ph4Blague")[nbRand]
                            else :
                                if ("oui" in requette) :
                                    nbRand = random.randint(0,8)
                                    text = (self.__language.getPhraseChatBotNormal("ph5Blague") +
                                            self.__language.getBlague(nbRand) + " " +
                                            self.__language.getReponseBlague(nbRand) + " .")
                                else :
                                    if (("vasy" in requette) or ("comme tu veux" in requette) 
                                        or ("si vous voulez" in requette)) :
                                        nbRand = random.randint(0,8)
                                        text = (self.__language.getPhraseChatBotNormal("ph5Blague") +
                                                self.__language.getBlague(nbRand) + " " +
                                                self.__language.getReponseBlague(nbRand) + " .")
                                    else :
                                        if ("pas besoin" in requette) :
                                            nbRand = random.randint(0,1)
                                            text = self.__language.getPhraseChatBotList("ph6Blague")[nbRand]
                        else :
                            if (("Je peux vous en racontez une autre" in oldsortie) 
                                or ("Je peux t'en raconter une autre" in oldsortie) 
                                or ("Si tu veux je peux t'en raconter une autre" in oldsortie)) :
                                if (("vasy" in requette) or ("comme tu veux" in requette) or ("si vous voulez" in requette)) :
                                    nbRand = random.randint(0,8) 
                                    text = self.__language.getPhraseChatBotNormal("ph7Blague")+self.__language.getBlague(nbRand)+" "+self.__language.getReponseBlague(nbRand)+"."
                            else :
                                if (("Désoler de ne pas etre drole pour vous " in oldsortie) 
                                    or ("Désoler si je ne suis pas drole" in oldsortie) 
                                    or ("Désoler de ne pas etre drole pour toi" in oldsortie)) :
                                    if ("pas grave" in requette) :
                                        text = self.__language.getPhraseChatBotNormal("ph8Blague")
                                    else :
                                        if (("ne sois pas desoler" in requette) 
                                            or ("c'est tres grave" in requette)) :
                                            text = self.__language.getPhraseChatBotNormal("ph9Blague")
                                else :
                                    if (("comment ça va " in requette) or ("ca va" in requette) 
                                        or ("ça va" in requette) or( "comment vas tu" in requette) 
                                        or ("comment allez vous" in requette) or ("tu vas bien" in requette) 
                                        or ("vous allez bien" in requette) or ("est ce que tout va bien" in requette) 
                                        or ("tout va bien pour toi" in requette) or ("tout va bien pour vous" in requette)): 
                                        nbRand = random.randint(0,1)
                                        text = self.__language.getPhraseChatBotNormal("ph10Blague")[nbRand]
                                    else :
                                        if (("tu peux me parler de toi" in requette) 
                                            or ("tu peux te presenter" in requette) 
                                            or ("presente toi" in requette)) :
                                            if (("tu es qui" in oldrequette) or ("présente toi" in oldrequette) 
                                                or ("présentation" in oldrequette) or ("qui es tu" in oldrequette) 
                                                or ("qui es tu" in oldrequette)):
                                                phrase = self.__language.getPhraseChatBotNormal("ph1Presentation")
                                            else :
                                                phrase = self.__language.getPhraseChatBotNormal("ph2Presentation")
                                            text = "Ok ," + phrase
                                        else :
                                            if (("toujours la"  in requette)  or ("es tu la" in requette)
                                                or (name in requette) or ("tu es la" in requette)
                                                or ("vous étes la" in requette) or ("vous etes la" in requette)) :
                                                nbRand = random.randint(0,2)
                                                text = self.__language.getPhraseChatBotList("ph1Other")[nbRand]
                                            else :
                                                if (("quesque tu peux faire" in requette) or
                                                        ("tu peux faire quoi" in requette) or
                                                        ("vous pouvez faire quoi" in requette)) :
                                                    listFonction = self.__gestionNeuron.getListFonction()
                                                    nbFonction = self.__gestionNeuron.getNbListFonction()
                                                    nb = nbFonction - 1
                                                    text = self.__language.getPhraseListeFonction()
                                                else :
                                                    if ("non" in requette) :
                                                        text = self.__language.getPhraseChatBotNormal("phNon")
                                                    else :
                                                        if ("oui" in requette) :
                                                            text = self.__language.getPhraseChatBotNormal("phOui")
                                                        else :
                                                            if ("merci" in requette) :
                                                                text = self.__language.getPhraseChatBotNormal("phMerci")
                                                            else:
                                                                if  ("ta gueule" in requette or "tais toi" in requette) :
                                                                    text = self.__language.getPhraseChatBotNormal("phTG")
            #Mise a jour de la valeur
            self.__valeurOut = self.__gestionNeuron.verrifSortie(text)
            #Retour des valeur
            self.__listSortie = [text,""]