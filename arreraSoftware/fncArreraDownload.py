from pytube import*
from librairy.travailJSON import *
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter import messagebox
import os
import webbrowser

class fncArreraVideoDownload :
    def __init__(self,ConfigNeuron:jsonWork):
        #variable
        self.fichierGestion = ConfigNeuron
        self.color = self.fichierGestion.lectureJSON("interfaceColor")
        self.textColor = self.fichierGestion.lectureJSON("interfaceTextColor")
        self.name = self.fichierGestion.lectureJSON("name")
        self.icon = self.fichierGestion.lectureJSON("iconAssistant")
        self.listChoix = ["simple","playlist"]
        self.fileMusic = "download"
        self.fileVideo = "download"
        self.btnColor = "red"
        self.textBTNcolor = "white"
        
    def fenetreDownload(self,mode):
        #fenetre TK
        self.screen = Tk()
        self.varChoix = StringVar(self.screen)
        self.screen.title(self.name+": Youtube Download")
        self.screen.config(bg=self.color)
        self.screen.iconphoto(False,PhotoImage(file=self.icon))
        self.screen.maxsize(500,300)
        self.screen.minsize(500,300)
        #cadre
        self.cadreDownload = Frame(self.screen,bg=self.color,width=450,height=250)
        self.cadreWait = Frame(self.screen,bg=self.color,width=450,height=250)
        #entry
        self.entryURL = Entry(self.cadreDownload,width=30,border=2,font=("arial",15))
        #label
        self.labelindiction = Label(self.cadreDownload,font=("arial",15),bg=self.color,fg=self.textColor)
        self.labelWait = Label(self.cadreWait,text="En court",font=("arial",25),bg=self.color,fg=self.textColor)
        #option menu
        self.menu = OptionMenu(self.cadreDownload,self.varChoix,*self.listChoix)
        #button
        self.boutonDownload = Button(self.cadreDownload,text="Télécharger",bg=self.btnColor,fg=self.textBTNcolor,font=("arial",15))
        self.boutonYoutube = Button(self.cadreDownload,text="Ouvrir Youtube",bg=self.btnColor,fg=self.textBTNcolor,font=("arial",15),command= lambda : webbrowser.open("https://www.youtube.com/"))
        #affichage
        
        self.labelindiction.place(x=100,y=0)
        self.menu.place(x=0,y=0)
        self.entryURL.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.boutonDownload.place(x=330,y=210)
        self.boutonYoutube.place(relx=0.5, rely=1.0, anchor="s")
        
        self.labelWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        if mode == "video" :
            self.labelindiction.configure(text="Copier L'URL d'une video")
            self.downloadView()
            self.boutonDownload.config(command=self.downloadVideo)
            self.screen.mainloop()
        else :
            if mode == "music" :
                self.labelindiction.configure(text="Copier L'URL d'une musique")
                self.downloadView()
                self.boutonDownload.config(command=self.downloadMusique)
                self.screen.mainloop()
            else :
                messagebox.showwarning("Attention", "Le mode que vous demandez n'existe pas.")
    
    def downloadVideoSimple(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download(self.fileVideo)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideoPlaylist(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download(self.fileVideo)      
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiqueSimple(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download(self.fileMusic)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiquePlaylist(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download(self.fileMusic)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideo(self):
        var = self.varChoix.get()
        if var == "simple" :
            self.downloadVideoSimple()
        else :
            self.downloadVideoPlaylist()
    
    def downloadMusique(self):
        var = self.varChoix.get()
        if var == "simple" :
            self.downloadMusiqueSimple()
        else :
            self.downloadMusiquePlaylist()
    
        
    def downloadView(self):
        
        self.cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.varChoix.set(self.listChoix[0])
        
    def waitView(self):
        self.cadreDownload.place_forget()
        self.cadreWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def waitNoView(self):
        self.cadreWait.place_forget()
        self.cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)        