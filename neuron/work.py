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

            if (("ouvre" in requette) and ((("un" in requette) and ("une" not in requette)) or ("fichier" in requette))):
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
                                                    if (etatVous == True):
                                                        self.__listSortie = ["Quelle fichier voulez-vous que je vous montre "+genre+". Le exel ou le word ?",""]
                                                    else : 
                                                        self.__listSortie = ["Quelle fichier veut tu que je te montre. Le exel ou le word ?",""]
                                                    self.__valeurOut = 1
                                    if ((("supprime" in requette) or ("suppr" in requette))
                                        and (("supprime une tache" not in requette) and ("supprimer une tache" not in requette) 
                                        and ("suppr une tache" not in requette) and ("suppr tache" not in requette))):
                                        
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
                                                                                                if (("ouvre" in requette) and ("pense bete" in requette)):
                                                                                                    if ("une" in requette):
                                                                                                        sortie,text = self.__fonctionArreraNetwork.sortieOpenPostiteWithFile()
                                                                                                        if (sortie == True):
                                                                                                            self.__objHistorique.setAction("Ouverture du pense bete "+self.__fonctionArreraNetwork.getNamePenseBete())
                                                                                                            self.__valeurOut = 5
                                                                                                        else :
                                                                                                            self.__valeurOut = 1
                                                                                                    else :
                                                                                                        text = self.__fonctionArreraNetwork.sortieOpenPostiteNoFile()
                                                                                                        self.__objHistorique.setAction("Ouverture d'un nouveau pense bete")
                                                                                                        self.__valeurOut = 5
                                                                                                    self.__listSortie = [text,""]
                                                                                                else :
                                                                                                    if ("aide tableur" in requette):
                                                                                                        self.__listSortie = ["Les fonction d'edition de tableur d'Arrera Work sont :"+
                                                                                                                        "\n- Pour ouvrir un tableur dite 'Ouvre un fichir exel', 'Ouvre un exel', 'Ouvre un fichir tableur' ou 'Ouvre un tableur'"+
                                                                                                                        "\n- Pour ouvrir le tableur sur le logiciel de l'ordinateur dit 'Ouvre le fichier tableur avec le logiciel de l'ordinateur' ou 'Ouvre le fichier tableur avec l'ordinateur'"+
                                                                                                                        "\n- Fermer le tableur dit 'ferme le tableur' ou 'ferme l'exel'"+
                                                                                                                        "\n- Dire le contenu du tableur 'Lis le tableur'"+
                                                                                                                        "\n- Ajouter une valeur 'Ajoute une valeur au tableur', 'Rajoute une valeur au tableur' ou 'ajout une valeur au tableur'"+
                                                                                                                        "\n- Ajouter une moyenne 'Ajoute une moyenne au tableur', 'Rajoute une moyenne au tableur' ou 'ajout une moyenne au tableur'"+
                                                                                                                        "\n- Ajouter une somme 'Ajoute une somme au tableur', 'Rajoute une somme au tableur' ou 'ajout une somme au tableur'"+
                                                                                                                        "\n- Ajouter un comptage 'Ajoute un comptage au tableur', 'Rajoute un comptage au tableur' ou 'ajout un comptage au tableur'"+
                                                                                                                        "\n- Ajouter un minimun 'Ajoute un minimun au tableur', 'Rajoute un minimun au tableur' ou 'ajout un minimun au tableur'"+
                                                                                                                        "\n- Ajouter un maximun 'Ajoute un maximun au tableur', 'Rajoute un maximun au tableur' ou 'ajout un maximun au tableur'"
                                                                                                                        "\n- Ouvrir le tableur avec l'interface de l'assistant dite 'montre le tableur' ou 'montre l'exel'"
                                                                                                                        "\n- Supprimer un valeur du tableur dite 'supprime une valeur au tableur', 'suppr une valeur au tableur', 'supprime une valeur a exel' ou 'suppr une valeur a exel'"
                                                                                                                        ,""]
                                                                                                        self.__valeurOut = 17 
                                                                                                    else :
                                                                                                        if ("aide word" in requette):
                                                                                                            self.__listSortie = ["Les fonction d'edition de fichier traitement de texte d'Arrera Work sont :"+
                                                                                                                        "\n- Pour ouvrir un fichier word dite 'Ouvre un fichier word', 'Ouvre un fichier traitement de texte', 'Ouvre un word' ou 'Ouvre un traitement de texte'"+
                                                                                                                        "\n- Pour ouvrir le traitement de texte sur le logiciel de l'ordinateur dit 'Ouvre le fichier traitement de texte avec le logiciel de l'ordinateur', 'Ouvre le fichier traitement de texte avec l'ordinateur', 'Ouvre le fichier word avec le logiciel de l'ordinateur' ou 'Ouvre le fichier word avec l'ordinateur'"+
                                                                                                                        "\n- Fermer le word dit 'ferme le word' ou 'ferme le traitement de texte'"+
                                                                                                                        "\n- Lire le word dite 'Lis le word'"+
                                                                                                                        "\n- Ecrire dans le fichier traitement de texte 'ecrit dans le word'"+
                                                                                                                        "\n- Ouvrir le traitement de texte avec l'interface de l'assistant dite 'montre le word', 'montre traitement de texte' ou 'montre document'"
                                                                                                                        ,""]
                                                                                                            self.__valeurOut = 17
                                                                                                        else :
                                                                                                            if ("aide projet" in requette):
                                                                                                                self.__listSortie = ["Les fonction de la fonctionnalités Arrera Project :"+
                                                                                                                        "\n- Crée un projet dite 'cree un projet nommer #name#', 'cree un nouveau projet nommer #name#', 'cree un projet nomme #name#' ou 'cree un nouveau projet nomme #name#'"+
                                                                                                                        "\n- Ouvrir un projet Arrera dite 'cree un projet nommer #name projet#', 'cree un nouveau projet nommer #name projet#', 'cree un projet nomme #name projet#' ou 'cree un nouveau projet nomme #name projet#'"+
                                                                                                                        "\n- Mettre un type au projet quand il vien d'étre crée dite 'Le type est #type#'"+
                                                                                                                        "\n- Mettre un type au projet dite 'Le type du projet est #type#'"+
                                                                                                                        "\n- Crée un fichier dite 'Crée un fichier #Type file# nommer #Name file#'" +
                                                                                                                        "\n- Pour voir les type de file qui peuvent etre crée dite 'Type fichier'"+
                                                                                                                        "\n- Fermer le projet dite 'ferme le projet'"+
                                                                                                                        "\n- Voir les fichier dans le projet dite 'ouvre le fichier du projet nommer #name file#' ou 'ouvre le fichier nommer #name file#'"+
                                                                                                                        "\n- Ajouter une tache au projet dite 'ajoute une tache au projet', 'ajouter une tache au projet', 'ajout tache au projet' ou 'add tache projet'"+
                                                                                                                        "\n- Supprimer une tache au projet dite 'supprime une tache au projet', 'supprimer une tache au projet','suppr une tache au projet' ou 'suppr tache projet' "+
                                                                                                                        "\n- Finir une tache au projet dite 'finir une tache au projet', 'terminer une tache au projet', 'termine une tache au projet' ou 'fini une tache au projet'"+
                                                                                                                        "\n- Voir les tache du projet dite 'montre mes taches du projet', 'fais voir mes taches du projet' ou 'montre les taches du projet'"+
                                                                                                                        "\n- Dire les tache qu'il a faire pour aujourd'hui sur le projet dite 'Dit moi le nombre de taches que j'ai pour aujourd'hui"+
                                                                                                                        "\n- Dire les tache qu'il a faire pour demain sur le projet dite 'Dit moi le nombre de taches que j'ai demain"+
                                                                                                                        "\n- Dire le nombre total de tache sur le projet 'Dit moi le nombre de taches que j'ai'"
                                                                                                                        ,""]
                                                                                                                self.__valeurOut = 17
                                                                                                            else : 
                                                                                                                if ("type fichier" in requette):
                                                                                                                    self.__listSortie = ["Les type sont :"
                                                                                                                                        +"\n- word"
                                                                                                                                        +"\n- odt"
                                                                                                                                        +"\n- open texte document"
                                                                                                                                        +"\n- txt"
                                                                                                                                        +"\n- texte"
                                                                                                                                        +"\n- python"
                                                                                                                                        +"\n- en tete"
                                                                                                                                        +"\n- json"
                                                                                                                                        +"\n- html"
                                                                                                                                        +"\n- css"
                                                                                                                                        +"\n- md"
                                                                                                                                        +"\n- cpp"
                                                                                                                                        +"\n- language c++"
                                                                                                                                        +"\n- language c"
                                                                                                                                        +"\n- exel"
                                                                                                                                        +"\n- tableur"
                                                                                                                                        +"\n- php"
                                                                                                                                        +"\n- javascript"
                                                                                                                                        +"\n- java script"
                                                                                                                                        +"\n- js"
                                                                                                                                        +"\n- java"
                                                                                                                                        +"\n- kotlin"
                                                                                                                                        +"\n- kt"
                                                                                                                                        ,""]
                                                                                                                    self.__valeurOut = 17