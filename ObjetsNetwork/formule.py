import random
from ObjetsNetwork.gestion import*
from  ObjetsNetwork.historique import*
class formule : 
    def __init__(self,gestionnaireNeuron:gestionNetwork,fncHist:CHistorique):
        self.__vous = bool(gestionnaireNeuron.getVous())
        self.__genre = str(gestionnaireNeuron.getGenre())
        self.__user  = str(gestionnaireNeuron.getUser())
        self.__fncHist = fncHist
    
    def nocomprehension(self):
        if self.__vous == True:
            text = "Je ne comprend pas ce que vous m'avez dit."
        else : 
            text = "Je ne comprend pas ce que tu m'as dit ou ce que tu demande."   
        return text
        
    def bootNoHist(self, hour):
        nbrand = random.randrange(0,1)
        if hour >= 0 and hour < 3:
            if self.__vous:
                formule = ["Bonjour "+self.__genre+" "+self.__user+". Que faites-vous à cette heure matinale ?",
                           "Bonjour "+self.__genre+" "+self.__user+". J'espère que vous avez suffisamment dormi."]
                
            else:
                formule = ["Zzzz... Il faudrait peut-être dormir "+self.__user+", non ?",
                           "Zzzz... Comment peux-tu travailler si tard "+self.__user+" ?"]
                return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                if self.__vous:
                    formule = ["Bonjour "+self.__genre+" "+self.__user+". Êtes-vous prêt à travailler ?",
                               "Désirez-vous poursuivre votre travail à une heure pareille "+self.__genre+" "+self.__user+" ?"]
                else:
                    formule = ["Zzzz... "+self.__user+"... Il faudrait peut-être dormir, non ?",
                               "Zzzz... Il est tard... Pourquoi travailles-tu encore "+self.__user+" ?"]
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    if self.__vous:
                        formule = ["Bonjour "+self.__genre+" "+self.__user+". J'espère que votre nuit fut reposante.",
                                   "Bonjour "+self.__genre+" "+self.__user+". J'espère que vous avez bien dormi."]
                    else:
                        formule = ["Hey "+self.__user+" ! Bien dormi ?","Hey "+self.__user+" ! As-tu passé une bonne nuit ?"]
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        if self.__vous:
                            formule = ["Bonjour "+self.__genre+" "+self.__user+". J'espère que vous passez une belle matinée.",
                                       "Bonjour "+self.__genre+" "+self.__user+". Avez-vous bien débuté votre journée ?"]
                        else:
                            formule = ["Salut "+self.__user+". Que fais-tu de beau ce matin ?",
                                       "Alors "+self.__user+", prêt à travailler ?"]
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 14:
                            if self.__vous:
                                formule = ["Bonjour "+self.__genre+" "+self.__user+". J'espère que vous passez une belle après-midi.",
                                           "Bonjour "+self.__genre+" "+self.__user+". J'espère que vous passez une belle après-midi."]
                            else:
                                formule = ["Alors "+self.__user+", prêt à travailler ?",
                                           "Alors "+self.__user+", es-tu prêt à travailler cet après-midi ?"]
                            return formule[nbrand]
                        else:
                            if hour >= 15 and hour <= 18:
                                if self.__vous:
                                    formule = ["Bonjour "+self.__genre+" "+self.__user+". En quoi puis-je vous aider cette après-midi ?",
                                               "Bonjour "+self.__genre+" "+self.__user+". Que puis-je faire pour vous aider ?"]
                                else:
                                    formule = ["Salut, "+self.__user+" ! En quoi consiste ton travail ?",
                                               "Salut, "+self.__user+" ! Dis-moi comment je peux t'aider ?"]
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.__vous:
                                        formule = ["Bonsoir, "+self.__genre+" "+self.__user+" Comment se passe votre début de soirée ?",
                                                   "Bonsoir, "+self.__genre+" "+self.__user+" J'espère que votre début de soirée se passe bien."]
                                    else:
                                        formule = ["Alors "+self.__user+" Que veux-tu faire ce soir ?",
                                                   "Alors "+self.__user+" Veux-tu travailler ou te divertir ce soir ?"]
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.__vous:
                                            formule = ["Bonsoir, "+self.__genre+" "+self.__user+" Comment se passe votre soirée ?",
                                                       "Bonsoir, "+self.__genre+" "+self.__user+" J'espère que votre soirée s'est bien passée."]
                                        else:
                                            formule = ["*bâille* "+self.__user+"  Que fais-tu si tard ?",
                                                       "*bâille* "+self.__user+" Pourquoi me réveilles-tu si tard ?"]
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.__vous:
                                                formule = ["Bonjour, "+self.__genre+" "+self.__user+"  Que faites-vous si tôt ?",
                                                           "Bonjour, "+self.__genre+" "+self.__user+" J'espère que vous avez un peu dormi."]
                                            else:
                                                formule = ["Zzzz "+self.__user+" . Il faudrait peut-être dormir, non ?",
                                                           "Zzzz "+self.__user+" . Comment peux-tu travailler si tard ?"]
                                            return formule[nbrand]
                                        else:
                                            if self.__vous:
                                                formule = "Bonjour, "+self.__genre+" "+self.__user+" Que voulez-vous qu'on fasse ?"
                                            else:
                                                formule = "Salut, "+self.__user+" Que veux-tu que je t'aide à faire ?"
                                            return formule
        
    def aurevoir(self, hour):
        nbrand = random.randrange(0,1)
        if hour >= 0 and hour < 3:
            if self.__vous:
                formule = ["Bonne nuit, "+self.__genre+" "+self.__user+" . Reposez-vous bien.",
                           "Bonne nuit, "+self.__genre+" "+self.__user+" . Passez une bonne nuit."]
            else:
                formule = ["Au revoir, "+self.__user+". Bonne nuit.",
                           "Au revoir, "+self.__user+" . Bonne nuit, repose-toi bien."]
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                if self.__vous:
                    formule = ["Bonne nuit, "+self.__genre+" "+self.__user+". Essayez de vous reposer.",
                               "Bonne nuit, "+self.__genre+" "+self.__user+" Reposez-vous bien."]
                else:
                    formule = ["Bonne nuit, "+self.__user+" Essaie de te reposer un peu.",
                               "Bonne nuit, "+self.__user+" Essaie de te reposer un peu."]
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    if self.__vous:
                        formule = ["Bonne journée, "+self.__genre+" "+self.__user+" Passez une bonne journée. ",
                                   "Bonne journée, "+self.__genre+" "+self.__user+" Profitez bien de votre journée."]
                    else:
                        formule = ["Au revoir, "+self.__user+" Passe une bonne journée.",
                                   "Au revoir, "+self.__user+" Profite bien de ta journée."]
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        if self.__vous:
                            formule = ["Au revoir, "+self.__genre+" "+self.__user+" . Passez une bonne fin de matinée.",
                                       "Au revoir, "+self.__genre+" "+self.__user+" Profitez bien de votre fin de matinée."]
                        else:
                            formule = ["Au revoir, Passe une bonne fin de matinée.",
                                       "Au revoir, Profite bien de ta fin de matinée."]
                    else:
                        if hour >= 13 and hour <= 16:
                            if self.__vous:
                                formule = ["Bonne après-midi, "+self.__genre+" "+self.__user+" Profitez bien.",
                                           "Au revoir, "+self.__genre+" "+self.__user+" Passez une bonne fin d'après-midi."]
                            else:
                                formule = ["Au revoir, "+self.__user+" .Profite bien de ta fin d'après-midi.",
                                           "Au revoir, "+self.__user+" .Profite bien de ta fin d'après-midi."]
                            return formule[nbrand]
                        else:
                            if hour >= 16 and hour <= 18:
                                if self.__vous:
                                    formule = ["Au revoir, "+self.__genre+" "+self.__user+" Profitez bien de votre fin de soirée.",
                                               "Bonne soirée, "+self.__genre+" "+self.__user+" Profitez bien"]
                                else:
                                    formule = ["Au revoir, "+self.__user+" Profite bien de ta soirée.",
                                               "Au revoir, "+self.__user+" Profite bien de ta soirée."]
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.__vous:
                                        formule = ["Bonne soirée, "+self.__genre+" "+self.__user+" Profitez bien",
                                                   "Bonne soirée, "+self.__genre+" "+self.__user+" Reposez-vous bien ce soir."]
                                    else:
                                        formule = ["Au revoir, "+self.__user+" Profite bien de ta soirée.",
                                                   "Au revoir, "+self.__user+" Repose-toi bien ce soir."]
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.__vous:
                                            formule = ["Bonne nuit, "+self.__genre+" "+self.__user+" Dormez bien.",
                                                       "Bonne nuit, "+self.__genre+" "+self.__user+" Reposez-vous bien."]
                                        else:
                                            formule = ["Bonne nuit, "+self.__user+" Dors bien.",
                                                       "Bonne nuit, "+self.__user+" Repose-toi bien."]
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.__vous:
                                                formule = ["Bonne nuit, "+self.__genre+" "+self.__user+" Dormez bien, soyez en forme pour demain.",
                                                           "Bonne nuit, "+self.__genre+" "+self.__user+" Reposez-vous bien pour demain."]
                                            else:
                                                formule = ["Bonne nuit, "+self.__user+" Dors bien, sois en forme pour demain.",
                                                           "Bonne nuit, "+self.__user+" Repose-toi bien pour demain."]
                                            return formule[nbrand]
                                        else:
                                            if self.__vous:
                                                formule = "Au revoir,  "+self.__genre+" "+self.__user+" J'espère vous revoir bientôt."
                                            else:
                                                formule = "Au revoir, "+self.__user+" J'espère te revoir bientôt."
                                            return formule    
    def bootWithHist(self,hour):
        
        sortie = self.__fncHist.verfiHist()
        if (sortie == True):
            self.__fncHist.startHistAction()
        
        if hour >= 0 and hour < 3:
            if self.__vous:
                formule = "Bonjour,"
                cmp = self.__genre + " " + self.__user
                phrase = "Je vous ai relancée votre travail. Mais il faudrais que tu dorme."
            else:
                formule = "Zzzz"
                cmp = self.__user
                phrase = "J'ai relancer la ou vous etais arriver. Mais il faudrais que tu dorme."
        else:
            if hour >= 3 and hour <= 6:
                if self.__vous:
                    formule = "Bonjour,"
                    cmp = self.__genre + " " + self.__user
                    phrase = "Je vous ai relancée votre travail. Mais il faudrais que tu dorme."
                else:
                    formule = "Zzzz"
                    cmp = self.__user
                    phrase =" J'ai relancer la ou vous etais arriver. Mais il faudrais que tu dorme."
            else:
                if hour >= 6 and hour <= 10:
                    if self.__vous:
                        formule = "Bonjour, "
                        cmp = self.__genre + " " + self.__user
                        phrase = "J'espère que vous avez passé une bonne nuit. J'ai relancer la ou vous etais arriver."
                    else:
                        formule = "Hey,"
                        cmp = self.__user
                        phrase = "J'espère tu as passé une bonne nuit. J'ai relancer la ou tu etais arriver."
                else:
                    if hour >= 10 and hour <= 12:
                        if self.__vous:
                            formule = "Bonjour, "
                            cmp = self.__genre + " " + self.__user
                            phrase = "J'espère que vous passez une bonne matinée. Je vous ai relancer ou vous etiez"
                        else:
                            formule = "Salut,"
                            cmp = self.__user
                            phrase = "Comment se passe ta matinée ?. J'ai relancer la ou tu etais arriver."
                    else:
                        if hour >= 13 and hour <= 14:
                            if self.__vous:
                                formule = "Bonjour,"
                                cmp = self.__genre + " " + self.__user
                                phrase = "J'espère que vous passez une bonne après-midi ? J'ai relancer la ou vous etais arriver."
                            else:
                                formule = "Alors"
                                cmp = self.__user
                                phrase = "Prêt à travailler ? Je t'ai relancer ou tu etais"
                        else:
                            if hour >= 15 and hour <= 18:
                                if self.__vous:
                                    formule = "Bonjour,"
                                    cmp = self.__genre + " " + self.__user
                                    phrase = "Sur quoi puis-je vous aider cet après-midi ? Je vous ai relancer ou vous etiez."
                                else:
                                    formule = "Salut,"
                                    cmp = self.__user
                                    phrase = "En quoi puis-je t'aider ? Je t'ai relancer ou tu etais"
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.__vous:
                                        formule = "Bonsoir,"
                                        cmp = self.__genre + " " + self.__user
                                        phrase = "J'espère que votre début de soirée se passe bien. J'ai relancer la ou vous etais arriver."
                                    else:
                                        formule = "Alors"
                                        cmp = self.__user
                                        phrase = "Prét a travailler ce soir. Je t'ai relancer ou tu etais."
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.__vous:
                                            formule = "Bonsoir,"
                                            cmp = self.__genre + " " + self.__user
                                            phrase = "J'espère que votre soirée s'est bien passée. J'ai relancer la ou vous etais arriver."
                                        else:
                                            formule = "*bâille*"
                                            cmp = self.__user
                                            phrase = "Pourquoi me réveilles-tu si tard ?. Je t'ai relancer ou tu etais."
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.__vous:
                                                formule = "Bonjour,"
                                                cmp = self.__genre + " " + self.__user
                                                phrase = "J'espère que vous avez un peu dormi. J'ai relancer la ou vous etais arriver."
                                            else:
                                                formule = "Zzzz"
                                                cmp = self.__user
                                                phrase = "Comment peux-tu travailler si tard ? Je vous ai relancer ou vous etiez."
                                        else:
                                            if self.__vous:
                                                formule = "Bonjour,"
                                                cmp = self.__genre + " " + self.__user
                                                phrase = "J'ai relancer la ou vous etais arriver."
                                            else:
                                                formule = "Salut,"
                                                cmp = self.__user
                                                phrase = "Je t'ai relancer ou tu etais."

            
            return str(formule+" "+cmp+" "+phrase)