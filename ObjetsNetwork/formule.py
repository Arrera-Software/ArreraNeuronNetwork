import random
from ObjetsNetwork.gestion import *
from ObjetsNetwork.historique import *
from ObjetsNetwork.CAlanguage import *


class formule:
    def __init__(self, gestionnaireNeuron: gestionNetwork, fncHist: CHistorique,canguage:CAlanguage):
        self.__vous = bool(gestionnaireNeuron.getVous())
        self.__genre = str(gestionnaireNeuron.getGenre())
        self.__user = str(gestionnaireNeuron.getUser())
        self.__fncHist = fncHist
        self.__calanguage = canguage

    def nocomprehension(self):
        return self.__calanguage.getNoComprehension()

    def bootNoHist(self, hour):
        nbrand = random.randrange(0, 1)
        if hour >= 0 and hour < 3:
            formule = self.__calanguage.getPhraseBootNormale("1",self.__genre, self.__user)
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                formule = self.__calanguage.getPhraseBootNormale("2",self.__genre, self.__user)
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    formule = self.__calanguage.getPhraseBootNormale("3",self.__genre, self.__user)
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        formule = self.__calanguage.getPhraseBootNormale("4",self.__genre, self.__user)
                        return formule[nbrand]
                    else:
                        if hour >= 13 and hour <= 14:
                            formule = self.__calanguage.getPhraseBootNormale("5",self.__genre, self.__user)
                            return formule[nbrand]
                        else:
                            if hour >= 15 and hour <= 18:
                                formule = self.__calanguage.getPhraseBootNormale("6",self.__genre, self.__user)
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    formule = self.__calanguage.getPhraseBootNormale("7",self.__genre, self.__user)
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        formule = self.__calanguage.getPhraseBootNormale("8",self.__genre, self.__user)
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            formule = self.__calanguage.getPhraseBootNormale("9",self.__genre, self.__user)
                                            return formule[nbrand]
                                        else:
                                            formule = self.__calanguage.getPhraseBootNormale("10",self.__genre, self.__user)
                                            return formule

    def aurevoir(self, hour):
        nbrand = random.randrange(0, 1)
        if hour >= 0 and hour < 3:
            if self.__vous:
                formule = ["Bonne nuit, " + self.__genre + " " + self.__user + " . Reposez-vous bien.",
                           "Bonne nuit, " + self.__genre + " " + self.__user + " . Passez une bonne nuit."]
            else:
                formule = ["Au revoir, " + self.__user + ". Bonne nuit.",
                           "Au revoir, " + self.__user + " . Bonne nuit, repose-toi bien."]
            return formule[nbrand]
        else:
            if hour >= 3 and hour <= 6:
                if self.__vous:
                    formule = ["Bonne nuit, " + self.__genre + " " + self.__user + ". Essayez de vous reposer.",
                               "Bonne nuit, " + self.__genre + " " + self.__user + " Reposez-vous bien."]
                else:
                    formule = ["Bonne nuit, " + self.__user + " Essaie de te reposer un peu.",
                               "Bonne nuit, " + self.__user + " Essaie de te reposer un peu."]
                return formule[nbrand]
            else:
                if hour >= 6 and hour <= 10:
                    if self.__vous:
                        formule = ["Bonne journée, " + self.__genre + " " + self.__user + " Passez une bonne journée. ",
                                   "Bonne journée, " + self.__genre + " " + self.__user + " Profitez bien de votre journée."]
                    else:
                        formule = ["Au revoir, " + self.__user + " Passe une bonne journée.",
                                   "Au revoir, " + self.__user + " Profite bien de ta journée."]
                    return formule[nbrand]
                else:
                    if hour >= 10 and hour <= 12:
                        if self.__vous:
                            formule = [
                                "Au revoir, " + self.__genre + " " + self.__user + " . Passez une bonne fin de matinée.",
                                "Au revoir, " + self.__genre + " " + self.__user + " Profitez bien de votre fin de matinée."]
                        else:
                            formule = ["Au revoir, Passe une bonne fin de matinée.",
                                       "Au revoir, Profite bien de ta fin de matinée."]
                    else:
                        if hour >= 13 and hour <= 16:
                            if self.__vous:
                                formule = ["Bonne après-midi, " + self.__genre + " " + self.__user + " Profitez bien.",
                                           "Au revoir, " + self.__genre + " " + self.__user + " Passez une bonne fin d'après-midi."]
                            else:
                                formule = ["Au revoir, " + self.__user + " .Profite bien de ta fin d'après-midi.",
                                           "Au revoir, " + self.__user + " .Profite bien de ta fin d'après-midi."]
                            return formule[nbrand]
                        else:
                            if hour >= 16 and hour <= 18:
                                if self.__vous:
                                    formule = [
                                        "Au revoir, " + self.__genre + " " + self.__user + " Profitez bien de votre fin de soirée.",
                                        "Bonne soirée, " + self.__genre + " " + self.__user + " Profitez bien"]
                                else:
                                    formule = ["Au revoir, " + self.__user + " Profite bien de ta soirée.",
                                               "Au revoir, " + self.__user + " Profite bien de ta soirée."]
                                return formule[nbrand]
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.__vous:
                                        formule = [
                                            "Bonne soirée, " + self.__genre + " " + self.__user + " Profitez bien",
                                            "Bonne soirée, " + self.__genre + " " + self.__user + " Reposez-vous bien ce soir."]
                                    else:
                                        formule = ["Au revoir, " + self.__user + " Profite bien de ta soirée.",
                                                   "Au revoir, " + self.__user + " Repose-toi bien ce soir."]
                                    return formule[nbrand]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.__vous:
                                            formule = [
                                                "Bonne nuit, " + self.__genre + " " + self.__user + " Dormez bien.",
                                                "Bonne nuit, " + self.__genre + " " + self.__user + " Reposez-vous bien."]
                                        else:
                                            formule = ["Bonne nuit, " + self.__user + " Dors bien.",
                                                       "Bonne nuit, " + self.__user + " Repose-toi bien."]
                                        return formule[nbrand]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.__vous:
                                                formule = [
                                                    "Bonne nuit, " + self.__genre + " " + self.__user + " Dormez bien, soyez en forme pour demain.",
                                                    "Bonne nuit, " + self.__genre + " " + self.__user + " Reposez-vous bien pour demain."]
                                            else:
                                                formule = [
                                                    "Bonne nuit, " + self.__user + " Dors bien, sois en forme pour demain.",
                                                    "Bonne nuit, " + self.__user + " Repose-toi bien pour demain."]
                                            return formule[nbrand]
                                        else:
                                            if self.__vous:
                                                formule = "Au revoir,  " + self.__genre + " " + self.__user + " J'espère vous revoir bientôt."
                                            else:
                                                formule = "Au revoir, " + self.__user + " J'espère te revoir bientôt."
                                            return formule

    def bootWithHist(self, hour):

        sortie = self.__fncHist.verfiHist()
        if (sortie == True):
            self.__fncHist.startHistAction()

        if hour >= 0 and hour < 3:
            if self.__vous:
                formule = "Bonjour,"
                cmp = self.__genre + " " + self.__user
                phrase = "Je vous ai relancé votre travail. Mais il faudrait que vous dormiez."
            else:
                formule = "Zzzz"
                cmp = self.__user
                phrase = "J'ai relancé là où tu t'étais arrêté. Mais il faudrait que tu dormes."
        else:
            if hour >= 3 and hour <= 6:
                if self.__vous:
                    formule = "Bonjour,"
                    cmp = self.__genre + " " + self.__user
                    phrase = "Je vous ai relancé votre travail. Mais il faudrait que vous dormiez."
                else:
                    formule = "Zzzz"
                    cmp = self.__user
                    phrase = "J'ai relancé là où tu t'étais arrêté. Mais il faudrait que tu dormes."
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
        return str(formule + " " + cmp + " " + phrase)