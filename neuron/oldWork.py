from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuronWork :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique):
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = self.__gestionNeuron.getEtatNeuronObjet()
        self.__objHistorique = objHist
        self.__listSortie = ["",""]
        self.__valeurOut = 0

    def getListSortie(self)->list:
        return self.__listSortie

    def getValeurSortie(self)->int :
        return self.__valeurOut

    def neurone(self,requette:str):
        if (self.__gestNeuron.getWork() == True):
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            oldRequette,oldSortie = self.__gestionNeuron.getOld()
            if (("ouvre" in requette) and ("ouvre le projet nommer" not in requette
                                           and "ouvre le projet nomme" not in requette and "ouvre le projet" not in requette)):

                else :

                    else :

                        else :

                            else :

            else :


                    else :
                        if (
                        else :


                        else :


                    else :

                        else :

                            else :

                                        and (("ajoute une tache" not in requette) or ("ajouter une tache"  not in  requette)
                                             or ("ajout tache" not in requette) or ("add tache" not in requette))):

                                else :

                                        else :


                                            else :
                                                if ("fichier" in requette):
                                                    self._listSortie = self._fonctionArreraNetwork.sortieBadFile()
                                                    self._valeurOut = 1
                                    if ((("supprime" in requette) or ("suppr" in requette))
                                            and (("supprime une tache" not in requette) and ("supprimer une tache" not in requette)
                                                 and ("suppr une tache" not in requette) and ("suppr tache" not in requette))):

                                        if ():

                                    else :
                                        if ((("Quelle fichier voulez-vous que je vous montre " in oldSortie and ". Le exel ou le word ?" in oldSortie) or
                                             (oldSortie == "Quelle fichier veut tu que je te montre. Le exel ou le word ?")) and ("le" in requette)):
                                            if (("word" in requette) or ("traitement de texte" in requette) or ("document" in requette) ):
                                                self._listSortie = [self._fonctionArreraNetwork.sortieOpenWordGUI(), ""]
                                                self._objHistorique.setAction("Ouverture du word " + self._fonctionArreraNetwork.getFileWord() + " dans l'interface de l'assistant")
                                                self._valeurOut = 5
                                            else :
                                                if ((("exel" in requette) or ("tableur" in requette))):
                                                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenTableurGUI(), ""]
                                                    self._objHistorique.setAction("Ouverture du tableur " + self._fonctionArreraNetwork.getFileTableur() + " dans l'interface de l'assistant")
                                                    self._valeurOut = 5
                                        else :

                                                    else :

                                                        else :


                                                                else :


                                                                                        else :

                                                                                            else :

                                                                                                else :

                                                                                                    else :

