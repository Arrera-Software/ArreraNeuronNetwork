from tkinter import*
from tkinter import messagebox
import time
from playsound import *
from librairy.travailJSON import*

class fncArreraHorloge :
    def __init__(self):
        self.mainColor = str
        self.textColor = str
        self.icon = str
        self.name = str
        self.emplacementBIP = str
        
        
    def setAttribut(self,mainColor:str,textColor:str,icon:str,name:str,bip:str):
        self.mainColor = mainColor
        self.textColor = textColor
        self.icon = icon
        self.name = name
        self.emplacementBIP = bip
    
    def setAtributJSON(self,fileJSON:jsonWork):
        self.mainColor = fileJSON.lectureJSON("interfaceColor")
        self.textColor = fileJSON.lectureJSON("interfaceTextColor")
        self.icon = fileJSON.lectureJSON("iconAssistant")
        self.name = fileJSON.lectureJSON("name")
        self.emplacementBIP = fileJSON.lectureJSON("emplacementAssetHorloge")
          
    def _fenetreTK(self):
        self.screen = Toplevel()
        self.screen.iconphoto(False,PhotoImage(file=self.icon))
        self.screen.title(self.name+" : Horloge")
        self.screen.minsize(500,500)
        self.screen.maxsize(500,500)
        self.screen.config(bg=self.mainColor)
        self.frameBottom = Frame(self.screen,bg=self.mainColor,width=500,height=35)
        self.frameChrono = Frame(self.screen,bg=self.mainColor,height=465,width=500)
        self.frameMinuteur = Frame(self.screen,bg=self.mainColor,height=465,width=500)
        self.frameHorloge = Frame(self.screen,bg=self.mainColor,height=465,width=500)
        self.btn2 = Button(self.frameBottom,text="Chronometre",font=("arial","13"),bg=self.mainColor,fg=self.textColor,command=self._affichageChrono)
        self.btn3 = Button(self.frameBottom,text="Minuteur",font=("arial","13"),bg=self.mainColor,fg=self.textColor,command=self._affichageMinuteur)
        self.btn4 = Button(self.frameBottom,text="Horloge",font=("arial","13"),bg=self.mainColor,fg=self.textColor,command=self._affichageHorloge)
        self.objetChrono = CHRONOMETRE(self.frameChrono,self.mainColor,self.textColor)
        self.objetAppMinuteur = AppMinuteur(self.frameMinuteur,self.mainColor,self.textColor,self.emplacementBIP)
        self.objetHorloge = Clock(self.frameHorloge,self.mainColor,self.textColor)
        self._affichageBottom()
    
    def _affichageBottom(self):
        self.btn2.place(x=0,y=0)
        self.btn3.place(x=150,y=0)
        self.btn4.place(x=260,y=0)
        self.frameBottom.pack(side="bottom")
    
    def resetAffichage(self):
        self.frameChrono.place_forget()
        self.frameHorloge.place_forget()
        self.frameMinuteur.place_forget()
    
    def modeChrono(self):
        self._fenetreToplevel()
        self.objetChrono.bootChrono()
        self.frameChrono.place(x=0,y=0)
    
    def modeMinuteur(self):
        self._fenetreToplevel()
        self.objetAppMinuteur.bootAppMinuteur()
        self.frameMinuteur.place(x=0,y=0)
    
    def modeBootMinuteur(self,duration:int) :
        self._fenetreToplevel()
        self.objetAppMinuteur.bootMinuteurInstentaner(duration)
        self.frameMinuteur.place(x=0,y=0)
    
    def modeHorloge(self):
        self._fenetreToplevel()
        self.objetHorloge.bootClock()
        self.frameHorloge.place(x=0,y=0)
    
    def _affichageChrono(self):
        self.resetAffichage() 
        self.objetChrono.bootChrono()
        self.frameChrono.place(x=0,y=0)
    
    def _affichageMinuteur(self):
        self.resetAffichage()
        self.objetAppMinuteur.bootAppMinuteur()
        self.frameMinuteur.place(x=0,y=0)
    
    def _affichageHorloge(self):
        self.resetAffichage()
        self.objetHorloge.bootClock()
        self.frameHorloge.place(x=0,y=0)
        
        
class CHRONOMETRE:
    def __init__(self,master,mainColor,textColor):
        self.master = master
        self.mainColor = mainColor
        self.textColor = textColor
        self.label = Label(self.master, text="00:00", font=("arial", 40),bg=self.mainColor,fg=self.textColor)
        self.start_button = Button(self.master, text="Start", command=self.start ,font=("arial", 15),bg=self.mainColor,fg=self.textColor)
        self.stop_button = Button(self.master, text="Stop", command=self.stop ,font=("arial", 15),bg=self.mainColor,fg=self.textColor)
        self.reset_button = Button(self.master, text="Reset", command=self.reset ,font=("arial", 15),bg=self.mainColor,fg=self.textColor)
        self.is_running = bool
        self.current_time = int
        self.start_time = int
        self.elapsed_time = int

    def bootChrono(self):
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.start_button.place(x=40,y=215)
        self.stop_button.place(x=400,y=215)
        self.reset_button.place(x=215,y=315)
        self.is_running = False
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            self.UpdateTemps()

    def stop(self):
        if self.is_running:
            self.is_running = False

    def reset(self):
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0
        self.label.configure(text="00:00")

    def UpdateTemps(self):
        if self.is_running:
            self.current_time = time.time()
            self.elapsed_time = self.current_time - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            self.label.configure(text=f"{int(minutes):02d}:{int(seconds):02d}")
            self.master.after(10, self.UpdateTemps)

        
class MINUTEUR:
    def __init__(self, master,mainColor,textColor,emplacementBIP:str):
        self.master = master
        self.mainColor = mainColor
        self.textColor =  textColor
        self.emplacementBIP =  emplacementBIP
        self.duration = int
        self.label = Label(master, font=("arial", 40),bg=self.mainColor,fg=self.textColor)
        self.stopBTN = Button(master, text="Stop", command=self.stop,font=("arial", 15),bg=self.mainColor,fg=self.textColor)
        self.running = False
        self.currentTime = 0
        self.startTime = 0
        self.elapsedTime = 0

        
    def bootMinuteur(self,duration:int):
        self.duration = duration
        self.objetAPP = AppMinuteur(self.master,self.mainColor,self.textColor,self.emplacementBIP)
        self.label.configure(text=self.FormatTemps(self.duration))
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.stopBTN.place(x=215,y=315)
        self.currentTime = 0
        self.startTime = 0
        self.elapsedTime = 0
        self.objetAPP.setOlminuteur(duration)
        if not self.running:
            self.startTime = time.time()
            self.running = True
            self.UpdateHorloge()

    def stop(self):
        self.label.place_forget()
        self.stopBTN.place_forget()
        self.objetAPP.bootAppMinuteur()
        if self.running:
            self.running = False


    def UpdateHorloge(self):
        if self.running:
            self.currentTime = time.time()
            self.elapsedTime = self.currentTime - self.startTime
            remaining_time = self.duration - self.elapsedTime
            if remaining_time <= 0:
                playsound(self.emplacementBIP)
                time.sleep(0.5)
                self.stop()
                self.label.place_forget()
                self.stopBTN.place_forget()
                self.objetAPP.bootAppMinuteur()
            self.label.configure(text=self.FormatTemps(remaining_time))
            self.master.after(10, self.UpdateHorloge)

    def FormatTemps(self, time):
        minutes, seconds = divmod(time, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"


class AppMinuteur :
    def __init__(self,master,mainColor:str,textColor:str,emplacementBIP:str):
        self.master = master
        self.mainColor = mainColor
        self.textColor = textColor
        self.emplacementBIP = emplacementBIP
        self.oldMinuteur = 0
        self.zoneEntrer = Frame(master,bg=mainColor)
        self.entryMin = Entry(self.zoneEntrer,width=5,font=("arial","15"))
        self.entrySec = Entry(self.zoneEntrer,width=5,font=("arial","15"))
        self.labelMin = Label(self.zoneEntrer,text="min",font=("arial","15"),bg=mainColor,fg=textColor)
        self.labelSec = Label(self.zoneEntrer,text="s",font=("arial","15"),bg=mainColor,fg=textColor)
        self.btnBoot = Button(master,text="Demarrer",bg=mainColor,fg=textColor,font=("arial","15"),command=self._boot)
        self.btnPrereglage1 = Button(master,text="15 minutes",bg=mainColor,fg=textColor,command=self._prereglage1,font=("arial","15"))
        self.btnPrereglage2 = Button(master,text="30 minutes",bg=mainColor,fg=textColor,command=self._prereglage2,font=("arial","15"))
        self.btnOldMinuteur = Button(master,text="Relancer minuteur",bg=mainColor,fg=textColor,font=("arial","15"),command=self._bootOldMinuteur)
        self.objetMinuteur = MINUTEUR(self.master,self.mainColor,self.textColor,self.emplacementBIP)
    
    def bootAppMinuteur(self):    
        self.zoneEntrer.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.entryMin.pack(side="left")
        self.labelMin.pack(side="left")
        self.entrySec.pack(side="left")
        self.labelSec.pack(side="left")
        self.btnBoot.place(x=185,y=315)
        self.btnPrereglage1.place(x=15,y=315)
        self.btnPrereglage2.place(x=370,y=315)
        if self.oldMinuteur != 0 :
            self.btnOldMinuteur.place(x=205,y=415)
            
    def bootMinuteurInstentaner(self,duration:int):
        self.objetMinuteur.bootMinuteur(duration)
        
    def setOlminuteur(self,nb:int):
        self.oldMinuteur =  nb
    
    def _noAffichage(self):
        self.zoneEntrer.place_forget()
        self.btnBoot.place_forget()
        self.btnPrereglage1.place_forget()
        self.btnPrereglage2.place_forget()
    
    def _prereglage1(self):
        self._noAffichage()
        self.objetMinuteur.bootMinuteur(900)
    
    def _prereglage2(self):
        self._noAffichage()
        self.objetMinuteur.bootMinuteur(1800)
        
    def _bootOldMinuteur(self):
        self._noAffichage() 
        self.objetMinuteur.bootMinuteur(self.oldMinuteur)
    
    def _boot(self):
        valMin = self.entryMin.get()
        valSec = self.entrySec.get()
        if valMin == "" :
            min = 0
        else :       
            min = int(valMin)*60
        if valSec == "" :
            sec = 0
        else :
            sec = int(valSec) 
        if sec == 0 and min == 0 :
            messagebox.showinfo("Minuteur imposible", "Imposible de lancer un minuteur de 0 minute et 0 second")
        else :
            self._noAffichage()      
            temps = min + sec
            self.objetMinuteur.bootMinuteur(temps)
            
        
class Clock() :
    def __init__(self,master,mainColor,textColor):
        self.master = master
        self.clock = Label(master, font = ("arial", 60, "bold"),bg=mainColor,fg=textColor)

    def bootClock(self):
        self.clock.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.time()
    
    def time(self): 
        self.running = True
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        self.master.after(10,self.time)