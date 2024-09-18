from librairy.travailJSON import*
from arreraSoftware.fonctionDate import*
from arreraSoftware.fncArreraNetwork import*

class CHistorique :
    def __init__(self,configNeuron:jsonWork,fncArreraNetwork:fncArreraNetwork):
        # Declaration des varriable est de objet
        self.__fileHist = jsonWork(configNeuron.lectureJSON("emplacementFileHist"))
        self.__dateToday = ""
        self.__dateTowmorow = ""
        self.__objDate = fncDate()
        self.__dictHist = dict
        self.__histToday = []
        self.__histTowmorow = []
        self.__listAction = []
        
        self.__setDateToday()
        self.__loadFile()

    
    def __setDateToday(self):
        self.__objDate.rafraichisement()
        self.__dateToday = self.__objDate.getDateToday()
        self.__dateTowmorow = self.__objDate.dateTowmoro()
    
    def __loadFile(self):
        self.__dictHist = self.__fileHist.getContenuJSON()
        if (self.__dictHist != {}):
            if (self.__dateToday in self.__dictHist):
                self.__histToday = self.__dictHist[self.__dateToday]
            if (self.__dateTowmorow in self.__dictHist):
                self.__histTowmorow = self.__dictHist[self.__dateTowmorow]
            
            self.__dictHist = {}
            self.__fileHist.writeDictOnJson(self.__dictHist)
    
    def setAction(self,action:str):
        if (action != ""):
            self.__histToday.append(action)
            return True
        else :
            return False
    
    def saveHistorique(self):
        if (self.__histToday != []):
            self.__dictHist[self.__dateToday] = self.__histToday
            self.__fileHist.writeDictOnJson(self.__dictHist)
            return True
        else :
            return False
    
    def verfiHist(self):
        listAction = []
        if (not self.__histTowmorow):
            histTowmorow = False
        else :
            nbTowmorow = len(self.__histTowmorow)-1
            histTowmorow = True 
        
        if (not self.__histToday) :
            histToday = False 
        else :
            nbToday = len(self.__histToday)-1
            histToday = True
            
        if ((histToday == False) and (histTowmorow == False)):
            return False 
        else :
            if ((histToday == True) and (histTowmorow == True)):
                for i in range(0,nbToday+1):
                    sortie = self.__verifAction(self.__histToday[i])
                    if (sortie != "none"):
                        listAction.append(sortie)
                for i in range(0,nbTowmorow+1):
                    sortie = self.__verifAction(self.__histTowmorow[i])
                    if (sortie != "none"):
                        listAction.append(sortie)
                self.__listAction = listAction
                return True
            else :
                if ((histToday == True) and (histTowmorow == False)):
                    for i in range(0,nbToday+1):
                        sortie = self.__verifAction(self.__histToday[i])
                        if (sortie != "none"):
                            listAction.append(sortie)
                    self.__listAction = listAction
                    return True
                else :
                    if ((histToday == False) and (histTowmorow == True)):
                        for i in range(0,nbTowmorow+1):
                            sortie = self.__verifAction(self.__histTowmorow[i])
                            if (sortie != "none"):
                                listAction.append(sortie)
                        self.__listAction = listAction                
                        return True
    
    def __get5oldAction(self,index:int,vlist:list):
        """_summary_

        Args:
            index (int): L'index le plus grand possible dans la liste
            vlist (list): La liste
        """
        outList = []
        for i in range ((index-5),index):
            outList.append(vlist[i])
        
        return outList
    
    def __verifAction(self,action:str):
        if ("Lancement de la radio" in action):
            radio = action.replace("Lancement de la radio")
            return "radio launch "+radio
        else :
            if ("Ouverture organisateur de varriable" in action):
                return "open orga var"
            else :
                if ("Ouverture selecteur de couleur" in action):
                    return "open select color"
                else :
                    if ("Ouverture de logiciel de gestion github" in action):
                        return "open gest github"
                    else :
                        if ("Ouverture de la librairy codehelp" in action):
                            return "lib codehelp"
                        else :
                            if ("Ouverture du logciel de présentation" in action):
                                return "soft presentation"
                            else :
                                if ("Ouverture du navigateur internet" in action):
                                    return "soft internet"
                                else :
                                    if ("Ouverture du logiciel de note" in action):
                                        return "soft note"
                                    else :
                                        if ("Ouverture du logiciel d'ecoute du musique" in action):
                                            return "soft music"
                                        else :
                                            if ("Ouverture du logiciel" in action):
                                                soft = action.replace("Ouverture du logiciel","")
                                                return "soft "+soft
                                            else :
                                                if ("Ouverture de youtube" in action):
                                                    return "site youtube"
                                                else :
                                                    if ("Ouverture du site de stokage cloud" in action):
                                                        return "site cloud"
                                                    else :
                                                        if ("Ouverture du site" in action):
                                                            site = action.replace("Ouverture du site","")
                                                            return "site "+site
                                                        else :
                                                            if ("Ouverture du logiciel de telechargement en mode video" in action):
                                                                return "soft arrera download video"
                                                            else :
                                                                if ("Ouverture du logiciel de telechargement en mode musique" in action):
                                                                    return "soft arrera download music"
                                                                else :
                                                                    if ("Ouverture de la calculatrice en mode nombre complex" in action):
                                                                        return "calculatrice complex"
                                                                    else :
                                                                        if ("Ouverture de la calculatrice en mode pythagore" in action):
                                                                            return "calculatrice pythagore"
                                                                        else :
                                                                            if ("Ouverture de la calculatrice" in action):
                                                                                return "calculatrice"
                                                                            else :
                                                                                if (("Ouverture du fichier tableur" in action) and ("sur l'ordinateur" in action)):
                                                                                    file = action.replace("Ouverture du fichier tableur","").replace("sur l'ordinateur","").replace(" ","")
                                                                                    return file+" open computer tableur"
                                                                                else :
                                                                                    if (("Ouverture du fichier word" in action) and ("sur l'ordinateur" in action)):
                                                                                        file = action.replace("Ouverture du fichier word","").replace("sur l'ordinateur","").replace(" ","")
                                                                                        return file+" open computer word"
                                                                                    else :
                                                                                        if ("Ouverture d'un fichier exel" in action):
                                                                                            file = action.replace("Ouverture d'un fichier exel","").replace(" ","")
                                                                                            return "open exel "+file
                                                                                        else :
                                                                                            if ("Ouverture d'un fichier word" in action):
                                                                                                file = action.replace("Ouverture d'un fichier word","").replace(" ","")
                                                                                                return "open word "+file
                                                                                            else :
                                                                                                if (("Ouverture du tableur" in action) and ("dans l'interface de l'assistant" in action)):
                                                                                                    file = action.replace("Ouverture du tableur","").replace("dans l'interface de l'assistant","").replace(" ","")
                                                                                                    return file+" open tableur assistant"
                                                                                                else :
                                                                                                    if (("Ouverture du word" in action) and ("dans l'interface de l'assistant" in action)):
                                                                                                        file = action.replace("Ouverture du word","").replace("dans l'interface de l'assistant","").replace(" ","")
                                                                                                        return file+" open word assistant"
                                                                                                    else :
                                                                                                        if (("Ouverture du projet" in action) or ("Creation d'un projet nommer" in action)):
                                                                                                            project = action.replace("Ouverture du projet","").replace("Creation d'un projet nommer","").replace(" ","")
                                                                                                            return "open projet "+project 
                                                                                                        else :
                                                                                                            return "none" 
    
    def getListAction(self):
        return self.__listAction                                                                                                                                                        