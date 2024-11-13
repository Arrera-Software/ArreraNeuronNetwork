from tkinter import*
import webbrowser as w
from librairy.travailJSON import*
from ObjetsNetwork.gestion import*


class CHLibrairy:
    def __init__(self,ConfigNeuron:jsonWork,gest:gestionNetwork):
        self.__lienLibrairy = "https://github.com/Arrera-Software/Arrera-librairy"
        self.__lienReadme =  "https://github.com/Arrera-Software/Arrera-librairy/blob/main/README.md"
        self.__lienObjetPython = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/python"
        self.__lienObjetCPP = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/C%2B%2B"
        self.__mainColor = ConfigNeuron.lectureJSON("interfaceColor")
        self.__textColor = ConfigNeuron.lectureJSON("interfaceTextColor")
        self.__iconAssistant = ConfigNeuron.lectureJSON("iconAssistant") 
        self.__name = ConfigNeuron.lectureJSON("name")
        self.objNET = gest.getNetworkObjet()
    
    def librairy(self):
        if (self.objNET.getEtatInternet() == True):
            try:
                response = requests.get(
                    "https://raw.githubusercontent.com/Arrera-Librairy/index-codehelp/refs/heads/main/index.json")
                response.raise_for_status()
                contenuJson = response.json()
                nb = len(contenuJson)+1
                listLib = []
                dictURLName = {}
                for i in range(1,nb):
                    listLib.append(contenuJson[str(i)]['name'])
                    dictURLName[contenuJson[str(i)]['name']] = contenuJson[str(i)]['url']

            except requests.exceptions.RequestException as e:
                return False



            self.__screenLibrairy = Toplevel()
            self.__varName = StringVar(self.__screenLibrairy)
            self.__screenLibrairy.title(self.__name + ": codeHelp librairy")
            self.__screenLibrairy.iconphoto(False, PhotoImage(file=self.__iconAssistant))
            self.__screenLibrairy.minsize(700, 500)
            self.__screenLibrairy.configure(bg=self.__mainColor)

            self.__optionName = OptionMenu(self.__screenLibrairy, self.__varName, *listLib)

            self.__optionName.place(relx=0.5, rely=0.5, anchor="center")

            return True
        else:
            return False

    def __destroyWindows(self):
        self.__screenLibrairy.destroy()

    def __openLib(self):
        w.open(self.__lienLibrairy)
        self.__destroyWindows()
    
    def __openReadme(self):
        w.open(self.__lienReadme)
        self.__destroyWindows()
    
    def __openObjPython(self):
        w.open(self.__lienObjetPython)
        self.__destroyWindows()
    
    def __openObjCPP(self):
        w.open(self.__lienObjetCPP)
        self.__destroyWindows()