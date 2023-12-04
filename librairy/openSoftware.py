from librairy.dectectionOS import*
from ObjetsNetwork.gestion import*
import subprocess
import os

class OpenSoftware :
    def __init__(self,objetGestion:gestionNetwork,name:str):
        detecteurOS = OS()
        self.__windowsOS = detecteurOS.osWindows()
        self.__linuxOS = detecteurOS.osLinux()
        self.__emplacement = ""
        self.__etat = bool
        if name == "":
            self.__etat = False
        else :
            if self.__windowsOS == True and self.__linuxOS == False :
                self.emplacement = os.path.abspath(objetGestion.getEmplacementSoftwareWindows()+"/"+name+".lnk")
                self.__etat = True
            else :
                if self.__windowsOS == False and self.__linuxOS == True : 
                        self.__emplacement = name
                        self.__etat = True
                else :
                    self.__etat = False
               
    def open(self):
        if self.__etat == False:
            return False
        else :
            if self.__windowsOS == False and self.__linuxOS == True :
                subprocess.Popen([self.__emplacement],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True 
            else :
                if self.__windowsOS == True and self.__linuxOS == False :
                    subprocess.Popen(["cmd", "/c", "start", self.__emplacement])
                    return True
                else :
                    return False