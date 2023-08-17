from librairy.dectectionOS import*
import subprocess
import os

class OpenSoftware :
    def __init__(self,emplacementLogiciel:str):
        detecteurOS = OS()
        self.windowsOS = detecteurOS.osWindows()
        self.linuxOS = detecteurOS.osLinux()
        if self.windowsOS == True and self.linuxOS == False :
            self.emplacement = os.path.abspath(emplacementLogiciel+".lnk")
        else :
           if self.windowsOS == False and self.linuxOS == True : 
                self.emplacement = emplacementLogiciel
           else :
               self.emplacement == "ereur"
               
    def open(self):
        if self.emplacement == "ereur":
            return False
        else :
            if self.windowsOS == False and self.linuxOS == True :
                subprocess.Popen([self.emplacement],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True 
            else :
                if self.windowsOS == True and self.linuxOS == False :
                    subprocess.Popen(["cmd", "/c", "start", self.emplacement])
                    return True
                else :
                    return False