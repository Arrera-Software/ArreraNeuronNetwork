from tkinter import*
import webbrowser as w
from github import Github
import requests
from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire

class CHGithub(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Github")
        self.__tokenGithub = self._gestionnaire.getTokenGithub()
        self.__listDepo = []

    def _mainframe(self):
        #Frame
        self.__main_frame = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameSearch = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameError = self._arrtk.createFrame(self._screen, width=500, height=500)
        self.__frameList = self._arrtk.createFrame(self._screen, width=500, height=500)
        #scrollbar
        self.__scroll = Scrollbar(self.__frameList,orient="vertical")
        #widget
        labelAcceuil = self._arrtk.createLabel(self.__main_frame, text="GitHub",ppolice="Arial",ptaille=25)
        btnList = self._arrtk.createButton(self.__main_frame, text="Vos depot", bg=self._btnColor, fg=self._btnTexteColor,ppolice="Arial",ptaille=15, command=self.__GUIListDepos)
        btnRecherche = self._arrtk.createButton(self.__main_frame, text="Recherche", bg=self._btnColor, fg=self._btnTexteColor,ppolice="Arial",ptaille=15, command=self.__GUISearch)
        self.__entrySeach = self._arrtk.createEntry(self.__frameSearch,ppolice="Arial",ptaille=15)
        labelSearch = self._arrtk.createLabel(self.__frameSearch,text="Recherche sur Github",ppolice="Arial",ptaille=25)
        btnSearch = self._arrtk.createButton(self.__frameSearch,text="Valider",bg=self._btnColor, fg=self._btnTexteColor,ppolice="Arial",ptaille=15,command=self.__search)
        labelError = self._arrtk.createLabel(self.__frameError,text="Aucun token enregistrer\nRendez-vous\ndans les parametre pour\nl'enregistrer",ppolice="Arial",ptaille=25)
        btnError = self._arrtk.createButton(self.__frameError,text="Quitter",bg=self._btnColor, fg=self._btnTexteColor,ppolice="Arial",ptaille=15,command=self.__backMain)
        btnListQuit = self._arrtk.createButton(self.__frameList,text="Quitter",bg=self._btnColor, fg=self._btnTexteColor,ppolice="Arial",ptaille=15,width=self.__frameList.winfo_reqwidth(),command=self.__backMain)
        self.boxlistDepot = Listbox(self.__frameList,width=500,height=500)
        #Affichage
        labelAcceuil.place(x=((self.__main_frame.winfo_reqwidth() - labelAcceuil.winfo_reqwidth()) // 2), y=0)
        btnList.place(x=((self.__main_frame.winfo_reqwidth() - btnList.winfo_reqwidth()) - 15), y=((self.__main_frame.winfo_reqheight() - btnList.winfo_reqheight()) // 2))
        btnRecherche.place(x=15, y=((self.__main_frame.winfo_reqheight() - btnRecherche.winfo_reqheight()) // 2))
        labelSearch.place(x=((self.__frameSearch.winfo_reqwidth()-labelSearch.winfo_reqwidth())//2),y=0)
        self.__entrySeach.place(relx=0.5,rely=0.5,anchor="center")
        btnSearch.place(x=((self.__frameSearch.winfo_reqwidth()-btnSearch.winfo_reqwidth())//2),y=self.__frameSearch.winfo_reqheight()-btnSearch.winfo_reqheight())
        labelError.place(relx=0.5,rely=0.5,anchor="center")
        btnError.place(x=((self.__frameError.winfo_reqwidth()-btnError.winfo_reqwidth())//2),y=((self.__frameError.winfo_reqheight()-btnError.winfo_reqheight())))
        btnListQuit.place(x=((self.__frameList.winfo_reqwidth()-btnListQuit.winfo_reqwidth())//2),y=((self.__frameList.winfo_reqheight()-btnListQuit.winfo_reqheight())))
        self.boxlistDepot.place(relx=0, rely=0, relwidth=0.95, relheight=1)
        self.__scroll.place(relx=0.95, rely=0, relwidth=0.05, relheight=1)
        self.__main_frame.place(relx=0.5, rely=0.5, anchor="center")

    def search(self,requette:str):
        urllink = requests.get("https://github.com/search?q="+requette)
        urllink = urllink.url
        w.open(urllink)
    
    def __GUISearch(self):
        self.__main_frame.place_forget()
        self.__frameSearch.place(relx=0.5,rely=0.5,anchor="center")
    
    def __search(self):
        self.__main_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.__frameSearch.place_forget()
        self.search(str(self.__entrySeach.get()))
        self.__entrySeach.delete("0",END)

    def __setListDepos(self)->bool:
        if self.__tokenGithub :
            access = Github(self.__tokenGithub)
            for repo in access.get_user().get_repos():
                self.__listDepo.append(str(repo.name))
            return True
        else :
            return False
    
    def __backMain(self):
        self.__frameList.place_forget()
        self.__frameError.place_forget()
        self.__frameSearch.place_forget()
        self.__main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
    def __GUIListDepos(self):
        self.__main_frame.place_forget()
        if self.__setListDepos() == False :
            self.__frameError.place(relx=0.5,rely=0.5,anchor="center")
        else :
            self.__frameList.place(relx=0.5,rely=0.5,anchor="center")
            for i in range(0,(len(self.__listDepo)-1)) :
                self.boxlistDepot.insert(END,self.__listDepo[i])
            self.__scroll.configure(command=self.boxlistDepot.yview)