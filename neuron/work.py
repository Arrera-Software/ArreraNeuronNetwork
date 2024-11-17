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

            if (("ouvre" in requette)):
                if ((("exel" in requette) or ("tableur" in requette)) 
                    and  ("ordinateur" in requette)):
                    self.__listSortie = [self.__fonctionArreraNetwork.sortieOpenSoftTableurFile(),""]
                    self.__objHistorique.setAction("Ouverture du fichier tableur "+self.__fonctionArreraNetwork.getFileTableur()+" sur l'ordinateur")
                    self.__valeurOut = 1
                else :
                    if (("word" in requette) or ("traitement de texte" in requette) or 
                         ("document" in requette)) and  ("ordinateur" in requette):
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
                        name = self.__fonctionArreraNetwork.getFileTableur()
                        self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseTableur(),""]
                        self.__objHistorique.setAction("Fermeture du fichier exel "+name)
                        self.__valeurOut = 8
                    else :
                        if (("word" in requette) or ("traitement de texte" in requette)):
                            name = self.__fonctionArreraNetwork.getFileWord()
                            self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseDocx(),""]
                            self.__objHistorique.setAction("Fermeture du fichier word "+name)
                            self.__valeurOut = 8
                        else :
                            if ("projet" in requette):
                                nameProjet = self.__fonctionArreraNetwork.getNameProjetOpen()
                                self.__listSortie = [self.__fonctionArreraNetwork.sortieCloseProject(),""]
                                self.__objHistorique.setAction("Fermeture du projet "+nameProjet)
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
                                    self.__listSortie = self.__fonctionArreraNetwork.sortieErrorReadTableur()
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
                                if (((("ajoute" in requette)  or ("rajoute" in requette) 
                                    or ("ajout" in requette)) and ("tableur" in requette)) 
                                    and (("ajoute une tache" not in requette) or ("ajouter une tache"  not in  requette) 
                                    or ("ajout tache" not in requette) or ("add tache" not in requette))):
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
                                                    self.__listSortie = self.__fonctionArreraNetwork.sortieBadFile()
                                                    self.__valeurOut = 1
                                    if ((("supprime" in requette) or ("suppr" in requette))
                                        and (("supprime une tache" not in requette) and ("supprimer une tache" not in requette) 
                                        and ("suppr une tache" not in requette) and ("suppr tache" not in requette))):
                                        
                                        if (("tableur" in requette) or ("exel" in requette)):
                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieSupprValeurTableur(),""]
                                            self.__objHistorique.setAction("Suppression d'une valeur au tableur "+self.__fonctionArreraNetwork.getFileTableur())
                                            self.__valeurOut = 5
                                    else : 
                                        if ((("Quelle fichier voulez-vous que je vous montre " in oldSortie and ". Le exel ou le word ?" in oldSortie) or
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
                                                self.__objHistorique.setAction("Creation d'un projet nommer "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                self.__valeurOut = 10
                                            else :
                                                if (("Quelle est le type de projet ?" in oldSortie) and ("le type est" in requette)):
                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieSetTypeProjet(requette),""]
                                                    self.__objHistorique.setAction("Mise en place d'un type au projet")
                                                    self.__valeurOut = 5
                                                else :
                                                    if ("le type du projet est" in requette):
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
                                                                    else :
                                                                        if((("montre mes taches"in requette) or ("fais voir mes taches"in requette) 
                                                                        or ("montre mes tache"in requette) or("fais voir mes tache"in requette))
                                                                        or ("montre les taches"in requette) and ("projet" in requette)):
                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieShowTacheProjet(),""]
                                                                            self.__objHistorique.setAction("Activation de l'interface des tache du projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                            self.__valeurOut = 5 
                                                                        else :
                                                                            if((("ajoute une tache" in requette) or ("ajouter une tache" in requette) 
                                                                            or ("ajout tache" in requette) or ("add tache" in requette)) and ("projet" in requette)):
                                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieAddTacheProjet(),""]
                                                                                self.__objHistorique.setAction("Ajout d'une tache au projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                                self.__valeurOut = 5
                                                                            else :
                                                                                if((("supprime une tache" in requette)or ("supprimer une tache" in requette) 
                                                                                or ("suppr une tache" in requette) or ("suppr tache" in requette))
                                                                                and ("projet" in requette)):
                                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieSupprTacheProjet(),""]
                                                                                    self.__objHistorique.setAction("Suppression d'une tache au projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                                    self.__valeurOut = 5
                                                                                else :
                                                                                    if((("finir une tache" in requette) or ("terminer une tache" in requette) 
                                                                                    or ("termine une tache" in requette) or ("fini une tache" in requette))
                                                                                    and ("projet" in requette)):
                                                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieSupprTacheProjet(),""]
                                                                                        self.__objHistorique.setAction("Finnision d'une tache au projet "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                                        self.__valeurOut = 5
                                                                                    else :
                                                                                        if ("dit moi" in requette) and (("nombre" in requette) or ("j'ai combien" in requette) 
                                                                                            and (("tache" in requette) or ("taches" in requette)) and ("projet" in requette)) :
                                                                                        
                                                                                            if  (("jour" in requette) or ("aujourd'hui" in requette)) :
                                                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieListeTacheTodayProjet(),""] 
                                                                                                self.__objHistorique.setAction("Enumeration des taches du "+self.__fonctionArreraNetwork.getNameProjetOpen()+" pour aujourd'hui")
                                                                                                self.__valeurOut = 1
                                                                                            else :
                                                                                                if ("demain" in requette):
                                                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieListTacheTowmorowProjet(),""]
                                                                                                    self.__objHistorique.setAction("Enumeration des taches du "+self.__fonctionArreraNetwork.getNameProjetOpen()+" pour demain")
                                                                                                    self.__valeurOut = 1
                                                                                                else :
                                                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieNbTacheProjet(),""]
                                                                                                    self.__objHistorique.setAction("Enumeration des taches du "+self.__fonctionArreraNetwork.getNameProjetOpen())
                                                                                                    self.__valeurOut = 1
                                                                                        else :
                                                                                            if ((("comment" in requette) and ("utiliser" in requette) and ("arrera work" in requette)) 
                                                                                                or ("aide work" in requette)):
                                                                                                self.__listSortie = ["Les fonction d'Arrera work sont :"+
                                                                                                                     "\n- Edition tableur (Taper aide tableur)"+
                                                                                                                     "\n- Edition fichier de traitement de texte (Taper aide word)"+
                                                                                                                     "\n- Fonction Arrera projet (Taper aide projet)"
                                                                                                                     ,""]
                                                                                                self.__valeurOut = 17 
                                                                                            else :
                                                                                                if ("aide tableur" in requette):
                                                                                                    self.__listSortie = [self.__fonctionArreraNetwork.sortieHelpWorkTableur()
                                                                                                        ,"tableur"]
                                                                                                    self.__valeurOut = 17
                                                                                                else :
                                                                                                    if ("aide word" in requette):
                                                                                                        self.__listSortie = [self.__fonctionArreraNetwork.sortieHelpWorkTraitementTexte()
                                                                                                                    ,"word"]
                                                                                                        self.__valeurOut = 17
                                                                                                    else :
                                                                                                        if ("aide projet" in requette):
                                                                                                            self.__listSortie = [self.__fonctionArreraNetwork.sortieHelpArreraWork()
                                                                                                                    ,"projet"]
                                                                                                            self.__valeurOut = 17
                                                                                                        else :
                                                                                                            if ("type fichier" in requette):
                                                                                                                self.__listSortie = [self.__fonctionArreraNetwork.sortieHelpWorkType()
                                                                                                                                    ,"fichier"]
                                                                                                                self.__valeurOut = 17