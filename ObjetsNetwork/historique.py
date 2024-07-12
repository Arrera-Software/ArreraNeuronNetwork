from librairy.travailJSON import*
from arreraSoftware.fonctionDate import*

class CHistorique :
    def __init__(self,configNeuron:jsonWork):
        # Declaration des varriable est de objet
        self.__fileHist = jsonWork(configNeuron.lectureJSON("emplacementFileHist"))
        self.__dateToday = str
        self.__dateTowmorow = str
        self.__objDate = fncDate()
        self.__dictHist = dict
        self.__histToday = list
        self.__histTowmorow = list

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
        
