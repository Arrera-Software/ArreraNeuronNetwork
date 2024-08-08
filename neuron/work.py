from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuronWork :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron,objHist:CHistorique):
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        self.__objHistorique = objHist
        self.__listSortie = ["",""]
        self.__valeurOut = int
    
    def getListSortie(self)->list:
        return self.__listSortie
    
    def getValeurSortie(self)->int :
        return self.__valeurOut
    
    def neurone(self,requette:str):
        if (self.__gestNeuron.getWork() == True):
            #Initilisation des variable nbRand et text et valeur
            self.__valeurOut = 0
            self.__listSortie = ["",""]
            etatVous = self.__gestionNeuron.getVous()
            genre = self.__gestionNeuron.getGenre()
            user = self.__gestionNeuron.getUser()
            oldRequette,oldSortie = self.__gestionNeuron.getOld()

            if (("ouvre" in requette) and (("fichier" in requette) or ("un" in requette))):
                if ((("exel" in requette) or ("tableur" in requette)) and ("logiciel" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSoftTableurFile(),""]
                    self.__objHistorique.setAction("Ouverture du fichier tableur "+self.__fonctionArreraNetwork.getFileTableur()+" sur l'ordinateur")
                    self.__valeurOut = 1
                else :
                    if ((("word" in requette) or ("traitement de texte" in requette) or ("document" in requette)) and ("logiciel" in requette)):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSoftWorkFile(),""]
                        self.__objHistorique.setAction("Ouverture du fichier word "+self.__fonctionArreraNetwork.getFileWord()+" sur l'ordinateur")
                        self.__valeurOut = 1
                    else :
                        if (("exel" in requette) or ("tableur" in requette)):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTableur(),""]
                            self.__objHistorique.setAction("Ouverture d'un fichier exel "+self.__fonctionArreraNetwork.getFileTableur())
                            self.__valeurOut = 7 
                        else :
                            if (("word" in requette) or ("traitement de texte" in requette) or ("document" in requette)):
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenWord(),""]
                                self.__objHistorique.setAction("Ouverture d'un fichier word "+self.__fonctionArreraNetwork.getFileWord())
                                self.__valeurOut = 7
                            else :
                                if (("projet" in requette) or ("nommer" in requette) and ("le" in requette)):
                                    text,file = self.__fonctionArreraNetwork.sortieOpenFileProject(requette)
                                    self.__listSortie = [text,""]
                                    if ("Il a peux être pas un projet ouvert." not in requette):
                                        self.__objHistorique.setAction("Ouverture du fichier "+file+" du projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                        self.__valeurOut = 7
                                    else :
                                        self.__valeurOut = 1

            else :
                if ("ferme" in requette) :
                    if (("exel" in requette) or ("tableur" in requette)):
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseTableur(),""]
                        self.__objHistorique.setAction("Fermeture d'un fichier exel")
                        self.__valeurOut = 8
                    else :
                        if (("word" in requette) or ("traitement de texte" in requette)):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseDocx(),""]
                            self.__objHistorique.setAction("Fermeture d'un fichier word")
                            self.__valeurOut = 8
                        else :
                            if ("projet" in requette):
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseProject(),""]
                                self.__objHistorique.setAction("Fermeture d'un projet")
                                self.__valeurOut = 1
                else :
                    if (("lis" in requette) and ("liste" not in requette)):
                        if ("word" in requette):
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieReadDocx(),""]
                            self.__objHistorique.setAction("Lecture du fichier word "+self.__fonctionArreraNetwork.getFileWord())
                            self.__valeurOut = 9
                        else :
                            if ("tableur" in requette):
                                sortieTableur = self.__fonctionArreraNetwork.sortieReadTableur()
                                if (sortieTableur[0] == "error"):
                                    self.__valeurOut = 1
                                    if (etatVous == True):
                                        self.__listSortie = ["Désoler "+genre+" "+user+" mais il a un probleme qui m'empéche de lire le tableur",""]
                                    else :
                                        self.__listSortie = ["Je ne peux pas faire ce que tu m'as demandé.",""]
                                else :
                                    self.__listSortie = sortieTableur
                                    self.__valeurOut = 13
                                    self.__objHistorique.setAction("Lecture du fichier tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                    
                    else :
                        if ("ecrit dans le word" in requette) :
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieWriteDocx(requette),""]
                            self.__objHistorique.setAction("Ecriture dans le fichier docx"+self.__fonctionArreraNetwork.getFileWord())
                            self.__valeurOut = 1
                        else :
                            if (("ouvert" in requette) and 
                                (("document" in requette) or ("tableur" in requette) 
                                 or ("fichier" in requette) or ("word" in requette))):
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieFileOpen(),""]
                                self.__valeurOut = 1
                            else :
                                if ((("ajoute" in requette)  or ("rajoute" in requette) or ("ajout" in requette)) 
                                    and ("tableur" in requette)):
                                    if (("valeur" in requette)):
                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieAddValeurTableur(),""]
                                        self.__objHistorique.setAction("Ajout d'une valeur au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                        self.__valeurOut = 5
                                    else :
                                        if ("somme" in requette) :
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieAddFormuleTableur(1),""]
                                            self.__objHistorique.setAction("Ajout d'une formule somme au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                            self.__valeurOut = 5
                                        else :
                                            if ("moyenne" in requette):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieAddFormuleTableur(2),""]
                                                self.__objHistorique.setAction("Ajout d'une formule moyenne au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                                self.__valeurOut = 5 
                                            else :
                                                if ("comptage" in requette):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieAddFormuleTableur(3),""]
                                                    self.__objHistorique.setAction("Ajout d'une formule comptage au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                                    self.__valeurOut = 5
                                                else :
                                                    if ("minimun" in requette):
                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieAddFormuleTableur(4),""]
                                                        self.__objHistorique.setAction("Ajout d'une formule minimun au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                                        self.__valeurOut = 5
                                                    else :
                                                        if ("maximun" in requette):
                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieAddFormuleTableur(1),""]
                                                            self.__objHistorique.setAction("Ajout d'une formule maximun au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                                            self.__valeurOut = 5
                                else :
                                    if ("montre" in requette):
                                        if ((("exel" in requette) or ("tableur" in requette))):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTableurGUI(),""]
                                            self.__objHistorique.setAction("Ouverture du tableur "+self.__fonctionArreraNetwork.getFileTableur()+" dans l'interface de l'assistant")
                                            self.__valeurOut = 5 
                                        else :
                                            if (("word" in requette) or ("traitement de texte" in requette) or ("document" in requette) ):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenWordGUI(),""]
                                                self.__objHistorique.setAction("Ouverture du word "+self.__fonctionArreraNetwork.getFileWord()+" dans l'interface de l'assistant")
                                                self.__valeurOut = 5
                                            else :
                                                if ("fichier" in requette):
                                                    if (etatVous == True):
                                                        self.__listSortie = ["Quelle fichier voulez-vous que je vous montre "+genre+". Le exel ou le word ?",""]
                                                    else : 
                                                        self.__listSortie = ["Quelle fichier veut tu que je te montre. Le exel ou le word ?",""]
                                                    self.__valeurOut = 1
                                    if (("supprime" in requette) or ("suppr" in requette)):
                                        if (("tableur" in requette) or ("exel" in requette)):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieSupprValeurTableur(),""]
                                            self.__objHistorique.setAction("Suppression d'une valeur au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                            self.__valeurOut = 5
                                    else : 
                                        if (((oldSortie == "Quelle fichier voulez-vous que je vous montre "+genre+". Le exel ou le word ?") or 
                                            (oldSortie == "Quelle fichier veut tu que je te montre. Le exel ou le word ?")) and ("le" in requette)):
                                            if (("word" in requette) or ("traitement de texte" in requette) or ("document" in requette) ):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenWordGUI(),""]
                                                self.__objHistorique.setAction("Ouverture du word "+self.__fonctionArreraNetwork.getFileWord()+" dans l'interface de l'assistant")
                                                self.__valeurOut = 5
                                            else :
                                                if ((("exel" in requette) or ("tableur" in requette))):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenTableurGUI(),""]
                                                    self.__objHistorique.setAction("Ouverture du tableur "+self.__fonctionArreraNetwork.getFileTableur()+" dans l'interface de l'assistant")
                                                    self.__valeurOut = 5 
                                        else :
                                            if (("cree un projet nommer" in requette) or ("cree un nouveau projet nommer" in requette)
                                                or ("cree un projet nomme" in requette) or ("cree un nouveau projet nomme" in requette)):
                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieCreateFolder(requette),""]
                                                self.__objHistorique.setAction("Creation d'un projet")
                                                self.__valeurOut = 10
                                            else :
                                                if (("Quelle est le type de projet ?" in oldSortie) or ("le type est" in requette)):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieSetTypeProjet(requette),""]
                                                    self.__objHistorique.setAction("Mise en place d'un type au projet")
                                                    self.__valeurOut = 5
                                                else :
                                                    if (("ouvre le projet nommer" in requette) or ("ouvre le projet nomme" in requette) or ("ouvre le projet" in requette)):
                                                        projet,text = self.__fonctionArreraNetwork.sortieOpenProjet(requette)
                                                        self.__listSortie = [text,""]
                                                        self.__objHistorique.setAction("Ouverture du projet "+projet)
                                                        self.__valeurOut = 14
                                                    else :
                                                        if ("cree un fichier" in requette):
                                                            if ("nommer" in requette and ( 
                                                                ("word"in requette) or ("odt"in requette) or 
                                                                ("txt"in requette) or ("python" in requette)  
                                                                or ("json" in requette) or ("html" in requette) or 
                                                                ("css" in requette) or("md" in requette) or 
                                                                ("cpp" in requette) or ("exel" in requette) or
                                                                ("texte" in requette) or ("en tete" in requette)or
                                                                ("open texte document " in requette) or ("tableur" in requette)
                                                                or ("language c++" in requette) or ("php" in requette) or
                                                                ("javascript" in requette) or ("java script" in requette) or 
                                                                ("js" in requette) or ("java" in requette) or 
                                                                ("kotlin" in requette )or ("kt" in requette))):
                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieCreateFileDirect(requette),""]
                                                                self.__objHistorique.setAction("Creation du fichier "+self.__fonctionArreraNetwork.getNameLastFile()+" dans le projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                self.__valeurOut = 16
                                                        else :
                                                            if (("Voulez-vous l'ouvrir ?" in oldSortie or "Es que tu veux que je te l'ouvre ?" in oldSortie) and
                                                                ("oui" in requette or "ouvre le" in requette or "vasy" in requette or "comme tu veux" in requette)):
                                                                nameFile = self.__fonctionArreraNetwork.getNameLastFile()
                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieopenFileCreated(),""]
                                                                self.__objHistorique.setAction("Ouverture du fichier "+nameFile+" du projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                self.__valeurOut = 7
                                                            else :
                                                                if (("liste" in requette) and ("fichier" in requette) and 
                                                                    (("projet" in requette ) or ("project" in requette ))):
                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieListFileProject(),""]
                                                                    self.__objHistorique.setAction("Liste de fichier du projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                    self.__valeurOut = 1